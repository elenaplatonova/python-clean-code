# Module 10: Try/Except for Flow Control

## Before you touch anything

Open [messy_code.py](messy_code.py) and read all four functions. Then answer these:

- `get_config_value` uses `try/except KeyError` to handle a missing key. Python has a built-in for this — what is it?
- `has_permission` accesses `user["permissions"]` in a try block. What if you just checked whether the key exists before accessing it?
- `get_first_tag` catches `IndexError` for an empty list. Is an empty list really an *exceptional* situation?
- `get_nested_value` catches `TypeError` in case the outer value isn't a dict. Could you handle that with a safe lookup instead?

Run the tests:

```bash
pytest test_code.py
```

All green. The code works — but it's using exceptions as an `if` statement in disguise.

---

## The Problem

Exceptions exist for *exceptional* situations — errors you couldn't predict or prevent. A missing dictionary key, an empty list, or a `None` value are not exceptional. They're normal outcomes you can check for directly.

Using `try/except` for these cases has real costs:

- It's slower — Python has to set up an exception handler even when nothing goes wrong.
- It hides intent — `try/except KeyError` says "this might blow up" when what you mean is "this key might not be here."
- It catches more than you intend — `try: return data[key1][key2]` might raise `KeyError` for `key1` or `key2`, and you can't tell which.

Python has cleaner tools for every case here.

## Your Task

Replace every `try/except` with the appropriate Python built-in:

| Problem | Instead of try/except, use |
|---|---|
| Dict key with fallback | `.get(key, default)` |
| Check key exists first | `if key in d:` |
| List first item with fallback | `items[0] if items else None` |
| Chained dict access | `.get(key1, {}).get(key2, default)` |

```python
# Before
try:
    return config[key]
except KeyError:
    return default

# After
return config.get(key, default)
```

```python
# Before
try:
    return data[key1][key2]
except (KeyError, TypeError):
    return default

# After
return data.get(key1, {}).get(key2, default)
```

## Rules

- No `try/except` blocks allowed anywhere in the file.
- Use `.get()`, `if key in dict`, or conditional expressions instead.
- All 16 tests must still pass.

## Workflow

```bash
pytest test_code.py   # green before
# refactor messy_code.py
pytest test_code.py   # green after
```

---

## What you just learned

The question to ask before reaching for `try/except`: **is this situation truly exceptional, or is it just a normal outcome I should check for?**

A missing key is not exceptional — it's a normal outcome. Use `.get()`.
A conversion that might fail on bad input is exceptional — use `try/except ValueError`.

The distinction matters because exceptions are a communication tool. When you see `try/except` in code, it signals "something genuinely risky happens here." Using it for routine lookups blurs that signal and makes the code harder to read.

---

## Submission 1 — The Exercise

Push your refactored `messy_code.py`. The autograding check runs automatically — all 16 tests must be green.

## Submission 2 — Real World PR (Optional)

**This submission is optional.** This pattern requires finding a `try/except` used as a substitute for a dict lookup or routine check — a specific habit that not every codebase has. If you don't find one, skip this one.

If you do find one:

1. Open your actual codebase and find one `try/except` used for a dict lookup, list access, or other routine check
2. Replace it with `.get()`, `if key in dict`, or a conditional expression
3. Open a PR in that codebase
4. On this repo, create a branch (e.g. `exception-flow-control-real-world`)
5. Fill in [REAL_WORLD.md](REAL_WORLD.md) — PR link, before/after snippets, one sentence explanation
6. Open a PR on this repo and request Elena's review
