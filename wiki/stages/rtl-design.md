---
title: RTL Design
type: stage
order: 2
sources: [S2, S5, S7, S8]
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

## Checks

- [Verilator](../tools/verilator.md) lints the SystemVerilog code it is given as part of its normal use. [S7 §Overview]
- The reference flow lints the RTL before doing anything else: its first step directories are a lint run followed by checkers for lint errors and warnings. [S2 §Run directory]

- Even the first check-ins should compile, be free of syntax errors, and follow the coding style guide. [S8 §Initial Skeleton Design]

## Related pages

- [ASIC Design Flow](../concepts/asic-design-flow.md)
- [Functional Verification](functional-verification.md)
- [Logic Synthesis](logic-synthesis.md)
- [RTL](../concepts/rtl.md)
- [Levels of Abstraction](../concepts/levels-of-abstraction.md)
- [Verilator](../tools/verilator.md)
- [Specification](specification.md)
