---
title: ASIC Design Flow
type: concept
sources: [S1, S2, S4]
updated: 2026-11-12
---

# ASIC Design Flow

## Definition

An ASIC, an application-specific integrated circuit, is silicon manufactured to carry out a specific function. [S4 §ASIC]

The ASIC design flow is the series of steps that takes a chip from an idea to the data used for fabrication. Each step is supported by electronic design automation (EDA) tools. [S2 §Newcomers' Tutorial]

The newcomers' tutorial lists five broad steps. [S2 §Newcomers' Tutorial]

1. Design entry: the design is described in a hardware description language, usually at the register transfer level. See [RTL Design](../stages/rtl-design.md). [S2 §Newcomers' Tutorial]
2. [Functional verification](../stages/functional-verification.md): simulation and formal verification confirm that the design behaves as required. [S2 §Newcomers' Tutorial]
3. [Synthesis](../stages/logic-synthesis.md): the description is converted into a [netlist](netlist.md). [S2 §Newcomers' Tutorial]
4. Physical implementation: the netlist is turned into a layout through [floorplanning](../stages/floorplanning.md), [placement](../stages/placement.md), [clock tree synthesis](../stages/clock-tree-synthesis.md), and [routing](../stages/routing.md). [S2 §Newcomers' Tutorial]
5. [Signoff](../stages/signoff.md): final checks before the layout is sent for manufacturing. [S2 §Newcomers' Tutorial]

Also called: PnR, Placement and Routing, Place and Route (all for step 4)

## Why it matters

- Designing an ASIC takes considerable expertise and can last several months; following a proven flow keeps the work on schedule. [S2 §Newcomers' Tutorial]
- The part from synthesis to the final layout file can be run automatically, without human intervention. [S1 §Running The Automated RTL-to-GDS Flow]
- The five steps are only the outline. Scan chain insertion, pattern generation, and one or more ECOs are also part of making a chip. [S2 §Newcomers' Tutorial]

- Digital design targets one of two technologies: ASIC manufacturing, with a higher upfront cost that scales cheaply, or an FPGA, cheaper upfront but costly to scale. [S4 §ASIC]
- EDA, electronic design automation, is the field that builds the software, hardware, and services which automate chip design tasks. [S4 §EDA]

- Placement determines the positions of standard cells and macros in the layout, and routing determines the shapes of the connections between them; each result is checked for legality. [S4 §PnR]

## Source differences

- Physical implementation: S2 treats floorplanning, placement, clock tree synthesis, and routing as sub-steps of one step [S2 §Newcomers' Tutorial], while S1 treats them as separate stages of the flow, each cleaned and rerun on its own. [S1 §Design Goals]
- The end of the flow: S2 ends with a signoff step made of DRC, LVS, STA, and an antenna check [S2 §Signoff Steps], while S1 has no stage called signoff and ends with layout generation. [S1 §Design Goals]
- The start of the flow: S2 begins at design entry and functional verification [S2 §Newcomers' Tutorial], while S1 begins with finished SystemVerilog files. [S1 §Design Input SystemVerilog]

- The scope of `PnR`: S2 uses the abbreviation as another name for the whole physical implementation step, floorplanning and clock tree synthesis included [S2 §Newcomers' Tutorial], while S4 defines it as a phase made of two things, placement and routing [S4 §PnR], and names floorplanning next to it in a list of what OpenROAD is used for. [S4 §OpenROAD]

## Related pages

- [RTL Design](../stages/rtl-design.md)
- [Functional Verification](../stages/functional-verification.md)
- [Logic Synthesis](../stages/logic-synthesis.md)
- [Floorplanning](../stages/floorplanning.md)
- [Placement](../stages/placement.md)
- [Clock Tree Synthesis](../stages/clock-tree-synthesis.md)
- [Routing](../stages/routing.md)
- [Layout Finishing](../stages/layout-finishing.md)
- [Signoff](../stages/signoff.md)
- [Netlist](netlist.md)
- [PPA](ppa.md)
- [RTL](rtl.md)
- [PDK](pdk.md)
- [Tape-out](tape-out.md)
