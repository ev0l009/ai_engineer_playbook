
# 🤖 The AI Engineer Playbook
# 🟣 Part 6 — Pythonic Features
## Batch 4 — Context Managers 🚪

> *"Use the resource. Finish your work. Clean up properly."*

---

# 🎯 Learning Objectives

By the end of this batch, you should be able to:

- Understand the problem context managers solve
- Use the `with` statement confidently
- Understand automatic resource cleanup
- Use context managers with files
- Explain why `with` is safer than manual cleanup
- Understand what `__enter__()` does
- Understand what `__exit__()` does
- Build a simple custom context manager
- Understand exceptions inside a context manager
- Recognize practical uses of context managers

---

# 🧭 Where You Are
# 🤖 AI Engineer Playbook

Phase 1 — Python Fluency 🐍

████████████████████████████████████████████████████

✅ Foundations
✅ Functions
✅ Collections
✅ Object-Oriented Programming
✅ Files & Python Ecosystem

🟣 Pythonic Features

    ✅ Iterators
    ✅ Generators
    ✅ Decorators
    🚪 Context Managers  ← YOU ARE HERE

🏆 Part 6 Boss Fight
    ⬜ Approaching...

🎯 Part Goal:
Understand and use Python's
more powerful language features.

---

# 🧠 Before We Begin

Let's start with something familiar.

Suppose we want to read a file.

You might write:

```python
file = open("players.txt")

data = file.read()

file.close()
```

This works.

The flow is:

```text
Open file
    ↓
Use file
    ↓
Close file
```

Simple enough.

But let's introduce a problem.

What happens here?

```python
file = open("players.txt")

data = file.read()

some_problem_happens()

file.close()
```

If this happens:

```text
💥 ERROR
```

before:

```python
file.close()
```

then:

```text
Open file
    ↓
Use file
    ↓
💥 ERROR
    ↓
file.close() never happens
```

Uh oh. 😬

The resource may not be cleaned up properly.

This is where context managers enter the arena.

---

# 🚪 The `with` Statement

Python gives us this:

```python
with open("players.txt") as file:
    data = file.read()
```

Now the flow becomes:

```text
Open resource
      ↓
Use resource
      ↓
Leave with block
      ↓
Clean up automatically
```

Even better:

```text
Open resource
      ↓
Use resource
      ↓
💥 ERROR?
      ↓
Clean up automatically
```

🤯

That is the big superpower of a context manager.

---

# 🧠 The Big Idea

A context manager helps manage something that needs:

```text
SETUP
  ↓
USE
  ↓
CLEANUP
```

Think about it like borrowing equipment.

```text
🏟️ Football Academy Equipment Room

1. Get the equipment
        ↓
2. Use the equipment
        ↓
3. Return the equipment
```

You shouldn't have to remember:

```text
"Wait...

Did I return it?

Did I close it?

Did I clean it up?"
```

The context manager handles that lifecycle.

```text
ENTER
  ↓
USE
  ↓
EXIT
```

---

# 🧪 Your First Context Manager

Let's look at the familiar pattern again:

```python
with open("players.txt") as file:
    data = file.read()
```

Break it apart.

```python
with open("players.txt") as file:
```

means roughly:

```text
"Open this file."

"Give me access to it as `file`."

"When I'm done with this block,
make sure cleanup happens."
```

Then:

```python
data = file.read()
```

does the actual work.

When Python reaches the end of the block:

```python
with open("players.txt") as file:
    data = file.read()

# Cleanup has happened here
```

the file is automatically closed.

---

# 🧱 The Shape of a Context Manager

```python
with something as name:
    # Work happens here
```

Conceptually:

```text
┌──────────────────────────────┐
│ ENTER CONTEXT                │
│                              │
│ Get resource                 │
│ Prepare resource             │
├──────────────────────────────┤
│                              │
│ YOUR CODE                    │
│                              │
│ Use resource                 │
│ Do your work                 │
├──────────────────────────────┤
│                              │
│ EXIT CONTEXT                 │
│                              │
│ Cleanup resource             │
└──────────────────────────────┘
```

