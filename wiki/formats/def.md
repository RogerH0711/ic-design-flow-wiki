---
title: DEF
type: format
sources: [S1, S2]
updated: 2026-11-12
---

# DEF

## What it is

A `.def` file holds the current state of the layout. [S2 §Run directory]

_Not yet covered by an ingested source._

## Produced by and used by

- Flow steps save the layout in this format next to the database file. [S2 §Run directory]
- LVS can take the layout either as GDSII or as DEF together with LEF. [S2 §LVS]
- Parasitics extraction works from the LEF/DEF model of the routed design. [S1 §Parasitics Extraction]

## Related pages

- [ODB](odb.md)
- [GDSII](gdsii.md)
- [LVS](../concepts/lvs.md)
