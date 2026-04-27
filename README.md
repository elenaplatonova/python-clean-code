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
cd guard_clause
pytest test_code.py   # should be green — verify before touching anything
# read the README, apply the constraint
pytest test_code.py   # must still be green — you pass when it is
```

The constraint is what makes it a refactoring exercise. You are not adding features. You are changing the structure of code whose behaviour is already locked in by the tests.

## The 12 Modules

| Module | Constraint | Concept |
|---|---|---|
| [Guard Clause](guard_clause/) | Flatten 5 levels of nesting — no `else`, no line indented more than once | Guard clauses / early return |
| [List Comprehension](list_comprehension/) | Replace every `for`+`append` loop with a single list comprehension | List comprehensions |
| [Explaining Variable](explaining_variable/) | Break one-liner expressions into named intermediate variables | Explaining variables |
| [Dataclass](dataclass/) | Replace a `dict`-based data model with a `dataclass` | Dataclasses |
| [Generator](generator/) | Replace `readlines()` + list with `yield` — hold one line in memory at a time | Generators |
| [Magic Numbers](magic_numbers/) | Extract every numeric literal into a named constant | Magic numbers |
| [Magic Strings](magic_strings/) | Replace string literals with Enums for roles, statuses, and types | Magic strings / Enums |
| [Bare and Broad Except](exception_handling/) | No bare `except`, no `except Exception` — catch only the specific exception | Specific exceptions |
| [Try/Except for Flow Control](exception_flow_control/) | No `try/except` for dict lookups or routine checks — use `.get()` and `if` | Exceptions vs conditionals |
| [Consistent Returns](consistent_returns/) | Every function returns one type — raise for bad input, return zero value for empty | Consistent return types |
| [Exception Logging](exception_logging/) | Every `except` block must log before returning | Exception logging |
| [Extract Function](extract_function/) | Extract every inline calculation into a named helper function | Function decomposition |

## Automated feedback

Every push triggers the GitHub Actions workflow in [.github/workflows/python-app.yml](.github/workflows/python-app.yml). Each module's tests run as a separate step. If you broke the logic while cleaning up, you get a red X on that step. All green = you're done.

## Prerequisites

```bash
pip install pytest
```

That's it. No other dependencies.
