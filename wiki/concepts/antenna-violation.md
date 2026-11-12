---
title: Antenna Violation
type: concept
sources: [S1, S2]
updated: 2026-11-12
---

# Antenna Violation

## Definition

An antenna violation occurs when a net's antenna ratio is larger than the limit given in the process design kit. [S1 §Antenna Checker]

The flow tutorial describes the antenna ratio as the ratio of the gate area to the gate oxide area, and says that the amount of charge collected depends on the size of the conductor. [S1 §Antenna Checker]

## Why it matters

- The rule guards against the antenna effect: during fabrication, a long metal wire attached to a transistor gate collects charge, and that charge can damage the gate's thin oxide. [S2 §Antenna Check]
- Foundries therefore supply antenna rules that a layout must obey. [S2 §Antenna Check]
- One remedy is to have the router keep wire segments short and bridge long ones; another is to add an antenna diode next to the affected input pin, which drains the charge without disturbing the circuit. [S2 §Antenna Check]
- An antenna checker reports which nets violate the rule. [S1 §Antenna Checker]

## Source differences

- The ratio: S1 describes the antenna ratio as gate area to gate oxide area [S1 §Antenna Checker], while S2 describes the rule as a limit on the ratio between the area that collects charge and the thin-oxide area that drains it. [S2 §Antenna Check]

## Related pages

- [Routing](../stages/routing.md)
- [Signoff](../stages/signoff.md)
