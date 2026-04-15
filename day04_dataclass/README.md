# Day 4: Native Types

## The Problem

[messy_code.py](messy_code.py) passes user data around as plain dictionaries. This is a common Python anti-pattern: there's nothing stopping you from writing `user["naem"]` and having a silent typo bug, and nothing tells a reader what fields a "user" actually has.

## Your Task

Replace the dictionary with a **Python `dataclass`**. Define it once at the top, then update every function to work with the dataclass instead of `dict` key lookups.

```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str
    age: int
    role: str = "viewer"
```

Once defined, `create_user` should return a `User` instance, and every other function should accept `User` objects and use **attribute access** (`user.name`) instead of dict access (`user["name"]`).

## Why

- Typo in a dict key raises `KeyError` at runtime. Typo in an attribute raises `AttributeError` at runtime AND your IDE underlines it in red immediately.
- Dataclasses are self-documenting: the class definition is the schema.
- Tab completion works on attributes, not on strings.

## Rules

- Define a `User` dataclass with `name`, `email`, `age`, and `role` (default `"viewer"`).
- No function may use `dict` key access (`user["field"]`) — use attribute access (`user.field`) throughout.
- `create_user` must return a `User` instance, not a `dict`.
- All 12 tests must still pass.

## Workflow

```bash
pytest test_code.py   # green before
# refactor
pytest test_code.py   # green after
```
