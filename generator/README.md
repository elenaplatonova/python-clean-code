# Module 5: The Generator / `yield`

## Before you touch anything

Open [messy_code.py](messy_code.py) and read `parse_log_file`. Then answer these:

- When does the function start processing lines — before or after the entire file is read?
- If the log file is 2GB, how much memory does this function use before it returns a single record?
- What if you only needed the first error — does the function still read the whole file?

Run the tests:

```bash
pytest test_code.py   # 9 pass, 1 fails — that's expected (see note below)
```

The failing test (`test_parse_log_file_returns_generator`) is the constraint itself, written as a test. Your job is to make it green.

---

## The Problem

`parse_log_file` reads the entire file into memory with `readlines()`, builds a full list of records, and returns it. For a 10-line test file this is fine. For a 500MB production log it will load the entire file into RAM before returning a single record — and you'll have two copies of the data in memory at the same time (the raw lines and the parsed records).

Python has a built-in solution: generators.

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
- All 10 tests must pass.

## Workflow

```bash
pytest test_code.py   # 9 pass, 1 fails — before
# refactor messy_code.py
pytest test_code.py   # all 10 pass — after
```

> **Note:** This module is slightly different. `test_parse_log_file_returns_generator` starts **red** — it's the constraint itself expressed as a test. Your job is to make it green while keeping the other 9 tests green too.

---

## What you just learned

A generator function uses `yield` instead of `return`. When called, it doesn't run at all — it returns a generator object. The code inside runs only when the caller asks for the next value.

The practical benefit is memory. A generator holds one item in memory at a time, regardless of how large the source is.

| Approach | Memory for a 500MB log file |
|---|---|
| `readlines()` + list | ~1GB (raw lines + parsed dicts) |
| `yield` generator | ~a few KB (one line at a time) |

Generators also compose well. `count_errors` and `first_critical` both work unchanged because they iterate over the result — they don't care whether it's a list or a generator. That's the other lesson: write functions that consume iterables, not specifically lists, and they work with everything.

---

---

## Submission 1 — The Exercise

Push your refactored `messy_code.py`. The autograding check runs automatically — all 10 tests must be green.

## Submission 2 — Real World PR (Optional)

**This submission is optional.** Generators are most useful in file processing, log parsing, and streaming pipelines. If your codebase doesn't have code that reads large files or builds large lists before processing them, skip this one.

If you do find one:

1. Open your actual codebase and find one place that reads a file or query result into a list before processing it
2. Refactor it to use `yield`
3. Open a PR in that codebase
4. On this repo, create a branch (e.g. `generator-real-world`)
5. Fill in [REAL_WORLD.md](REAL_WORLD.md) — PR link, before/after snippets, one sentence explanation
6. Open a PR on this repo and request Elena's review
