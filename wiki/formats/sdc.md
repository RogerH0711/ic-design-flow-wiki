---
title: SDC
type: format
sources: [S1, S2]
updated: 2026-11-12
---

# SDC

## What it is

An `.sdc` file holds the timing constraints of a design. [S1 §Timing Constraints]

The least it must contain is a clock definition: a named clock, its period, and the port it enters through. [S1 §Timing Constraints]

## Produced by and used by

- The designer supplies it; the design configuration points to it with `SDC_FILE`. [S1 §Design Configuration]
- Every stage writes its own copy next to its other results, from `1_synth.sdc` to `6_final.sdc`. [S1 §Viewing OpenROAD-flow-scripts Directory Structure And Results]
- LibreLane steps likewise save the constraints currently applied to the design. [S2 §Run directory]
- Static timing analysis inspects the constraints themselves, for example for ports with no input delay or registers with no clock. [S2 §STA]

## Related pages

- [Logic Synthesis](../stages/logic-synthesis.md)
- [Timing Violations](../concepts/timing-violations.md)
- [Static Timing Analysis](../concepts/static-timing-analysis.md)
