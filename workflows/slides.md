# Slides workflow

Builds the teaching deck "How a digital chip gets from RTL to GDSII" from the
wiki, and from nothing else. Approved by the owner on 2026-11-14.

The workflow is a graph, not a straight line: every node writes a file, every
node has a check, and a failed check sends the work back to a named earlier
node. All files of one run live in `slides/run-<nn>/`.

## Graph

```
 [1 retrieve] -> [2 coverage] -> [3 evidence] -> [4 outline] -> [5 draft] -> [6 review] -> [7 render] -> [8 accept]
      ^   fail        | stop          ^  ^            | HUMAN        ^  ^          |            ^           | HUMAN
      +---------------+ ask owner     |  +--- fail ---+              |  +-- fail --+            +-- fail ---+
                                      +------------- "no evidence for this" ---------+
                                                                     +---------- "wording / order" --------+
```

| # | Node | Writes | Check (who) | On failure go to |
|---|------|--------|-------------|------------------|
| 1 | Retrieve: choose the wiki pages the deck may use, starting from `wiki/index.md` | `01-retrieval.json` | script: every page exists, all ten stage pages are included | 1 |
| 2 | Coverage: count cited statements and gap markers per stage and per required section | `02-coverage.json` | script: every stage has a cited Purpose and at least 5 cited statements | **stop and ask the owner** (more sources, or accept the gap) |
| 3 | Evidence cards: one card per point the deck may make. A card holds the exact wiki sentence, its page, and its citations | `03-evidence.json` | script: the sentence is found word for word in that wiki page, and the citations in the card are the ones on that sentence | 3 (redo the card) |
| 4 | Outline: 16-20 slides; each has a title, a purpose, and the card ids it will use | `04-outline.json` | script: slide count, every card id exists, every stage appears, no content slide without cards. Then **the owner approves** | 4 |
| 5 | Draft: write each slide from its cards only | `05-slides.json` | script: every bullet names at least one card, at most 5 bullets and 60 words per slide, English only, wiki terminology | 5 (that slide) |
| 6 | Faithfulness review: a fresh sub-agent that has not seen nodes 1-5 compares every bullet with the wiki sentences on its cards | `06-review.md` | sub-agent, instructions in `workflows/slides-review.md` | 5 for wording; 3 when the cards do not support the point |
| 7 | Render: produce one self-contained HTML file | `docs/slides/index.html` | script: slide count matches, every content slide shows its sources, no slide overflows its frame at 1280x720, screenshots saved | 7 |
| 8 | Accept: **the owner approves** the rendered deck | `08-acceptance.md` | owner | 5 for content, 7 for layout |

## Rules

- A node may read only the files of earlier nodes and the wiki. Nodes 5 and 6
  may not read `raw/`: the deck is built from the wiki, and the wiki's own
  faithfulness is the job of the ingest review.
- Nothing is done from memory. If a point is wanted and no card supports it,
  go back to node 3; if the wiki does not say it, the point is dropped.
- A gap marker in the wiki is never papered over. A slide may say that the
  sources do not cover something.
- Where the wiki records a source difference, the slide shows both versions.
- At most 3 rounds per node. After the third failure, stop and ask.
- Every check run is appended to `slides/run-<nn>/run-log.md`, failures
  included. Nobody edits that file by hand.
- The agent that drafts (node 5) never reviews (node 6).

## What repeats

- Node 3 repeats per card and node 5 per slide: only the failing card or
  slide is redone, not the whole file.
- The loop 5 -> 6 -> 5 repeats until the review has no open finding.
- The loop 3 -> 4 -> 5 is re-entered whenever the review says a point has no
  evidence.

## Why the checks sit where they do

Ingest showed that unfaithful statements are cheap to catch early and
expensive late: the lint passed while the independent review found 98
problems in nine sources. So the deck's first faithfulness check is at node 3,
before any slide exists: a card must quote the wiki exactly, which a script
can verify. By the time prose is written at node 5 every point already has a
verified anchor, and the reviewer at node 6 only has to compare a bullet with
two or three quoted sentences.

## Commands

```
python3 scripts/slides_check.py retrieval slides/run-01
python3 scripts/slides_check.py coverage  slides/run-01
python3 scripts/slides_check.py evidence  slides/run-01
python3 scripts/slides_check.py outline   slides/run-01
python3 scripts/slides_check.py draft     slides/run-01
python3 scripts/render_slides.py          slides/run-01
python3 scripts/slides_check.py render    slides/run-01
```
