---
title: IR Drop
type: concept
sources: [S1]
updated: 2026-11-12
---

# IR Drop

## Definition

IR drop is the voltage lost in the metal wires of the power grid before the supply reaches the power pins of the standard cells. [S1 §IR Drop Analysis]

## Why it matters

- It has to be kept small because it slows the cells down and so limits the performance of the whole chip. [S1 §IR Drop Analysis]
- A static IR analysis of the placed design with its power grid reports the worst IR drop and the worst current density, and finds power stripes that are left floating. [S1 §IR Drop Analysis]

## Related pages

- [Floorplanning](../stages/floorplanning.md)
- [OpenROAD](../tools/openroad.md)
