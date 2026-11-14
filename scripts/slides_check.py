#!/usr/bin/env python3
"""Checks for the slides workflow (workflows/slides.md).

    python3 scripts/slides_check.py <node> slides/run-01

node is one of: retrieval, coverage, evidence, outline, draft, render.
`coverage` also writes 02-coverage.json, because that file is a measurement,
not something an agent should compose. Every run is appended to
<run>/run-log.md with its verdict and its errors.
"""
import datetime
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
GAP = "_Not yet covered by an ingested source._"
CITATION = re.compile(r"\[(S\d+) §([^\]]+)\]")
CJK = re.compile(r"[぀-ヿ㐀-鿿＀-￯]")
STAGE_SECTIONS = ["Purpose", "Inputs", "Outputs", "What happens", "Checks"]
MIN_STATEMENTS = 5
MIN_SLIDES, MAX_SLIDES = 16, 20
MAX_BULLETS, MAX_WORDS = 5, 60
NO_CARD_KINDS = {"title", "agenda", "recap", "quiz", "sources"}


def load(run, name):
    return json.loads((run / name).read_text(encoding="utf-8"))


def flat(text):
    return re.sub(r"\s+", " ", text).strip()


def stage_pages():
    pages = {}
    for p in sorted((WIKI / "stages").glob("*.md")):
        m = re.search(r"^order:\s*(\d+)", p.read_text(encoding="utf-8"), re.M)
        pages[p.relative_to(WIKI).as_posix()] = int(m.group(1))
    return pages


