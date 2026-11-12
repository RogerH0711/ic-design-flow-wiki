---
title: Dotlib
type: format
sources: [S2, S4]
updated: 2026-11-12
---

# Dotlib

Also called: `.lib`

## What it is

Dotlib is a library format that gives an abstract model of each cell: what its interface is and how it behaves in time. It is used for macros, which here includes standard cells. [S4 §dotlib]

## Produced by and used by

- It is typically used for synthesis and for static timing analysis. [S4 §dotlib]
- The LibreLane flow writes `lib` views of the finished design among its final results. [S2 §Final Results]

## Related pages

- [Static Timing Analysis](../concepts/static-timing-analysis.md)
- [Standard Cell Library](../concepts/standard-cell-library.md)
- [Logic Synthesis](../stages/logic-synthesis.md)
- [LEF](lef.md)
