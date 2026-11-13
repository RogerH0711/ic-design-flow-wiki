---
title: RTL Design
type: stage
order: 2
sources: [S2, S5, S7, S8, S9]
updated: 2026-11-12
---

# RTL Design

Also called: Design Entry

## Purpose

The design is written down in a hardware description language such as Verilog. For digital designs this is normally done at the register transfer level (RTL). [S2 §Newcomers' Tutorial]

## Inputs

- A higher-level model of the desired function: a design usually starts as a high-level or system-level simulation, which is then rewritten by hand into a synthesizable description. [S5 §Script-based synthesis flows]

## Outputs

- RTL source files. The tutorial's multiplier example consists of two Verilog files. [S2 §RTL]

## What happens

- Only a subset of Verilog can be synthesized; it is defined in its own IEEE standard. [S5 §Features of synthesizable Verilog]
- Clocked logic is written as code that runs on a clock edge, and synthesis turns it into data path logic followed by flip-flops. [S5 §Behavioural level]
- Latched logic is often considered bad style and is in many cases the result of careless coding, so many synthesis tools warn when they generate it. [S5 §Behavioural modelling]
- Tool scripts and settings count as design sources and belong under version control with the code. [S5 §Script-based synthesis flows]

- One recommended way to begin is a skeleton: a definition of the registers, a basic document, and a Verilog module for the top of that one block with all of its known IO, clocking, and reset. The method is not mandatory. [S8 §Initial Skeleton Design]
- The skeleton is then filled in step by step, in changes small enough for reviewers to digest. [S8 §Full Design]
- When a block is ready it can be included in the top-level design of the whole chip, after agreement on how to integrate it and a check that the top-level simulation is not harmed. [S8 §Top Level Inclusion]

- The lowRISC style guide aims at consistency, best practices, and code reuse; the next items are rules from it. [S9 §Summary]
- Clocked logic uses non-blocking assignments and purely combinational logic uses blocking assignments. [S9 §Blocking and Non-blocking Assignments]
- Flip-flops are used in place of latches unless a latch is absolutely necessary. [S9 §Sequential Logic (Latches)]
- Synthesizable modules are designed for zero-delay simulation and contain no delay statements. [S9 §Delay Modeling]
- A state machine has three parts: an enumeration of its states, a combinational block that computes the next state, and a clocked block that updates the state. [S9 §Finite State Machines]
- Clock signal names begin with `clk`, and resets are active-low and asynchronous. [S9 §Clocks] [S9 §Resets]

## Checks

- [Verilator](../tools/verilator.md) lints the SystemVerilog code it is given as part of its normal use. [S7 §Overview]
- The reference flow lints the RTL before doing anything else: its first step directories are a lint run followed by checkers for lint errors and warnings. [S2 §Run directory]

- Even the first check-ins should compile, be free of syntax errors, and follow the coding style guide. [S8 §Initial Skeleton Design]

- No signal may be left for the tools to infer: each one is declared, with a data type, before it is used. [S9 §Declare all signals]
- Designers are encouraged to place SystemVerilog assertions all through the design, both as correctness checks and to catch invalid conditions. [S9 §Assertion Macros]

## Common problems

- Simulation and synthesis disagreeing. Assigning `X` to mark don't-care conditions can cause such mismatches, and so can a latch inferred inside a function. [S9 §Don't Cares (`X`'s)] [S9 §Combinational Logic]
- A register described with both kinds of assignment will not simulate correctly. [S9 §Sequential Logic (Registers)]

## Related pages

- [ASIC Design Flow](../concepts/asic-design-flow.md)
- [Functional Verification](functional-verification.md)
- [Logic Synthesis](logic-synthesis.md)
- [RTL](../concepts/rtl.md)
- [Levels of Abstraction](../concepts/levels-of-abstraction.md)
- [Verilator](../tools/verilator.md)
- [Specification](specification.md)