def sections(path):
    """{section: [paragraph or list item, ...]} for one wiki page."""
    out, current, buf = {}, "_intro", []
    body = path.read_text(encoding="utf-8").split("---", 2)[2]

    def flush():
        if buf:
            out.setdefault(current, []).append(flat(" ".join(buf)))
            buf.clear()

    for line in body.split("\n"):
        h = re.match(r"^##\s+(.+)$", line)
        if h:
            flush()
            current = h.group(1).strip()
        elif not line.strip() or line.startswith("# "):
            flush()
        elif re.match(r"^\s*(?:[-*]|\d+\.)\s+", line):
            flush()
            buf.append(re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", line))
        else:
            buf.append(line)
    flush()
    return out


def check_retrieval(run, err):
    data = load(run, "01-retrieval.json")
    chosen = [p["page"] for p in data["pages"]]
    for page in chosen:
        if not (WIKI / page).exists():
            err(f"page does not exist: {page}")
    for page in stage_pages():
        if page not in chosen:
            err(f"stage page not retrieved: {page}")
    if len(chosen) != len(set(chosen)):
        err("a page is listed twice")
    return f"{len(chosen)} pages"


def check_coverage(run, err):
    report = {"stages": []}
    for page, order in sorted(stage_pages().items(), key=lambda kv: kv[1]):
        secs = sections(WIKI / page)
        row = {"order": order, "page": page, "sections": {}, "cited_statements": 0, "gaps": []}
        for name, items in secs.items():
            cited = [i for i in items if CITATION.search(i)]
            if name != "Related pages":
                row["cited_statements"] += len(cited)
            if name in STAGE_SECTIONS:
                row["sections"][name] = len(cited)
                if GAP in items:
                    row["gaps"].append(name)
        report["stages"].append(row)
        if row["sections"].get("Purpose", 0) == 0:
            err(f"{page}: Purpose has no cited statement")
        if row["cited_statements"] < MIN_STATEMENTS:
            err(f"{page}: only {row['cited_statements']} cited statements (minimum {MIN_STATEMENTS})")
    report["all_gaps"] = [
        p.relative_to(WIKI).as_posix()
        for p in sorted(WIKI.rglob("*.md"))
        if GAP in p.read_text(encoding="utf-8")
    ]
    (run / "02-coverage.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    weakest = min(report["stages"], key=lambda r: r["cited_statements"])
    return f"10 stages; weakest is {weakest['page']} with {weakest['cited_statements']} statements; gaps in {len(report['all_gaps'])} pages"


def check_evidence(run, err):
    cards = load(run, "03-evidence.json")["cards"]
    allowed = {p["page"] for p in load(run, "01-retrieval.json")["pages"]}
    seen = set()
    for c in cards:
        cid = c.get("id", "?")
        if cid in seen:
            err(f"{cid}: duplicate id")
        seen.add(cid)
        page = WIKI / c["page"]
        if c["page"] not in allowed:
            err(f"{cid}: page {c['page']} was not retrieved at node 1")
            continue
        text = flat(page.read_text(encoding="utf-8"))
        sentence = flat(c["wiki_sentence"])
        if sentence not in text:
            err(f"{cid}: sentence not found word for word in {c['page']}: '{sentence[:50]}...'")
            continue
        on_sentence = sorted(f"{s} §{t}" for s, t in CITATION.findall(sentence))
        if not on_sentence:
            err(f"{cid}: the wiki sentence carries no citation")
        if sorted(c.get("citations", [])) != on_sentence:
            err(f"{cid}: citations in the card differ from those on the sentence")
        if not c.get("point", "").strip():
            err(f"{cid}: card has no point")
    return f"{len(cards)} cards"


def check_outline(run, err):
    slides = load(run, "04-outline.json")["slides"]
    cards = {c["id"]: c for c in load(run, "03-evidence.json")["cards"]}
    if not MIN_SLIDES <= len(slides) <= MAX_SLIDES:
        err(f"{len(slides)} slides; must be {MIN_SLIDES}-{MAX_SLIDES}")
    used_pages = set()
    for n, s in enumerate(slides, 1):
        if s.get("n") != n:
            err(f"slide {n}: wrong number")
        for key in ("title", "purpose", "kind"):
            if not s.get(key):
                err(f"slide {n}: missing {key}")
        ids = s.get("cards", [])
        if s.get("kind") not in NO_CARD_KINDS and not ids:
            err(f"slide {n}: content slide without evidence cards")
        for cid in ids:
            if cid not in cards:
                err(f"slide {n}: unknown card {cid}")
            else:
                used_pages.add(cards[cid]["page"])
    for page in stage_pages():
        if page not in used_pages:
            err(f"stage never used in the outline: {page}")
    unused = sorted(set(cards) - {c for s in slides for c in s.get("cards", [])})
    return f"{len(slides)} slides, {len(cards) - len(unused)} of {len(cards)} cards used"


def check_draft(run, err):
    slides = load(run, "05-slides.json")["slides"]
    outline = load(run, "04-outline.json")["slides"]
    cards = {c["id"] for c in load(run, "03-evidence.json")["cards"]}
    terms = json.loads((WIKI / "terminology.json").read_text(encoding="utf-8"))["terms"]
    if len(slides) != len(outline):
        err(f"{len(slides)} slides drafted, outline has {len(outline)}")
    for s, o in zip(slides, outline):
        n = s.get("n")
        if s.get("title") != o["title"]:
            err(f"slide {n}: title differs from the approved outline")
        bullets = s.get("bullets", [])
        if len(bullets) > MAX_BULLETS:
            err(f"slide {n}: {len(bullets)} bullets (maximum {MAX_BULLETS})")
        words = sum(len(b["text"].split()) for b in bullets) + len(s.get("lead", "").split())
        if words > MAX_WORDS:
            err(f"slide {n}: {words} words (maximum {MAX_WORDS})")
        for b in bullets:
            if o["kind"] not in NO_CARD_KINDS:
                if not b.get("cards"):
                    err(f"slide {n}: bullet without a card: '{b['text'][:40]}'")
                for cid in b.get("cards", []):
                    if cid not in cards:
                        err(f"slide {n}: unknown card {cid}")
                    elif cid not in o["cards"]:
                        err(f"slide {n}: card {cid} is not in the approved outline for this slide")
            plain = re.sub(r"`[^`]*`", "", b["text"])
            if CJK.search(plain):
                err(f"slide {n}: non-English text")
            for t in terms:
                for bad in t["not"]:
                    if re.search(r"(?<![A-Za-z0-9])" + re.escape(bad) + r"(?![A-Za-z0-9])", plain, re.I):
                        err(f"slide {n}: use '{t['use']}' instead of '{bad}'")
    return f"{len(slides)} slides"


def check_render(run, err):
    html_path = ROOT / "docs" / "slides" / "index.html"
    if not html_path.exists():
        err("docs/slides/index.html does not exist")
        return "no file"
    html = html_path.read_text(encoding="utf-8")
    slides = load(run, "05-slides.json")["slides"]
    outline = load(run, "04-outline.json")["slides"]
    count = len(re.findall(r'<section class="slide', html))
    if count != len(slides):
        err(f"{count} slides rendered, {len(slides)} drafted")
    if re.search(r'(src|href)="https?://', html.split("</head>")[0]):
        err("the page loads an external resource; it must be self-contained")
    for o in outline:
        if o["kind"] not in NO_CARD_KINDS:
            block = html.split(f'id="s{o["n"]}"', 1)[-1].split("</section>", 1)[0]
            if 'class="sources"' not in block:
                err(f"slide {o['n']}: no sources line")
    overflow = None
    try:
        from playwright.sync_api import sync_playwright

        shots = run / "screenshots"
        shots.mkdir(exist_ok=True)
        with sync_playwright() as pw:
            browser = pw.chromium.launch(channel="chrome")
            page = browser.new_page(viewport={"width": 1280, "height": 720})
            page.goto(html_path.as_uri())
            page.wait_for_timeout(300)
            overflow = []
            for i in range(count):
                page.evaluate("n => window.showSlide(n)", i)
                page.wait_for_timeout(60)
                bad = page.evaluate(
                    """() => { const s = document.querySelector('.slide.active');
                    return s.scrollHeight > s.clientHeight + 1 || s.scrollWidth > s.clientWidth + 1; }"""
                )
                if bad:
                    overflow.append(i + 1)
                page.screenshot(path=str(shots / f"slide-{i + 1:02d}.png"))
            browser.close()
        for n in overflow:
            err(f"slide {n}: content overflows the 1280x720 frame")
    except Exception as exc:  # no browser available
        err(f"could not open the page in a browser: {exc}")
    return f"{count} slides rendered, overflow on {overflow}"


CHECKS = {
    "retrieval": check_retrieval,
    "coverage": check_coverage,
    "evidence": check_evidence,
    "outline": check_outline,
    "draft": check_draft,
    "render": check_render,
}


def main():
    node, run = sys.argv[1], (ROOT / sys.argv[2]).resolve()
    errors = []
    summary = CHECKS[node](run, errors.append)
    for e in errors:
        print("ERROR", e)
    verdict = "PASS" if not errors else "FAIL"
    print(f"slides_check {node}: {verdict} ({summary}; {len(errors)} errors)")
    log = run / "run-log.md"
    if not log.exists():
        log.write_text("# Run log\n\nAppended by `scripts/slides_check.py`. Failed runs are kept.\n", encoding="utf-8")
    stamp = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
    with log.open("a", encoding="utf-8") as fh:
        fh.write(f"\n## {stamp:%Y-%m-%d %H:%M} | {node} | {verdict} | {summary}\n\n")
        for e in errors:
            fh.write(f"- `{e}`\n")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
