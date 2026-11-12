---
title: Logic Synthesis
type: stage
order: 4
sources: [S1, S2, S5]
updated: 2026-11-12
---

# Logic Synthesis

## Purpose

When software, and not a person, turns a higher-level description of a circuit into a lower-level one that behaves the same, the step is called synthesis. [S5 §Levels of abstraction]

Synthesis converts the hardware description of the design into a [netlist](../concepts/netlist.md), a circuit built from logic cells. [S2 §Newcomers' Tutorial]

It is the first stage of the automated RTL-to-GDSII flow. [S1 §Running The Automated RTL-to-GDS Flow]

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

- Logic synthesis faces two challenges: finding optimizations within the gate-level netlist, and mapping that netlist well onto an equivalent one made of gate types that are physically available. [S5 §Logical gate level]
- Converting a design into cells available in the target architecture is called [technology mapping](../concepts/technology-mapping.md). [S5 §Technology mapping]
- Operators in the description, such as addition, are replaced by cells that implement them. [S5 §Expressions in Verilog]
- Optimizations differ in what they target: some aim at area and others at speed, and a good tool lets the designer choose. [S5 §Optimizations]

## Checks

- `synth_check.txt` collects the warnings and errors raised during synthesis. [S1 §Viewing OpenROAD-flow-scripts Directory Structure And Results]
- In the LibreLane reference flow, synthesis is followed directly by checkers for unmapped cells, for synthesis problems, and for assign statements left in the netlist. [S2 §Run directory]
- The effect of an area-oriented synthesis should be judged after [floorplanning](floorplanning.md), because later timing repair enlarges the design to meet timing whatever netlist synthesis produced. [S1 §Area And Timing Optimization]

- The synthesis results are verified again by simulation, and whenever the design description changes, synthesis is rerun and re-verified. [S5 §Script-based synthesis flows]

## Related pages

- [RTL Design](rtl-design.md)
- [Functional Verification](functional-verification.md)
- [Floorplanning](floorplanning.md)
- [Netlist](../concepts/netlist.md)
- [ASIC Design Flow](../concepts/asic-design-flow.md)
- [Yosys](../tools/yosys.md)
- [SDC](../formats/sdc.md)
- [PPA](../concepts/ppa.md)
- [Technology Mapping](../concepts/technology-mapping.md)
- [Levels of Abstraction](../concepts/levels-of-abstraction.md)
