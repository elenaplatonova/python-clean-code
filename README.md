# Python Clean Code — 5-Day Refactoring Course

A test-driven, constraint-based course for writing more idiomatic Python. No lectures. No slides. Just messy code, a failing constraint, and a green test suite telling you whether you got it right.

## How it works

Every day has three files:

| File | Purpose |
|---|---|
| `messy_code.py` | Working but ugly code — this is what you edit |
| `test_code.py` | Pytest suite — **do not edit this** |
| `README.md` | The constraint for the day |

**The daily loop:**

```bash
cd dayXX_topic
pytest test_code.py   # should be green — verify before touching anything
# read the README, apply the constraint
pytest test_code.py   # must still be green — you pass when it is
```

The constraint is what makes it a refactoring exercise. You are not adding features. You are changing the structure of code whose behaviour is already locked in by the tests.

## The 5 Days

| Day | Constraint | Concept |
|---|---|---|
| [Day 1](day01_guard_clause/) | Flatten 5 levels of nesting — no `else`, no line indented more than once | Guard clauses / early return |
| [Day 2](day02_list_comprehension/) | Replace every `for`+`append` loop with a single list comprehension | List comprehensions |
| [Day 3](day03_explaining_variable/) | Break one-liner expressions into named intermediate variables | Explaining variables |
| [Day 4](day04_dataclass/) | Replace a `dict`-based data model with a `dataclass` | Dataclasses |
| [Day 5](day05_generator/) | Replace `readlines()` + list with `yield` — hold one line in memory at a time | Generators |

## Automated feedback

Every push triggers the GitHub Actions workflow in [.github/workflows/python-app.yml](.github/workflows/python-app.yml). Each day's tests run as a separate step. If you broke the logic while cleaning up, you get a red X on that step. All green = you're done.

## Prerequisites

```bash
pip install pytest
```

That's it. No other dependencies.
