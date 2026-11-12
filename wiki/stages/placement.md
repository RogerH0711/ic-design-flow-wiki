---
title: Placement
type: stage
order: 6
sources: [S1]
updated: 2026-11-12
---

# Placement

## Purpose

Placement puts the standard cells into the core area. How densely they are packed affects both area and timing. [S1 §Macro Placement]

## Inputs

- `PLACE_DENSITY`, the desired cell density, where 1 means tightly packed and 0 means widely spread. [S1 §Design Configuration]
- `CORE_UTILIZATION`, the percentage of the core to be used. [S1 §Design Configuration]

## Outputs

- `3_place.odb` and `3_place.sdc`, plus one [ODB](../formats/odb.md) snapshot per sub-step. [S1 §Viewing OpenROAD-flow-scripts Directory Structure And Results]
- `final_placement.webp`, an image of the design after final placement. [S1 §Viewing OpenROAD-flow-scripts Directory Structure And Results]

## What happens

- The stage writes four logs in order: `3_1_place_gp.log`, `3_2_place_iop.log`, `3_3_resizer.log`, and `3_4_opendp.log`. [S1 §Viewing Results And Logs]
- The flow's list of steps includes global placement, detailed placement, and timing optimization with a resizer. [S1 §Running The Automated RTL-to-GDS Flow]
- A design-repair step inserts buffers to fix maximum slew, maximum capacitance, and maximum fanout violations, buffers long wires to cut their RC delay, and resizes gates; it works from parasitics estimated after placement. [S1 §Timing Optimization Using repair_design]

## Checks

- A placement density heat map shows how spread out the cells are. For `ibex`, raising core utilization from 20 to 40 while lowering placement density from 0.60 to 0.50 spreads the cells more widely. [S1 §Defining Placement Density]
- Counts of slew, capacitance, and fanout violations are compared before and after repair; in the tutorial's example all 31 are fixed. [S1 §Timing Optimization Using repair_design]

## Related pages

- [Floorplanning](floorplanning.md)
- [Clock Tree Synthesis](clock-tree-synthesis.md)
- [Core Utilization and Placement Density](../concepts/placement-density.md)
- [Timing Violations](../concepts/timing-violations.md)
- [ODB](../formats/odb.md)
