---
title: OpenROAD
type: tool
sources: [S1, S2]
updated: 2026-11-12
---

# OpenROAD

## What it is

OpenROAD is the application that carries out the automated flow: Tcl scripts drive open-source tools from synthesis through to the final layout file. [S1 §Running The Automated RTL-to-GDS Flow]

Results can be examined either with commands in a shell or in its graphical interface. [S1 §Timing]

## Role in the flow

The tutorial points to one component per flow step, each documented inside the OpenROAD project. [S1 §Running The Automated RTL-to-GDS Flow]

- Pdngen does the power planning. [S1 §Power Planning And Analysis]
- PDNSim is a static IR analyzer for the power grid. [S1 §IR Drop Analysis]
- ICeWall places I/O cells around the edge of a chip. [S1 §Chip Level IO Pad Placement]
- TritonRoute is the detailed router. [S1 §Detail Routing]
- OpenRCX is the parasitics extraction tool. [S1 §Parasitics Extraction]
- The graphical interface includes a viewer for design rule violations. [S1 §DRC Viewer]
- The LibreLane reference flow also builds on it: its floorplan and timing analysis steps are OpenROAD steps. [S2 §Run directory]
- The layout of a LibreLane run can be opened in the OpenROAD graphical interface as well. [S2 §Viewing the Layout]

## Related pages

- [OpenROAD Flow Scripts](openroad-flow-scripts.md)
- [LibreLane](librelane.md)
- [Floorplanning](../stages/floorplanning.md)
- [Routing](../stages/routing.md)
- [IR Drop](../concepts/ir-drop.md)
- [ODB](../formats/odb.md)
