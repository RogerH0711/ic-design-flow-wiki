---
title: cocotb
type: tool
sources: [S10, S11]
updated: 2026-11-13
---

# cocotb

## What it is

_Not yet covered by an ingested source._

cocotb testbenches are written in Python: its logging uses Python's logging library, and signal values can be assigned as Python integers. [S11 §Logging] [S11 §Signed and unsigned values]

## Role in the flow

- A test is a coroutine marked with the cocotb test decorator. [S11 §Identifying tests]
- The test reads values from the DUT through handle objects. [S11 §Reading values from signals]
- Coroutines can run one after another or concurrently, so several activities can go on at once in a test. [S11 §Concurrent and sequential execution]
- A test passes if its main coroutine finishes without raising an exception, and fails if an assert statement fails or if it raises an exception other than a cancellation. [S11 §Passing and failing tests]
- Besides ordinary assignments, signals can be forced to a value or frozen at their current one, where the simulator supports it. [S11 §Forcing and freezing signals]
- The OpenTitan project names it among the open-source verification methodologies it promotes. [S10 §Language and Tool Selection]

## Related pages

- [Functional Verification](../stages/functional-verification.md)
- [Verilator](verilator.md)
- [Testplan](../concepts/testplan.md)
