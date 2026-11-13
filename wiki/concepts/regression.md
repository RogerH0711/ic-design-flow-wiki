---
title: Regression
type: concept
sources: [S10]
updated: 2026-11-13
---

# Regression

## Definition

A regression is a run of all of a project's simulations; in OpenTitan this happens at night and on weekends. [S10 §Nightly]

There are two main regression suites, called sanity and nightly. [S10 §Regressions]

## Why it matters

- The sanity suite is a set of simple tests through a major data path of each design. Because much code is shared, breakages are frequent, and this suite gives a quick way to check that a change broke nothing. [S10 §Sanity]
- In the nightly suite each constrained random test is run with many random seeds, coverage is collected and merged, and the results are published on a dashboard. [S10 §Nightly]
- Passing the nightly regression at 100 percent, consistently, is one of the conditions for calling verification complete. [S10 §Nightly]

## Related pages

- [Functional Verification](../stages/functional-verification.md)
- [Coverage](coverage.md)
- [Testplan](testplan.md)
