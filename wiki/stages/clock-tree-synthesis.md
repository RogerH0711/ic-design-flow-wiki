---
title: Clock Tree Synthesis
type: stage
order: 7
sources: [S1]
updated: 2026-11-12
---

# Clock Tree Synthesis

Also called: CTS

## Purpose

Clock tree synthesis builds a well-balanced clock tree once placement is finished. [S1 §Clock Tree Synthesis]

## Inputs

- The placed design: the flow generates the clock tree after placement. [S1 §Clock Tree Synthesis]

## Outputs

- `4_cts.odb`, `4_cts.sdc`, and `4_cts.v`. [S1 §Viewing OpenROAD-flow-scripts Directory Structure And Results]
- `final_clocks.webp`, an image of the design after clock tree synthesis. [S1 §Viewing OpenROAD-flow-scripts Directory Structure And Results]

## What happens

- Clock buffers are inserted so that the tree structure is balanced. [S1 §Clock Tree Synthesis]
- Timing repair for setup and hold violations runs after this stage, with propagated clocks. [S1 §Timing Optimization Using repair_timing]
- The stage's second log is `4_2_cts_fillcell.log`. [S1 §Viewing Results And Logs]
- Filler cells close the gaps between placed cells so that the power and ground rails run unbroken along each row. [S1 §Adding Filler Cells]

## Checks

- Clock skew is reported; the flow fixes skew problems that could later cause hold violations. [S1 §Reporting Clock Skews]
- A metrics report lists the number of clock roots, inserted buffers, clock subnets, and sinks. [S1 §Reporting CTS Metrics]
- The balanced tree can be inspected in a clock tree viewer. [S1 §Clock Tree Synthesis]

## Related pages

- [Placement](placement.md)
- [Routing](routing.md)
- [Timing Violations](../concepts/timing-violations.md)
- [Tap, Endcap, Tie, and Filler Cells](../concepts/tap-endcap-tie-filler-cells.md)
