# Module 1: The Guard Clause

## Before you touch anything

Open [messy_code.py](messy_code.py) and read `process_payment`. Then answer these:

- How many seconds did it take you to find where the actual charge is calculated?
- If you needed to add a 7th condition (e.g. "user must have a verified email"), where would it go?
- If there's a bug where the wrong error reason is returned, how quickly can you spot it?

Now run the tests to confirm the code works:

```bash
pytest test_code.py
```

All green. The code is correct. It's just hard to read.

---

## The Problem

`process_payment` has **5 levels of nesting**. Every happy-path line is buried deep inside a pyramid of `if/else` blocks. The deeper the nesting, the more conditions your brain has to track simultaneously just to understand one line.

This is sometimes called the "arrow anti-pattern" — if you squint at the indentation, it looks like an arrow pointing right.

## Your Task

Refactor `process_payment` so that **no line of real logic is indented more than once** inside the function body.

**The technique:** Use *guard clauses* — early `return` statements that handle failure cases at the top, so the happy path runs last with no indentation.

```python
# Before: logic buried in nesting
def process_payment(user, order):
    if user is not None:
        if user.get("is_active"):
            ...  # happy path buried 4 levels deep

# After: guards up top, happy path flat at the bottom
def process_payment(user, order):
    if user is None:
        return {"status": "error", "reason": "no_user"}
    if not user.get("is_active"):
        return {"status": "error", "reason": "inactive_user"}
    ...  # happy path — no nesting needed
```

## Rules

- No `else` statements allowed.
- No line of logic should be indented more than **one level** inside the function.
- All 8 tests must still pass.

## Workflow

```bash
pytest test_code.py   # green before
# refactor messy_code.py
pytest test_code.py   # green after
```

---

## What you just learned

**Guard clauses** make the failure cases explicit and get them out of the way early. The happy path — the thing the function actually exists to do — sits at the bottom with no indentation.

The practical benefit: when you come back to this function in three months, you read top to bottom. Each guard clause is a complete thought: "if this is wrong, stop here." No need to hold multiple conditions in your head at once.

This is one of the most common refactors in professional codebases. Most deeply nested code can be flattened with early returns.

---

---

## Submission 1 — The Exercise

Push your refactored `messy_code.py`. The autograding check runs automatically — all 8 tests must be green.

## Submission 2 — Real World PR

1. Open your actual codebase and find one function with more than two levels of nesting
2. Apply the guard clause technique — flatten it, remove the `else` statements
3. Open a PR in that codebase
4. On this repo, create a branch (e.g. `guard-clause-real-world`)
5. Fill in [REAL_WORLD.md](REAL_WORLD.md) — PR link, before/after snippets, one sentence explanation
6. Open a PR on this repo and request Elena's review
