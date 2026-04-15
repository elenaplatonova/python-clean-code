# Day 3: The Explaining Variable

## The Problem

[messy_code.py](messy_code.py) has two functions where all the logic is crammed onto one or two lines. The expressions are correct but completely unreadable — you have to decode what they do rather than read what they *mean*.

## Your Task

Break each dense expression into **named intermediate variables** whose names describe what the value represents.

```python
# Before — what does this even mean?
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
# refactor
pytest test_code.py   # green after
```
