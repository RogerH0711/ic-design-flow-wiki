---
title: ODB
type: format
sources: [S1]
updated: 2026-11-12
---

# ODB

## What it is

`.odb` is one of the file types the flow leaves in its results directory, next to `.v`, `.sdc`, `.def`, and `.spef` files. [S1 §Viewing OpenROAD-flow-scripts Directory Structure And Results]

The flow's list of components has a Database entry, documented under the name `odb`. [S1 §Running The Automated RTL-to-GDS Flow]

_Not yet covered by an ingested source._

## Produced by and used by

- From floorplanning onward, every sub-step saves one, for example `2_1_floorplan.odb` or `5_route.odb`. [S1 §Viewing OpenROAD-flow-scripts Directory Structure And Results]
- Parasitics extraction works through the database (OpenDB) and stores its results on the database objects. [S1 §Parasitics Extraction]

## Related pages

- [Floorplanning](../stages/floorplanning.md)
- [Placement](../stages/placement.md)
- [OpenROAD](../tools/openroad.md)
