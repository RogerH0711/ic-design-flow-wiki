---
title: Specification
type: stage
order: 1
sources: [S2, S8]
updated: 2026-11-12
---

# Specification

## Purpose

In the OpenTitan project, Specification is the first of three broad stages in the life of a design. [S8 §Stages of a Design]

Later stages are judged against it: functional verification checks that the design behaves as expected against the requirements. [S2 §Newcomers' Tutorial]

## Inputs

- A concept. It may come from a module known to be needed, a proposed product feature, or a new approach to an existing design. [S8 §Concept and RFC]

## Outputs

- A specification complete enough that the rest of the project can review it in detail. [S8 §Detailed Specification]
- Once ready for publication, the specification should be converted to a Markdown document stored in the OpenTitan repository. [S8 §Initial Skeleton Design]

## What happens

1. The concept is written up as a brief proposal with the basic features and goes through a request-for-comment process. [S8 §Concept and RFC]
2. After the feature set and high-level description have been reviewed, the full detailed specification is completed. [S8 §Detailed Specification]
3. The specification is published to the wider team, and the authors answer comments and questions and keep refining it. [S8 §Specification Publication]
4. In parallel with that review, a first skeleton of the design can already be started. [S8 §Initial Skeleton Design]

The process applies to new designs; a minor change to an existing design is handled as a pull request or an issue instead. [S8 §Concept and RFC]

## Checks

- Three reviews are mentioned: an initial review of the feature set and high-level description, a potential security review, and a further detailed review of the full specification by other project members. [S8 §Detailed Specification]
- Open questions do not have to block progress: they may be kept in a section of their own while work goes on where there is agreement. [S8 §Specification Publication]

## Related pages

- [RTL Design](rtl-design.md)
- [Functional Verification](functional-verification.md)
- [ASIC Design Flow](../concepts/asic-design-flow.md)
