---
title: Coverage
type: concept
sources: [S7, S10]
updated: 2026-11-12
---

# Coverage

## Definition

_Not yet covered by an ingested source._

There are two key kinds of coverage metric: code coverage and functional coverage. [S10 §Coverage Collection]

- Code coverage is extracted automatically by the simulator from structures in the design such as lines, branches, state machines, conditions, and toggling signals. It needs no extra work, and is sometimes called implicit coverage. [S10 §Code Coverage]
- Functional coverage needs the designer or verification engineer to write cover points, which record whether signals have taken an interesting set or sequence of values. It is sometimes called explicit coverage. [S10 §Functional Coverage]

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

- Coverage answers the question of when testing is done, and it exposes flaws: bugs, and places where the design falls short of its specification. [S10 §Coverage Collection]
- Both kinds are needed. Full code coverage shows that all code ran, not that it does the right thing; full functional coverage can still leave part of the design unexercised, which code coverage would reveal. [S10 §Do we need both types of coverage]
- Gaps must be understood and then either closed with more tests or waived; working toward 100 percent this way is called coverage closure. [S10 §Coverage Collection]
- A waived item is recorded as an exclusion with a stated reason, and designers must approve exclusions in review. [S10 §Exclusions]
- Coverage closure is perhaps the most time-consuming part of verification, so what is collected should be chosen with care. [S10 §Coverage Collection Guidelines]

## Source differences

- Grouping: S7 lists six forms of coverage side by side [S7 §Coverage Analysis], while S10 sorts the metrics into two kinds, code coverage and functional coverage. [S10 §Coverage Collection]
- Toggle coverage: S7 inserts a counter for every bit of every signal in a module [S7 §Toggle Coverage], while S10 calls full toggle coverage very difficult and not particularly useful, and closes it only on the I/O ports of the design under test and of pre-verified IPs inside it. [S10 §Code Coverage]

## Related pages

- [Functional Verification](../stages/functional-verification.md)
- [Verilator](../tools/verilator.md)
- [Testplan](testplan.md)
- [Regression](regression.md)
