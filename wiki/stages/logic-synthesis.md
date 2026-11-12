---
title: Logic Synthesis
type: stage
order: 4
sources: [S1]
updated: 2026-11-12
---

# Logic Synthesis

## Purpose

Synthesis is the first stage of the automated RTL-to-GDSII flow. [S1 §Running The Automated RTL-to-GDS Flow]

_Not yet covered by an ingested source._

## Inputs

- The design's Verilog files, named by the `VERILOG_FILES` variable. [S1 §Design Configuration]
- The timing constraints in an [SDC](../formats/sdc.md) file, named by `SDC_FILE`. [S1 §Design Configuration]

## Outputs

- `1_synth.v` and `1_synth.sdc` in the results directory. [S1 §Viewing OpenROAD-flow-scripts Directory Structure And Results]
- `synth_stat.txt`, the design statistics after synthesis. [S1 §Viewing OpenROAD-flow-scripts Directory Structure And Results]

## What happens

- The flow's list of steps points to [Yosys](../tools/yosys.md) for synthesis. [S1 §Running The Automated RTL-to-GDS Flow]
- The synthesis log is `1_1_yosys.log`. [S1 §Viewing Results And Logs]
- The user can steer optimization toward area (`ABC_AREA=1`) or toward timing (`ABC_SPEED=1`). [S1 §Area And Timing Optimization]
- In the tutorial's `gcd` example both settings give the same number of cells, and the final design area is smaller with the area setting. [S1 §Area And Timing Optimization]

## Checks

- `synth_check.txt` collects the warnings and errors raised during synthesis. [S1 §Viewing OpenROAD-flow-scripts Directory Structure And Results]
- The effect of an area-oriented synthesis should be judged after [floorplanning](floorplanning.md), because later timing repair enlarges the design to meet timing whatever netlist synthesis produced. [S1 §Area And Timing Optimization]

## Related pages

- [Floorplanning](floorplanning.md)
- [Yosys](../tools/yosys.md)
- [SDC](../formats/sdc.md)
- [PPA](../concepts/ppa.md)
