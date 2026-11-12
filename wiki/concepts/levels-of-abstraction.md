---
title: Levels of Abstraction
type: concept
sources: [S5]
updated: 2026-11-12
---

# Levels of Abstraction

## Definition

A digital circuit can be represented at several levels of abstraction. A design usually starts at a higher level, and implementing it means finding a functionally equivalent representation at a lower one. [S5 §Levels of abstraction]

The synthesis primer then describes the levels one by one; they are listed here in its order. [S5 §Levels of abstraction]

1. System level: only the largest building blocks, such as CPUs, usually written in an ordinary programming language. [S5 §System level]
2. High level, sometimes called algorithmic level: ordinary programming languages again, with a reduced set of features. [S5 §High level]
3. Behavioral level: a hardware description language, with imperative code describing data paths and registers in at least part of the description. [S5 §Behavioural level]
4. Register-transfer level: combinational data paths and registers, usually D-type flip-flops. See [RTL](rtl.md). [S5 §Register-Transfer Level (RTL)]
5. Logical gate level: a [netlist](netlist.md) that uses only a small set of single-bit cells, such as basic logic gates and registers. [S5 §Logical gate level]
6. Physical gate level: only gates that really exist on the target. Sometimes that is just NAND, NOR, and NOT gates with registers; sometimes it includes cells more complex than the logical ones. [S5 §Physical gate level]
7. Switch level: a netlist whose cells are single transistors, seldom used in modern designs. [S5 §Switch level]

## Why it matters

- Each step down can be done by a tool, in which case it is called synthesis, or by hand. [S5 §Levels of abstraction]
- Either way, the lower-level result is usually verified by comparing its simulation results with those of the higher level, so every level needs a representation that can be simulated. [S5 §Levels of abstraction]
- Synthesis tool chains usually stop at the physical gate level and go no lower. [S5 §Physical gate level]

## Related pages

- [RTL](rtl.md)
- [Netlist](netlist.md)
- [Technology Mapping](technology-mapping.md)
- [Logic Synthesis](../stages/logic-synthesis.md)
- [RTL Design](../stages/rtl-design.md)