---

# 🧪 Practice — Reading a File

Write a context manager using `with` that:

1. Opens:

```text
players.txt
```

2. Reads its contents.

3. Prints the contents.

Use:

```python
with open(...) as file:
    ...
```

---

# 🧠 Why Is This Better?

Compare these two approaches.

## Manual Approach

```python
file = open("players.txt")

data = file.read()

file.close()
```

## Context Manager Approach

```python
with open("players.txt") as file:
    data = file.read()
```

The second version says:

```text
"This resource belongs to this block."
```

Once we're done with the block:

```text
Cleanup.
```

Python handles it.

---

# 🐛 Debugging Lab — The Forgotten Close

Look at this:

```python
file = open("players.txt")

for line in file:
    print(line)

file.close()
```

Now imagine the loop causes an error halfway through.

```text
Open file
    ↓
Start reading
    ↓
💥 ERROR
    ↓
file.close() skipped
```

Rewrite the code using:

```python
with
```

Then explain:

> Why is the `with` version safer?

---

# ⚔️ Mini Challenge — Save a Training Session

Imagine you have:

```python
session = "Speed training completed"
```

Write code that:

1. Opens:

```text
training_log.txt
```

2. Uses write mode.

3. Writes the session.

4. Uses a context manager.

The structure should look roughly like:

```python
with open(...) as file:
    ...
```

---

# 🧠 Context Managers Are Not Just for Files

Files are the classic example.

But the idea is much bigger.

A context manager can manage things like:

```text
📁 Files
🔒 Locks
🌐 Network connections
🗄️ Database connections
⏱ Timers
🧪 Temporary resources
```

The common pattern remains:

```text
Acquire resource
       ↓
Use resource
       ↓
Release resource
```

Or:

```text
SETUP
  ↓
WORK
  ↓
CLEANUP
```

---

# 🤔 The Problem

Imagine you have a database connection.

Without automatic management:

```python
connection = connect_to_database()

# Do work

connection.close()
```

Again:

```text
What if an error happens?
```

You could try:

```python
connection = connect_to_database()

try:
    # Do work

finally:
    connection.close()
```

This is safer.

Because:

```text
try
    ↓
Do work
    ↓
finally
    ↓
Cleanup
```

But Python gives us a cleaner pattern for many situations:

```python
with resource:
    # Do work
```

---

# 🧠 Context Managers and Exceptions

This is one of their biggest strengths.

Consider:

```python
with open("players.txt") as file:
    data = file.read()

    number = 10 / 0
```

Inside the block:

```text
💥 ZeroDivisionError
```

Something goes wrong.

But the context manager still gets the chance to clean up.

Conceptually:

```text
ENTER
  ↓
Open file
  ↓
Run block
  ↓
💥 ERROR
  ↓
EXIT
  ↓
Close file
  ↓
Error continues
```

This is incredibly useful.

---

# 🧠 The Secret Behind `with`

Now...

we go beneath the surface. 👀

Remember this:

```python
with something as name:
    # code
```

Python is using a special protocol.

And yes...

we've seen special methods before. 😏

Welcome back:

# ✨ Dunder Methods

The two important ones are:

```python
__enter__()
```

and:

```python
__exit__()
```

Conceptually:

```text
with starts
    │
    ▼
__enter__()
    │
    ▼
YOUR CODE
    │
    ▼
__exit__()
```

🤯

So context managers connect directly to something you already learned:

```text
Classes
    ↓
Objects
    ↓
Dunder Methods
    ↓
Context Managers
```

See?

Python has been quietly preparing you. 🥋

---

# 🧱 Building a Custom Context Manager

Let's create a simple class.

