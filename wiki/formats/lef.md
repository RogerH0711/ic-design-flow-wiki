---
title: LEF
type: format
sources: [S1, S2, S4]
updated: 2026-11-12
---

# LEF

Also called: Layout Exchange Format

## What it is

LEF is an abstract view of pre-hardened macros and standard cells. It records a cell's dimensions, the positions of its pins, and its shapes on the metal layers. [S4 §LEF]

## Produced by and used by

- When a design is hardened, a LEF view of it is generated from its DEF view. [S4 §DEF]
- Together with DEF it can stand for the layout in LVS. [S2 §LVS]
- Parasitics extraction works from the LEF/DEF model of the routed design. [S1 §Parasitics Extraction]

## Related pages

- [DEF](def.md)
- [GDSII](gdsii.md)
- [PDK](../concepts/pdk.md)
- [Standard Cell Library](../concepts/standard-cell-library.md)
