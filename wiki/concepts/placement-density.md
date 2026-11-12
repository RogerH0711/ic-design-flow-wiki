---
title: Core Utilization and Placement Density
type: concept
sources: [S1]
updated: 2026-11-12
---

# Core Utilization and Placement Density

## Definition

- Core utilization is a percentage set for the design's core area through the `CORE_UTILIZATION` variable. [S1 §Design Configuration]
- Placement density describes how spread out the cells are within the core: 1 means tightly packed and 0 means widely spread. [S1 §Design Configuration]

## Why it matters

- A floorplan can be sized from a utilization target instead of explicit dimensions. [S1 §Floorplan Based On Core Utilization]
- Placement density decides how widely standard cells are spread over the core. [S1 §Macro Placement]
- Changing the two settings visibly changes the placement, which a density heat map makes easy to see. [S1 §Defining Placement Density]

## Related pages

- [Floorplanning](../stages/floorplanning.md)
- [Placement](../stages/placement.md)
- [PPA](ppa.md)
