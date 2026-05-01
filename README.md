# Python Clean Code — 12-Module Refactoring Course

**New here? Read [WHY.md](WHY.md) first.**

A test-driven, constraint-based course for writing more idiomatic Python. No lectures. No slides. Just messy code, a failing constraint, and a green test suite telling you whether you got it right.

## How it works

Every module has three files:

| File | Purpose |
|---|---|
| `messy_code.py` | Working but ugly code — this is what you edit |
| `test_code.py` | Pytest suite — **do not edit this** |
| `README.md` | The constraint for the module |

**The workflow:**

```bash
cd 01_guard_clause
pytest test_code.py   # should be green — verify before touching anything
# read the README, apply the constraint
pytest test_code.py   # must still be green — you pass when it is
```

The constraint is what makes it a refactoring exercise. You are not adding features. You are changing the structure of code whose behaviour is already locked in by the tests.

## Recommended order

The modules can be done in any order, but this sequence builds concepts progressively — easier wins first, more advanced patterns later.

**Start here — readability basics:**

1. [Guard Clause](01_guard_clause/) — most immediate visual payoff, everyone has nested ifs
2. [Explaining Variable](02_explaining_variable/) — naming things, no new Python required
3. [List Comprehension](03_list_comprehension/) — Pythonic idiom, satisfying to apply
4. [Extract Function](04_extract_function/) — naming at the function level, builds on explaining_variable

**Then — Python-specific patterns:**

5. [Magic Numbers](05_magic_numbers/) — simple, mechanical change
6. [Magic Strings](06_magic_strings/) — builds on magic numbers, introduces Enums
7. [Dataclass](07_dataclass/) — structured data, requires understanding classes *(real-world PR optional)*
8. [Generator](08_generator/) — memory and iteration, more advanced Python *(real-world PR optional)*

**Save for last — exception handling cluster:**

9. [Bare and Broad Except](09_exception_handling/) — start here for exceptions
10. [Try/Except for Flow Control](10_exception_flow_control/) — exceptions vs conditionals *(real-world PR optional)*
11. [Consistent Returns](11_consistent_returns/) — thinking in contracts
12. [Exception Logging](12_exception_logging/) — ties the exception cluster together

---

## Prerequisites

```bash
pip install pytest
```

That's it. No other dependencies.
