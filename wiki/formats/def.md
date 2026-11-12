---
title: DEF
type: format
sources: [S1, S2, S4]
updated: 2026-11-12
---

# DEF

Also called: Design Exchange Format

## What it is

A `.def` file holds the current state of the layout. [S2 §Run directory]

DEF is an abstract view of the design being worked on. It lists the instantiated cells and macros and every element on the metal layers, pins included. [S4 §DEF]

## Produced by and used by

- Flow steps save the layout in this format next to the database file. [S2 §Run directory]
- LVS can take the layout either as GDSII or as DEF together with LEF. [S2 §LVS]
- Parasitics extraction works from the LEF/DEF model of the routed design. [S1 §Parasitics Extraction]

- The DEF view is the starting point for two others: hardening a design produces its [LEF](lef.md) and GDSII views from it. [S4 §DEF]

## Related pages

- [ODB](odb.md)
- [GDSII](gdsii.md)
- [LVS](../concepts/lvs.md)
- [LEF](lef.md)
