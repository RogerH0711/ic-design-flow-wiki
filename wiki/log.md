# Log

Append-only. Entry types: `setup`, `ingest`, `conflict`, `decision`, `gap`.

## [2026-11-12] setup | Repository created

- Requirements interview finished and summary confirmed by the owner
  (`docs/interview.md`, `docs/requirements.md`).
- `AGENTS.md` generated from the confirmed summary.
- Eleven raw sources (S1–S11) downloaded at pinned commits with
  `scripts/fetch_raw.py`; checksums in `raw/SHA256SUMS`.
- Nothing ingested yet.

## [2026-11-12] ingest | S1 OpenROAD Flow Scripts Tutorial

- Created (20): source page `sources/s1-orfs-flow-tutorial.md`; stages
  `logic-synthesis`, `floorplanning`, `placement`, `clock-tree-synthesis`,
  `routing`, `layout-finishing`; concepts `ppa`, `placement-density`,
  `ir-drop`, `tap-endcap-tie-filler-cells`, `timing-violations`,
  `antenna-violation`; tools `openroad-flow-scripts`, `openroad`, `yosys`;
  formats `sdc`, `gdsii`, `spef`, `odb`.
- Updated: `index.md`.
- Conflicts: none (first source).

## [2026-11-12] decision | Terminology after S1

S1 mixes spellings, so the wiki fixes one each in `terminology.json`:
GDSII (not GDS), detailed routing (not detail routing), tap cell (not
tapcell), filler cell (not fill cell), floorplanning.

## [2026-11-12] gap | Open after S1

- `stages/logic-synthesis.md` Purpose: S1 never says what synthesis does to
  the design. Expected from S5.
- `stages/routing.md` Inputs: S1 does not state what routing takes as input.
- `concepts/timing-violations.md` Definition: S1 uses slack, setup, and hold
  without defining them. Expected from S2 and S3.
- `concepts/antenna-violation.md` Why it matters: S1 gives the rule, not the
  damage it prevents. Expected from S2.
- `tools/yosys.md`, `formats/gdsii.md`, `formats/odb.md` What it is: S1 only
  names them. Expected from S4, S5, S6.
- Stages 1–3 (specification, RTL design, functional verification) have no
  page: S1 starts from finished RTL. Expected from S8–S11.

## [2026-11-12] ingest | S2 LibreLane Newcomers' Tutorial

- Created (15): source page `sources/s2-librelane-newcomers-tutorial.md`;
  stages `rtl-design`, `functional-verification`, `signoff`; concepts
  `asic-design-flow`, `netlist`, `drc`, `lvs`, `static-timing-analysis`,
  `timing-corners`; tools `librelane`, `klayout`, `magic`, `netgen`;
  format `def`.
- Updated (13): stages `logic-synthesis`, `floorplanning`, `routing`,
  `layout-finishing`; concepts `timing-violations`, `antenna-violation`,
  `ppa`; tools `openroad`, `yosys`; formats `gdsii`, `sdc`, `odb`; and
  `index.md`.
- Gaps closed: `logic-synthesis` Purpose, `timing-violations` Definition,
  `antenna-violation` Why it matters, `odb` What it is.

## [2026-11-12] conflict | S1 and S2 divide the flow differently

Recorded in `concepts/asic-design-flow.md`, Source differences.

- S2 has one physical implementation step with four sub-steps; S1 has four
  separate stages.
- S2 ends with a signoff step; S1 has no such stage and ends with layout
  generation.
- S2 starts at design entry; S1 starts from finished RTL.

## [2026-11-12] conflict | S1 and S2 place DRC at different points

Recorded in `concepts/drc.md`. S2: a signoff step with two tools. S1: a
report at the end of detailed routing.

## [2026-11-12] conflict | S1 and S2 word the antenna ratio differently

Recorded in `concepts/antenna-violation.md`. S1: gate area to gate oxide
area. S2: charge-collecting area to thin-oxide area.

## [2026-11-12] decision | How stage pages are divided (needs owner review)

Stage pages keep S1's finer division (floorplanning, placement, clock tree
synthesis, routing as four pages) and add S2's design entry, functional
verification, and signoff as pages of their own. Neither source is declared
right; the difference stays visible on `concepts/asic-design-flow.md`.
`layout-finishing` (S1) and `signoff` (S2) are separate pages for now.

## [2026-11-12] decision | Terminology after S2

Added: clock tree synthesis (not clock-tree synthesis), signoff, tape-out,
physical implementation (S2 also writes Layout/Physical Synthesis and PnR;
the aliases are listed once on `concepts/asic-design-flow.md`).

## [2026-11-12] gap | Open after S2

- Stage 1, specification: still no page. S2 only mentions requirements in
  passing. Expected from S8.
- `stages/rtl-design.md` Inputs and What happens. Expected from S8, S9.
- `stages/functional-verification.md` Outputs and Checks. Expected from S7,
  S10, S11.
