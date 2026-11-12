---
title: Technology Mapping
type: concept
sources: [S5]
updated: 2026-11-12
---

# Technology Mapping

## Definition

Technology mapping rewrites a design using only cells that the target architecture actually offers; the result is a netlist of such cells. [S5 §Technology mapping]

## Why it matters

- In an ASIC flow the available cells may be the process-specific cell library supplied by the fab; in an FPGA flow they may be LUT cells and special function units. [S5 §Technology mapping]
- Mapping a logic gate netlist well onto physically available gate types is named as one of the two challenges of logic synthesis. [S5 §Logical gate level]
- For an ASIC, the cell library may also say how each physical cell is built from transistors. [S5 §Physical gate level]

## Related pages

- [Logic Synthesis](../stages/logic-synthesis.md)
- [Standard Cell Library](standard-cell-library.md)
- [Levels of Abstraction](levels-of-abstraction.md)
- [Netlist](netlist.md)
