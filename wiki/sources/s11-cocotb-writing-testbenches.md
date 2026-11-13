---
title: "S11: cocotb, Writing Testbenches"
type: source
source_id: S11
sources: [S11]
updated: 2026-11-13
---

# S11: cocotb, Writing Testbenches

## Summary

A practical chapter of the cocotb documentation on writing testbenches: logging, reading signal values, marking functions as tests, running things concurrently, and what makes a test pass or fail. [S11 §Writing Testbenches]

## Key points

- A test is a function marked with a decorator, which tells cocotb that it is meant to either pass or fail. [S11 §Identifying tests]
- Values inside the DUT are read through handle objects. [S11 §Reading values from signals]
- A test fails when an assert statement fails or when it raises an exception, with one exception type excepted, and passes when it ends without one. [S11 §Passing and failing tests]
- Log messages only log; they never make a test fail. [S11 §Logging]
- Signals can be forced to a value or frozen, though not every simulator supports it. [S11 §Forcing and freezing signals]

## Coverage

- Usage notes for one library; it does not explain what a testbench is or how to plan tests. [S11 §Writing Testbenches]

## Related pages

- [cocotb](../tools/cocotb.md)
- [Functional Verification](../stages/functional-verification.md)
