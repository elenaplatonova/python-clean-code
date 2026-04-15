# Module 10: Consistent Return Types

## Before you touch anything

Open [messy_code.py](messy_code.py) and read all three functions. Then answer these:

- `find_user` returns a `dict` when the user exists and a `str` when it doesn't. What does the caller have to do before using the result?
- `calculate_discount` returns a `float`, a `str`, or `False`. How many type checks does the caller need to write?
- `get_page_count` returns `None`, a `str`, or an `int`. Can you write `total = get_page_count(items, size) + 1` safely?

Run the tests:

```bash
pytest test_code.py
```

Some tests will be **red** — that's expected. Those tests define the correct behaviour. Your job is to make them green.

---

## The Problem

A function that returns different types depending on what happened is a contract that can't be trusted. The caller has to inspect the return value before using it — effectively writing defensive code against the function they just called.

```python
result = find_user(users, user_id)
if isinstance(result, str):   # is it an error?
    ...
elif result is None:          # or is it None?
    ...
else:
    print(result["name"])     # finally, the actual work
```

This is noise that belongs inside the function, not scattered across every call site.

**The two clean patterns:**

1. **Return `None` for "not found"** — the caller uses `if result is not None:` — one check, unambiguous.
2. **Raise `ValueError` for invalid input** — errors that are the *caller's fault* should be exceptions, not return values. The caller passed bad data; they should handle it explicitly with `try/except`, or fix the bad input upstream.

## Your Task

Fix each function:

- `find_user` — return `None` when not found, never a string.
- `calculate_discount` — raise `ValueError` for invalid totals; return `0.0` (not `False`) when no coupon matches.
- `get_page_count` — raise `ValueError` for zero page size; return `0` (not a string) for zero items.

## Rules

- Every function must return exactly **one type** on the happy path.
- Invalid input (caller's fault) → raise `ValueError` with a clear message.
- "Not found" or "empty" → return the zero value of the return type (`None`, `0`, `[]`).
- All 15 tests must pass — including the ones that start red.

## Workflow

```bash
pytest test_code.py   # some red — that's the starting point
# refactor messy_code.py
pytest test_code.py   # all green
```

---

## What you just learned

A function's return type is part of its contract. When callers can't trust what they'll get back, they write defensive code — and that defensive code spreads everywhere the function is called.

The rule: **inputs that are the caller's fault → raise. Outcomes that are valid but empty → return the zero value of your type.**

A function that returns a `dict | str | None | bool` depending on the situation is four functions poorly disguised as one.

---

## Submission 1 — The Exercise

Push your refactored `messy_code.py`. The autograding check runs automatically — all 15 tests must be green.

## Submission 2 — Real World PR

1. Open your actual codebase and find one function that returns different types depending on what happened
2. Fix it — pick one return type, raise for invalid input
3. Open a PR in that codebase
4. On this repo, create a branch (e.g. `consistent-returns-real-world`)
5. Fill in [REAL_WORLD.md](REAL_WORLD.md) — PR link, before/after snippets, one sentence explanation
6. Open a PR on this repo and request Elena's review
