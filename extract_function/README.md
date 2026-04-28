# Module 4: Extract Function

## Before you touch anything

Open [messy_code.py](messy_code.py) and read `generate_report`. Then answer these:

- How many separate things does this function do?
- If the weighted average calculation had a bug, how quickly could you find the line responsible?
- If you saw `generate_report` called in another file, could you tell what it returns just from reading the call?
- The grade assignment fits on one line — does that make it easier or harder to read?

Run the tests:

```bash
pytest test_code.py   # 9 pass, 4 fail — the 4 failures define your task
```

---

## The Problem

`generate_report` does four separate things in one body: it calculates a weighted average, finds top scorers, computes a pass rate, and assigns a letter grade. Every step is written inline — some as one-liners, some as chained ternaries.

The one-liners are the most interesting case. This line fits on one line and is not wrong:

```python
weighted_avg = sum(s * w for s, w in zip(scores, weights)) / sum(weights)
```

But `weighted_avg = weighted_average(scores, weights)` is better — not because it's shorter, but because the name tells you what the expression *means*, not just what it does. The reader no longer has to parse the formula to understand the intent.

A function name is a comment that the interpreter also reads.

## Your Task

Extract each calculation in `generate_report` into its own named function. After refactoring, `generate_report` should read almost like plain English — a list of steps, not a list of formulas.

```python
# Before — four calculations crammed into one function
def generate_report(scores, weights, thresholds):
    weighted_avg = sum(s * w for s, w in zip(scores, weights)) / sum(weights)
    cutoff = sorted(scores)[int(len(scores) * 0.8)]
    top = [s for s in scores if s > cutoff]
    passing = round(len([s for s in scores if s >= thresholds["pass"]]) / len(scores) * 100, 1)
    grade = "A" if weighted_avg >= thresholds["A"] else "B" if weighted_avg >= thresholds["B"] else "C" if weighted_avg >= thresholds["C"] else "F"
    return {"weighted_average": round(weighted_avg, 2), "top_scorers": top, "pass_rate": passing, "grade": grade}

# After — each step has a name; generate_report just orchestrates
def weighted_average(scores, weights):
    return sum(s * w for s, w in zip(scores, weights)) / sum(weights)

def top_scorers(scores, percentile=0.8):
    cutoff = sorted(scores)[int(len(scores) * percentile)]
    return [s for s in scores if s > cutoff]

def pass_rate(scores, threshold):
    return round(len([s for s in scores if s >= threshold]) / len(scores) * 100, 1)

def letter_grade(average, thresholds):
    if average >= thresholds["A"]:
        return "A"
    if average >= thresholds["B"]:
        return "B"
    if average >= thresholds["C"]:
        return "C"
    return "F"

def generate_report(scores, weights, thresholds):
    avg = weighted_average(scores, weights)
    return {
        "weighted_average": round(avg, 2),
        "top_scorers": top_scorers(scores),
        "pass_rate": pass_rate(scores, thresholds["pass"]),
        "grade": letter_grade(avg, thresholds),
    }
```

Notice that `letter_grade` is longer than the original one-liner — and still better. The ternary chain forced you to read it three times to understand it. The if-chain reads top to bottom.

## Rules

- Extract `weighted_average`, `top_scorers`, `pass_rate`, and `letter_grade` as separate functions (the 4 failing tests enforce this by name).
- `generate_report` must still return the same dict with the same values — the 9 passing tests must stay green.
- No logic inside `generate_report` — it should only call helpers and return the result.

## Workflow

```bash
pytest test_code.py   # 9 pass, 4 fail — before
# refactor messy_code.py
pytest test_code.py   # all 13 pass — after
```

> **Note:** Like the generator and consistent_returns modules, 4 tests start red — they define the target structure. Your job is to make them green while keeping the other 9 green.

---

## What you just learned

A function that does one thing is easier to name, easier to test, and easier to change than a function that does five things. This is sometimes called the **Single Responsibility Principle** at the function level.

The other lesson: **length is not the criterion for extraction**. A one-liner is worth extracting if giving it a name makes the call site clearer. `weighted_average(scores, weights)` is shorter to read than the formula, even though the formula is only one line.

After this refactor:

- Each helper function can be tested independently (and the 4 new tests do exactly that)
- If the weighted average formula changes, you change one function, not one line buried in a larger function
- `generate_report` itself is now a readable summary of what a report contains

---

## Submission 1 — The Exercise

Push your refactored `messy_code.py`. The autograding check runs automatically — all 13 tests must be green.

## Submission 2 — Real World PR

1. Open your actual codebase and find one function that does more than one thing — even if it's short
2. Extract each logical step into a named helper function
3. Open a PR in that codebase
4. On this repo, create a branch (e.g. `extract-function-real-world`)
5. Fill in [REAL_WORLD.md](REAL_WORLD.md) — PR link, before/after snippets, one sentence explanation
6. Open a PR on this repo and request Elena's review