- `stages/routing.md` Inputs: still open.
- `tools/yosys.md`, `tools/magic.md`, `formats/gdsii.md`, `formats/def.md`
  What it is: only named so far. Expected from S4, S5, S6.
- Placement and clock tree synthesis: S2 adds nothing; both rest on S1 only.

## [2026-11-12] decision | Owner review of S1 and S2

The owner read the wiki after two ingests and approved: the division of
stage pages; adding an independent faithfulness review to the ingest
workflow (AGENTS.md section 8, step 6), because the lint passed on the
first round twice while twelve unfaithful statements had to be caught by
hand; and extending S7 with the Simulating chapter of the same guide.

## [2026-11-12] ingest | S3 LibreLane: Achieving Timing Closure

- Created (6): source page; concepts `timing-closure`, `timing-paths`,
  `clock-skew`, `standard-cell-library`; format `sdf`.
- Updated (8): concepts `timing-violations`, `static-timing-analysis`,
  `asic-design-flow` (alias); stages `clock-tree-synthesis`, `placement`,
  `functional-verification`; format `sdc`; tool `librelane`; and `index.md`.
- Conflicts: none. S3 agrees with S1 that hold repair may be allowed to
  create setup violations only on request, and with S2 on the STA steps.
- Terminology: standard cell library (not SCL); "Place and Route" added as
  a variant of physical implementation.
- License: the S3 page declares itself CC-BY-SA 4.0, unlike the rest of its
  repository; noted in `raw/sources.json`.
- Gaps: none closed; `routing` Inputs still open. New: a general
  definition of a standard cell library (expected from S4, S6).

## [2026-11-12] ingest | S4 LibreLane Glossary

- Created (6): source page; concepts `pdk`, `rtl`, `tape-out`; formats
  `lef`, `dotlib`.
- Updated (19): concepts `netlist`, `drc`, `lvs`, `static-timing-analysis`,
  `timing-closure`, `timing-corners`, `asic-design-flow`,
  `standard-cell-library`; formats `gdsii`, `def`, `sdc`, `spef`, `sdf`;
  tools `klayout`, `magic`, `netgen`, `yosys`, `openroad`, `librelane`;
  and `index.md`.
- Gaps closed: `gdsii`, `def`, `magic`, `yosys` What it is.
- Citations to this source use the glossary term as the section name.

## [2026-11-12] conflict | S3 and S4 define timing closure differently

Recorded in `concepts/timing-closure.md`. S3: a process. S4: a state.

## [2026-11-12] conflict | S2 and S4 give PnR different scopes

Recorded in `concepts/asic-design-flow.md`. S2: the whole physical
implementation step. S4: placement and routing only.

## [2026-11-12] decision | Terminology after S4

The `.lib` page is named Dotlib, the word S4 uses. A first draft named it
Liberty, a name that appears in no ingested source; corrected before review.

## [2026-11-12] ingest | S5 Yosys: A primer on digital circuit synthesis

- Created (3): source page; concepts `levels-of-abstraction`,
  `technology-mapping`.
- Updated (8): stages `logic-synthesis`, `rtl-design`,
  `functional-verification`; concepts `rtl`, `netlist`, `asic-design-flow`;
  tool `yosys`; and `index.md`.
- Gaps closed: `rtl-design` Inputs and What happens.
- Not used: the section on compiler methods (lexing, parsing), below
  overview depth.
- Terminology: behavioral (S5 writes behavioural), combinational (S5 writes
  combinatorial).

## [2026-11-12] conflict | S4 and S5 place behavioral description differently

Recorded in `concepts/rtl.md`. S4 treats behavioral models and RTL as one
level; S5 has a behavioral level above RTL.

## [2026-11-12] decision | Lint bug fixed during S5

`scripts/lint_wiki.py` treated a reStructuredText heading underline made of
`~` as a markdown code fence, so it could not see about half of the
headings in `.rst` sources and reported 22 valid S5 citations as invalid.
Fence handling now applies to `.md` files only. No rule changed. The owner
is told in the hand-over.

## [2026-11-12] ingest | S6 SkyWater SKY130 PDK: Libraries and File Types

- Created (1): source page.
- Updated (9): concepts `pdk`, `standard-cell-library`, `drc`, `lvs`;
  formats `lef`, `dotlib`; tools `magic`, `netgen`; and `index.md`.
- The File Types page is one table with a single heading, so every
  citation to it is `[S6 §File Types]`: section-level precision is not
  available for this source.
- The name Liberty for the timing file format does appear here, so it is
  now listed as an alias on `formats/dotlib.md`.
- Gap still open: a general definition of a standard cell library.

## [2026-11-12] conflict | S4 and S6 expand LEF differently

Recorded in `formats/lef.md`. S4: Layout Exchange Format. S6: Library
Exchange Format.
