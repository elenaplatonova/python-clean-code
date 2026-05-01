# Module 2: The Explaining Variable

## Before you touch anything

Open [messy_code.py](messy_code.py) and read both functions. Then answer these:

- In `get_user_msg_from_error_log` — what does `group(3)` refer to in the f-string? Can you tell without counting the brackets in the regex?
- If someone added a new capture group in the middle of the pattern, would the output change silently or loudly?
- In `summarize_scores` — what does `(len(scores) + 1) // 2` represent? What real-world concept does it describe?
- If either function had a bug, where would you even start looking?

Run the tests:

```bash
pytest test_code.py
```

All green. The logic is correct — you just can't read it.

---

## The Problem

Both functions pack multiple operations onto single lines. The expressions are correct but unreadable — to understand what the code does, you have to mentally execute it step by step.

A well-named variable eliminates that work. It tells you what a value *is*, so the reader doesn't have to figure it out.

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

### `get_user_msg_from_error_log`

The log line format is: `"2024-01-15T09:32:11 ERROR failed to connect"`

The function returns a user-facing message string. Name the regex pattern, the match result, and each group before using them. `group(1)`, `group(2)`, `group(3)`, `group(4)` inside an f-string are completely opaque — give each one a name that describes what it contains:

```python
# Before — what does group(2) mean in this f-string?
match = re.match(r"(\w+)\s+(\d+)\s+(.+)", record)
return f"Event {match.group(2)} of type {match.group(1)}: {match.group(3)}"

# After — no ambiguity, no counting
RECORD_PATTERN = r"(\w+)\s+(\d+)\s+(.+)"
match = re.match(RECORD_PATTERN, record)
record_type = match.group(1)
record_id = match.group(2)
label = match.group(3)
return f"Event {record_id} of type {record_type}: {label}"
```

### `summarize_scores`

Break the one-liner into named intermediate variables. The function returns two things — the average of the top third of scores, and the bottom half. Each of those concepts should have a name.

## Rules

- Every intermediate value must have a name that describes what it *is*, not how it's computed.
- All 11 tests must still pass.

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
