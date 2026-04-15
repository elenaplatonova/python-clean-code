# Day 1: The Guard Clause

## The Problem

`process_payment` in [messy_code.py](messy_code.py) has **5 levels of nesting**. Every happy-path line is buried deep inside a pyramid of `if/else` blocks. This makes it hard to read and hard to extend.

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
# 1. Confirm tests are green before you touch anything
pytest test_code.py

# 2. Refactor messy_code.py

# 3. Confirm tests are still green
pytest test_code.py
```
