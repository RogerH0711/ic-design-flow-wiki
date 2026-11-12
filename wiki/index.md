# Index

Catalogue of every page in this wiki. Start with the stage pages in flow
order, then follow links into concepts, tools, and formats.

## Stages

In flow order. Stage 1 (specification) has no page yet.

2. [RTL Design](stages/rtl-design.md) — the design is written in a hardware description language.
3. [Functional Verification](stages/functional-verification.md) — simulation and formal verification against the requirements.
4. [Logic Synthesis](stages/logic-synthesis.md) — turns the Verilog design and its constraints into the first netlist of the flow.
5. [Floorplanning](stages/floorplanning.md) — sets the chip outline, pins, macros, tap cells, and power grid.
6. [Placement](stages/placement.md) — puts the standard cells into the core area.
7. [Clock Tree Synthesis](stages/clock-tree-synthesis.md) — builds a balanced clock tree after placement.
8. [Routing](stages/routing.md) — global routing, then detailed routing.
9. [Layout Finishing](stages/layout-finishing.md) — metal fill, parasitics extraction, and the final layout file.
10. [Signoff](stages/signoff.md) — DRC, LVS, STA, and the antenna check before tape-out.

## Concepts

- [ASIC Design Flow](concepts/asic-design-flow.md) — the whole path from idea to fabrication data; start here.
- [Antenna Violation](concepts/antenna-violation.md) — an antenna ratio above the limit set by the process design kit.
- [Core Utilization and Placement Density](concepts/placement-density.md) — how much of the core is used and how tightly cells are packed.
- [DRC](concepts/drc.md) — checking the layout against the foundry's manufacturing rules.
- [IR Drop](concepts/ir-drop.md) — voltage lost in the power grid before it reaches the cells.
- [LVS](concepts/lvs.md) — checking that layout and schematic are wired the same way.
- [Netlist](concepts/netlist.md) — the circuit of logic cells produced by synthesis.
- [PPA](concepts/ppa.md) — area, timing, and power, the three goals of optimization.
- [Static Timing Analysis](concepts/static-timing-analysis.md) — computing arrival and required times on every timing path.
- [Tap, Endcap, Tie, and Filler Cells](concepts/tap-endcap-tie-filler-cells.md) — cells added for physical reasons, not for logic.
- [Timing Corners](concepts/timing-corners.md) — the extreme conditions under which timing is analyzed.
- [Timing Violations](concepts/timing-violations.md) — setup and hold problems and how the flow reports and repairs them.

## Tools

- [KLayout](tools/klayout.md) — layout viewer, and one of the two DRC tools.
- [LibreLane](tools/librelane.md) — a library for building implementation flows, with an open-source reference flow.
- [Magic](tools/magic.md) — the other DRC tool.
- [Netgen](tools/netgen.md) — the LVS tool.
- [OpenROAD](tools/openroad.md) — the application that carries out the automated flow.
- [OpenROAD Flow Scripts](tools/openroad-flow-scripts.md) — scripts that run the whole flow with one command.
- [Yosys](tools/yosys.md) — the synthesis tool.

## Formats

- [DEF](formats/def.md) — the layout as saved by flow steps.
- [GDSII](formats/gdsii.md) — the final layout file.
- [ODB](formats/odb.md) — the database file saved after each sub-step.
- [SDC](formats/sdc.md) — timing constraints.
- [SPEF](formats/spef.md) — extracted wire parasitics.

## Sources

- [S1: OpenROAD Flow Scripts Tutorial](sources/s1-orfs-flow-tutorial.md) — a full RTL-to-GDSII run, stage by stage.
- [S2: LibreLane Newcomers' Tutorial](sources/s2-librelane-newcomers-tutorial.md) — the list of flow steps and the four signoff checks.
