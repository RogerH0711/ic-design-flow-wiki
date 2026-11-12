---
title: Static Timing Analysis
type: concept
sources: [S2, S3, S4]
updated: 2026-11-12
---

# Static Timing Analysis

Also called: STA

## Definition

Static timing analysis (STA) finds the timing paths of a design and, at the end of every path, works out when data actually arrives, at the earliest and at the latest, and when it is required to arrive. [S2 §STA]

It makes sure that the circuit will perform its function correctly, but says nothing about whether that function is the right one. [S2 §STA]

Slack is the margin between the two: for a setup check it is the required arrival time minus the latest actual arrival time, and for a hold check it is the earliest actual arrival time minus the required one. Either must be positive. [S3 §Timing Constraints]

It judges whether a chip's timing is valid without running a full functional simulation of it. [S4 §STA]

## Why it matters

- It is how [timing violations](timing-violations.md) are found. [S2 §STA]
- It runs several times while the design is being implemented, to show how each stage changes timing, and once more at signoff on the finished design, which gives the accurate result. [S2 §STA]
- LibreLane's Classic flow runs it at three kinds of point: before physical implementation on the synthesized netlist, several times during it, and after it with parasitics extracted from the final floorplan, which is the most accurate. [S3 §Tips for Achieving Timing Closure]
- A report for one path has four parts: a header with the start and end points, the data arrival time, the data required time, and the slack. [S3 §Tips for Achieving Timing Closure]
- It is repeated for every [timing corner](timing-corners.md), and the summary reports each corner separately. [S2 §STA]
- Besides slack, its checks cover maximum capacitance, maximum slew, and maximum fanout violations, paths with no constraint, and problems in the constraints themselves. [S2 §STA]

## Related pages

- [Timing Violations](timing-violations.md)
- [Timing Paths](timing-paths.md)
- [Timing Closure](timing-closure.md)
- [SDF](../formats/sdf.md)
- [Timing Corners](timing-corners.md)
- [Signoff](../stages/signoff.md)
- [SDC](../formats/sdc.md)
