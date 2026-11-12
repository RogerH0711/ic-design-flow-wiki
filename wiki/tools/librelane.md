---
title: LibreLane
type: tool
sources: [S2]
updated: 2026-11-12
---

# LibreLane

## What it is

LibreLane is an infrastructure library for building physical implementation flows for digital ASICs out of open-source and commercial EDA tools. Its predecessor is OpenLane. [S2 §What is LibreLane?]

It includes a reference flow, named Classic, that uses only open-source tools and is configured through a single file. [S2 §What is LibreLane?]

## Role in the flow

- A design is described by a configuration file; the minimum is the design name, the Verilog files, the clock period, and the clock port. [S2 §Configuration]
- A flow is a sequence of steps. Each step gets its own numbered directory holding its logs, reports, metrics, and outputs. [S2 §Run directory]
- The state of the design is passed from step to step, so the layout can be opened as it was after any step. [S2 §Run directory]
- A `final` directory gathers every view of the finished design, together with its metrics. [S2 §Final Results]
- Flows can be extended or changed with Python scripts. [S2 §What is LibreLane?]

## Related pages

- [OpenROAD](openroad.md)
- [Yosys](yosys.md)
- [KLayout](klayout.md)
- [Magic](magic.md)
- [Netgen](netgen.md)
- [Signoff](../stages/signoff.md)
- [ASIC Design Flow](../concepts/asic-design-flow.md)
