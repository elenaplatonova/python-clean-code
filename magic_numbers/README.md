# Module 5: Magic Numbers

## Before you touch anything

Open [messy_code.py](messy_code.py) and read all four functions. Then answer these:

- What does `0.20` mean in `calculate_order_total`? Is it a VAT rate? A markup? A penalty?
- What does `25` mean in `paginate`? If the product team asks "can we change the page size to 20?", how many places do you need to update?
- What does `650` mean in `is_eligible_for_credit`? If the credit policy changes, will you find every occurrence?
- What happens if someone copies `0.08` from one function to another and the original changes to `0.09`?

Run the tests:

```bash
pytest test_code.py
```

All green. The logic is correct — but the numbers are invisible.

---

## The Problem

A **magic number** is a numeric literal that appears in code without explanation. The number works, but it carries no meaning — you have to read the surrounding code and guess what it represents.

The real danger is duplication. When `0.15` appears in three functions, changing the discount policy means hunting down every occurrence. Miss one and you have a bug that only shows up in a specific code path.

## Your Task

Extract every magic number into a **named constant** at the top of the file.

```python
# Before — what is 0.15? what is 1000?
if subtotal > 1000:
    discount = subtotal * 0.15

# After — unambiguous
LARGE_ORDER_THRESHOLD = 1000
LARGE_ORDER_DISCOUNT = 0.15

if subtotal > LARGE_ORDER_THRESHOLD:
    discount = subtotal * LARGE_ORDER_DISCOUNT
```

Name constants after **what they mean**, not what they are. `TAX_RATE = 0.20` is good. `POINT_TWO = 0.20` is useless.

## Rules

- Every numeric literal in function bodies must be replaced with a named constant.
- Constants are defined at the **top of the file**, in `UPPER_SNAKE_CASE`.
- No magic numbers allowed inside any function — not even `0` or `1` if they carry domain meaning.
- All 15 tests must still pass.

## Workflow

```bash
pytest test_code.py   # green before
# refactor messy_code.py
pytest test_code.py   # green after
```

---

## What you just learned

Named constants make the domain visible in the code. When you read `LARGE_ORDER_THRESHOLD = 1000` at the top of a file, you learn something about the business rules — not just the mechanics.

The practical benefits:
- **One place to change.** Policy changes update in one line, not scattered across the codebase.
- **Self-documenting.** `TAX_RATE` needs no comment. `0.20` does.
- **Searchable.** You can grep for `TAX_RATE`. You cannot reliably grep for `0.20` without false positives.

---

## Submission 1 — The Exercise

Push your refactored `messy_code.py`. The autograding check runs automatically — all 15 tests must be green.

## Submission 2 — Real World PR

1. Open your actual codebase and find one function with numeric literals that carry business meaning
2. Extract them into named constants
3. Open a PR in that codebase
4. On this repo, create a branch (e.g. `magic-numbers-real-world`)
5. Fill in [REAL_WORLD.md](REAL_WORLD.md) — PR link, before/after snippets, one sentence explanation
6. Open a PR on this repo and request Elena's review
