---
title: SPEF
type: format
sources: [S1, S4]
updated: 2026-11-12
---

# SPEF

Also called: Standard Parasitic Exchange Format

## What it is

An `.spef` file is the optional output of parasitics extraction, which works out the resistance and capacitance of the routed wires. [S1 §Parasitics Extraction]

SPEF is the IEEE-standard way to record how much parasitic resistance and capacitance the wires of a circuit have. [S4 §SPEF]

## Produced by and used by

- The parasitics extraction tool writes it from the routed design. [S1 §Parasitics Extraction]
- The flow keeps the final one as `6_final.spef`. [S1 §Viewing OpenROAD-flow-scripts Directory Structure And Results]

## Related pages

- [Layout Finishing](../stages/layout-finishing.md)
