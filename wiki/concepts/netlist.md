---
title: Netlist
type: concept
sources: [S2, S4]
updated: 2026-11-12
---

# Netlist

## Definition

A netlist is a representation of a circuit as pre-hardened elements, that is, standard cells and macros, and the connections between them. [S4 §Netlist]

Synthesis produces it from a hardware description. [S2 §Newcomers' Tutorial]

## Why it matters

- It is what physical implementation turns into a layout. [S2 §Newcomers' Tutorial]
- It has to be verified too: functional verification is applied to the gate-level netlist as well as to the RTL. [S2 §Newcomers' Tutorial]
- Flow steps write the current gate-level netlist as Verilog in two forms, one without power connections and one with them. [S2 §Run directory]
- At signoff, the layout is compared against the schematic, which is usually given as Verilog. [S2 §LVS]

- In LibreLane, a netlist written in Verilog is a gate-level netlist: it models cells under ideal conditions and serves to check logical correctness. A SPICE netlist goes down to the transistor level and can be simulated under various physical conditions. [S4 §Netlist]
- An engineering change order (ECO) is a manual modification of a netlist that tools have already processed, used for last-minute fixes. [S4 §ECO]

## Related pages

- [Logic Synthesis](../stages/logic-synthesis.md)
- [Functional Verification](../stages/functional-verification.md)
- [ASIC Design Flow](asic-design-flow.md)
- [LVS](lvs.md)
- [RTL](rtl.md)
- [Standard Cell Library](standard-cell-library.md)
