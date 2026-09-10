# 🤖 The AI Engineer Playbook
# 🟢 Part 7 — Professional Python
## Batch 1 — Exception Handling ⚠️

> *"Good programmers don't prevent every error. They build programs that know how to respond when things go wrong."*

---

# 🎯 Learning Objectives

By the end of this batch, you should be able to:

- Understand what an exception actually is
- Distinguish syntax errors from runtime exceptions
- Use `try` and `except`
- Catch specific exception types
- Handle multiple exception types
- Use `else`
- Use `finally`
- Understand the exception hierarchy
- Raise exceptions intentionally with `raise`
- Create useful error messages
- Understand exception propagation
- Avoid overly broad `except` blocks
- Create custom exception classes
- Design cleaner error-handling flows

---

# 🧭 Where You Are
# 🤖 AI Engineer Playbook

# Phase 1 — Python Fluency 🐍

├── Foundations                 ✅
├── Functions                   ✅
├── Collections                 ✅
├── Object-Oriented Programming ✅
├── Files & Python Ecosystem    ✅
├── Pythonic Features           ✅ 🏆
│
└── Part 7 — Professional Python
    │
    ├── ⚠️ Exception Handling   ← YOU ARE HERE
    ├── 🏷️ Static Typing
    ├── 📚 Documentation
    ├── 📝 Docstrings
    └── 🧪 Pytest
          │
          ▼
       🏆 BOSS FIGHT

🎯 Exit Criteria:
Writes clean, testable Python

---

# 🧠 THE BIG IDEA

Your program can fail in two very different ways.

Sometimes Python can't even understand your code.

Sometimes Python understands your code perfectly...

but something goes wrong **while the program is running**.

Those are different problems.

---

# 💥 Syntax Errors

Consider:

```python
if score > 10
    print("Excellent")
```

Python can't parse this.

The program doesn't get to meaningfully execute.

You get a:

```text
SyntaxError
```

Think:

```text
Your code
    ↓
Python tries to understand it
    ↓
❌ "I don't understand this."
    ↓
SyntaxError
```

---

# 💥 Runtime Exceptions

Now:

```python
score = 10
result = score / 0
```

Python understands the syntax.

But when it executes:

```python
score / 0
```

something impossible happens.

```text
10 / 0
   ↓
💥 ZeroDivisionError
```

That's an exception.

---

# 🧠 The Difference

```text
SYNTAX ERROR
────────────

"I can't understand your code."


EXCEPTION
─────────

"I understand your code,
but something went wrong
while running it."
```

This distinction is important.

Exception handling primarily deals with **runtime problems**.

---

# ⚠️ What Is an Exception?

An exception is Python's way of saying:

> **"Something unexpected happened, and normal execution can't continue this way."**

Examples:

```text
ValueError
TypeError
ZeroDivisionError
IndexError
KeyError
FileNotFoundError
NameError
```

Each one communicates a different kind of problem.

---

# 🧪 Meet `try`

Suppose we have:

```python
number = int(input("Enter a number: "))
```

A user could type:

```text
42
```

Perfect.

But what if they type:

```text
hello
```

Python can't convert `"hello"` into an integer.

That causes:

```text
ValueError
```

We can handle it:

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid number.")
```

Now the flow becomes:

```text
User input
    ↓
try
    ↓
Convert input
    │
    ├── Works → continue
    │
    └── ValueError
            ↓
          except
            ↓
      Show useful message
```

---

# 🧠 THE BIG IDEA

`try` means:

> **"Attempt this operation."**

`except` means:

> **"If this specific problem happens, here's what to do."**

That's the foundation of exception handling.

---

# 🥋 Practice 1 — Safe Integer

Write a small program that asks:

```text
Enter your age:
```

Convert the answer to an integer.

If the user enters something invalid, print:

```text
⚠️ Please enter a valid age.
```

You should use:

```python
try:
```

and:

```python
except ValueError:
```

---

# 🧠 Why Catch Specific Exceptions?

You might see this:

```python
try:
    number = int(input("Enter a number: "))
except:
    print("Something went wrong.")
```

It works.

But...

it's usually a bad habit.

Why?

Because you're catching **everything**.

Imagine the code contains a completely different bug.

```python
try:
    number = int(input("Enter a number: "))
    mysterious_bug()
