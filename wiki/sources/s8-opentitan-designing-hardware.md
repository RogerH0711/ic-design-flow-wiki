---
title: "S8: OpenTitan, Designing Hardware"
type: source
source_id: S8
sources: [S8]
updated: 2026-11-12
---

# S8: OpenTitan, Designing Hardware

## Summary

A guide for RTL designers in the OpenTitan project on how to start a hardware design: the typical process for declaring features and finding reviewers. [S8 §Designing Hardware]

## Key points

- The life of a design has three broad stages: Specification, In Development, and Signed off. [S8 §Stages of a Design]
- A design starts as a brief proposal of its basic features, handled through a request-for-comment process. [S8 §Concept and RFC]
- After a first review, a full detailed specification is written. [S8 §Detailed Specification]
- It is then published to the wider team, whose comments the authors address. [S8 §Specification Publication]
- Coding can begin in parallel with that review, starting from a skeleton design. [S8 §Initial Skeleton Design]
- The skeleton grows into the full design in small steps and is finally included in the top level. [S8 §Full Design]

## Coverage

- Describes one project's process and says so: these are methods that have worked there, not fixed rules. [S8 §Stages of a Design]
- The last third is specific to changing interrupts in that project and was not used. [S8 §Change of Interrupts]

## Related pages

- [Specification](../stages/specification.md)
- [RTL Design](../stages/rtl-design.md)
- [ASIC Design Flow](../concepts/asic-design-flow.md)
