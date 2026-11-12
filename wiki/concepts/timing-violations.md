---
title: Timing Violations
type: concept
sources: [S1]
updated: 2026-11-12
---

# Timing Violations

## Definition

Timing results are summarized with three numbers: the worst slack, the total negative slack (TNS), and the worst negative slack (WNS). [S1 §Timing]

Violations come in two kinds, setup and hold, and the flow has a repair step for each. [S1 §Timing Optimization Using repair_timing]

_Not yet covered by an ingested source._

## Why it matters

- Timing is one of the stated design goals; for the `ibex` example it is a clock period that must be met. [S1 §Design Goals]
- Setup and hold are analyzed at different corners: setup optimization uses the slow corner and hold optimization uses the fast corner. [S1 §Timing Optimization Based On Multiple Corners]
- Repairing a hold violation by adding buffers can create a setup violation, so by default the repair step will not do that. [S1 §Timing Optimization Using repair_timing]
- A setup violation can also be removed by lengthening the clock period, that is, by lowering the clock frequency. [S1 §Fixing Setup Violations]
- The flow repairs such violations automatically after clock tree synthesis and after global routing. [S1 §Fixing Setup Violations]

## Related pages

- [Placement](../stages/placement.md)
- [Clock Tree Synthesis](../stages/clock-tree-synthesis.md)
- [Layout Finishing](../stages/layout-finishing.md)
- [PPA](ppa.md)
