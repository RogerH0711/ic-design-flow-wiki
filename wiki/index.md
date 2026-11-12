# Index

Catalogue of every page in this wiki. Start with the stage pages in flow
order, then follow links into concepts, tools, and formats.

## Stages

In flow order. Stages 1–3 (specification, RTL design, functional
verification) have no page yet.

4. [Logic Synthesis](stages/logic-synthesis.md) — turns the Verilog design and its constraints into the first netlist of the flow.
5. [Floorplanning](stages/floorplanning.md) — sets the chip outline, pins, macros, tap cells, and power grid.
6. [Placement](stages/placement.md) — puts the standard cells into the core area.
7. [Clock Tree Synthesis](stages/clock-tree-synthesis.md) — builds a balanced clock tree after placement.
8. [Routing](stages/routing.md) — global routing, then detailed routing.
9. [Layout Finishing](stages/layout-finishing.md) — metal fill, parasitics extraction, and the final layout file.

## Concepts

- [Antenna Violation](concepts/antenna-violation.md) — an antenna ratio above the limit set by the process design kit.
- [Core Utilization and Placement Density](concepts/placement-density.md) — how much of the core is used and how tightly cells are packed.
- [IR Drop](concepts/ir-drop.md) — voltage lost in the power grid before it reaches the cells.
- [PPA](concepts/ppa.md) — area, timing, and power, the three goals of optimization.
- [Tap, Endcap, Tie, and Filler Cells](concepts/tap-endcap-tie-filler-cells.md) — cells added for physical reasons, not for logic.
- [Timing Violations](concepts/timing-violations.md) — setup and hold problems and how the flow reports and repairs them.

## Tools

- [OpenROAD](tools/openroad.md) — the application that carries out the automated flow.
- [OpenROAD Flow Scripts](tools/openroad-flow-scripts.md) — scripts that run the whole flow with one command.
- [Yosys](tools/yosys.md) — the synthesis tool.

## Formats

- [GDSII](formats/gdsii.md) — the final layout file.
- [ODB](formats/odb.md) — the database file saved after each sub-step.
- [SDC](formats/sdc.md) — timing constraints.
- [SPEF](formats/spef.md) — extracted wire parasitics.

## Sources

- [S1: OpenROAD Flow Scripts Tutorial](sources/s1-orfs-flow-tutorial.md) — a full RTL-to-GDSII run, stage by stage.