```python
class TrainingSession:

    def __enter__(self):
        print("🏃 Training session started")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("🏁 Training session ended")
```

Now we can use:

```python
with TrainingSession() as session:
    print("Players are training.")
```

Conceptually:

```text
with TrainingSession()
        │
        ▼
__enter__()
        │
        ▼
🏃 Training session started
        │
        ▼
Run block
        │
        ▼
Players are training.
        │
        ▼
__exit__()
        │
        ▼
🏁 Training session ended
```

---

# 🧠 What Does `__enter__()` Do?

When the `with` block begins:

```python
with TrainingSession() as session:
```

Python calls:

```python
__enter__()
```

This is where we usually:

```text
Prepare something
Open something
Acquire something
Set something up
```

For example:

```python
def __enter__(self):
    print("Starting...")
    return self
```

The returned value becomes:

```python
session
```

So:

```python
with TrainingSession() as session:
```

can be thought of as:

```text
__enter__()
    │
    ▼
Returns something
    │
    ▼
Assigned to `session`
```

---

# 🧠 What Does `__exit__()` Do?

When we leave the block:

```python
with TrainingSession() as session:
    print("Players are training.")
```

Python calls:

```python
__exit__()
```

This is where cleanup happens.

```python
def __exit__(self, exc_type, exc_value, traceback):
    print("Cleaning up...")
```

Conceptually:

```text
WORK FINISHED

        OR

💥 ERROR OCCURRED

        ↓

__exit__()

        ↓

CLEANUP
```

---

# 🧪 Practice — Academy Gate

Create a context manager class:

```python
class AcademyGate:
```

When entering:

```text
🚪 Academy gate opened.
```

When leaving:

```text
🔒 Academy gate closed.
```

Use it like:

```python
with AcademyGate():
    print("Players entered the academy.")
```

Expected output:

```text
🚪 Academy gate opened.
Players entered the academy.
🔒 Academy gate closed.
```

---

# 🧠 The `as` Keyword

Look again:

```python
with TrainingSession() as session:
```

The:

```python
as session
```

gets whatever:

```python
__enter__()
```

returns.

Example:

```python
class Player:

    def __enter__(self):
        return "Salah"

    def __exit__(self, exc_type, exc_value, traceback):
        print("Session ended")
```

Then:

```python
with Player() as player:
    print(player)
```

Conceptually:

```text
__enter__()
    │
    ▼
returns "Salah"
    │
    ▼
player = "Salah"
```

So:

```text
`as variable`
```

is connected to:

```python
return value
```

inside:

```python
__enter__()
```

---

# 🧪 Practice — Player Session

Create:

```python
class PlayerSession:
```

Give it:

```python
def __enter__(self):
```

that returns:

```text
"Saka"
```

Then use:

```python
with PlayerSession() as player:
    print(f"Current player: {player}")
```

Finally, make:

```python
__exit__()
```

print:

```text
Player session closed.
```

---

# 🐛 Debugging Lab — Where Did `session` Come From?

Look at this:

```python
class TrainingSession:

    def __enter__(self):
        return "Morning Session"

    def __exit__(self, exc_type, exc_value, traceback):
        print("Session ended")
```

Then:

```python
with TrainingSession() as session:
    print(session)
```

Output:

```text
Morning Session
Session ended
```

## Your Mission

Explain:

1. Where did `session` get its value?
2. Which method returned it?
3. When did `__exit__()` run?

---

# 🧠 Exceptions Inside `__exit__()`

Now let's look closer at:

```python
def __exit__(self, exc_type, exc_value, traceback):
```

Those three parameters contain information about an exception if one happened.

Conceptually:

```text
No Error

exc_type  → None
exc_value → None
traceback → None
```

But if something goes wrong:

```text
💥 ERROR
```

Python can provide information about it.

For example:

```python
class TrainingSession:

    def __enter__(self):
        print("Session started")
        return self

    def __exit__(self, exc_type, exc_value, traceback):

        if exc_type:
            print("Something went wrong!")

        print("Cleaning up...")
```

