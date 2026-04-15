# Module 11: Exception Logging

## Before you touch anything

Open [messy_code.py](messy_code.py) and read all three functions. Then answer these:

- `parse_config` returns `{}` on invalid JSON. In production, how do you know this happened?
- `process_record` returns `None` when a field is missing or unparseable. Which field failed? What was the bad value?
- `read_user_file` returns `[]` for both "file not found" and "file contains invalid JSON". How do you tell them apart in your monitoring dashboard?

Run the tests:

```bash
pytest test_code.py
```

Some tests will be **red** — specifically the ones that check for logging. That's the starting point.

---

## The Problem

Catching an exception and returning a fallback value is sometimes correct. But doing it silently means the error never happened as far as anyone can tell. No log, no trace, no alert.

In production, silent failures are worse than crashes. A crash is loud — someone notices immediately. A silent failure quietly returns wrong data for hours before anyone realises.

```python
# This is a silent failure factory
except (KeyError, ValueError):
    return None   # which key? which value? when? on what input?
```

## Your Task

Add a `logger` at the top of the file and log an `ERROR` in every `except` block before returning the fallback.

```python
import logging

logger = logging.getLogger(__name__)

def parse_config(text):
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        logger.error("parse_config: failed to parse JSON — %s", e)
        return {}
```

The log message should answer: **what function, what went wrong, what was the input.**

## Rules

- Add `logger = logging.getLogger(__name__)` at the top of the file.
- Every `except` block must call `logger.error(...)` before returning.
- The log message must include enough context to diagnose the problem without reading the code (function name + error + relevant input).
- Return values must not change — all existing tests must still pass.
- All 14 tests must pass — including the ones that start red.

## Workflow

```bash
pytest test_code.py   # some red — logging tests fail before refactoring
# refactor messy_code.py
pytest test_code.py   # all green
```

---

## What you just learned

Logging in `except` blocks is not optional in production code. It's the difference between "something went wrong at 3am, here's exactly what and why" and "something went wrong at 3am, good luck."

The pattern:
```python
except SomeSpecificError as e:
    logger.error("function_name: description — input=%r error=%s", input_value, e)
    return fallback
```

Use `logger.error` for errors you're recovering from. Use `logger.exception` if you also want the full stack trace in the log (useful for unexpected failures).

---

## Submission 1 — The Exercise

Push your refactored `messy_code.py`. The autograding check runs automatically — all 14 tests must be green.

## Submission 2 — Real World PR

1. Open your actual codebase and find one `except` block that has no logging
2. Add a `logger.error(...)` call with enough context to diagnose the problem
3. Open a PR in that codebase
4. On this repo, create a branch (e.g. `exception-logging-real-world`)
5. Fill in [REAL_WORLD.md](REAL_WORLD.md) — PR link, before/after snippets, one sentence explanation
6. Open a PR on this repo and request Elena's review
