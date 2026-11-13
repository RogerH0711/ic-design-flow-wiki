---
title: "S9: lowRISC Verilog Coding Style Guide"
type: source
source_id: S9
sources: [S9]
updated: 2026-11-13
---

# S9: lowRISC Verilog Coding Style Guide

## Summary

A coding style guide for Verilog and SystemVerilog, covering both synthesizable code and test bench code. Its stated goals are consistency across hardware projects, best practices, and more sharing and reuse of code. [S9 §Summary]

## Key points

- All RTL and tests should be developed in SystemVerilog. [S9 §Which Verilog to Use]
- Sequential logic uses non-blocking assignments and combinational blocks use blocking assignments; the two are never mixed in one block. [S9 §Blocking and Non-blocking Assignments]
- Latches are discouraged in favor of flip-flops. [S9 §Sequential Logic (Latches)]
- Synthesizable modules contain no delay statements. [S9 §Delay Modeling]
- `X` literals in RTL are strongly discouraged and must not be used to tell synthesis "don't care"; SVAs should flag invalid conditions instead. [S9 §Don't Cares (`X`'s)]
- A state machine is written as a list of states, a combinational block, and a clocked block. [S9 §Finite State Machines]
- Any deviation from the guide must be justified in a comment. [S9 §Style Guide Exceptions]

## Coverage

- The guide also has formatting rules, largely inherited from a C++ style guide. [S9 §Default to C-like Formatting]
- The heading "Summary" occurs four times in the guide; citations to it here refer to the first, under Basics. [S9 §Summary]

## Related pages

- [RTL Design](../stages/rtl-design.md)
- [RTL](../concepts/rtl.md)
- [Functional Verification](../stages/functional-verification.md)