---

# 🧠 Important Distinction

This:

```python
__exit__()
```

does not automatically mean:

```text
"The error disappears."
```

By default, cleanup can happen and the exception can still continue.

Conceptually:

```text
Error
  ↓
__exit__ runs
  ↓
Cleanup
  ↓
Error may still propagate
```

This is important.

Context managers are mainly about ensuring the cleanup phase gets a chance to happen.

---

# 🧪 Practice — Error Detector

Create:

```python
class SafeTraining:
```

Requirements:

### `__enter__()`

Print:

```text
🏃 Training started.
```

### `__exit__()`

If an exception happened:

```text
⚠️ Training encountered a problem.
```

Then always print:

```text
🧹 Cleaning up training equipment.
```

Use it with:

```python
with SafeTraining():
    print("Running drills...")
```

Then try another version where something inside the block causes an error.

Observe the flow.

---

# 🧠 The Lifecycle

A custom context manager follows this pattern:

```text
OBJECT CREATED
      │
      ▼
__enter__()
      │
      ▼
VALUE RETURNED
      │
      ▼
`as variable`
      │
      ▼
WITH BLOCK RUNS
      │
      ├── Normal completion
      │
      └── 💥 Exception
              │
              ▼
          __exit__()
              │
              ▼
           CLEANUP
```

That's the whole lifecycle.

---

# ⚔️ Mini Challenge — Training Facility

Create a context manager:

```python
class TrainingFacility:
```

When entering:

```text
🏟️ Training facility opened.
```

Return the object itself.

The class should have a method:

```python
train(self, player):
```

which prints:

```text
[player] is training.
```

When exiting:

```text
🏟️ Training facility closed.
```

Use it like:

```python
with TrainingFacility() as facility:
    facility.train("Saka")
    facility.train("Salah")
```

Expected idea:

```text
🏟️ Training facility opened.
Saka is training.
Salah is training.
🏟️ Training facility closed.
```

This is a nice connection between:

```text
OOP
    +
Context Managers
```

---

# 🧠 Context Managers Without Classes

Here's something interesting.

You don't always need to create a class.

Python also provides tools for creating context managers in other ways.

One pattern uses:

```python
contextlib
```

For example, Python has:

```python
from contextlib import contextmanager
```

Then a generator function can help define the setup and cleanup phases.

The general idea looks like:

```python
from contextlib import contextmanager


@contextmanager
def training_session():

    print("Starting session")

    yield

    print("Ending session")
```

Then:

```python
with training_session():
    print("Players are training.")
```

Conceptually:

```text
Code before yield
        ↓
ENTER

yield
        ↓
WITH BLOCK RUNS

Code after yield
        ↓
EXIT
```

🤯

Did you notice what just happened?

```text
Generators ⚡
        +
Decorators 🎁
        +
Context Managers 🚪
```

The things you've been learning are starting to connect.

---

# 🧠 Don't Panic

At this stage, the class-based version is the clearest way to understand what is happening.

Remember:

```python
class MyContext:

    def __enter__(self):
        # Setup
        return something

    def __exit__(self, exc_type, exc_value, traceback):
        # Cleanup
```

That's your foundation.

The:

```python
@contextmanager
```

approach is another useful tool.

You don't need to memorize every pattern immediately.

Understand the lifecycle first.

---

# 🧪 Practice — Generator Context Manager

Using:

```python
from contextlib import contextmanager
```

create:

```python
@contextmanager
def academy_session():
```

Before:

```python
yield
```

print:

```text
🎬 Academy session begins.
```

After:

```python
yield
```

print:

```text
🏁 Academy session ends.
```

Use:

```python
with academy_session():
    print("Players are learning.")
```

Expected:

```text
🎬 Academy session begins.
Players are learning.
🏁 Academy session ends.
```

---

