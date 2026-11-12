---
title: Tap, Endcap, Tie, and Filler Cells
type: concept
sources: [S1]
updated: 2026-11-12
---

# Tap, Endcap, Tie, and Filler Cells

## Definition

- A tap cell is a non-functional cell that ties the well, the substrate, or both. It is needed when most of the library's standard cells have no such taps of their own. [S1 §Tapcell insertion]
- An endcap cell, also called a boundary cell, is placed at both ends of every placement row to terminate it. [S1 §Tapcell insertion]
- A tie cell is a standard cell that supplies a constant high or low value to a gate input. [S1 §Tie Cells]
- A filler cell has no logical connection; it fills a gap between placed cells. [S1 §Adding Filler Cells]

## Why it matters

- Tap cells hold the supply and ground levels steady, which prevents drift and latch-up. They are placed at regular intervals, and the largest allowed distance between them is a design rule of the technology. [S1 §Tapcell insertion]
- Endcap cells protect the gates of the cells at the row boundary from damage during manufacturing. [S1 §Tapcell insertion]
- Wherever the netlist connects a pin to logic 0 or logic 1, a tie cell is inserted to drive it. [S1 §Tie Cells]
- Filler cells keep the power and ground rails continuous along each row. [S1 §Adding Filler Cells]

## Related pages

- [Floorplanning](../stages/floorplanning.md)
- [Clock Tree Synthesis](../stages/clock-tree-synthesis.md)
