---
title: Routing
type: stage
order: 8
sources: [S1, S2]
updated: 2026-11-12
---

# Routing

## Purpose

Routing is done in two passes. Global routing shares out the available routing resources, and only a design that passes it without violations goes on to detailed routing. [S1 §Global Routing]

## Inputs

_Not yet covered by an ingested source._

## Outputs

- `5_route.odb` and `5_route.sdc`, together with `route.guide`. [S1 §Viewing OpenROAD-flow-scripts Directory Structure And Results]
- `congestion.rpt` for global routing congestion and `5_route_drc.rpt` for design rule violations. [S1 §Viewing OpenROAD-flow-scripts Directory Structure And Results]

## What happens

- The global router analyzes the routing resources and allocates them so that no region overflows in the horizontal or vertical direction. [S1 §Global Routing]
- The detailed router works through pin access analysis, track assignment, an initial detailed routing, and search and repair, and has its own design rule checking engine. [S1 §Detail Routing]
- An antenna check reports the nets with an [antenna violation](../concepts/antenna-violation.md). [S1 §Antenna Checker]
- In the LibreLane reference flow the antenna check runs right after global routing and again as part of an antenna repair step, so that the effect of the repair can be seen. [S2 §Antenna Check]
- That repair inserts an antenna diode, a standard cell, next to each cell input pin that is affected. [S2 §Antenna Check]

## Checks

- The global router's congestion report lists, for each GCell, the total resources, the demand, the utilization, the location, and whether there is a violation. [S1 §Global Routing]
- A successful detailed routing run ends with zero violations. [S1 §Detail Routing]
- Any design rule violation left after routing is written to `5_route_drc.rpt`; the file is empty otherwise. [S1 §DRC Viewer]

## Common problems

- Congestion: a design with too much routing demand makes global routing stop with an error. A congestion heat map shows where the problem is. [S1 §Debugging Problems in Global Routing]
- The congestion data can also be written to a text file for closer inspection. [S1 §Dump congestion information to a text file]

## Related pages

- [Clock Tree Synthesis](clock-tree-synthesis.md)
- [Layout Finishing](layout-finishing.md)
- [Signoff](signoff.md)
- [DRC](../concepts/drc.md)
- [ASIC Design Flow](../concepts/asic-design-flow.md)
- [Antenna Violation](../concepts/antenna-violation.md)
- [OpenROAD](../tools/openroad.md)
