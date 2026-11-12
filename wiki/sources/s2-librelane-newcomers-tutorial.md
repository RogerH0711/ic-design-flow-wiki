---
title: "S2: LibreLane Newcomers' Tutorial"
type: source
source_id: S2
sources: [S2]
updated: 2026-11-12
---

# S2: LibreLane Newcomers' Tutorial

## Summary

An introduction for readers who already know some digital design. It opens with the steps needed to realize an ASIC, from design entry to signoff, and then introduces LibreLane. [S2 §Newcomers' Tutorial]

The rest is a worked example: a 32-bit multiplier is run through the default flow, and the results are inspected, with most attention on the signoff checks. [S2 §PM32 example]

## Key points

- The broad steps are design entry, functional verification, synthesis, physical implementation, and signoff; other steps such as scan chain insertion exist but are left out. [S2 §Newcomers' Tutorial]
- LibreLane is a library for building physical implementation flows, and ships a reference flow made only of open-source tools. [S2 §What is LibreLane?]
- A design needs at least four settings: its name, its Verilog files, the clock period, and the clock port. [S2 §Configuration]
- A flow is a sequence of steps, and every step leaves its own directory of logs, reports, metrics, and outputs. [S2 §Run directory]
- Signoff is the last phase before manufacturing and consists of DRC, LVS, STA, and an antenna check. [S2 §Signoff Steps]
- Timing is checked at several corners that combine interconnect, process, voltage, and temperature extremes. [S2 §STA]

## Coverage

- Covered in detail: the four signoff checks, what each compares, and how to read their reports. [S2 §Signoff Steps]
- Covered briefly: the overall list of steps, each in a sentence or two. [S2 §Newcomers' Tutorial]
- Not explained: what happens inside synthesis, floorplanning, placement, clock tree synthesis, and routing. They appear only as names of step directories. [S2 §Run directory]

## Related pages

- [ASIC Design Flow](../concepts/asic-design-flow.md)
- [RTL Design](../stages/rtl-design.md)
- [Functional Verification](../stages/functional-verification.md)
- [Logic Synthesis](../stages/logic-synthesis.md)
- [Floorplanning](../stages/floorplanning.md)
- [Routing](../stages/routing.md)
- [Layout Finishing](../stages/layout-finishing.md)
- [Signoff](../stages/signoff.md)
- [Netlist](../concepts/netlist.md)
- [DRC](../concepts/drc.md)
- [LVS](../concepts/lvs.md)
- [Static Timing Analysis](../concepts/static-timing-analysis.md)
- [Timing Corners](../concepts/timing-corners.md)
- [Timing Violations](../concepts/timing-violations.md)
- [Antenna Violation](../concepts/antenna-violation.md)
- [LibreLane](../tools/librelane.md)
- [KLayout](../tools/klayout.md)
- [Magic](../tools/magic.md)
- [Netgen](../tools/netgen.md)
- [OpenROAD](../tools/openroad.md)
- [Yosys](../tools/yosys.md)
- [DEF](../formats/def.md)
- [GDSII](../formats/gdsii.md)
- [ODB](../formats/odb.md)
- [SDC](../formats/sdc.md)
