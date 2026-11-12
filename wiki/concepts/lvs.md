---
title: LVS
type: concept
sources: [S2]
updated: 2026-11-12
---

# LVS

Also called: Layout Versus Schematic

## Definition

Layout versus schematic (LVS) compares the layout with the schematic, which is usually a Verilog netlist, and confirms that the connectivity of the two matches. [S2 §LVS]

## Why it matters

- Mistakes in the user's configuration, and even in the tools, can leave the layout wired differently from the design; LVS is the check that catches them. [S2 §LVS]
- Typical findings are shorts, opens, and missing components. [S2 §LVS]
- To make the comparison, the layout is first converted to a SPICE netlist, and then both sides are given to the comparison tool. [S2 §LVS]

## Related pages

- [Signoff](../stages/signoff.md)
- [Netlist](netlist.md)
- [Netgen](../tools/netgen.md)
- [DRC](drc.md)
