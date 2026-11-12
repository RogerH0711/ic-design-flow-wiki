---
title: PDK
type: concept
sources: [S4, S6]
updated: 2026-11-12
---

# PDK

Also called: Process Design Kit

## Definition

A process design kit (PDK) describes one fabrication process to the design tools. It is a set of files, and the tools used to design a chip rely on it as their model of that process. [S4 §PDK]

- A foundry is a semiconductor manufacturer. [S4 §foundry]
- A process node is one manufacturing process run by a particular foundry, usually named by the foundry and a number. The number once referred to a physical characteristic such as the minimum feature length, but since the mid-1990s it has been more or less arbitrary. [S4 §process node]

## Why it matters

- A design can only be made for a particular process node with the PDK of that node. [S4 §process node]
- sky130 is an open-source PDK for a 180 nm to 130 nm hybrid technology of SkyWater, and the default PDK of LibreLane. [S4 §sky130]
- Design rules are set by the foundry for a given manufacturing process. [S4 §DRC]

- The SKY130 PDK is made up of libraries. Each library name states the process, the library's source, its type (for example digital standard cells or I/O and periphery), and optionally a name. [S6 §Library Naming]
- Its table of file types includes a DRC deck, an LVS deck, abstract cell views, timing files, transistor-level netlists, and device models for use with SPICE. [S6 §File Types]
- The same table has rows for seal ring rules, marked ready for open tooling, and for fill structure rules and scribe line rules, which are not. Open tools are mostly marked ready, while the closed-tool entries are mostly in progress. [S6 §File Types]

## Related pages

- [DRC](drc.md)
- [Standard Cell Library](standard-cell-library.md)
- [Tape-out](tape-out.md)
- [LEF](../formats/lef.md)
- [Dotlib](../formats/dotlib.md)
