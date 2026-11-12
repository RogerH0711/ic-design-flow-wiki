#!/usr/bin/env python3
"""Lint the wiki. "Done" is decided by this script, not by the agent.

    python3 scripts/lint_wiki.py                      check, print errors, exit 1 on any
    python3 scripts/lint_wiki.py --record "ingest S1" also append the result to
                                                      docs/checks/lint-history.md

Checks (the four groups agreed in docs/requirements.md, plus two guards):
  CITE   every claim carries [S<n> §<section>]; the source id exists in
         raw/sources.json and the section is a real heading (or glossary term)
         of that raw file; frontmatter `sources` matches what the body cites
  LINK   relative links resolve; every page is listed in wiki/index.md;
         no orphan pages; every ingested source has a log.md entry
  FORMAT frontmatter fields, page type vs folder, required sections per type,
         kebab-case file names, unique stage order
  TERM   spellings listed under "not" in wiki/terminology.json are not used
  LANG   wiki pages are English only (no CJK characters)
  RAW    files in raw/ still match raw/SHA256SUMS
"""
import datetime
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
WIKI = ROOT / "wiki"
HISTORY = ROOT / "docs" / "checks" / "lint-history.md"

GAP_MARKER = "_Not yet covered by an ingested source._"
ALIAS_PREFIX = "Also called:"
NO_CITATION_SECTIONS = {"Related pages"}
SPECIAL_PAGES = {"index.md", "log.md"}

TYPE_FOLDER = {
    "source": "sources",
    "stage": "stages",
    "concept": "concepts",
    "tool": "tools",
    "format": "formats",
}
REQUIRED_SECTIONS = {
    "source": ["Summary", "Key points", "Coverage", "Related pages"],
    "stage": ["Purpose", "Inputs", "Outputs", "What happens", "Checks", "Related pages"],
    "concept": ["Definition", "Why it matters", "Related pages"],
    "tool": ["What it is", "Role in the flow", "Related pages"],
    "format": ["What it is", "Produced by and used by", "Related pages"],
}
REQUIRED_FIELDS = ["title", "type", "sources", "updated"]

CITATION = re.compile(r"\[(S\d+) §([^\]]+)\]")
CITATION_LIKE = re.compile(r"\[S\d+[^\]]*\]")
MD_LINK = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)\s]+)\)")
CJK = re.compile(r"[぀-ヿ㐀-鿿＀-￯]")
LIST_ITEM = re.compile(r"^\s*(?:[-*]|\d+\.)\s+")
RST_UNDERLINE = re.compile(r"^([=\-~^\"'`#*+.:_])\1{2,}\s*$")


def norm(text: str) -> str:
    """Normalise a heading or a cited section name for comparison."""
    text = re.sub(r":[A-Za-z_]+:`([^`]*)`", r"\1", text)  # rst roles
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)  # markdown links
    text = text.replace("`", "").replace("*", "")
    text = re.sub(r"\s+", " ", text).strip().strip("#").strip()
    return text.lower()


def raw_sections(path: Path) -> set:
    """Headings (and MyST glossary terms) of one raw file."""
    lines = path.read_text(encoding="utf-8").split("\n")
    found = set()
    fence = None  # "code" or "glossary"
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            if fence is None:
                fence = "glossary" if "{glossary}" in stripped else "code"
            else:
                fence = None
            continue
        if fence == "code":
            continue
        if fence == "glossary":
            if line and not line[0].isspace() and not line.startswith(":"):
                found.add(norm(line))
            continue
        if path.suffix == ".md":
            m = re.match(r"^#{1,6}\s+(.+)$", line)
            if m:
                found.add(norm(m.group(1)))
        else:  # reStructuredText: a title line followed by an underline
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            if (
                stripped
                and not RST_UNDERLINE.match(line)
                and RST_UNDERLINE.match(nxt)
                and len(nxt.rstrip()) >= len(line.rstrip())
            ):
                found.add(norm(line))
    return found


def parse_page(path: Path):
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    meta, body_start = {}, 0
    if lines and lines[0].strip() == "---":
        for j in range(1, len(lines)):
            if lines[j].strip() == "---":
                body_start = j + 1
                break
            if ":" in lines[j]:
                key, value = lines[j].split(":", 1)
                value = value.strip()
                if value.startswith("[") and value.endswith("]"):
                    value = [v.strip() for v in value[1:-1].split(",") if v.strip()]
                meta[key.strip()] = value
    return meta, lines, body_start


