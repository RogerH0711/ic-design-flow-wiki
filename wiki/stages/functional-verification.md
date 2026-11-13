---
title: Functional Verification
type: stage
order: 3
sources: [S2, S3, S5, S7, S10]
updated: 2026-11-12
---

# Functional Verification

Also called: Design Verification, DV

## Purpose

Functional verification makes sure that the design behaves as its requirements say it should. [S2 §Newcomers' Tutorial]

The design being verified is called the design under test, or DUT. [S10 §Design Verification Methodology within OpenTitan]

## Inputs

- The RTL, and later the gate-level [netlist](../concepts/netlist.md): the tutorial calls it essential to verify both. [S2 §Newcomers' Tutorial]

- The design specification: the [testplan](../concepts/testplan.md) lists tests for the features it contains. [S10 §Testplan]

## Outputs

- With Verilator, if enabled, the simulation executable can produce waveform traces of the design for viewing and [coverage](../concepts/coverage.md) data for later analysis. [S7 §Overview]

## What happens

- Two techniques are combined: simulation of the hardware description, and formal verification. [S2 §Newcomers' Tutorial]
- At the end of implementation, simulating the final gate-level netlist with [SDF](../formats/sdf.md) delay annotations is recommended; it is the closest thing to the behavior of the fabricated chip. [S3 §Tips for Achieving Timing Closure]
- Such timing simulation is slow and cannot replace static timing analysis, but it helps to uncover and validate false paths. [S3 §SDF Annotated GL Simulation using CVC]

- The hand-written description is checked against the higher-level model by simulating both and comparing the results. [S5 §Script-based synthesis flows]
- The check is repeated at each lower level and after every change to a model. [S5 §Script-based synthesis flows]

- Design code is read by the synthesis tool, by simulators, and sometimes by a formal verification tool, so all of them must interpret it in the same way. [S5 §Standards compliance]

- In the OpenTitan methodology the two key techniques are dynamic simulation with functional tests and formal property verification. [S10 §Language and Tool Selection]
- At the level of single IPs, OpenTitan generates stimulus with a constrained random approach, and the verification environment checks the design's behavior independently of the stimulus. [S10 §IP Level DV]
- Testing grows in steps. First a basic smoke test brings the design out of reset and exercises a major data path. [S10 §Basic Smoke Test]
- The first real tests then validate the software interface of the design, its CSRs. [S10 §CSR Suite of Tests]
- The bulk of functional testing comes in the following stage. [S10 §Progressing towards V2]
- Stress tests exercise several interfaces or features at once and are well suited to finding bugs and closing coverage. [S10 §Stress Tests]
- The work is spread over three tiers: IP level, core level, and chip level. [S10 §DV Efforts in OpenTitan]
- Chip-level verification aims to ensure that all the IPs are integrated correctly into the chip. [S10 §Chip Level DV]
- All simulations are run regularly as a [regression](../concepts/regression.md). [S10 §Nightly]

## Checks

- After all tests have run, Verilator's coverage command produces a source listing annotated with coverage details, in which the lines it believes need more coverage are marked. [S7 §Coverage Collection]

- The effort is split into verification stages, each with a checklist of tasks; only when every item in every stage's checklist is ticked does the project call verification complete. [S10 §Defining Verification Complete: Stages and Checklists]
- Among the conditions are a consistent 100 percent pass rate in nightly regressions [S10 §Nightly] and coverage that has been collected, analyzed, and reported, with waivers. [S10 §Coverage Collection]
- A final review confirms that every checklist item is complete without major exceptions or open issues. [S10 §Sign-off Reviews]

- Standard RTL simulation can miss problems with unknown values that gate-level simulation would detect; OpenTitan enables X-propagation in RTL simulation to catch them. [S10 §X-Propagation (Xprop)]

## Source differences

- Tools: S10 chooses one professional simulator as its ground truth for signoff, and says it works toward a future in which open-source tools such as Verilator and cocotb are signoff-grade [S10 §Language and Tool Selection], while S2 describes a reference flow built entirely from open-source tools. [S2 §What is LibreLane?]

## Related pages

- [ASIC Design Flow](../concepts/asic-design-flow.md)
- [RTL Design](rtl-design.md)
- [Logic Synthesis](logic-synthesis.md)
- [Netlist](../concepts/netlist.md)
- [SDF](../formats/sdf.md)
- [Coverage](../concepts/coverage.md)
- [Verilator](../tools/verilator.md)
- [Specification](specification.md)
- [Testplan](../concepts/testplan.md)
- [Regression](../concepts/regression.md)
