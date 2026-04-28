# Module 6: Magic Strings

## Before you touch anything

Open [messy_code.py](messy_code.py) and read all the functions. Then answer these:

- If someone types `user["role"] == "Admin"` instead of `"admin"`, what happens? When do you find out?
- The string `"admin"` appears in three different functions. If the role is renamed to `"superuser"`, how many places need to change?
- Is there anything stopping someone from inventing a new status like `"in_transit"` instead of `"shipped"`? How would you know it happened?
- Can your IDE autocomplete `"pending"` when you're typing a status check?

Run the tests:

```bash
pytest test_code.py
```

All green. The logic is correct — but the strings are invisible and fragile.

---

## The Problem

A **magic string** is a string literal used as a meaningful value — a role, a status, a type — scattered across the codebase. The problems are the same as magic numbers, but worse:

- Typos are silent. `"Admin" != "admin"` fails at runtime, not at write time.
- No fixed set. Nothing defines what the valid roles or statuses actually are.
- No autocomplete. You have to remember (or copy-paste) the exact string every time.

## Your Task

Replace magic strings with **Enums** — Python's built-in way to define a fixed set of named values.

```python
from enum import Enum

class Role(Enum):
    ADMIN = "admin"
    EDITOR = "editor"
    VIEWER = "viewer"

class OrderStatus(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"
```

Then update every function to compare against enum members instead of string literals:

```python
# Before
if user["role"] == "admin":

# After
if user["role"] == Role.ADMIN.value:
```

## Rules

- Define a `Role` enum and an `OrderStatus` enum at the top of the file.
- No string literals like `"admin"`, `"editor"`, `"pending"` etc. inside any function body — use enum members instead.
- All 21 tests must still pass.

## Workflow

```bash
pytest test_code.py   # green before
# refactor messy_code.py
pytest test_code.py   # green after
```

---

## What you just learned

An `Enum` defines a closed set of valid values. Once you have `Role.ADMIN`, you can't accidentally create `Role.ADNIM` — it doesn't exist, and Python will tell you immediately.

The practical benefits:
- **Typos fail loudly.** `Role.ADNIM` raises `AttributeError` at write time (your IDE underlines it). `"adnim"` fails silently at runtime.
- **One place to change.** Rename a status by changing one line in the enum definition.
- **Autocomplete works.** Type `Role.` and your IDE shows you the valid options.
- **Grep works.** Search for `Role.ADMIN` across the codebase. You can't reliably search for `"admin"` without false positives.
- **The set is documented.** Anyone reading the file sees immediately what all valid roles and statuses are.

---

## Submission 1 — The Exercise

Push your refactored `messy_code.py`. The autograding check runs automatically — all 21 tests must be green.

## Submission 2 — Real World PR

1. Open your actual codebase and find one place where string literals are used to represent a fixed set of values (roles, statuses, types, categories)
2. Replace them with an Enum
3. Open a PR in that codebase
4. On this repo, create a branch (e.g. `magic-strings-real-world`)
5. Fill in [REAL_WORLD.md](REAL_WORLD.md) — PR link, before/after snippets, one sentence explanation
6. Open a PR on this repo and request Elena's review