# 🐛 Debugging Lab — Missing Cleanup

Look at this:

```python
from contextlib import contextmanager


@contextmanager
def session():
    print("Session started")

    yield
```

Then:

```python
with session():
    print("Training...")
```

It works.

But imagine this context manager represents something that needs cleanup.

## Your Mission

Add cleanup behavior after:

```python
yield
```

Explain why code after `yield` represents the exit phase.

---

# 🧠 Context Managers vs Decorators

Interesting...

we just learned decorators.

Now context managers.

They can look similar because both can use:

```text
Before
    ↓
Something happens
    ↓
After
```

But their purposes are different.

## Decorator 🎁

Wraps a:

```text
FUNCTION
```

to add behavior.

```text
Before
  ↓
Function
  ↓
After
```

---

## Context Manager 🚪

Wraps a:

```text
BLOCK OF CODE
```

while managing a resource or context.

```text
Enter
  ↓
Code Block
  ↓
Exit / Cleanup
```

---

# 🧠 The Big Comparison

```text
🎁 DECORATOR

@decorator
def function():
    ...

        ↓

Adds behavior around
a function call.


────────────────────────


🚪 CONTEXT MANAGER

with context:
    ...

        ↓

Manages setup and cleanup
around a block of code.
```

That distinction matters.

---

# 🔥 Hard Challenge — Football Academy Resource Manager

Create a class:

```python
class AcademySession:
```

Requirements:

### When entering:

Print:

```text
🚪 Academy session opened.
```

Return:

```python
self
```

The class should have:

```python
add_player(self, name)
```

which prints:

```text
[name] joined the session.
```

And:

```python
start_training(self, drill)
```

which prints:

```text
Training drill: [drill]
```

When leaving:

Print:

```text
🧹 Cleaning up academy resources.
🔒 Academy session closed.
```

Use it like:

```python
with AcademySession() as academy:
    academy.add_player("Saka")
    academy.add_player("Salah")

    academy.start_training("Speed")
```

---

## 🔥 Upgrade

Inside the block, deliberately cause an error.

For example, you might try an invalid operation.

Modify:

```python
__exit__()
```

so that it can detect whether an exception happened.

Your flow should conceptually become:

```text
ENTER
  ↓
Open Academy Session
  ↓
Run Academy Code
  ↓
💥 Error?
  │
  ├── Yes → Report it
  │
  └── No → Continue normally
  ↓
Cleanup
  ↓
Close Session
```

---

# 🧠 Comprehension Check

Complete these sentences.

### 1.

> A context manager is useful when something needs __________________ before use and __________________ after use.

### 2.

> The `with` statement helps ensure that __________________ happens.

### 3.

> `__enter__()` runs when __________________.

### 4.

> `__exit__()` runs when __________________.

### 5.

> The value after `as` usually comes from __________________.

### 6.

> A decorator wraps a __________________.

### 7.

> A context manager manages a __________________.

---

# 🥋 Skill Check

## Question 1

Why is this:

```python
with open("players.txt") as file:
    data = file.read()
```

usually safer than:

```python
file = open("players.txt")

data = file.read()

file.close()
```

?

---

## Question 2

What are the two important dunder methods used by a class-based context manager?

---

## Question 3

Explain the lifecycle:

```text
ENTER
    ↓
WORK
    ↓
EXIT
```

---

## Question 4

What does:

```python
return self
```

inside:

```python
__enter__()
```

allow us to do?

---

## Question 5

What happens if an error occurs inside a `with` block?

---

## Question 6

What is the role of:

```python
yield
```

inside a function decorated with:

```python
@contextmanager
```

?

---

## Question 7

Explain the difference between:

```text
🎁 Decorator
```

and:

```text
🚪 Context Manager
```

in your own words.

---

# 🧠 Explain It Like You're Teaching Someone

Imagine you're explaining context managers to a beginner using this story:

