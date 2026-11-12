---
title: Static Timing Analysis
type: concept
sources: [S2]
updated: 2026-11-12
---

# Static Timing Analysis

Also called: STA

## Definition

Static timing analysis (STA) finds the timing paths of a design and, at the end of every path, works out when data actually arrives, at the earliest and at the latest, and when it is required to arrive. [S2 §STA]

It makes sure that the circuit will perform its function correctly, but says nothing about whether that function is the right one. [S2 §STA]

## Why it matters

- It is how [timing violations](timing-violations.md) are found. [S2 §STA]
- It runs several times while the design is being implemented, to show how each stage changes timing, and once more at signoff on the finished design, which gives the accurate result. [S2 §STA]
- It is repeated for every [timing corner](timing-corners.md), and the summary reports each corner separately. [S2 §STA]
- Besides slack, its checks cover maximum capacitance, maximum slew, and maximum fanout violations, paths with no constraint, and problems in the constraints themselves. [S2 §STA]

## Related pages

- [Timing Violations](timing-violations.md)
- [Timing Corners](timing-corners.md)
- [Signoff](../stages/signoff.md)
- [SDC](../formats/sdc.md)
