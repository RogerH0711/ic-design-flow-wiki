#!/usr/bin/env python3
"""Node 7: render slides/run-<nn>/05-slides.json into docs/slides/index.html.

    python3 scripts/render_slides.py slides/run-01

One self-contained HTML file: no external scripts, styles, or fonts. Every
content slide carries a sources line built from its evidence cards, and the
E key opens the exact wiki sentences behind the slide.
"""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = "https://github.com/RogerH0711/ic-design-flow-wiki/blob/main/wiki/"
STAGES = [
    "Specification", "RTL design", "Verification", "Synthesis", "Floorplanning",
    "Placement", "Clock tree", "Routing", "Finishing", "Signoff",
]
LABELS = ("In", "Out", "Checked by", "Common problem", "Problem", "Risk", "Side effect", "Goal", "Steps", "Style rule")
CITATION = re.compile(r"\[(S\d+) §([^\]]+)\]")


def esc(text):
    text = html.escape(text, quote=False)
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", text)


def bullet_html(text):
    for label in LABELS:
        if text.startswith(label + ": "):
            return f'<span class="tag">{label}</span>{esc(text[len(label) + 2:])}'
    return esc(text)


def plain_sentence(sentence):
    return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", sentence)


def main():
    run = (ROOT / sys.argv[1]).resolve()
    slides = json.loads((run / "05-slides.json").read_text(encoding="utf-8"))["slides"]
    outline = {s["n"]: s for s in json.loads((run / "04-outline.json").read_text(encoding="utf-8"))["slides"]}
    cards = {c["id"]: c for c in json.loads((run / "03-evidence.json").read_text(encoding="utf-8"))["cards"]}

    stage_of = {}
    for n, o in outline.items():
        m = re.match(r"Stage (\d+):", o["title"])
        if m:
            stage_of[n] = int(m.group(1))

    sections = []
    for s in slides:
        n, kind = s["n"], outline[s["n"]]["kind"]
        ids = []
        for b in s["bullets"]:
            for cid in b.get("cards", []):
                if cid not in ids:
                    ids.append(cid)
        strip = ""
        if kind not in ("title",):
            chips = "".join(
                f'<li class="{"on" if stage_of.get(n) == i else ""}"><b>{i}</b>{name}</li>'
                for i, name in enumerate(STAGES, 1)
            )
            strip = f'<ol class="strip" aria-label="The ten stages">{chips}</ol>'
        lead = f'<p class="lead">{esc(s["lead"])}</p>' if s.get("lead") else ""
        tag = "ol" if kind in ("quiz",) or n == 4 else "ul"
        items = "".join(f"<li>{bullet_html(b['text'])}</li>" for b in s["bullets"])
        body = f"<{tag} class=\"points\">{items}</{tag}>" if items else ""
        sources = evidence = ""
        if ids:
            pages = []
            cites = []
            for cid in ids:
                page = cards[cid]["page"]
                if page not in pages:
                    pages.append(page)
                for c in cards[cid].get("citations", []):
                    if c not in cites:
                        cites.append(c)
            page_links = ", ".join(f'<a href="{REPO}{p}">{p[:-3]}</a>' for p in pages)
            sources = (
                f'<p class="sources"><b>Wiki</b> {page_links} <b>Sources</b> '
                f'{html.escape("; ".join(cites))}</p>'
            )
            rows = "".join(
                f"<li><b>{cid}</b> <i>{cards[cid]['page']}</i><br>"
                + (
                    f"Section \u201c{cards[cid]['section']}\u201d carries the marker: not yet covered by an ingested source."
                    if cards[cid].get("kind") == "gap"
                    else esc(plain_sentence(cards[cid]["wiki_sentence"]))
                )
                + "</li>"
                for cid in ids
            )
            evidence = f'<aside class="evidence" id="e{n}" hidden><h3>Wiki sentences behind slide {n}</h3><ul>{rows}</ul></aside>'
        extra = ""
        if kind == "title":
            extra = '<p class="byline">Built only from the pages of an LLM Wiki. Press <kbd>E</kbd> on any slide to see the wiki sentences behind it.</p>'
        sections.append(
            f'<section class="slide k-{kind}" id="s{n}" data-n="{n}">{strip}'
            f'<div class="body"><h2>{esc(s["title"])}</h2>{lead}{body}{extra}</div>'
            f'{sources}<span class="num">{n} / {len(slides)}</span></section>{evidence}'
        )

    page = TEMPLATE.replace("{{SLIDES}}", "\n".join(sections)).replace("{{TITLE}}", html.escape(slides[0]["title"]))
    out = ROOT / "docs" / "slides" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")
    print(f"render_slides: {len(slides)} slides -> {out.relative_to(ROOT)} ({out.stat().st_size} bytes)")


TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{TITLE}}</title>
<style>
:root { --paper:#f4f1ea; --ink:#18212b; --soft:#5b6673; --line:#d5cfc2; --accent:#0b6e6e; --warm:#b4552d; }
* { box-sizing:border-box; }
html,body { height:100%; margin:0; background:#23282e; color:var(--ink);
  font-family: "Helvetica Neue", Helvetica, Arial, "Segoe UI", sans-serif; }
#stage { position:fixed; left:50%; top:50%; width:1280px; height:720px; transform-origin:center center; }
.slide { position:absolute; inset:0; display:none; overflow:hidden; background:var(--paper);
  padding:28px 64px 64px; }
.slide.active { display:block; }
.strip { list-style:none; display:flex; gap:6px; margin:0 0 30px; padding:0; font-size:13px; color:var(--soft); }
.strip li { flex:1; border-top:3px solid var(--line); padding-top:6px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
.strip b { margin-right:5px; font-variant-numeric:tabular-nums; }
.strip li.on { border-top-color:var(--warm); color:var(--ink); font-weight:600; }
h2 { font-family: Georgia, "Iowan Old Style", "Times New Roman", serif; font-weight:400; font-size:44px;
  line-height:1.12; margin:0 0 22px; letter-spacing:-0.01em; max-width:1050px; }
.lead { font-size:23px; line-height:1.4; color:var(--soft); margin:0 0 20px; max-width:1000px; }
.points { margin:0; padding:0 0 0 1.2em; font-size:25px; line-height:1.36; max-width:1090px; }
ul.points { list-style:none; padding-left:0; }
ul.points li { padding-left:26px; position:relative; }
ul.points li::before { content:""; position:absolute; left:2px; top:0.6em; width:10px; height:2px; background:var(--accent); }
.points li { margin:0 0 13px; }
ol.points li::marker { color:var(--accent); font-weight:600; }
.tag { display:inline-block; font-size:14px; font-weight:700; letter-spacing:0.06em; text-transform:uppercase;
  color:var(--accent); border:1.5px solid var(--accent); border-radius:3px; padding:1px 7px; margin-right:10px;
  vertical-align:0.18em; }
code { font-family: ui-monospace, Menlo, Consolas, monospace; font-size:0.86em; background:#e8e3d8; padding:1px 5px; border-radius:3px; }
.sources { position:absolute; left:64px; right:150px; bottom:16px; margin:0; font-size:11.5px; line-height:1.35;
  color:var(--soft); max-height:32px; overflow:hidden; }
.sources b { color:var(--ink); font-weight:600; margin-right:3px; }
.sources a { color:var(--accent); }
.num { position:absolute; right:64px; bottom:18px; font-size:13px; color:var(--soft); font-variant-numeric:tabular-nums; }
.k-title { padding-top:170px; }
.k-title h2 { font-size:68px; max-width:980px; }
.k-title .lead { font-size:27px; max-width:860px; }
.byline { font-size:17px; color:var(--soft); margin-top:44px; }
kbd { font:inherit; border:1px solid var(--soft); border-radius:3px; padding:0 6px; }
.k-quiz .points li { margin-bottom:18px; }
.evidence { position:absolute; right:0; top:0; bottom:0; width:520px; background:#fffdf8; border-left:3px solid var(--warm);
  padding:26px 28px; overflow:auto; font-size:15px; line-height:1.45; box-shadow:-12px 0 30px rgba(0,0,0,.18); z-index:5; }
.evidence h3 { margin:0 0 14px; font-size:17px; }
.evidence ul { margin:0; padding-left:0; list-style:none; }
.evidence li { margin-bottom:14px; }
.evidence i { color:var(--soft); font-size:13px; }
#nav { position:fixed; left:0; right:0; bottom:8px; text-align:center; z-index:9; }
#nav button { font:inherit; font-size:14px; background:#3a424b; color:#e9e6df; border:0; border-radius:4px; padding:7px 14px; margin:0 3px; cursor:pointer; }
#nav button:hover { background:#4b5560; }
#nav button:focus-visible { outline:2px solid #fff; }
@media print { #nav { display:none; } #stage { position:static; transform:none !important; }
  .slide { display:block; position:relative; width:1280px; height:720px; page-break-after:always; } }
</style>
</head>
<body>
<main id="stage">
{{SLIDES}}
</main>
<nav id="nav"><button id="prev" aria-label="Previous slide">&larr; Prev</button><button id="ev">Evidence (E)</button><button id="next" aria-label="Next slide">Next &rarr;</button></nav>
<script>
(function () {
  var slides = Array.prototype.slice.call(document.querySelectorAll('.slide'));
  var stage = document.getElementById('stage');
  var cur = 0;
  function fit() {
    var s = Math.min(window.innerWidth / 1280, (window.innerHeight - 46) / 720);
    stage.style.transform = 'translate(-50%, -50%) translateY(-18px) scale(' + s + ')';
  }
  function hideEvidence() {
    Array.prototype.forEach.call(document.querySelectorAll('.evidence'), function (e) { e.hidden = true; });
  }
  window.showSlide = function (i) {
    cur = Math.max(0, Math.min(slides.length - 1, i));
    slides.forEach(function (s, k) { s.classList.toggle('active', k === cur); });
    hideEvidence();
    if (history.replaceState) { history.replaceState(null, '', '#' + (cur + 1)); }
  };
  function toggleEvidence() {
    var e = document.getElementById('e' + (cur + 1));
    if (e) { e.hidden = !e.hidden; }
  }
  document.getElementById('prev').onclick = function () { showSlide(cur - 1); };
  document.getElementById('next').onclick = function () { showSlide(cur + 1); };
  document.getElementById('ev').onclick = toggleEvidence;
  document.addEventListener('keydown', function (ev) {
    if (ev.key === 'ArrowRight' || ev.key === 'PageDown' || ev.key === ' ') { showSlide(cur + 1); ev.preventDefault(); }
    else if (ev.key === 'ArrowLeft' || ev.key === 'PageUp') { showSlide(cur - 1); ev.preventDefault(); }
    else if (ev.key === 'Home') { showSlide(0); }
    else if (ev.key === 'End') { showSlide(slides.length - 1); }
    else if (ev.key === 'e' || ev.key === 'E') { toggleEvidence(); }
    else if (ev.key === 'Escape') { hideEvidence(); }
  });
  var x0 = null;
  document.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
  document.addEventListener('touchend', function (e) {
    if (x0 === null) { return; }
    var dx = e.changedTouches[0].clientX - x0; x0 = null;
    if (Math.abs(dx) > 50) { showSlide(cur + (dx < 0 ? 1 : -1)); }
  });
  window.addEventListener('resize', fit);
  fit();
  showSlide((parseInt(location.hash.slice(1), 10) || 1) - 1);
})();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main()