except:
    print("Something went wrong.")
```

You might accidentally hide a bug you actually needed to see.

Instead:

```python
except ValueError:
```

says:

> "I'm expecting this particular problem."

That's much clearer.

---

# 🧠 Specific > Generic

Prefer:

```python
except ValueError:
```

over:

```python
except:
```

when you know what problem you're handling.

Think:

```text
❌ "Catch anything."

        vs

✅ "I know what can go wrong here,
   and this is how I'll handle it."
```

That's professional thinking.

---

# 🧪 Practice 2 — Division

Write a program that asks for two numbers and divides them.

Potential problems:

```text
User enters "hello"
        ↓
ValueError

User enters 0 as divisor
        ↓
ZeroDivisionError
```

Handle both separately.

Your program should produce useful messages.

For example:

```text
⚠️ Please enter valid numbers.
```

and:

```text
⚠️ You cannot divide by zero.
```

---

# 🧠 Multiple Exceptions

You can have multiple `except` blocks:

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("You cannot divide by zero.")
```

The flow:

```text
                    try
                     │
             ┌───────┴────────┐
             ▼                ▼
         ValueError      ZeroDivisionError
             │                │
             ▼                ▼
       Handler #1         Handler #2
```

Each exception gets its appropriate response.

---

# 🧪 Practice 3 — Football Score

Ask the user for:

```text
Enter goals scored:
```

Convert it to an integer.

Then calculate:

```text
100 / goals
```

Handle:

* Invalid input
* Zero goals

Use separate exception handlers.

---

# ⚠️ A Common Mistake

Look at:

```python
try:
    number = int(input("Number: "))
    result = 100 / number

except ValueError:
    print("Invalid input.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

print("Done.")
```

What happens if the input is:

```text
5
```

?

The program continues after the exception structure.

But what if:

```text
0
```

?

The error is caught.

Then Python continues after the `try/except`.

Conceptually:

```text
try
 ↓
Error
 ↓
except handles it
 ↓
Continue here
 ↓
rest of program
```

That's an important property.

---

# 🧠 `else`

Python gives us another piece:

```python
else:
```

Example:

```python
try:
    number = int(input("Number: "))

except ValueError:
    print("Invalid number.")

else:
    print(f"You entered {number}.")
```

The `else` block runs **only if no exception occurred**.

Think:

```text
try
 │
 ├── 💥 Error → except
 │
 └── ✅ Success → else
```

---

# 🧠 Why Use `else`?

Compare:

```python
try:
    number = int(input("Number: "))
    print(f"You entered {number}.")
except ValueError:
    print("Invalid number.")
```

with:

```python
try:
    number = int(input("Number: "))

except ValueError:
    print("Invalid number.")

else:
    print(f"You entered {number}.")
```

The second version clearly separates:

```text
RISKY OPERATION
```

from:

```text
SUCCESS LOGIC
```

That's often cleaner.

---

# 🧪 Practice 4 — Successful Training

Write a program that asks:

```text
Enter training duration in minutes:
```

Try converting it to an integer.

If invalid:

```text
⚠️ Invalid duration.
```

If successful:

```text
🏃 Training duration recorded.
```

Use `else`.

---

# 🚪 `finally`

Now we introduce:

```python
finally:
```

This block runs whether an exception happened or not.

Example:

```python
try:
    number = int(input("Number: "))

except ValueError:
    print("Invalid number.")

finally:
    print("Program finished.")
```

Whether the conversion succeeds or fails:

```text
finally
    ↓
runs
```

---

# 🧠 THE BIG IDEA

Think of the structure like this:

```text
try
 │
 ├── Something works
 │       ↓
 │      else
 │
 └── Something fails
         ↓
       except
         
Both paths
    ↓
finally
    ↓
Cleanup
```

---

# 🚪 Why Is `finally` Useful?

Imagine opening a resource:

```text
Open file
    ↓
Do work
    ↓
Close file
```

If something fails during the work, you still want cleanup.

That's exactly the sort of situation `finally` is designed for.

---

# 🧪 Practice 5 — Cleanup

Create a small program that:

```text
1. Attempts an operation
2. Handles an expected error
3. Always prints:
   🧹 Cleanup complete.
```

Use:

```python
finally:
```

