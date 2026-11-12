---
title: Tape-out
type: concept
sources: [S2, S4]
updated: 2026-11-12
---

# Tape-out

## Definition

Tape-out ends IC design. Once every check has passed, the design goes to a fabrication facility, which makes the masks from the GDSII data or an equivalent format. [S4 §tape-out]

The name is left over from the time when the data was physically delivered to foundries on tape. [S4 §tape-out]

## Why it matters

- It is the point of commitment that signoff prepares for. [S2 §Signoff Steps]
- A design that has not reached timing closure is usually not fit for tape-out. [S4 §timing closure]
- A multi-project wafer puts several different chips on one wafer so that the cost is shared between projects. [S4 §MPW]

## Related pages

- [Signoff](../stages/signoff.md)
- [GDSII](../formats/gdsii.md)
- [Timing Closure](timing-closure.md)
- [PDK](pdk.md)
