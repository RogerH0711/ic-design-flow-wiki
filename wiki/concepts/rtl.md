---
title: RTL
type: concept
sources: [S4, S5, S9]
updated: 2026-11-12
---

# RTL

Also called: Register-Transfer Level

## Definition

The register-transfer level (RTL) is a way of describing a circuit at a high level in a hardware description language. Lower-level descriptions, and eventually the real wiring, are derived from it. [S4 §RTL]

A hardware description language (HDL) is a computer language for describing the structure or the behavior of a hardware chip. Verilog and VHDL are the best known. [S4 §HDL]

At this level a design consists of combinational data paths and registers. It is the first level at which the circuit is a graph of circuit elements and signals. [S5 §Register-Transfer Level (RTL)]

## Why it matters

- Designing at this level is the normal practice in modern digital design. [S4 §RTL]
- An HDL can describe hardware at several levels, from a list of every gate, which is a gate-level [netlist](netlist.md), up to more abstract behavioral models; a synthesis tool turns the abstract models into concrete netlists. [S4 §HDL]
- Verilog is most often used for designing and verifying digital circuits at this level. [S4 §Verilog]

- Keeping the design in an HDL at this level makes simulation simple, because no extra tool is needed. [S5 §Register-Transfer Level (RTL)]
- Many optimizations and analyses work best here, for example FSM detection and optimization. [S5 §Register-Transfer Level (RTL)]

- The same language allows widely differing styles, which leads to code conflicts and slow reviews; the lowRISC style guide answers this with rules for synthesizable code and test bench code alike. [S9 §Summary]
- That guide prefers flip-flops and discourages latches. [S9 §Sequential Logic (Latches)]

## Source differences

- Where behavioral description sits: S4 speaks of abstract behavioral models and the register-transfer level as the same thing [S4 §HDL], while S5 describes them as two levels: its own tool takes a behavioral description as input and can produce a register-transfer level description as output. [S5 §Yosys]

## Related pages

- [RTL Design](../stages/rtl-design.md)
- [Logic Synthesis](../stages/logic-synthesis.md)
- [Netlist](netlist.md)
- [Levels of Abstraction](levels-of-abstraction.md)