The important part isn't the operation.

It's proving that you understand:

> `finally` runs regardless of whether an exception occurred.

---

# 🧠 THE COMPLETE STRUCTURE

You can combine everything:

```python
try:
    # risky operation

except SomeError:
    # handle problem

else:
    # successful operation

finally:
    # always happens
```

Mental model:

```text
             TRY
              │
       ┌──────┴──────┐
       │             │
      💥             ✅
       │             │
    EXCEPT          ELSE
       │             │
       └──────┬──────┘
              │
           FINALLY
              │
              ▼
           Continue
```

---

# 🥋 Practice 6 — Full Structure

Build a small program that asks the user for a player's shirt number.

Requirements:

### `try`

Convert the input to an integer.

### `except`

Handle invalid input.

### `else`

Print:

```text
⚽ Player number accepted.
```

### `finally`

Print:

```text
📋 Registration attempt complete.
```

---

# 🧠 EXCEPTION INFORMATION

Sometimes you want the actual exception object.

You can write:

```python
try:
    number = int("hello")

except ValueError as error:
    print(error)
```

The:

```python
as error
```

gives you access to the exception object.

You can think of it as:

```text
ValueError
    ↓
exception object
    ↓
error
```

---

# 🧪 Practice 7 — Inspect the Error

Write code that intentionally causes a `ValueError`.

Catch it using:

```python
except ValueError as error:
```

Print:

```text
The error was:
```

followed by the exception message.

---

# 🧠 EXCEPTION HIERARCHY

Python exceptions aren't just a random collection of names.

They form a hierarchy.

A simplified version:

```text
BaseException
    │
    └── Exception
          │
          ├── ValueError
          ├── TypeError
          ├── LookupError
          │      ├── IndexError
          │      └── KeyError
          │
          ├── ArithmeticError
          │      └── ZeroDivisionError
          │
          └── OSError
                 └── FileNotFoundError
```

This matters because exceptions can be caught at different levels.

---

# 🤯 Example

Because:

```text
ZeroDivisionError
```

belongs under:

```text
ArithmeticError
```

you can technically catch:

```python
except ArithmeticError:
```

and it can handle a `ZeroDivisionError`.

But there's an important principle:

> **Catch the narrowest exception that makes sense for the situation.**

If you specifically expect:

```python
ZeroDivisionError
```

then prefer:

```python
except ZeroDivisionError:
```

---

# 🧠 Parent vs Child Exceptions

Think of:

```text
Animal
  ↓
Dog
```

A dog is an animal.

Similarly:

```text
ArithmeticError
  ↓
ZeroDivisionError
```

A `ZeroDivisionError` is an `ArithmeticError`.

So:

```python
except ArithmeticError:
```

can catch it.

But it's less specific.

---

# 🐛 DEBUGGING LAB — The Lazy Catch

Here's some suspicious code:

```python
try:
    age = int(input("Age: "))
    score = 100 / age

except Exception:
    print("Something went wrong.")
```

Your mission:

### 1.

Identify why this might be too broad.

### 2.

Rewrite it using more specific exception handlers.

### 3.

Explain which errors you're expecting.

---

# 🧠 `raise`

So far, we've been reacting to exceptions.

But sometimes **you** want to create one.

That's where:

```python
raise
```

comes in.

Example:

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative.")
```

Python now deliberately raises:

```text
ValueError
```

---

# 🧠 THE BIG IDEA

`raise` means:

> **"This situation is invalid. Stop normal execution and signal an exception."**

You're no longer merely responding to errors.

You're defining the rules of your program.

---

# 🥋 Practice 8 — Player Age

Write a function:

```python
def set_player_age(age):
```

It should:

* Accept an age
* Reject negative ages
* Raise `ValueError` if the age is invalid
* Otherwise return the age

Think about this carefully:

```text
Is this really an "unexpected crash"?

Or is it an invalid input
that your function should explicitly reject?
```

That's the mindset behind `raise`.

---

# 🧠 Validation + `raise`

Imagine:

```python
def register_player(name, age):

    if not name:
        raise ValueError("Player name cannot be empty.")

    if age < 0:
        raise ValueError("Player age cannot be negative.")

    return {
        "name": name,
        "age": age
    }
```

Now your function protects its own rules.

```text
Caller
  ↓