```text
🚪 Enter a room
      ↓
🛠️ Do your work
      ↓
🚪 Leave the room
      ↓
🧹 Someone makes sure the room
   is properly cleaned up
```

Connect that story to:

```python
with something:
    ...
```

If you can explain why cleanup still matters when something goes wrong...

you're getting it. 🥋

---

# 🏗️ Project Connection — Football Academy AI

Your Football Academy AI will eventually deal with things that need careful management.

For example:

```text
📁 Player data files
🗄️ Databases
🌐 API connections
🔒 Shared resources
```

Imagine:

```python
with database_connection() as db:
    players = db.get_players()

    db.save_player(...)
```

The context manager can conceptually handle:

```text
Connect
   ↓
Use database
   ↓
Disconnect
```

The code inside the block focuses on:

```text
THE ACTUAL WORK
```

while the context manager focuses on:

```text
SETUP
+
CLEANUP
```

This separation is clean.

And very Pythonic. 🐍

---

# 🧠 Batch Summary

You started with this problem:

```text
Open resource
    ↓
Use resource
    ↓
Remember to clean up 😬
```

Then Python gave us:

```python
with resource:
    # Use resource
```

Which gives us:

```text
ENTER
  ↓
USE
  ↓
EXIT
  ↓
CLEANUP
```

For class-based context managers:

```python
class MyContext:

    def __enter__(self):
        # Setup
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Cleanup
```

The lifecycle:

```text
with MyContext() as value:
        │
        ▼
    __enter__()
        │
        ▼
    value returned
        │
        ▼
    BLOCK RUNS
        │
        ▼
    __exit__()
```

And using:

```python
@contextmanager
```

we can also create a context manager using:

```text
Before yield
    ↓
ENTER

yield
    ↓
WITH BLOCK

After yield
    ↓
EXIT
```

---

# 🧠 The Final Big Idea

A context manager is not primarily about:

```text
"Using `with` because Python programmers like it."
```

😂

It's about responsibility.

```text
Acquire resource
        ↓
Use resource
        ↓
Release resource
```

Or more generally:

```text
SETUP
  ↓
WORK
  ↓
CLEANUP
```

And Python helps make sure that cleanup isn't forgotten.

Even when:

```text
💥 Things go sideways.
```

---

# 🏅 Batch Progress

```text
🟣 PART 6 — PYTHONIC FEATURES

🔁 Iterators
    ██████████  COMPLETE ✅

⚡ Generators
    ██████████  COMPLETE ⚡

🎁 Decorators
    ██████████  COMPLETE 🥋

🚪 Context Managers
    ██████████  COMPLETE 🚪
                 ↑
              YOU ARE HERE

🏆 Part Boss Fight
    ░░░░░░░░░░  NEXT...
```

---

# 🏅 Context Manager Badge Unlocked

```text
╔══════════════════════════════════════╗
║                                      ║
║       🚪 CONTEXT KEEPER              ║
║                                      ║
║  "I enter cleanly.                   ║
║   I exit responsibly."               ║
║                                      ║
╚══════════════════════════════════════╝
```

😎🥋🐍

---

# 🏁 PYTHONIC FEATURES — BATCHES COMPLETE

```text
ITERATORS
    ↓
"How do I move through data one item at a time?"

        ↓

GENERATORS
    ↓
"How do I produce values efficiently when needed?"

        ↓

DECORATORS
    ↓
"How do I add behavior around functions?"

        ↓

CONTEXT MANAGERS
    ↓
"How do I manage setup and cleanup around a block?"
```

And now...

```text
╔════════════════════════════════════╗
║                                    ║
║        🏆 PART 6 BOSS FIGHT        ║
║                                    ║
║       PYTHONIC FEATURES            ║
║                                    ║
║  Iterators ⚡ Generators 🎁 Doors  ║
║                                    ║
╚════════════════════════════════════╝
```

The final fight for this part is waiting. 😈🥋