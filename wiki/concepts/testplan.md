---
title: Testplan
type: concept
sources: [S10]
updated: 2026-11-13
---

# Testplan

## Definition

In the OpenTitan methodology a testplan has two parts: a high-level list of the tests planned to verify every feature in the design specification, and a functional coverage plan listing the coverage points needed to show that those features really are tested. [S10 §Testplan]

It is accompanied by a DV document, which records the overall strategy, a block diagram of the testbench, the reference models, the functional coverage model, and the checkers. [S10 §DV document]

## Why it matters

- It ties verification back to the specification: every listed feature gets planned tests. [S10 §Testplan]
- It is written in a machine-readable form, so nightly results can be annotated with it to track progress through the plan. [S10 §Testplan]
- The testplan and DV document are reviewed early with designers, verification peers, leads, the software team, and others; the review can also expose imprecise or missing items in the design specification itself. [S10 §Sign-off Reviews]

## Related pages

- [Functional Verification](../stages/functional-verification.md)
- [Specification](../stages/specification.md)
- [Coverage](coverage.md)
- [Regression](regression.md)
