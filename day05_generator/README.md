# Day 5: The Generator / `yield`

## The Problem

`parse_log_file` in [messy_code.py](messy_code.py) reads the entire file into memory with `readlines()`, builds a full `records` list, and returns it. For a small file this is fine. For a 500 MB production log, it will OOM your process.

## Your Task

Refactor `parse_log_file` to use **`yield`** instead of building and returning a list. The function should process and yield one record at a time, holding only one line in memory at a time.

```python
# Before — loads everything, then returns
def parse_log_file(filepath):
    with open(filepath) as f:
        lines = f.readlines()   # entire file in RAM
    records = []
    for line in lines:
        ...
        records.append(record)
    return records              # second copy in RAM

# After — yields one record at a time
def parse_log_file(filepath):
    with open(filepath) as f:
        for line in f:          # Python iterates file line-by-line
            ...
            yield record        # caller gets one record, we move on
```

`count_errors` and `first_critical` call `parse_log_file` — check whether they need any changes to work with a generator instead of a list.

## Rules

- `parse_log_file` must use `yield` and return a **generator** (the last test enforces this explicitly).
- No `readlines()`, no intermediate list of records.
- Iterating over the open file directly (`for line in f`) is the idiomatic way.
- All 10 tests must still pass.

## Why generators matter

| Approach | Memory used for 500 MB file |
|---|---|
| `readlines()` + list | ~1 GB (file + list of strings + list of dicts) |
| `yield` generator | ~a few KB (one line at a time) |

## Workflow

```bash
pytest test_code.py   # 9 pass, 1 fails (test_parse_log_file_returns_generator — that's expected)
# refactor
pytest test_code.py   # all 10 pass
```

> **Note:** This day is slightly different. `test_parse_log_file_returns_generator` starts **red** — it's the constraint itself expressed as a test. Your job is to make it green while keeping the other 9 tests green too.
