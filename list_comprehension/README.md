# Module 2: Death to the `for` Loop

## Before you touch anything

Open [messy_code.py](messy_code.py) and read the three functions. Then answer these:

- For `get_discounted_prices` — how many lines does it take to say "give me the prices of in-stock items, discounted by 10%"?
- Could you read each function and say out loud in one sentence what it does?
- What's the minimum number of lines each function actually needs?

Now run the tests:

```bash
pytest test_code.py
```

All green. Correct — just noisy.

---

## The Problem

All three functions follow the same pattern: create an empty list, loop over items, conditionally append, return the list. This is the most common form of noise in Python code.

It's not wrong. It's just 4 lines where 1 would do.

## Your Task

Replace every function body with a **single list comprehension**. No helper variables, no `append`, no multi-line `for` loop.

```python
# Before — 4 lines to say one thing
def get_names(items):
    names = []
    for item in items:
        names.append(item["name"])
    return names

# After — 1 line that reads like English
def get_names(items):
    return [item["name"] for item in items]
```

For functions that filter *and* transform, the comprehension handles both:

```python
[transform(x) for x in items if condition(x)]
```

## Rules

- Each function body must be a **single `return` statement** containing one list comprehension.
- No `for` loops, no `.append()`, no intermediate list variables.
- All 7 tests must still pass.

## Workflow

```bash
pytest test_code.py   # green before
# refactor messy_code.py
pytest test_code.py   # green after
```

---

## What you just learned

A list comprehension is Python's way of saying "build me a list by doing X for each item in Y, optionally filtered by Z" — all in one readable line.

The practical benefit: when a function is one line, you understand it in one glance. When it's four lines, you have to read and mentally execute each step. Multiply that by a hundred functions in a codebase and you understand why readability compounds.

List comprehensions also signal intent. A `for` loop with `append` could be doing anything — collecting results, running side effects, modifying state. A list comprehension is unambiguous: it builds a list. Nothing else.

---

---

## Submission 1 — The Exercise

Push your refactored `messy_code.py`. The autograding check runs automatically — all 7 tests must be green.

## Submission 2 — Real World PR

1. Open your actual codebase and find one `for` loop that appends to a list
2. Replace it with a list comprehension
3. Open a PR in that codebase
4. On this repo, create a branch (e.g. `list-comprehension-real-world`)
5. Fill in [REAL_WORLD.md](REAL_WORLD.md) — PR link, before/after snippets, one sentence explanation
6. Open a PR on this repo and request Elena's review
