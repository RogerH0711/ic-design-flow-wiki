---
title: GDSII
type: format
sources: [S1, S2, S4]
updated: 2026-11-12
---

# GDSII

Also called: GDS, Graphic Design System II

## What it is

The `.gds` file is the end product of the flow: everything from synthesis onward leads up to its creation. [S1 §Running The Automated RTL-to-GDS Flow]

GDSII is a binary stream format and the de facto industry standard for exchanging IC layout data. A file holds planar geometric shapes, text labels, and other layout information, organized as a hierarchy, with every detail the manufacturer needs. [S4 §GDSII]

## Produced by and used by

- The last stage writes a merged file, `6_1_merged.gds`, and copies it to `6_final.gds`. [S1 §Viewing OpenROAD-flow-scripts Directory Structure And Results]
- The final layout can be opened in [KLayout](../tools/klayout.md). [S2 §Viewing the Layout]
- LVS can take the layout in this form. [S2 §LVS]

- Masks are made from it at [tape-out](../concepts/tape-out.md). [S4 §tape-out]
- For tape-out it has been replaced by a more compact format, OASIS; LibreLane still uses GDSII because open-source tools support it better, although shuttle providers generally ask for OASIS. [S4 §GDSII]
- When a design is hardened, its GDSII view is generated from the DEF view. [S4 §DEF]

## Related pages

- [Layout Finishing](../stages/layout-finishing.md)
- [Signoff](../stages/signoff.md)
- [KLayout](../tools/klayout.md)
- [DEF](def.md)
- [Tape-out](../concepts/tape-out.md)
