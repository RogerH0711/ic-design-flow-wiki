---
title: Timing Paths
type: concept
sources: [S3]
updated: 2026-11-12
---

# Timing Paths

## Definition

A timing path is described by its two ends. It can begin in one of two places, an input port or a flip-flop's clock pin, and finish in one of two places, an output port or a flip-flop's data input. [S3 §Timing Paths]

That gives four types: input to output, input to flip-flop, flip-flop to output, and flip-flop to flip-flop. [S3 §Timing Paths]

In a flip-flop to flip-flop path, the first flip-flop releases the data and the second captures it. [S3 §Timing Paths]

## Why it matters

- Static timing analysis works path by path: it computes arrival times at the endpoint of every timing path. [S3 §Timing Paths]
- The other three types are really flip-flop to flip-flop paths too, with the releasing flip-flop, the capturing one, or both sitting outside the design unit. [S3 §Timing Paths]
- A false path exists in the circuit but is never exercised. [S3 §Timing Constraints]
- False paths should be identified and added to the constraints; otherwise violations get reported, and fixed, on paths that do not matter. [S3 §Tips for Achieving Timing Closure]
- A multi-cycle path is one where data is allowed more than one clock cycle to travel between the two flip-flops. [S3 §Timing Constraints]

## Related pages

- [Static Timing Analysis](static-timing-analysis.md)
- [Timing Violations](timing-violations.md)
- [Timing Closure](timing-closure.md)
- [SDC](../formats/sdc.md)