register_player()
  ↓
Validate
  │
  ├── Invalid → raise
  │
  └── Valid → return player
```

---

# 🧠 Exception Propagation

Here's something important.

Suppose:

```python
def divide(a, b):
    return a / b
```

And:

```python
def calculate():
    return divide(10, 0)
```

And:

```python
calculate()
```

The exception starts here:

```text
divide()
   ↓
ZeroDivisionError
```

But there is no handler there.

So Python looks upward:

```text
divide()
   ↓
calculate()
   ↓
caller
   ↓
top-level program
```

This is called:

> **Exception propagation**

---

# 🧠 The Call Stack

Think:

```text
main()
  ↓
calculate()
  ↓
divide()
  ↓
💥 ERROR
```

Python looks backward through the call stack for a handler.

```text
divide()
   │
   │ no handler
   ▼
calculate()
   │
   │ no handler
   ▼
main()
   │
   │ handler found!
   ▼
except
```

This is why you don't necessarily need an `except` inside every function.

---

# 🧪 Practice 9 — Let It Travel

Create:

```python
def divide(a, b):
```

Then:

```python
def calculate():
```

Then call `calculate()` from your main code.

Put the `try/except` **outside** the helper functions.

Your goal is to observe:

```text
divide()
   ↓
exception
   ↓
calculate()
   ↓
caller
   ↓
except
```

---

# 🧠 Where Should You Catch Exceptions?

This is a professional-level question.

Don't automatically write:

```python
try:
    # entire program
except:
    # shrug
```

😂

Instead ask:

> **Who can actually do something useful about this error?**

For example:

```text
Function
  ↓
Detects invalid data
  ↓
Raises ValueError
  ↓
Higher-level code
  ↓
Shows user a helpful message
```

This separation is powerful.

---

# 🐛 DEBUGGING LAB — The Giant Try Block

Consider:

```python
try:
    name = input("Name: ")
    age = int(input("Age: "))
    score = 100 / age
    print(f"{name}: {score}")
    save_to_database(name, score)
    send_email(name)

except Exception:
    print("Something went wrong.")
```

What's wrong with this design?

Think about how many completely different operations are being hidden inside one `try`.

Possible problems include:

```text
Input
Conversion
Calculation
Database
Email
```

If something fails:

```text
🤷 "Something went wrong."
```

Not very useful.

---

# 🧠 Better Thinking

A `try` block should generally surround the operations for which you're intentionally handling exceptions.

Not:

```text
"Let's put half the application inside try."
```

but:

```text
"What specific operation am I protecting,
and what problem do I expect?"
```

---

# 🥋 Practice 10 — Narrow the Scope

Take the previous giant `try` block.

Break the thinking apart.

Ask:

```text
Which operation can raise ValueError?

Which operation can raise ZeroDivisionError?

Which operation might raise an I/O-related exception?

Which failures should be allowed to propagate?
```

You don't need to implement a database or email system.

The objective is to reason about **where exception handling belongs**.

---

# 🧱 CUSTOM EXCEPTIONS

Sometimes built-in exceptions aren't expressive enough.

Imagine Football Academy AI has:

```text
Player not registered
Training session full
Insufficient wallet balance
Invalid transfer
```

You could raise:

```python
ValueError
```

for everything.

But that's not always ideal.

Instead, you can define your own exception.

---

# 🧱 Creating a Custom Exception

Example:

```python
class PlayerNotFoundError(Exception):
    pass
```

Now:

```python
raise PlayerNotFoundError("Player does not exist.")
```

You've created a domain-specific exception.

---

# 🧠 Why Custom Exceptions?

Compare:

```text
ValueError
```

with:

```text
PlayerNotFoundError
```

The second tells the programmer much more about what happened.

It communicates the **meaning of the failure**, not merely its general category.

---

# 🧪 Practice 11 — Academy Exception

Create:

```python
class PlayerNotRegisteredError(Exception):
    pass
```

Then create:

```python
def find_player(players, name):
```

If the player doesn't exist:

```python
raise PlayerNotRegisteredError(...)
```

Otherwise return the player.

Then catch your custom exception in the calling code.

---

# 🧠 Custom Exception Hierarchies

You can even create a family of related exceptions.

For example:

```python
class AcademyError(Exception):
    pass


