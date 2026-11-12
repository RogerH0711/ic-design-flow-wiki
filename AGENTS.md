# AGENTS.md

Rules for any AI agent working in this repository. Written from the requirements
the owner confirmed in `docs/requirements.md` (interview record:
`docs/interview.md`). If a rule here and that summary disagree, stop and ask.

## 1. What this repository is

An LLM Wiki in the sense of Karpathy's note: the agent reads raw sources once,
and maintains a set of interlinked markdown pages that it keeps current.

- **Topic:** the digital IC design flow, end to end: specification → RTL →
  functional verification → logic synthesis → floorplanning → placement →
  clock tree synthesis → routing → signoff → GDSII.
- **Depth:** an overview. For every stage say what goes in, what comes out,
  and what is checked. Do not explain algorithms.
- **Reader:** a second-year computer science student who knows logic gates and
  flip-flops but has never seen an IC design flow. Define every other term on
  first use or link to its concept page.
- **Language:** English only, in the wiki and in the slides.

## 2. Layout

```
raw/                 verbatim sources, pinned by raw/sources.json   READ-ONLY
wiki/index.md        catalogue of every page, grouped by type
wiki/log.md          append-only record of ingests and decisions
wiki/terminology.json  one spelling per concept
wiki/sources/        one page per raw source          type: source
wiki/stages/         one page per flow stage          type: stage
wiki/concepts/       cross-stage ideas and terms      type: concept
wiki/tools/          EDA tools                        type: tool
wiki/formats/        file formats                     type: format
scripts/             fetch_raw.py, lint_wiki.py
docs/                interview, requirements, check records (may be in Chinese)
```

## 3. Hard rules

1. **Never edit `raw/`.** New sources are added only after the owner approves
   them, by editing `raw/sources.json` and running `scripts/fetch_raw.py`.
2. **The wiki contains only what the raw sources say.** No outside knowledge,
   not even to fill an obvious gap. If the sources do not cover something a
   page needs, write exactly `_Not yet covered by an ingested source._` in
   that section and list the gap in `wiki/log.md`.
3. **Every claim is cited** (section 5). A paragraph or list item without a
   citation is a lint error.
4. **Paraphrase.** Do not copy sentences from raw sources; quote at most a
   short phrase when the exact wording matters.
5. **Do not change this file, `scripts/`, or `wiki/terminology.json` rules
   silently.** Propose the change, get approval, and record it in the log.

## 4. Page formats

Every page starts with frontmatter and one `# Title`:

```
---
title: Clock Tree Synthesis
type: stage            # source | stage | concept | tool | format
sources: [S1, S2]      # exactly the ids cited in the body
updated: 2026-11-12
order: 6               # stage pages only: position in the flow
source_id: S1          # source pages only
---
```

Required `##` sections, in this order:

| type | sections |
|---|---|
| source | Summary · Key points · Coverage · Related pages |
| stage | Purpose · Inputs · Outputs · What happens · Checks · Related pages |
| concept | Definition · Why it matters · Related pages |
| tool | What it is · Role in the flow · Related pages |
| format | What it is · Produced by and used by · Related pages |

Optional sections: `Common problems` (stage), `Source differences` (any).
File names are kebab-case. Link between pages with relative markdown links.
`Related pages` holds links only and needs no citations. A line that starts
with `Also called:` lists alternative names and is exempt from the
terminology check.

## 5. Citations

Format: `[S3 §Section Title]`, one bracket per source section, placed at the
end of the sentence or list item it supports.

- `S3` is the id in `raw/sources.json`.
- `Section Title` is the heading in the raw file under which the statement
  appears, copied as written (case and markup are ignored). For a glossary
  source, use the term being defined.
- Cite the nearest heading that actually contains the statement, not the
  document title, unless the statement sits before the first sub-heading.

## 6. Terminology

`wiki/terminology.json` lists the one spelling to use and the spellings to
avoid. When a new source uses a different name for an existing concept, keep
the wiki's spelling, add the variant to `not`, and mention it once on the
concept page in an `Also called:` line.

## 7. When sources disagree

Do not pick a side. On the affected page add a `## Source differences`
section; each item states both versions and cites both sources. Also add a
`conflict` entry to `wiki/log.md`. Differences in how the flow is divided
into stages, in stage names, and between open-source and commercial practice
all count.

## 8. Ingest workflow (one source at a time)

1. Read the whole raw file for the next source id.
2. Write `wiki/sources/<id>-<slug>.md`.
3. Create or update every stage, concept, tool, and format page the source
   informs. Updating existing pages matters more than creating new ones.
4. Update `wiki/index.md` and append an `ingest` entry to `wiki/log.md`:
   `## [YYYY-MM-DD] ingest | S<n> <title>`, listing pages created, pages
   updated, conflicts found, and gaps left open.
5. Run `python3 scripts/lint_wiki.py --record "ingest S<n>"`. Fix only what
   the report lists and rerun. Stop after 3 failed rounds and ask.
6. Independent review (from S3 on). Start a fresh sub-agent that has not seen
   the ingest and give it only `workflows/ingest-review.md`, the raw file(s)
   of this source, and the list of pages touched. It checks every statement
   that cites this source against the cited section and writes
   `docs/checks/reviews/S<n>.md`. The agent that wrote the pages must not
   review them. Fix every finding marked UNSUPPORTED or WRONG-SECTION, rerun
   the lint, and record the fixes in the same review file. If the reviewer
   and the writer disagree, keep both views in the file and ask the owner.
7. Commit: one source, one commit, message `Ingest S<n>: <title>`.

The first two sources (S1, S2) were ingested before step 6 existed. The
owner read the result and raised no problem, but they have had no
independent review.

## 9. Definition of done

A change is done when `python3 scripts/lint_wiki.py` exits 0 and, for an
ingest, the independent review has no open finding. "I checked it" is not
verification. The lint covers citations, links and index, page format,
terminology, English-only text, and raw-file integrity; it cannot tell
whether a statement is faithful to the section it cites, which is what the
review is for.

## 10. Slides

The wiki's downstream product is a 16–20 slide teaching deck in HTML, "how a
digital chip gets from RTL to GDSII", built **only** from wiki pages. Its
workflow lives in `workflows/slides.md`. Do not generate slides until that
file exists and the owner has approved it. Two human gates are fixed: the
owner approves the outline, and the owner approves the rendered deck.

## 11. Ask before you

- add, remove, or replace a raw source;
- resolve a conflict in favour of one source;
- leave a required section as a gap when a new source might fill it;
- change the page formats, the lint, or this file.
