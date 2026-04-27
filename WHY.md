# Why Clean Code?

You probably already know the feeling.

You open a file you wrote three months ago and spend 10 minutes just trying to remember what it does. Or you need to add one small thing and you're scared to touch it because you don't know what will break. Or you ask a colleague to review your code and they come back with "I'm not sure what this does."

That's not a problem of knowledge. That's a problem of clarity.

Clean code is code that's easy to read, easy to change, and hard to break accidentally. It's not about following rules for the sake of rules. It's about writing code that communicates to your colleagues, and to yourself six months from now.

---

## Before and after

Here's a real example. Both versions do exactly the same thing.

**Before:**
```python
def process(u, o):
    if u is not None:
        if u.get("active"):
            if o is not None:
                if o.get("total") > 0:
                    return o["total"] * 1.08
                else:
                    return None
            else:
                return None
        else:
            return None
    else:
        return None
```

**After:**
```python
def process_payment(user, order):
    if user is None:
        return None
    if not user.get("active"):
        return None
    if order is None:
        return None
    if order.get("total") <= 0:
        return None
    return order["total"] * 1.08
```

Same logic. Same output. But the second version:
- Takes 5 seconds to read instead of 30
- Is easy to add a new condition to
- Has nowhere for a bug to hide

---

## What this course is

Twelve modules. Each one gives you working but messy code and one specific constraint to apply. You refactor the code, run the tests, check the builds and if they're all green — you got it right.

The constraints are not arbitrary. Each one is a technique that professional developers use every day to make code easier to live with.

You won't agree with all of them at first. That's fine. Do the exercise anyway and see how the code looks after. The goal isn't to memorise rules — it's to build an instinct for what "easy to read" actually means in practice.

---

## How to work through it

One module at a time. Each exercise takes 15–30 minutes.

```
guard_clause/           ← start here
list_comprehension/
explaining_variable/
dataclass/
generator/
magic_numbers/
magic_strings/
exception_handling/
exception_flow_control/
consistent_returns/
exception_logging/
extract_function/
```

Each folder has a README with the constraint for the module. Read it, run the tests, refactor, run the tests again.

That's it.
