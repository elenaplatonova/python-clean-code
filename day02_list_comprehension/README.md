# Day 2: Death to the `for` Loop

## The Problem

[messy_code.py](messy_code.py) has three functions that all follow the same pattern: create an empty list, loop over items, conditionally append, return the list. This is the most common form of noise in Python code.

## Your Task

Replace every function body with a **single list comprehension**. No helper variables, no `append`, no multi-line `for` loop.

```python
# Before
def get_names(items):
    names = []
    for item in items:
        names.append(item["name"])
    return names

# After
def get_names(items):
    return [item["name"] for item in items]
```

For functions that filter *and* transform, the comprehension can do both:

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
# refactor
pytest test_code.py   # green after
```
