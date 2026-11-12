---
title: "S6: SkyWater SKY130 PDK, Libraries and File Types"
type: source
source_id: S6
sources: [S6]
updated: 2026-11-12
---

# S6: SkyWater SKY130 PDK, Libraries and File Types

## Summary

Two reference pages about the SKY130 PDK. One explains how the libraries in the PDK are named. [S6 §Library Naming]

The other is a single table of file types: what each does, and for open and for closed tooling the tool, its status, the file format, and where the file comes from. [S6 §File Types]

## Key points

- A library name has up to four parts: the process, who made the library, the type of content, and an optional name. [S6 §Library Naming]
- Library types are primitive cells, digital standard cells, build space, I/O and periphery, and miscellaneous. [S6 §Library Naming]
- The file types listed include a DRC deck, an LVS deck, abstract cell views, timing files, transistor-level netlists, and device models. [S6 §File Types]

## Coverage

- A naming scheme and a table; neither page explains how the files are used in a flow. [S6 §File Types]

## Related pages

- [PDK](../concepts/pdk.md)
- [Standard Cell Library](../concepts/standard-cell-library.md)
- [DRC](../concepts/drc.md)
- [LVS](../concepts/lvs.md)
- [LEF](../formats/lef.md)
- [Dotlib](../formats/dotlib.md)
- [Magic](../tools/magic.md)
- [Netgen](../tools/netgen.md)
