---
title: KLayout
type: tool
sources: [S1, S2, S4]
updated: 2026-11-12
---

# KLayout

## What it is

KLayout is a free, open-source viewer and editor for layouts in DEF or GDSII form. [S4 §KLayout]

The newcomers' tutorial uses it to open the final layout. [S2 §Viewing the Layout]

## Role in the flow

- It is one of the two tools that run [DRC](../concepts/drc.md) at signoff. [S2 §DRC]
- Its marker browser loads a DRC report and shows the violations on the layout. [S2 §DRC]
- The flow tutorial links to it for the layout generation step. [S1 §Running The Automated RTL-to-GDS Flow]

- It can convert GDSII to OASIS. [S4 §GDSII]

## Related pages

- [Signoff](../stages/signoff.md)
- [DRC](../concepts/drc.md)
- [Magic](magic.md)
- [GDSII](../formats/gdsii.md)
