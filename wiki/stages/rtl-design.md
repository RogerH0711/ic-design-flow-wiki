---
title: RTL Design
type: stage
order: 2
sources: [S2]
updated: 2026-11-12
---

# RTL Design

Also called: Design Entry

## Purpose

The design is written down in a hardware description language such as Verilog. For digital designs this is normally done at the register transfer level (RTL). [S2 §Newcomers' Tutorial]

## Inputs

_Not yet covered by an ingested source._

## Outputs

- RTL source files. The tutorial's multiplier example consists of two Verilog files. [S2 §RTL]

## What happens

_Not yet covered by an ingested source._

## Checks

- The reference flow lints the RTL before doing anything else: its first step directories are a lint run followed by checkers for lint errors and warnings. [S2 §Run directory]

## Related pages

- [ASIC Design Flow](../concepts/asic-design-flow.md)
- [Functional Verification](functional-verification.md)
- [Logic Synthesis](logic-synthesis.md)
- [RTL](../concepts/rtl.md)
