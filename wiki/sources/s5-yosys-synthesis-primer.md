---
title: "S5: Yosys, A Primer on Digital Circuit Synthesis"
type: source
source_id: S5
sources: [S5]
updated: 2026-11-12
---

# S5: Yosys, A Primer on Digital Circuit Synthesis

## Summary

A chapter of the Yosys documentation that introduces the basic principles of digital circuit synthesis. [S5 §A primer on digital circuit synthesis]

It walks through the levels at which a circuit can be described [S5 §Levels of abstraction], reviews which parts of Verilog can be synthesized [S5 §Features of synthesizable Verilog], and summarizes the main challenges of synthesis. [S5 §Challenges in digital circuit synthesis]

## Key points

- Synthesis means that software produces the lower-level, functionally equivalent description of a circuit. [S5 §Levels of abstraction]
- A netlist is a graph of circuit elements and signals written down as a list of cells and connections. [S5 §Register-Transfer Level (RTL)]
- Logic synthesis has two problems to solve: optimizing the gate-level netlist, and mapping it onto the gates that physically exist. [S5 §Logical gate level]
- Technology mapping restricts the design to cells that the target architecture offers. [S5 §Technology mapping]
- Results at each lower level are verified again by simulation, and real projects go round this loop several times. [S5 §Script-based synthesis flows]

## Coverage

- Covered in detail: abstraction levels [S5 §Levels of abstraction] and synthesizable Verilog. [S5 §Features of synthesizable Verilog]
- Also contains a section on compiler techniques used inside synthesis tools, which is below the depth of this wiki and was not used. [S5 §Methods from compiler design]

## Related pages

- [Levels of Abstraction](../concepts/levels-of-abstraction.md)
- [Technology Mapping](../concepts/technology-mapping.md)
- [RTL](../concepts/rtl.md)
- [Netlist](../concepts/netlist.md)
- [Logic Synthesis](../stages/logic-synthesis.md)
- [RTL Design](../stages/rtl-design.md)
- [Functional Verification](../stages/functional-verification.md)
- [ASIC Design Flow](../concepts/asic-design-flow.md)
- [Yosys](../tools/yosys.md)
