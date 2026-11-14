---
title: "S1: OpenROAD Flow Scripts Tutorial"
type: source
source_id: S1
sources: [S1]
updated: 2026-11-12
---

# S1: OpenROAD Flow Scripts Tutorial

## Summary

A hands-on tutorial that runs a complete RTL-to-GDSII flow with OpenROAD Flow Scripts and then revisits the key flow stages one by one with small examples. [S1 §Introduction]

Its running example is `ibex`, a 32-bit RISC-V CPU core, implemented in the `sky130hd` technology. [S1 §Getting Started]

## Key points

- The flow runs from synthesis to the final `.gds` file through Tcl scripts, with no human intervention needed. [S1 §Running The Automated RTL-to-GDS Flow]
- A design is described to the flow by a handful of variables: the platform, the top-level module name, the Verilog files, an SDC file, the core utilization, and the placement density. [S1 §Design Configuration]
- The smallest usable timing constraint is a clock definition. [S1 §Timing Constraints]
- The flow is cleaned stage by stage with six targets, which the tutorial matches to synthesis, floorplanning, macro placement, clock tree synthesis, routing, and layout generation. [S1 §Design Goals]
- Log files carry a numeric prefix, from `1_1_yosys.log` to `6_report.log`, that shows where each step sits in the flow. [S1 §Viewing Results And Logs]
- The flow is automated, but the user can step in to explore and optimize a design for area, timing, and power. [S1 §Understanding and Analyzing OpenROAD Flow Stages and Results]
- The flow ends by writing a merged final layout file, `6_final.gds`. [S1 §Viewing OpenROAD-flow-scripts Directory Structure And Results]

## Coverage

- Covered in detail: synthesis options, floorplanning, pin and pad placement, power planning, placement, timing optimization, clock tree synthesis, global and detailed routing, antenna checking, metal fill, and parasitics extraction. [S1 §Understanding and Analyzing OpenROAD Flow Stages and Results]
- Outside its scope: everything before RTL exists. The tutorial starts from finished SystemVerilog files, so specification, RTL writing, and functional verification are not discussed. [S1 §Design Input SystemVerilog]
- DRC is mentioned in passing, as an engine inside the detailed router and as a viewer for violations left after routing, but is not explained. [S1 §DRC Viewer]

## Related pages

- [Logic Synthesis](../stages/logic-synthesis.md)
- [Floorplanning](../stages/floorplanning.md)
- [Placement](../stages/placement.md)
- [Clock Tree Synthesis](../stages/clock-tree-synthesis.md)
- [Routing](../stages/routing.md)
- [Layout Finishing](../stages/layout-finishing.md)
- [PPA](../concepts/ppa.md)
- [Core Utilization and Placement Density](../concepts/placement-density.md)
- [IR Drop](../concepts/ir-drop.md)
- [Tap, Endcap, Tie, and Filler Cells](../concepts/tap-endcap-tie-filler-cells.md)
- [Timing Violations](../concepts/timing-violations.md)
- [Antenna Violation](../concepts/antenna-violation.md)
- [OpenROAD Flow Scripts](../tools/openroad-flow-scripts.md)
- [OpenROAD](../tools/openroad.md)
- [Yosys](../tools/yosys.md)
- [SDC](../formats/sdc.md)
- [GDSII](../formats/gdsii.md)
- [SPEF](../formats/spef.md)
- [ODB](../formats/odb.md)
