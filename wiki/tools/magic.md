---
title: Magic
type: tool
sources: [S2, S4, S6]
updated: 2026-11-12
---

# Magic

## What it is

Magic is a free software viewer and editor for layouts in DEF or GDSII form. [S4 §Magic]

It is one of the two tools the reference flow uses for [DRC](../concepts/drc.md). [S2 §DRC]

## Role in the flow

- It runs a DRC step at signoff and writes its own report. [S2 §DRC]
- The other DRC step uses [KLayout](klayout.md); both tools have blind spots that the other covers. [S2 §DRC]

- In the SKY130 file type table, Magic is the open tool listed for the DRC deck, for creating mask layout data, and for the abstract cell views, and one of two listed for the LVS deck. [S6 §File Types]

## Related pages

- [Signoff](../stages/signoff.md)
- [DRC](../concepts/drc.md)
- [KLayout](klayout.md)
- [PDK](../concepts/pdk.md)
