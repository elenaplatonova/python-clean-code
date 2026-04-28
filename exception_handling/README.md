# Module 9: Bare and Broad Except

## Before you touch anything

Open [messy_code.py](messy_code.py) and read all three functions. Then answer these:

- In `parse_int` — the bare `except:` catches *everything*, including `KeyboardInterrupt` and `SystemExit`. What happens if someone presses Ctrl+C while this runs?
- In `parse_price` — `except Exception as e:` catches the error but `e` is never used. What information are you throwing away?
- In `load_json` — if the file doesn't exist you get `{}`. If the file contains invalid JSON you also get `{}`. In production, how would you tell the difference?

Run the tests:

```bash
pytest test_code.py
```

All green. But the exception handling is hiding problems rather than communicating them.

---

## The Problem

**Bare `except:`** catches literally everything — including `KeyboardInterrupt`, `SystemExit`, and `GeneratorExit`. These are signals that should terminate your program. Swallowing them is almost always a bug.

**`except Exception as e:` without using `e`** is slightly less catastrophic but still wrong. You're catching a broad class of errors and silently discarding the reason. You lose the information that would tell you *what* went wrong.

Both patterns share the same root cause: not knowing (or not caring) which specific exception the operation can actually raise. The fix is always the same — look up what the operation raises, and catch exactly that.

## Your Task

Replace every bare or broad `except` with the **specific exception** the operation actually raises.

| Operation | Specific exception |
|---|---|
| `int(value)` | `ValueError` |
| `float(text)` | `ValueError` |
| `open(filepath)` | `FileNotFoundError` |
| `json.load(f)` | `json.JSONDecodeError` |

```python
# Before — catches everything, loses the reason
except:
except Exception as e:

# After — catches only what can actually go wrong here
except ValueError:
except FileNotFoundError:
except json.JSONDecodeError:
```

For `load_json`, the file might not exist *or* the JSON might be invalid — catch both separately so you can distinguish them:

```python
except FileNotFoundError:
    return {}
except json.JSONDecodeError:
    return {}
```

## Rules

- No bare `except:` anywhere.
- No `except Exception` — catch only the specific exception(s) the operation raises.
- All 11 tests must still pass.

## Workflow

```bash
pytest test_code.py   # green before
# refactor messy_code.py
pytest test_code.py   # green after
```

---

## What you just learned

The rule: **catch the most specific exception possible.**

When you catch specifically, you only suppress errors you actually know how to handle. Everything else — unexpected bugs, signals, memory errors — propagates up where it can be seen and fixed.

A useful question to ask: "If a bug causes a *different* exception here, do I want to hide it?" Bare `except` always answers yes. Specific exceptions answer no.

---

## Submission 1 — The Exercise

Push your refactored `messy_code.py`. The autograding check runs automatically — all 11 tests must be green.

## Submission 2 — Real World PR

1. Open your actual codebase and find one bare `except:` or `except Exception` 
2. Replace it with the specific exception the operation can actually raise
3. Open a PR in that codebase
4. On this repo, create a branch (e.g. `exception-handling-real-world`)
5. Fill in [REAL_WORLD.md](REAL_WORLD.md) — PR link, before/after snippets, one sentence explanation
6. Open a PR on this repo and request Elena's review
