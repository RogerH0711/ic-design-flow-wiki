---
title: Netgen
type: tool
sources: [S2]
updated: 2026-11-12
---

# Netgen

## What it is

Netgen is the tool the reference flow uses for [LVS](../concepts/lvs.md). [S2 §LVS]

## Role in the flow

- It receives the layout, already converted to a SPICE netlist, and the schematic, and compares them. [S2 §LVS]
- Its log ends with a one-line verdict; a clean result says that the circuits match uniquely. [S2 §LVS]
- When there are errors, a second, more detailed report sets layout and schematic side by side. [S2 §LVS]

## Related pages

- [Signoff](../stages/signoff.md)
- [LVS](../concepts/lvs.md)
- [Netlist](../concepts/netlist.md)
