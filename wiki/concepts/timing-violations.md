---
title: Timing Violations
type: concept
sources: [S1, S2, S3]
updated: 2026-11-12
---

# Timing Violations

## Definition

A timing violation exists when data reaches the end of a timing path at the wrong moment compared with when it is required. It shows up as negative slack. [S2 §STA]

- Setup violation: the data arrives after it is required. [S2 §STA]
- Hold violation: the data arrives before it is required. [S2 §STA]

Both come from what a flip-flop needs: its input must be stable for some time before the clock edge (the setup time) and for some time after it (the hold time). [S3 §Introduction]

Timing results are summarized with three numbers: the worst slack, the total negative slack (TNS), and the worst negative slack (WNS). [S1 §Timing]

The flow has a repair step for each kind of violation. [S1 §Timing Optimization Using repair_timing]

## Why it matters

- A flip-flop whose setup or hold time is not respected becomes metastable: the value it stores is unknown, and so is the state of the whole system. [S3 §Introduction]
- When the clock frequency is not fixed by a specification, hold violations come first, because a setup violation can be removed by adjusting the clock period while a hold violation can leave the chip non-functional. [S3 §Tips for Achieving Timing Closure]
- Maximum capacitance and maximum transition violations are tolerable when there are no setup or hold violations, but they are worth checking as signs of design problems. [S3 §Tips for Achieving Timing Closure]
- Timing is one of the stated design goals; for the `ibex` example it is a clock period that must be met. [S1 §Design Goals]
- Setup and hold are analyzed at different [timing corners](timing-corners.md): setup optimization uses the slow corner and hold optimization uses the fast corner. [S1 §Timing Optimization Based On Multiple Corners]
- Repairing a hold violation by adding buffers can create a setup violation, so by default the repair step will not do that. [S1 §Timing Optimization Using repair_timing]
- A setup violation can also be removed by lengthening the clock period, that is, by lowering the clock frequency. [S1 §Fixing Setup Violations]
- The flow repairs such violations automatically after clock tree synthesis and after global routing. [S1 §Fixing Setup Violations]

## Related pages

- [Timing Closure](timing-closure.md)
- [Timing Paths](timing-paths.md)
- [Clock Skew](clock-skew.md)
- [Static Timing Analysis](static-timing-analysis.md)
- [Timing Corners](timing-corners.md)
- [Signoff](../stages/signoff.md)
- [Placement](../stages/placement.md)
- [Clock Tree Synthesis](../stages/clock-tree-synthesis.md)
- [Layout Finishing](../stages/layout-finishing.md)
- [PPA](ppa.md)
