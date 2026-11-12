---
title: Floorplanning
type: stage
order: 5
sources: [S1, S2]
updated: 2026-11-12
---

# Floorplanning

## Purpose

Floorplanning prepares the chip before standard cells are placed; the tutorial calls the end of this work the pre-placement stage. [S1 §Tapcell insertion]

Its six logs name the sub-steps: `2_1_floorplan`, `2_2_floorplan_io`, `2_3_tdms_place`, `2_4_floorplan_macro`, `2_5_floorplan_tapcell`, and `2_6_floorplan_pdn`. [S1 §Viewing Results And Logs]

## Inputs

- A size target, given either as explicit die and core areas [S1 §Floorplan Initialization Based On Core And Die Area] or as a core utilization percentage. [S1 §Floorplan Based On Core Utilization]
- The `CORE_UTILIZATION` variable of the design configuration. [S1 §Design Configuration]

## Outputs

- `2_floorplan.odb`, `2_floorplan.sdc`, and `2_floorplan.v`, plus one [ODB](../formats/odb.md) snapshot per sub-step. [S1 §Viewing OpenROAD-flow-scripts Directory Structure And Results]

## What happens

1. The floorplan is initialized. One tutorial example sets a die area of 1000 by 1000 microns with a core area inset by 100 microns on each side. [S1 §Floorplan Initialization Based On Core And Die Area]
2. I/O pins are placed on the die boundary, on the routing track grid, so that net wirelength is kept small; each pin gets a metal shape. [S1 §IO Pin Placement]
   When the block will later sit inside a larger design, its pins should instead be assigned to the sides that suit the top-level connections, which is done with a pin order file. [S2 §Adding custom pin placement configuration]
3. For a full chip, I/O cells are placed around the periphery of the design and matched to the I/O cells in the netlist. [S1 §Chip Level IO Pad Placement]
4. Macros are placed; a halo of empty space around them leaves room for routing. [S1 §Macro Placement With Halo Spacing]
5. Tap cells and endcap cells are inserted after macro placement and power rail creation. [S1 §Tapcell insertion]
6. Pins tied to constant 0 or 1 in the netlist are connected to tie cells. [S1 §Tie Cells]
7. A power grid is created for the design. [S1 §Power Planning And Analysis]

## Checks

- The design area and its utilization can be reported. [S1 §Area]
- [IR drop](../concepts/ir-drop.md) analysis reports the worst voltage drop and worst current density in the power grid and looks for floating power stripes. [S1 §IR Drop Analysis]

## Related pages

- [Logic Synthesis](logic-synthesis.md)
- [ASIC Design Flow](../concepts/asic-design-flow.md)
- [Placement](placement.md)
- [Core Utilization and Placement Density](../concepts/placement-density.md)
- [IR Drop](../concepts/ir-drop.md)
- [Tap, Endcap, Tie, and Filler Cells](../concepts/tap-endcap-tie-filler-cells.md)
- [ODB](../formats/odb.md)
