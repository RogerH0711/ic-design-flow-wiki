---
title: SDC
type: format
sources: [S1]
updated: 2026-11-12
---

# SDC

## What it is

An `.sdc` file holds the timing constraints of a design. [S1 §Timing Constraints]

The least it must contain is a clock definition: a named clock, its period, and the port it enters through. [S1 §Timing Constraints]

## Produced by and used by

- The designer supplies it; the design configuration points to it with `SDC_FILE`. [S1 §Design Configuration]
- Every stage writes its own copy next to its other results, from `1_synth.sdc` to `6_final.sdc`. [S1 §Viewing OpenROAD-flow-scripts Directory Structure And Results]

## Related pages

- [Logic Synthesis](../stages/logic-synthesis.md)
- [Timing Violations](../concepts/timing-violations.md)
