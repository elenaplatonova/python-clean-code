# Module 2: The Explaining Variable

## Before you touch anything

Open [messy_code.py](messy_code.py) and read both functions. Then answer these:

- What does `(len(scores) + 1) // 2` represent? What real-world concept does that expression describe?
- If you needed to change how "top third" is calculated, could you find that logic quickly?
- In `extract_report_data` — what does `group(3)` refer to? Could you tell without counting the brackets in the regex?

Run the tests:

```bash
pytest test_code.py
```

All green. The logic is correct — you just can't read it.

---

## The Problem

Both functions pack multiple operations onto single lines. The expressions are correct but unreadable — to understand what the code does, you have to mentally execute it step by step.

A well-named variable eliminates that work. It tells you what a value *is*, so you don't have to figure it out.

## Your Task

The idea is simple — pull each calculated value out of the expression and give it a name:

```python
# Before — what does this slice mean?
return data[len(data) // 4:]

# After — obvious at a glance
quarter_point = len(data) // 4
return data[quarter_point:]
```

```python
# Before — what is parts[1] here?
parts = "London,UK".split(",")
return parts[0], parts[1]

# After — no ambiguity
city, country = "London,UK".split(",")
return city, country
```

### `summarize_scores`

Break the one-liner into named intermediate variables. The function returns two things — the average of the top third of scores, and the bottom half. Each of those concepts should have a name.

### `extract_report_data`

The regex works, but the log format is fixed and simple:

```
2024-01-15T09:32:11 ERROR failed to connect
```

Regex isn't always the wrong choice. It compiles to an efficient state machine — for parsing millions of log lines it can be faster than Python string operations. And a regex with 2–3 groups is manageable.

The problem is scale. A regex with 15 groups like `group(7)` or `group(12)` is a bug waiting to happen — you can't tell what you're extracting without counting brackets, and adding a new group in the middle silently shifts all the numbers after it.

The rule of thumb: if your regex has more groups than you can count on one hand, rewrite it. If the format is fixed and simple, `.split()` is almost always clearer regardless.

For example, parsing a fixed-format string like `"2024-01-15 Alice 42"`:

```python
# With regex — works, but you have to read it carefully
match = re.match(r"(\d{4}-\d{2}-\d{2})\s+(\w+)\s+(\d+)", line)
date, name, age = match.group(1), match.group(2), match.group(3)

# With split — same result, no pattern to decode
parts = line.split()
date = parts[0]
name = parts[1]
age = parts[2]
```

Rewrite `extract_report_data` the same way. Use `.split()` and name every intermediate value.

## Rules

- Every intermediate value must have a name that describes what it *is*, not how it's computed.
- `extract_report_data` must not use `import re` or any regex.
- All 10 tests must still pass.

## Workflow

```bash
pytest test_code.py   # green before
# refactor messy_code.py
pytest test_code.py   # green after
```

---

## What you just learned

An explaining variable gives a name to an intermediate result that would otherwise be buried inside a larger expression. The name is the documentation.

Code is read far more often than it is written. Every time someone reads a dense one-liner, they pay a comprehension tax — they have to mentally execute it to understand it. A named variable eliminates that tax permanently.

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
