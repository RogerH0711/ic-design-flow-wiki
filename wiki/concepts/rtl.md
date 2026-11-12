---
title: RTL
type: concept
sources: [S4]
updated: 2026-11-12
---

# RTL

Also called: Register-Transfer Level

## Definition

The register-transfer level (RTL) is a way of describing a circuit at a high level in a hardware description language. Lower-level descriptions, and eventually the real wiring, are derived from it. [S4 §RTL]

A hardware description language (HDL) is a computer language for describing the structure or the behavior of a hardware chip. Verilog and VHDL are the best known. [S4 §HDL]

## Why it matters

- Designing at this level is the normal practice in modern digital design. [S4 §RTL]
- An HDL can describe hardware at several levels, from a list of every gate, which is a gate-level [netlist](netlist.md), up to more abstract behavioral models; a synthesis tool turns the abstract models into concrete netlists. [S4 §HDL]
- Verilog is most often used for designing and verifying digital circuits at this level. [S4 §Verilog]

## Related pages

- [RTL Design](../stages/rtl-design.md)
- [Logic Synthesis](../stages/logic-synthesis.md)
- [Netlist](netlist.md)
