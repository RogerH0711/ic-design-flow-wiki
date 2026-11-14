---
title: Layout Finishing
type: stage
order: 9
sources: [S1, S2]
updated: 2026-11-12
---

# Layout Finishing

## Purpose

The last of the flow's stages is called layout generation, with the clean target `clean_finish`. [S1 §Design Goals]

Its logs are `6_1_merge.log` and `6_report.log`. [S1 §Viewing Results And Logs]

## Inputs

- The routed design: metal fill is run after routing. [S1 §Metal Fill]
- The LEF/DEF layout model of the routed design, which parasitics extraction reads. [S1 §Parasitics Extraction]

## Outputs

- `6_final.gds`, the final layout in [GDSII](../formats/gdsii.md) form. [S1 §Viewing OpenROAD-flow-scripts Directory Structure And Results]
- `6_final.odb`, `6_final.sdc`, `6_final.v`, and `6_final.spef`. [S1 §Viewing OpenROAD-flow-scripts Directory Structure And Results]
- The LibreLane reference flow has a `final` directory holding several directories with the different layout views (among them `gds`, `def`, `lef`, `lib`, `sdc`, `sdf`, `spef`, and `spice`), with the final metrics alongside. [S2 §Final Results]

## What happens

- Metal fill adds floating metal shapes in empty areas so that the metal density rules are met without breaking other design rules. It is mandatory at advanced process nodes, where it keeps the wafer evenly planarized. [S1 §Metal Fill]
- Parasitics extraction computes the resistance, coupling capacitance, and ground capacitance of the routed wires and can write them to a [SPEF](../formats/spef.md) file. [S1 §Parasitics Extraction]
- The flow finishes by writing a merged layout file. [S1 §Viewing OpenROAD-flow-scripts Directory Structure And Results]

## Checks

- Timing of the final design is reported as worst slack, total negative slack, and worst negative slack. [S1 §Timing]
- The design area and its utilization are reported. [S1 §Area]
- Power is reported for sequential cells, combinational cells, macros, and pads. [S1 §Power]

## Related pages

- [Routing](routing.md)
- [Signoff](signoff.md)
- [ASIC Design Flow](../concepts/asic-design-flow.md)
- [PPA](../concepts/ppa.md)
- [Timing Violations](../concepts/timing-violations.md)
- [GDSII](../formats/gdsii.md)
- [SPEF](../formats/spef.md)
