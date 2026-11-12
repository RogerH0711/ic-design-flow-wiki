---
title: Timing Corners
type: concept
sources: [S1, S2]
updated: 2026-11-12
---

# Timing Corners

Also called: IPVT corners

## Definition

A timing corner is one combination of extreme conditions under which timing is analyzed. The four ingredients are interconnect, process, voltage, and temperature. [S2 §STA]

- Process, voltage, and temperature corners stand for the extremes of manufacturing variation, supply voltage, and operating temperature that a chip may meet. [S2 §STA]
- Interconnect corners account for variation in the wires: their width, thickness, and height, and the material around them. [S2 §STA]

## Why it matters

- Analyzing the worst cases is what gives confidence that the chip works under all conditions. [S2 §STA]
- The slowest case combines a slow process, low voltage, high temperature, and maximum interconnect delay; setup violations are most likely there. [S2 §STA]
- The fastest case combines a fast process, high voltage, low temperature, and minimum interconnect delay; hold violations are most likely there. [S2 §STA]
- The flow tutorial pairs them the same way: setup optimization works on the slow corner and hold optimization on the fast corner. [S1 §Timing Optimization Based On Multiple Corners]

## Related pages

- [Static Timing Analysis](static-timing-analysis.md)
- [Timing Violations](timing-violations.md)
- [Signoff](../stages/signoff.md)
