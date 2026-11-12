# ic-design-flow-wiki

An LLM Wiki about the digital IC design flow (RTL to GDSII), and a teaching
slide deck generated from it. Week 10 homework for the TAICA generative AI course.

- **Wiki:** start at [`wiki/index.md`](wiki/index.md)
- **Rules the AI agent follows:** [`AGENTS.md`](AGENTS.md)
- **How the requirements were decided:** [`docs/interview.md`](docs/interview.md),
  [`docs/requirements.md`](docs/requirements.md)
- **Check records:** [`docs/checks/`](docs/checks/)

## Checks

```
python3 scripts/fetch_raw.py --verify   # raw sources are unmodified
python3 scripts/lint_wiki.py            # citations, links, format, terminology
```

## Sources and licenses

`raw/` holds verbatim copies of openly licensed documentation, each pinned to
an upstream commit in [`raw/sources.json`](raw/sources.json). Each file stays
under its original license (BSD-3-Clause, Apache-2.0, ISC, CC-BY-4.0,
LGPL-3.0-only OR Artistic-2.0); license texts are in `raw/licenses/`.
Figures from the original documents are not copied. The wiki pages are
paraphrased summaries that cite the raw file and section they come from.
