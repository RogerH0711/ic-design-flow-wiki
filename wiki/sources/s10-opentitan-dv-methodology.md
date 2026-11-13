---
title: "S10: Design Verification Methodology within OpenTitan"
type: source
source_id: S10
sources: [S10]
updated: 2026-11-13
---

# S10: Design Verification Methodology within OpenTitan

## Summary

The OpenTitan project's description of how it verifies its designs, with the stated aim of matching the quality required for a full production chip. [S10 §Design Verification Methodology within OpenTitan]

## Key points

- Two techniques carry the work: dynamic simulation with functional tests, and formal property verification. [S10 §Language and Tool Selection]
- Completion is defined by checklists, one per verification stage. [S10 §Defining Verification Complete: Stages and Checklists]
- Planning is documented in a testplan and a DV document. [S10 §Documentation]
- Regressions come in two main suites, sanity and nightly. [S10 §Regressions]
- Coverage answers the question of when testing is done, and comes in two kinds, code coverage and functional coverage. [S10 §Coverage Collection]
- Verification ends with a final review of the checklist. [S10 §Sign-off Reviews]

## Coverage

- Describes one project's methodology, built on professional simulation tools and a specific testbench methodology. [S10 §Language and Tool Selection]
- Formal verification is only pointed to, not described. [S10 §FPV]

## Related pages

- [Functional Verification](../stages/functional-verification.md)
- [Coverage](../concepts/coverage.md)
- [Testplan](../concepts/testplan.md)
- [Regression](../concepts/regression.md)
- [Signoff](../stages/signoff.md)
- [Verilator](../tools/verilator.md)
