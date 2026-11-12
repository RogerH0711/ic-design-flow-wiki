---
title: SDF
type: format
sources: [S2, S3]
updated: 2026-11-12
---

# SDF

Also called: Standard Delay Format

## What it is

SDF is a standardized (IEEE) way of writing down timing data so that it can be exchanged between steps of the design process. One file covers the timing of every cell in the design. [S3 §SDF Annotated GL Simulation using CVC]

## Produced by and used by

- SDF files are typically written by static timing analysis tools. [S3 §SDF Annotated GL Simulation using CVC]
- Simulators read them to simulate the gate-level netlist with timing. [S3 §SDF Annotated GL Simulation using CVC]
- If such a simulation shows violations that static timing analysis did not, the design was not constrained properly and the flow has to be rerun. [S3 §SDF Annotated GL Simulation using CVC]
- The LibreLane reference flow writes one among its final results. [S2 §Final Results]

## Related pages

- [Functional Verification](../stages/functional-verification.md)
- [Static Timing Analysis](../concepts/static-timing-analysis.md)
- [Netlist](../concepts/netlist.md)
