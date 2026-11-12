---
title: Signoff
type: stage
order: 10
sources: [S2]
updated: 2026-11-12
---

# Signoff

## Purpose

Signoff is the last phase of implementation: physical and timing verification of the design before it is committed to manufacturing, an event known as tape-out. [S2 §Signoff Steps]

## Inputs

- The finished layout and the rule file of the process design kit, for [DRC](../concepts/drc.md). [S2 §DRC]
- The layout and the schematic, the latter usually as Verilog, for [LVS](../concepts/lvs.md). [S2 §LVS]

## Outputs

- A DRC report from each DRC tool. [S2 §DRC]
- An LVS log with a summary, and a detailed report that compares layout and schematic node by node. [S2 §LVS]
- A timing summary across all corners, plus a directory of reports for every corner. [S2 §STA]
- An antenna report and a summary table of antenna violations. [S2 §Antenna Check]

## What happens

The reference flow runs four checks. [S2 §Signoff Steps]

1. [DRC](../concepts/drc.md) checks the layout against the foundry's manufacturing rules, using two tools that cover each other's blind spots. [S2 §DRC]
2. [LVS](../concepts/lvs.md) confirms that the layout and the schematic have the same connectivity. [S2 §LVS]
3. [Static timing analysis](../concepts/static-timing-analysis.md) is run on the fully implemented design. Earlier runs during implementation are less accurate because the design is not finished. [S2 §STA]
4. The antenna check looks for [antenna violations](../concepts/antenna-violation.md). [S2 §Antenna Check]

## Checks

- DRC: any violation makes the flow report an error with the number of violations found. [S2 §DRC]
- LVS: a clean run ends with the message that the circuits match uniquely. [S2 §LVS]
- STA: the summary shows, for every corner, the worst setup and hold slack and the number of setup, hold, maximum capacitance, and maximum slew violations. [S2 §STA]
- Antenna: the summary table lists each violating net and pin with its metal layer. [S2 §Antenna Check]

## Common problems

- LVS shorts: wires that should be separate are connected, most seriously power to ground. [S2 §LVS]
- LVS opens: wires or components that should be connected are left dangling. [S2 §LVS]
- LVS missing components: a component expected from the schematic is absent from the layout. [S2 §LVS]

## Related pages

- [ASIC Design Flow](../concepts/asic-design-flow.md)
- [Layout Finishing](layout-finishing.md)
- [DRC](../concepts/drc.md)
- [LVS](../concepts/lvs.md)
- [Static Timing Analysis](../concepts/static-timing-analysis.md)
- [Timing Corners](../concepts/timing-corners.md)
- [Antenna Violation](../concepts/antenna-violation.md)
- [KLayout](../tools/klayout.md)
- [Magic](../tools/magic.md)
- [Netgen](../tools/netgen.md)
