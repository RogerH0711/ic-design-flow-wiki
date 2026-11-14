---
title: SDC
type: format
sources: [S1, S2, S3, S4]
updated: 2026-11-12
---

# SDC

## What it is

An `.sdc` file holds the timing constraints of a design. [S1 §Timing Constraints]

The constraints state the designer's intent so that the tools can optimize and analyze the design. They are written as Tcl-based statements in an industry-standard format called SDC (Synopsys Design Constraints). [S3 §Timing Constraints]

Basic constraints are the clock definition, the delays of input and output ports relative to the clock, the load on output ports, and the cells driving the input ports. The format also expresses timing exceptions: false paths and multi-cycle paths. [S3 §Timing Constraints]

The least it must contain is a clock definition: a named clock, its period, and the port it enters through. [S1 §Timing Constraints]

The glossary describes it more broadly, as a format for telling EDA tools the design's requirements, including timing, power, and area. [S4 §SDC]

## Produced by and used by

- The designer supplies it; the design configuration points to it with `SDC_FILE`. [S1 §Design Configuration]
- Every stage writes its own copy next to its other results, from `1_synth.sdc` to `6_final.sdc`. [S1 §Viewing OpenROAD-flow-scripts Directory Structure And Results]
- In the LibreLane tutorial's example, a step directory likewise contains the constraints currently on the design. [S2 §Run directory]
- LibreLane sets some constraints from its configuration, but completing them in a custom SDC file is the designer's job. Separate files can be given for implementation and for signoff, so that implementation can be constrained more tightly than the final analysis. [S3 §Tips for Achieving Timing Closure]
- Static timing analysis inspects the constraints themselves, for example for ports with no input delay or registers with no clock. [S2 §STA]

## Related pages

- [Logic Synthesis](../stages/logic-synthesis.md)
- [Timing Violations](../concepts/timing-violations.md)
- [Timing Paths](../concepts/timing-paths.md)
- [Timing Closure](../concepts/timing-closure.md)
- [Static Timing Analysis](../concepts/static-timing-analysis.md)
