---
title: Yosys
type: tool
sources: [S1, S2, S4, S5]
updated: 2026-11-12
---

# Yosys

## What it is

Yosys is described as a framework on which RTL synthesis tools are built; it supports most of Verilog-2005. [S4 §Yosys]

The flow tutorial lists it for the synthesis step. [S1 §Running The Automated RTL-to-GDS Flow]

In its own documentation Yosys is a Verilog synthesis tool: it takes a behavioral design description and produces a description at the register-transfer, logical gate, or physical gate level. [S5 §Yosys]

## Role in the flow

- It runs first: its log, `1_1_yosys.log`, carries the lowest prefix in the flow. [S1 §Viewing Results And Logs]
- Its result, `1_1_yosys.v`, is the first file in the results directory. [S1 §Viewing OpenROAD-flow-scripts Directory Structure And Results]
- Two options choose between optimizing for area and optimizing for speed. [S1 §Area And Timing Optimization]
- The LibreLane reference flow uses it for synthesis too; the step directory is `06-yosys-synthesis`. [S2 §Run directory]

- For the logic synthesis step it can use a separate tool, ABC, which is the recommended choice. [S5 §Logical gate level]

## Related pages

- [Logic Synthesis](../stages/logic-synthesis.md)
- [OpenROAD Flow Scripts](openroad-flow-scripts.md)
- [LibreLane](librelane.md)
- [Netlist](../concepts/netlist.md)
- [Levels of Abstraction](../concepts/levels-of-abstraction.md)
