---
title: Yosys
type: tool
sources: [S1, S2]
updated: 2026-11-12
---

# Yosys

## What it is

Yosys is the tool the flow tutorial lists for the synthesis step. [S1 §Running The Automated RTL-to-GDS Flow]

_Not yet covered by an ingested source._

## Role in the flow

- It runs first: its log, `1_1_yosys.log`, carries the lowest prefix in the flow. [S1 §Viewing Results And Logs]
- Its result, `1_1_yosys.v`, is the first file in the results directory. [S1 §Viewing OpenROAD-flow-scripts Directory Structure And Results]
- Two options choose between optimizing for area and optimizing for speed. [S1 §Area And Timing Optimization]
- The LibreLane reference flow uses it for synthesis too; the step directory is `06-yosys-synthesis`. [S2 §Run directory]

## Related pages

- [Logic Synthesis](../stages/logic-synthesis.md)
- [OpenROAD Flow Scripts](openroad-flow-scripts.md)
- [LibreLane](librelane.md)
- [Netlist](../concepts/netlist.md)
