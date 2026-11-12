---
title: SPEF
type: format
sources: [S1]
updated: 2026-11-12
---

# SPEF

## What it is

An `.spef` file is the optional output of parasitics extraction, which works out the resistance and capacitance of the routed wires. [S1 §Parasitics Extraction]

## Produced by and used by

- The parasitics extraction tool writes it from the routed design. [S1 §Parasitics Extraction]
- The flow keeps the final one as `6_final.spef`. [S1 §Viewing OpenROAD-flow-scripts Directory Structure And Results]

## Related pages

- [Layout Finishing](../stages/layout-finishing.md)
