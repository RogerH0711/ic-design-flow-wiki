---
title: "S7: Verilator User's Guide, Overview and Simulating"
type: source
source_id: S7
sources: [S7]
updated: 2026-11-12
---

# S7: Verilator User's Guide, Overview and Simulating

## Summary

Two chapters of the Verilator guide. The overview says what Verilator is, a compiler that turns a hardware description into an executable model, and lists the steps of using it. [S7 §Overview]

The simulating chapter covers running such a model: the summary it prints, performance tuning, coverage, and profiling. [S7 §Simulating (Verilated-Model Runtime)]

## Key points

- Verilator's output is not a simulation result but a model, in C++ or SystemC, which must be compiled before it can run. [S7 §Overview]
- While reading the code it also lints it, and it can add support for coverage and for waveform traces. [S7 §Overview]
- Six forms of coverage can be enabled together: property, covergroup, FSM, line, branch, and toggle. [S7 §Coverage Analysis]
- Each test writes a coverage file, and a separate command merges the files into an annotated listing of the source. [S7 §Coverage Collection]

## Coverage

- The simulating chapter has a section on options and compiler flags for performance. [S7 §Benchmarking & Optimization]

## Related pages

- [Verilator](../tools/verilator.md)
- [Coverage](../concepts/coverage.md)
- [Functional Verification](../stages/functional-verification.md)
- [RTL Design](../stages/rtl-design.md)
