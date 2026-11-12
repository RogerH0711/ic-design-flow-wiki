---
title: PPA
type: concept
sources: [S1]
updated: 2026-11-12
---

# PPA

## Definition

PPA is the shorthand the flow tutorial uses for the three goals a design is optimized for: area, timing, and power. [S1 §Understanding and Analyzing OpenROAD Flow Stages and Results]

## Why it matters

- The flow can run without supervision, but a user who wants good PPA still explores different configurations and optimizations stage by stage. [S1 §Understanding and Analyzing OpenROAD Flow Stages and Results]
- Design goals are written in these terms. For the `ibex` example they are a die and core size (area) and a clock period of 17.4 ns (timing). [S1 §Design Goals]
- After the flow, the same three quantities are reported: area [S1 §Area], timing [S1 §Timing], and power. [S1 §Power]

## Related pages

- [ASIC Design Flow](asic-design-flow.md)
- [Logic Synthesis](../stages/logic-synthesis.md)
- [Layout Finishing](../stages/layout-finishing.md)
- [Timing Violations](timing-violations.md)
- [Core Utilization and Placement Density](placement-density.md)
