---
title: GDSII
type: format
sources: [S1, S2]
updated: 2026-11-12
---

# GDSII

Also called: GDS

## What it is

The `.gds` file is the end product of the flow: everything from synthesis onward leads up to its creation. [S1 §Running The Automated RTL-to-GDS Flow]

_Not yet covered by an ingested source._

## Produced by and used by

- The last stage writes a merged file, `6_1_merged.gds`, and copies it to `6_final.gds`. [S1 §Viewing OpenROAD-flow-scripts Directory Structure And Results]
- The final layout can be opened in [KLayout](../tools/klayout.md). [S2 §Viewing the Layout]
- LVS can take the layout in this form. [S2 §LVS]

## Related pages

- [Layout Finishing](../stages/layout-finishing.md)
- [Signoff](../stages/signoff.md)
- [KLayout](../tools/klayout.md)
- [DEF](def.md)
