---
title: Standard Cell Library
type: concept
sources: [S3]
updated: 2026-11-12
---

# Standard Cell Library

Also called: SCL

## Definition

A standard cell library typically contains several sizes of the same cell. [S3 §Timing Optimizations]

A cell is another name for a CMOS logic gate. [S3 §Modeling CMOS Cells]

_Not yet covered by an ingested source._

A cell's size indicates its driving strength: how much current it can supply to its load. [S3 §Timing Optimizations]

## Why it matters

- A stronger cell has less delay for the same capacitive load, so swapping in a larger size is one way to fix timing. [S3 §Timing Optimizations]
- Sizing up is not free: a larger cell is a heavier load for the cell that drives it, which slows that one down. [S3 §Timing Optimizations]
- The buffer is a cell with no logic function that matters a great deal for timing. It sharpens a slow signal, splits a long wire into shorter segments, and can add delay to a data path to fix a hold violation. [S3 §Timing Optimizations]
- Cell delay is estimated with a simple resistance and capacitance model, in which the load includes the wires and the input pins of the cells being driven. [S3 §Modeling CMOS Cells]

## Related pages

- [Timing Closure](timing-closure.md)
- [Timing Violations](timing-violations.md)
- [Tap, Endcap, Tie, and Filler Cells](tap-endcap-tie-filler-cells.md)
- [Netlist](netlist.md)
