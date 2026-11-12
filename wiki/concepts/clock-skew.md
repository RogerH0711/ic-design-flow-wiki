---
title: Clock Skew
type: concept
sources: [S1, S3]
updated: 2026-11-12
---

# Clock Skew

## Definition

Clock skew is the difference between the times at which the clock arrives at different flip-flops. [S3 §Timing Constraints]

The skew is called positive when the clock edge reaches the releasing flip-flop before the capturing one, and negative in the opposite case. [S3 §Timing Constraints]

## Why it matters

- Clock skew is the main cause of hold violations. [S3 §Tips for Achieving Timing Closure]
- A perfectly balanced clock tree with zero skew cannot be built, so the skew report should be checked and the causes of high skew, such as a badly placed macro, dealt with. [S3 §Tips for Achieving Timing Closure]
- Timing analysis right after synthesis treats the clock as ideal, so there is no skew yet and no hold violation is reported at that point, though setup violations can be. [S3 §Tips for Achieving Timing Closure]
- The flow tutorial reports clock skew after clock tree synthesis and fixes skew problems that could cause hold violations later. [S1 §Reporting Clock Skews]

## Related pages

- [Clock Tree Synthesis](../stages/clock-tree-synthesis.md)
- [Timing Violations](timing-violations.md)
- [Timing Closure](timing-closure.md)