class PlayerError(AcademyError):
    pass


class PlayerNotRegisteredError(PlayerError):
    pass


class PlayerSuspendedError(PlayerError):
    pass
```

Now you have:

```text
AcademyError
      │
      └── PlayerError
             │
             ├── PlayerNotRegisteredError
             │
             └── PlayerSuspendedError
```

You can catch:

```python
except PlayerNotRegisteredError:
```

for one specific problem.

Or:

```python
except PlayerError:
```

for player-related problems generally.

Or:

```python
except AcademyError:
```

for academy-specific failures generally.

This is where exception hierarchies become genuinely useful.

---

# 🧠 Exception Chaining

Sometimes one exception causes another.

For example:

```python
try:
    number = int("hello")

except ValueError as error:
    raise RuntimeError("Player data could not be processed.") from error
```

The:

```python
from error
```

connects the new exception to the original one.

Conceptually:

```text
Original problem
      ↓
ValueError
      ↓
Handled
      ↓
New higher-level problem
      ↓
RuntimeError
```

This is useful when you want to add context without losing the original cause.

---

# 🧠 Why This Matters

Imagine your application has layers:

```text
User Input
     ↓
Service Layer
     ↓
Data Layer
     ↓
File / Database
```

A low-level error might be:

```text
FileNotFoundError
```

But your application's higher-level meaning might be:

```text
PlayerDataUnavailableError
```

Exception chaining lets you preserve both:

```text
WHAT happened originally
+
WHAT it means to my application
```

That's powerful.

---

# 🧪 Mini Challenge — Layered Failure

Imagine:

```python
def load_player_data():
    ...
```

Suppose the underlying file isn't found.

Your job:

1. Catch the low-level exception.
2. Raise a more meaningful custom exception.
3. Chain the original exception.
4. Handle the custom exception at the calling level.

Conceptually:

```text
FileNotFoundError
       ↓
PlayerDataUnavailableError
       ↓
Application handles it
```

---

# ⚔️ DEBUGGING LAB — Don't Hide the Evidence

What's wrong with this?

```python
try:
    load_player_data()

except Exception:
    pass
```

The program silently ignores the problem.

```text
💥 ERROR

        ↓

        🤫

        ↓

Nothing.
```

This can make debugging miserable.

If an exception truly cannot be recovered from, silently swallowing it is usually a terrible idea.

---

# 🧠 Professional Rule

Don't catch an exception merely because you can.

Catch it because:

> **You know what it means and what useful action you can take.**

That one rule will save you a lot of pain.

---

# 🔥 MINI PROJECT — Safe Player Registration

Build a small registration system.

Create:

```python
def register_player(name, age, position):
```

Requirements:

### Name

Reject an empty name.

Raise:

```text
ValueError
```

with a useful message.

### Age

Reject:

```text
age < 0
```

Raise:

```text
ValueError
```

### Position

Allow only:

```text
"Forward"
"Midfielder"
"Defender"
"Goalkeeper"
```

If the position isn't valid, raise:

```text
ValueError
```

### Success

Return a dictionary:

```text
{
    "name": ...,
    "age": ...,
    "position": ...
}
```

---

# 🔥 MINI PROJECT UPGRADE

Create a custom exception:

```python
class RegistrationError(Exception):
    pass
```

Use it where appropriate.

Then write calling code that:

```text
Attempts registration
       ↓
Handles expected registration errors
       ↓
Prints a useful message
       ↓
Continues running
```

---

# 🧠 FINAL COMPREHENSION CHECK

Answer these without looking back.

### 1.

What's the difference between a syntax error and a runtime exception?

### 2.

What does `try` mean?

### 3.

Why is this generally better:

```python
except ValueError:
```

than:

```python
except:
```

?

### 4.

When does `else` execute?

### 5.

When does `finally` execute?

### 6.

What does:

```python
raise
```

allow you to do?

### 7.

What is exception propagation?

### 8.

Why shouldn't you put an entire application inside one giant `try` block?

### 9.

Why might you create a custom exception?

### 10.

What does:

```python
raise NewError(...) from error
```

accomplish?

---

# 🥋 SKILL CHECK

For each situation, choose the most appropriate strategy.

---

## Scenario A

A user types:

```text
hello
```

when your program expects an integer.

```text
Your choice:
____________________
```

---

## Scenario B

Your function receives a negative player age that violates the function's rules.

```text
Your choice:
____________________
```

---

## Scenario C

A file your program needs doesn't exist.

```text
Your choice:
____________________
```

---

## Scenario D

Your program encounters an unexpected programming bug that your current code does not know how to recover from.

```text
Your choice:
____________________
```

---

## Scenario E

A database-related low-level error needs to be converted into a meaningful application-level error.

```text
Your choice:
____________________
```

---

# 🧠 THE PROFESSIONAL MINDSET

Beginner thinking:

```text
"How do I stop Python from crashing?"
```

Better thinking:

```text
"What can go wrong here?"
```

Professional thinking:

```text
"What can go wrong here?

