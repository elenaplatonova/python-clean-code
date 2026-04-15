# Module 3: The Explaining Variable

## Before you touch anything

Open [messy_code.py](messy_code.py) and read both functions. Then answer these:

- In `summarize_scores` — what does `(len(scores) + 1) // 2` mean? What does it represent in the real world?
- In `extract_report_data` — if the regex pattern had a bug, how would you know which group captures which field?
- If a colleague asked you "what's the bottom half cutoff?" could you point to a line that answers that question?

Run the tests:

```bash
pytest test_code.py
```

All green. The logic is correct — you just can't read it.

---

## The Problem

Both functions pack multiple operations onto single lines. The expressions are correct but they force the reader to mentally execute the code rather than just read it. You have to decode what it does instead of understanding what it means.

Comments could help, but they go out of date. A well-named variable never lies — it *is* the documentation.

## Your Task

Break each dense expression into **named intermediate variables** whose names describe what the value represents.

```python
# Before — what does this mean?
return data[len(data) // 2 :]

# After — obvious at a glance
midpoint = len(data) // 2
return data[midpoint:]
```

For `extract_report_data`: name the regex pattern and the match result before calling `.group()`.

For `summarize_scores`: pull the slice index and the list slice into named variables before computing the average.

## Rules

- No line may contain more than **one significant operation** (no chaining transforms on a single line).
- Every intermediate value must have a name that describes *what it is*, not how it's computed (e.g., `top_third` not `slice_end`).
- All 10 tests must still pass.

## Workflow

```bash
pytest test_code.py   # green before
# refactor messy_code.py
pytest test_code.py   # green after
```

---

## What you just learned

An explaining variable gives a name to an intermediate result that would otherwise exist only inside a larger expression. The name is the documentation.

The practical benefit: code is read far more often than it is written. Every time someone (including you) reads a dense one-liner, they pay a comprehension tax — they have to mentally execute it to understand it. A named variable eliminates that tax permanently.

There's a common fear that more variables means slower code. In Python, for the kind of operations you're doing here, the difference is immeasurable. Clarity is almost always worth it.

---

---

## Submission 1 — The Exercise

Push your refactored `messy_code.py`. The autograding check runs automatically — all 10 tests must be green.

## Submission 2 — Real World PR

1. Open your actual codebase and find one line with more than two operations chained together
2. Break it into named intermediate variables
3. Open a PR in that codebase
4. On this repo, create a branch (e.g. `explaining-variable-real-world`)
5. Fill in [REAL_WORLD.md](REAL_WORLD.md) — PR link, before/after snippets, one sentence explanation
6. Open a PR on this repo and request Elena's review