def blocks(lines, start):
    """Yield (line_no, section, text) for each paragraph or list item."""
    section, fence = None, False
    buf, buf_line = [], 0

    def flush():
        nonlocal buf
        if buf:
            out = (buf_line, section, " ".join(s.strip() for s in buf))
            buf = []
            return out
        return None

    for idx in range(start, len(lines)):
        line = lines[idx]
        stripped = line.strip()
        if stripped.startswith("```"):
            done = flush()
            if done:
                yield done
            fence = not fence
            continue
        if fence:
            continue
        heading = re.match(r"^(#{1,6})\s+(.+)$", line)
        if heading or not stripped:
            done = flush()
            if done:
                yield done
            if heading and len(heading.group(1)) == 2:
                section = heading.group(2).strip()
            continue
        if LIST_ITEM.match(line):
            done = flush()
            if done:
                yield done
            buf, buf_line = [LIST_ITEM.sub("", line)], idx + 1
        else:
            if not buf:
                buf_line = idx + 1
            buf.append(line)
    done = flush()
    if done:
        yield done


def main() -> int:
    errors = []

    def err(group, path, line, message):
        where = str(path.relative_to(ROOT)) if isinstance(path, Path) else path
        errors.append(f"{group:6} {where}:{line}: {message}")

    manifest = json.loads((RAW / "sources.json").read_text(encoding="utf-8"))
    sections = {}
    for src in manifest["sources"]:
        found = set()
        for f in src["files"]:
            found |= raw_sections(RAW / f["local"])
        sections[src["id"]] = found

    # RAW: checksums
    sums = RAW / "SHA256SUMS"
    for entry in sums.read_text(encoding="utf-8").splitlines():
        digest, name = entry.split("  ", 1)
        target = RAW / name
        if not target.exists():
            err("RAW", "raw/" + name, 0, "file listed in SHA256SUMS is missing")
        elif hashlib.sha256(target.read_bytes()).hexdigest() != digest:
            err("RAW", "raw/" + name, 0, "raw file was modified (checksum mismatch)")

    terms = json.loads((WIKI / "terminology.json").read_text(encoding="utf-8"))["terms"]
    term_rules = []
    for t in terms:
        for bad in t["not"]:
            pattern = re.compile(r"(?<![A-Za-z0-9])" + re.escape(bad) + r"(?![A-Za-z0-9])", re.I)
            term_rules.append((pattern, bad, t["use"]))

    pages = sorted(p for p in WIKI.rglob("*.md"))
    content_pages = [p for p in pages if p.name not in SPECIAL_PAGES]
    inbound = {p: set() for p in pages}
    cited_ids = set()
    stage_orders = {}

    for page in pages:
        meta, lines, body_start = parse_page(page)
        special = page.parent == WIKI and page.name in SPECIAL_PAGES

        for n, line in enumerate(lines, 1):
            if CJK.search(line):
                err("LANG", page, n, "non-English (CJK) text in a wiki page")
                break

        # LINK: relative links resolve
        fence = False
        for n, line in enumerate(lines, 1):
            if line.strip().startswith("```"):
                fence = not fence
            if fence:
                continue
            for _, target in MD_LINK.findall(line):
                if re.match(r"^[a-z]+://", target) or target.startswith(("#", "mailto:")):
                    continue
                dest = (page.parent / target.split("#")[0]).resolve()
                if not dest.exists():
                    err("LINK", page, n, f"broken link -> {target}")
                elif dest in inbound and dest != page and not special:
                    inbound[dest].add(page)

        if special:
            continue

        # FORMAT
        if not re.fullmatch(r"[A-Za-z0-9]+(-[a-z0-9]+)*\.md", page.name):
            err("FORMAT", page, 1, "file name must be kebab-case")
        for field in REQUIRED_FIELDS:
            if field not in meta:
                err("FORMAT", page, 1, f"frontmatter is missing '{field}'")
        ptype = meta.get("type")
        if ptype not in TYPE_FOLDER:
            err("FORMAT", page, 1, f"unknown page type '{ptype}'")
            continue
        if page.parent.name != TYPE_FOLDER[ptype]:
            err("FORMAT", page, 1, f"type '{ptype}' must live in wiki/{TYPE_FOLDER[ptype]}/")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(meta.get("updated", ""))):
            err("FORMAT", page, 1, "'updated' must be YYYY-MM-DD")
        h2 = [m.group(1).strip() for l in lines[body_start:] if (m := re.match(r"^##\s+(.+)$", l))]
        for needed in REQUIRED_SECTIONS[ptype]:
            if needed not in h2:
                err("FORMAT", page, 1, f"missing required section '## {needed}'")
        if not any(re.match(r"^#\s+\S", l) for l in lines[body_start:]):
            err("FORMAT", page, 1, "missing '# Title' heading")
        if ptype == "stage":
            order = str(meta.get("order", ""))
            if not order.isdigit():
                err("FORMAT", page, 1, "stage pages need an integer 'order'")
            elif order in stage_orders:
                err("FORMAT", page, 1, f"stage order {order} already used by {stage_orders[order]}")
            else:
                stage_orders[order] = page.name
        if ptype == "source" and meta.get("source_id") not in sections:
            err("FORMAT", page, 1, "source pages need a valid 'source_id'")

        # CITE and TERM, block by block
        body_ids = set()
        for line_no, section, text in blocks(lines, body_start):
            cites = CITATION.findall(text)
            for sid, sec in cites:
                body_ids.add(sid)
                if sid not in sections:
                    err("CITE", page, line_no, f"unknown source id {sid}")
                elif norm(sec) not in sections[sid]:
                    err("CITE", page, line_no, f"{sid} has no section named '{sec}'")
            for loose in CITATION_LIKE.findall(text):
                if not CITATION.fullmatch(loose):
                    err("CITE", page, line_no, f"malformed citation {loose}")
            exempt = (
                section in NO_CITATION_SECTIONS
                or text == GAP_MARKER
                or text.startswith(ALIAS_PREFIX)
            )
            if not exempt and not cites:
                err("CITE", page, line_no, f"claim without a citation: '{text[:60]}'")
            if section == "Source differences" and len({sid for sid, _ in cites}) < 2:
                err("CITE", page, line_no, "a source difference must cite at least two sources")
            if ptype == "source" and any(sid != meta.get("source_id") for sid, _ in cites):
                err("CITE", page, line_no, "a source page may only cite its own source")
            if not text.startswith(ALIAS_PREFIX):
                plain = re.sub(r"`[^`]*`", "", CITATION.sub("", MD_LINK.sub(r"\1", text)))
                for pattern, bad, use in term_rules:
                    if pattern.search(plain):
                        err("TERM", page, line_no, f"use '{use}' instead of '{bad}'")
        cited_ids |= body_ids
        declared = set(meta.get("sources", [])) if isinstance(meta.get("sources"), list) else set()
        if declared != body_ids:
            err("CITE", page, 1, f"frontmatter sources {sorted(declared)} != cited {sorted(body_ids)}")

    # LINK: index coverage, orphans, log entries
    index_text = (WIKI / "index.md").read_text(encoding="utf-8")
    log_text = (WIKI / "log.md").read_text(encoding="utf-8")
    for page in content_pages:
        rel = page.relative_to(WIKI).as_posix()
        if f"({rel})" not in index_text:
            err("LINK", page, 1, "page is not listed in wiki/index.md")
        meta, _, _ = parse_page(page)
        if meta.get("type") == "source":
            sid = meta.get("source_id", "")
            if sid not in cited_ids:
                err("LINK", page, 1, f"source {sid} is not cited by any page")
            if not re.search(rf"^## \[\d{{4}}-\d{{2}}-\d{{2}}\] ingest \| {sid}\b", log_text, re.M):
                err("LINK", page, 1, f"wiki/log.md has no ingest entry for {sid}")
        elif not inbound[page]:
            err("LINK", page, 1, "orphan page: no other page links to it")

    for e in errors:
        print(e)
    summary = f"lint_wiki: {len(content_pages)} pages, {len(errors)} errors"
    print(summary)

    if "--record" in sys.argv:
        label = sys.argv[sys.argv.index("--record") + 1]
        HISTORY.parent.mkdir(parents=True, exist_ok=True)
        if not HISTORY.exists():
            HISTORY.write_text(
                "# Lint history\n\nAppended by `scripts/lint_wiki.py --record`. "
                "Failed runs are kept on purpose.\n",
                encoding="utf-8",
            )
        stamp = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
        with HISTORY.open("a", encoding="utf-8") as fh:
            status = "PASS" if not errors else "FAIL"
            fh.write(f"\n## {stamp:%Y-%m-%d %H:%M} | {label} | {status} | {summary}\n\n")
            for e in errors:
                fh.write(f"- `{e}`\n")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