Which failures are expected?

Which ones can I recover from?

Where should they be handled?

What information should the caller receive?

Which errors should propagate?"
```

That's the direction we're heading.

---

# 🏗️ CONNECTION TO YOUR PROJECTS

Remember your future projects:

```text
⚽ Football Academy AI
💰 Wallet App
🛒 Terminal Store
```

They will all need error handling.

Imagine the Wallet App:

```text
Withdraw ₦10,000
       ↓
Check balance
       │
       ├── Enough money
       │       ↓
       │    Withdraw
       │
       └── Insufficient funds
               ↓
        InsufficientFundsError
```

Or the Terminal Store:

```text
Product lookup
      ↓
Product missing
      ↓
ProductNotFoundError
```

Or Football Academy:

```text
Find player
      ↓
Not registered
      ↓
PlayerNotRegisteredError
```

Exception handling gives your programs a way to **communicate failure deliberately**.

---

# 🧠 BATCH SUMMARY

You've gone from:

```text
💥 "Python crashed."
```

to:

```text
⚠️ "I know what went wrong."
```

and eventually toward:

```text
🧠 "I designed my program
   to handle this failure properly."
```

Your core toolkit now looks like:

```text
try
 ↓
Attempt risky operation

except
 ↓
Handle expected failure

else
 ↓
Handle successful execution

finally
 ↓
Guarantee cleanup

raise
 ↓
Signal an invalid condition

custom exceptions
 ↓
Give domain-specific meaning

exception propagation
 ↓
Let errors travel to
the layer that can handle them
```

---

# 🏅 PART 7 — PROGRESS

```text
🟢 PROFESSIONAL PYTHON

⚠️ Exception Handling
   ██████████  BATCH 1

🏷️ Static Typing
   ░░░░░░░░░░  LOCKED

📚 Documentation
   ░░░░░░░░░░  LOCKED

📝 Docstrings
   ░░░░░░░░░░  LOCKED

🧪 Pytest
   ░░░░░░░░░░  LOCKED

🏆 Part 7 Boss Fight
   ░░░░░░░░░░  LATER
```

---

# 🎯 EXIT CRITERIA — PART 7

Eventually, you should be able to say:

```text
"I don't just write Python that works.

I write Python that:

✅ Handles expected failures
✅ Communicates errors clearly
✅ Uses appropriate exception types
✅ Validates its assumptions
✅ Can be understood by another developer
✅ Can be tested confidently
"
```

And that's the standard we're building toward.

---

# 🥋 SENSEI'S FINAL WORD

Don't try to memorize every exception.

That's not the point.

You can always look up:

```text
"Which exception does this operation raise?"
```

What matters is developing the instinct to ask:

```text
🤔 What can fail?

🤔 Is this failure expected?

🤔 Can I recover?

🤔 Where should I handle it?

🤔 Should I raise something more meaningful?

🤔 Am I accidentally hiding a bug?
```

That instinct is worth far more than memorizing a list of exception names.

---

# 🏁 BATCH 1 COMPLETE

```text
Exception Handling
        │
        ├── try              ✅
        ├── except           ✅
        ├── else             ✅
        ├── finally          ✅
        ├── raise            ✅
        ├── propagation      ✅
        ├── custom errors    ✅
        └── chaining         ✅
```

Next through the gates:

```text
🏷️ STATIC TYPING
```

But first...

**practice this batch until `try/except` stops feeling like a rescue rope and starts feeling like part of your program's design.** 😎🥋🐍