---
title: IR Drop
type: concept
sources: [S1]
updated: 2026-11-12
---

# IR Drop

## Definition

Supply voltage has to travel through the metal wires of the power grid to reach each standard cell's power pins; the voltage that drops along the way is the IR drop. [S1 §IR Drop Analysis]

## Why it matters

- It must be limited because it affects the speed of the cells and the overall performance of the chip. [S1 §IR Drop Analysis]
- A static IR analysis of the placed design with its power grid reports the worst IR drop and the worst current density, and finds power stripes that are left floating. [S1 §IR Drop Analysis]

## Related pages

- [Floorplanning](../stages/floorplanning.md)
- [OpenROAD](../tools/openroad.md)
