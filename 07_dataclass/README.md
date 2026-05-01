# Module 7: Native Types

## Before you touch anything

Open [messy_code.py](messy_code.py) and read the `User` class and the functions that use it. Then answer these:

- If you mistyped `user.naem` instead of `user.name`, when would you find out?
- Can you tell from looking at the class definition exactly what fields a User has and what types they are?
- If someone new joined the team and asked "what does a User look like?", where would you point them?

Run the tests:

```bash
pytest test_code.py
```

All green. But the structure could tell us more.

---

## The Problem

The current `User` class is written in a style from before Python 3.7. It works, but it makes you write a lot of boilerplate — a manual `__init__` that just stores fields, no type hints, no auto-generated `__repr__` or `__eq__`. You also can't tell at a glance what the default values are.

Python's `dataclass` decorator was introduced specifically to eliminate this boilerplate.

## Your Task

Replace the manual `User` class with a **Python `dataclass`**. Define it once at the top with type hints and default values, and let Python generate the rest.

```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str
    age: int
    role: str = "viewer"
```

This single definition replaces the manual `__init__` and gives you `__repr__` and `__eq__` for free. Update `create_user` to return a `User` instance using the constructor directly.

## Rules

- Define a `User` dataclass with `name`, `email`, `age`, and `role` (default `"viewer"`).
- `create_user` must return a `User` instance constructed normally (no `__new__`).
- All 12 tests must still pass.

## Workflow

```bash
pytest test_code.py   # green before
# refactor messy_code.py
pytest test_code.py   # green after
```

---

## What you just learned

A `dataclass` is a class whose purpose is to hold data. The decorator generates `__init__`, `__repr__`, and `__eq__` automatically from the field definitions — the things you'd otherwise write by hand every time.

The practical benefits:
- **Type hints make the schema explicit.** Anyone reading `User` knows immediately what fields exist and what types they are.
- **Typos fail loudly.** `user.naem` raises `AttributeError` immediately. The same typo in a dict key raises `KeyError` at runtime, but only on the code path that actually hits it — which might be rare.
- **`__repr__` is free.** Print a dataclass and you get `User(name='Alice', email='alice@example.com', age=30, role='viewer')`. Print a manually written class without `__repr__` and you get `<__main__.User object at 0x10f3a2b50>`.
- **`__eq__` is free.** Two users with the same fields are equal. You'd have to write that by hand otherwise.

---

---

## Submission 1 — The Exercise

Push your refactored `messy_code.py`. The autograding check runs automatically — all 12 tests must be green.

## Submission 2 — Real World PR (Optional)

**This submission is optional.** Dataclasses are most useful when your code has manual class definitions or dictionaries passed between functions to represent structured objects. If your codebase is mostly scripts or notebooks without custom classes, skip this one.

If you do find one:

1. Open your actual codebase and find one place where a dictionary is passed between functions to represent a structured object (a user, an order, a config)
2. Refactor it to use a dataclass
3. Open a PR in that codebase
4. On this repo, create a branch (e.g. `dataclass-real-world`)
5. Fill in [REAL_WORLD.md](REAL_WORLD.md) — PR link, before/after snippets, one sentence explanation
6. Open a PR on this repo and request Elena's review
