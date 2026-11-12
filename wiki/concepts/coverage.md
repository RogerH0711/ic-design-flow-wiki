---
title: Coverage
type: concept
sources: [S7]
updated: 2026-11-12
---

# Coverage

## Definition

_Not yet covered by an ingested source._

The Verilator guide lists the forms of coverage its simulations can collect. [S7 §Coverage Analysis]

- Line coverage: a counter at each basic block of code. [S7 §Line Coverage]
- Branch coverage: coverage analysis at each point where the flow of the code changes, such as a branch. [S7 §Branch Coverage]
- Toggle coverage: counts how often each individual signal bit changes value. [S7 §Toggle Coverage]
- FSM coverage: state coverage and transition coverage for a conservative subset of state machines; the feature is described as experimental. [S7 §FSM Coverage]
- Property and covergroup coverage: points that the user has written into the code by hand. [S7 §Property Coverage] [S7 §Covergroup Coverage]

## Why it matters

- Running a model built with coverage produces a coverage file; after all tests have run, the files are combined into a source listing annotated with coverage details. [S7 §Coverage Collection]
- The same data can be used to grade tests, that is, to work out which tests matter for full verification coverage of the design. [S7 §Coverage Collection]
- Toggle counts may include edges near time zero while the model settles, so it is good practice to reset all coverage just before reset is released. [S7 §Toggle Coverage]

## Related pages

- [Functional Verification](../stages/functional-verification.md)
- [Verilator](../tools/verilator.md)
