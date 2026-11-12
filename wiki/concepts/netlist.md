---
title: Netlist
type: concept
sources: [S2]
updated: 2026-11-12
---

# Netlist

## Definition

A netlist is the circuit of logic cells that synthesis produces from a hardware description. [S2 §Newcomers' Tutorial]

## Why it matters

- It is what physical implementation turns into a layout. [S2 §Newcomers' Tutorial]
- It has to be verified too: functional verification is applied to the gate-level netlist as well as to the RTL. [S2 §Newcomers' Tutorial]
- Flow steps write the current gate-level netlist as Verilog in two forms, one without power connections and one with them. [S2 §Run directory]
- At signoff, the layout is compared against the schematic, which is usually given as Verilog. [S2 §LVS]

## Related pages

- [Logic Synthesis](../stages/logic-synthesis.md)
- [Functional Verification](../stages/functional-verification.md)
- [ASIC Design Flow](asic-design-flow.md)
- [LVS](lvs.md)
