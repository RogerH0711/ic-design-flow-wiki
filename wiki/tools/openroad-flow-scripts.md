---
title: OpenROAD Flow Scripts
type: tool
sources: [S1]
updated: 2026-11-12
---

# OpenROAD Flow Scripts

Also called: ORFS

## What it is

OpenROAD Flow Scripts is a set of scripts that runs the complete OpenROAD flow from RTL to the final layout. [S1 §Introduction]

It expects a fixed directory structure, which the user should not rearrange. [S1 §User Guidelines]

## Role in the flow

- One `make` command with a design configuration file runs every stage in order. [S1 §Design Goals]
- A platform configuration holds the variables for one technology, such as `sky130hd`, and is normally left unchanged. [S1 §Platform Configuration]
- A design configuration names the platform, the top-level module, the Verilog files, the SDC file, and the density targets. [S1 §Design Configuration]
- Each run fills four directories: `logs`, `results`, `reports`, and `objects`. [S1 §Viewing OpenROAD-flow-scripts Directory Structure And Results]
- Several public process design kits ship with it under `platforms`. [S1 §Viewing OpenROAD-flow-scripts Directory Structure And Results]
- A run can usually restart from a partial result, and the files of individual stages can be deleted with per-stage clean targets. [S1 §Design Goals]

## Related pages

- [OpenROAD](openroad.md)
- [Yosys](yosys.md)
- [Logic Synthesis](../stages/logic-synthesis.md)
- [Layout Finishing](../stages/layout-finishing.md)
