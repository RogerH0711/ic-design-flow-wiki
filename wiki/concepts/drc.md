---
title: DRC
type: concept
sources: [S1, S2, S4]
updated: 2026-11-12
---

# DRC

Also called: Design Rule Checking, Design Rule Checks

## Definition

Design rule checking (DRC) tests the layout against rules set by the chip foundry. A layout must satisfy them to be manufacturable; one example is a minimum spacing between two shapes on the same metal layer. [S2 §DRC]

The rules come with the process design kit as a rule file, and the checking tool reads that file together with the layout. [S2 §DRC]

## Why it matters

- It is one of the four signoff checks. [S2 §Signoff Steps]
- A layout with violations stops the flow with an error that gives the number of violations. [S2 §DRC]
- Violations can be viewed graphically, as markers on the layout. [S2 §DRC]

- A design with no violations is called DRC-clean. [S4 §DRC]
- A DRC deck is an implementation of a set of design rule checks for one particular tool. [S4 §DRC deck]

## Source differences

- Where it happens: S2 runs DRC as a signoff step on the finished layout, with two tools [S2 §DRC], while S1 reports design rule violations at the end of detailed routing, in a report that is empty when routing succeeded. [S1 §DRC Viewer]

## Related pages

- [Signoff](../stages/signoff.md)
- [Routing](../stages/routing.md)
- [KLayout](../tools/klayout.md)
- [Magic](../tools/magic.md)
- [LVS](lvs.md)
- [PDK](pdk.md)
