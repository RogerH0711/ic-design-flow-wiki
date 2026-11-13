---
title: Verilator
type: tool
sources: [S2, S3, S7, S10]
updated: 2026-11-12
---

# Verilator

## What it is

Verilator converts a design written in Verilog or SystemVerilog into a C++ or SystemC model which, once compiled, can be run. It describes itself as a compiler and not a traditional simulator. [S7 §Overview]

## Role in the flow

- Simulation with it takes a few steps: Verilator produces the model, the user writes a small C++ wrapper that instantiates it, everything is compiled into an executable, and running that executable performs the simulation. [S7 §Overview]
- It lints the code it reads. [S7 §Overview]
- The LibreLane flow uses it for exactly that: its first step is a Verilator lint run. [S2 §Run directory]
- The executable can write waveform traces for viewing and [coverage](../concepts/coverage.md) data for later analysis. [S7 §Overview]
- When a simulation ends, a model built with the right option prints a summary with the simulated time reached, the wall-clock time, and the simulation speed. [S7 §Simulation Summary Report]
- It does not support SDF, so it cannot run gate-level simulation with timing. [S3 §SDF Annotated GL Simulation using CVC]

- The OpenTitan project promotes it as an open-source verification tool, while a different simulator remains its tool for signoff. [S10 §Language and Tool Selection]

## Related pages

- [Functional Verification](../stages/functional-verification.md)
- [RTL Design](../stages/rtl-design.md)
- [Coverage](../concepts/coverage.md)
- [LibreLane](librelane.md)
