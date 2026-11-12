---
title: Functional Verification
type: stage
order: 3
sources: [S2, S3]
updated: 2026-11-12
---

# Functional Verification

## Purpose

Functional verification makes sure that the design behaves as its requirements say it should. [S2 §Newcomers' Tutorial]

## Inputs

- The RTL, and later the gate-level [netlist](../concepts/netlist.md): the tutorial calls it essential to verify both. [S2 §Newcomers' Tutorial]

## Outputs

_Not yet covered by an ingested source._

## What happens

- Two techniques are combined: simulation of the hardware description, and formal verification. [S2 §Newcomers' Tutorial]
- At the end of implementation, simulating the final gate-level netlist with [SDF](../formats/sdf.md) delay annotations is recommended; it is the closest thing to the behavior of the fabricated chip. [S3 §Tips for Achieving Timing Closure]
- Such timing simulation is slow and cannot replace static timing analysis, but it helps to uncover and validate false paths. [S3 §SDF Annotated GL Simulation using CVC]

## Checks

_Not yet covered by an ingested source._

## Related pages

- [ASIC Design Flow](../concepts/asic-design-flow.md)
- [RTL Design](rtl-design.md)
- [Logic Synthesis](logic-synthesis.md)
- [Netlist](../concepts/netlist.md)
- [SDF](../formats/sdf.md)
