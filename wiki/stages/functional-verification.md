---
title: Functional Verification
type: stage
order: 3
sources: [S2, S3, S5, S7]
updated: 2026-11-12
---

# Functional Verification

## Purpose

Functional verification makes sure that the design behaves as its requirements say it should. [S2 §Newcomers' Tutorial]

## Inputs

- The RTL, and later the gate-level [netlist](../concepts/netlist.md): the tutorial calls it essential to verify both. [S2 §Newcomers' Tutorial]

## Outputs

- With Verilator, if enabled, the simulation executable can produce waveform traces of the design for viewing and [coverage](../concepts/coverage.md) data for later analysis. [S7 §Overview]

## What happens

- Two techniques are combined: simulation of the hardware description, and formal verification. [S2 §Newcomers' Tutorial]
- At the end of implementation, simulating the final gate-level netlist with [SDF](../formats/sdf.md) delay annotations is recommended; it is the closest thing to the behavior of the fabricated chip. [S3 §Tips for Achieving Timing Closure]
- Such timing simulation is slow and cannot replace static timing analysis, but it helps to uncover and validate false paths. [S3 §SDF Annotated GL Simulation using CVC]

- The hand-written description is checked against the higher-level model by simulating both and comparing the results. [S5 §Script-based synthesis flows]
- The check is repeated at each lower level and after every change to a model. [S5 §Script-based synthesis flows]

- Design code is read by the synthesis tool, by simulators, and sometimes by a formal verification tool, so all of them must interpret it in the same way. [S5 §Standards compliance]

## Checks

- After all tests have run, Verilator's coverage command produces a source listing annotated with coverage details, in which the lines it believes need more coverage are marked. [S7 §Coverage Collection]

## Related pages

- [ASIC Design Flow](../concepts/asic-design-flow.md)
- [RTL Design](rtl-design.md)
- [Logic Synthesis](logic-synthesis.md)
- [Netlist](../concepts/netlist.md)
- [SDF](../formats/sdf.md)
- [Coverage](../concepts/coverage.md)
- [Verilator](../tools/verilator.md)
