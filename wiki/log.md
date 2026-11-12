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
