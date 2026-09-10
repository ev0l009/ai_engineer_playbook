# 🤖 The AI Engineer Playbook
# 🟣 Part 6 — Pythonic Features
## Batch 2 — Generators ⚡

> *"Don't build the entire conveyor belt at once. Produce the next item when someone asks for it."*

---

# 🎯 Learning Objectives

By the end of this batch, you should be able to:

- Explain what a generator is
- Understand how `yield` differs from `return`
- Explain why generators are iterators
- Use `next()` with generators
- Understand lazy evaluation
- Create generator functions
- Create generator expressions
- Understand generator exhaustion
- Use generators to process data efficiently
- Recognize when a generator is more appropriate than a list

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
    ⚡ Generators  ← YOU ARE HERE
    ⬜ Decorators
    ⬜ Context Managers

🎯 Part Goal:
Understand and use Python's
more powerful language features.

---

# 🧠 Before We Begin — Remember This

In the previous batch, we built our own iterator.

It looked something like this:

```python
class Counter:
    def __init__(self, limit):
        self.current = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            value = self.current
            self.current += 1
            return value

        raise StopIteration
```

And that worked.

But look at everything we had to manage:

```text
🧱 Class
    ↓
🧠 State
    ↓
__iter__()
    ↓
__next__()
    ↓
Manual updating
    ↓
StopIteration
```

That's a lot of machinery just to say:

> "Give me the next number."

Python looked at that and said:

> **"Yeah... we can make this easier."**

Enter:

# ⚡ Generators

---

# 🤔 The Problem

Imagine you want to produce:

```text
1
2
3
4
5
```

You could return them all at once.

For example:

```python
def get_numbers():
    return [1, 2, 3, 4, 5]
```

That gives us:

```text
[1, 2, 3, 4, 5]
```

But notice what happened.

Python created:

```text
1
2
3
4
5
```

**all at once.**

Now imagine:

```text
1
2
3
...
1,000,000
```

Or:

```text
Football match 1
Football match 2
Football match 3
...
10,000,000 matches
```

Do we always need all of that data immediately?

Sometimes...

**No.**

Sometimes we only need:

```text
Give me one.

Now give me the next one.

Now another one.

Okay, stop.
```

And that's where generators become useful.

---

# ⚡ The Big Idea

A generator produces values:

```text
ONE AT A TIME
```

Instead of:

```text
CREATE EVERYTHING
        ↓
STORE EVERYTHING
        ↓
RETURN EVERYTHING
```

A generator can work like:

```text
Create value
    ↓
Give it to me
    ↓
Pause
    ↓
Wait...
    ↓
Need another?
    ↓
Continue
    ↓
Create next value
    ↓
Pause again
```

This idea is called:

# 💤 Lazy Evaluation

Don't do the work yet.

Do it **when the value is actually needed**.

---

# 🧠 `return` vs `yield`

You already know `return`.

For example:

```python
def greet():
    return "Hello"
```

When Python reaches:

```python
return "Hello"
```

the function:

```text
Returns the value
        ↓
Function finishes
        ↓
Bye 👋
```

But now look at:

```python
def greet():
    yield "Hello"
```

`yield` behaves differently.

Instead of:

```text
Return
    ↓
Function ends
```

we get:

```text
yield
    ↓
Give value
    ↓
PAUSE FUNCTION ⏸️
```

And this is the first big 🤯 moment.

The function does **not necessarily finish**.

It can pause.

And later...

continue from where it stopped.

---

# 🧪 Our First Generator

Let's create one:

```python
def count():
    yield 1
    yield 2
    yield 3
```

Now:

```python
numbers = count()
```

Important:

At this point, we haven't received:

```text
1
2
3
```

Instead:

```text
count()
    ↓
Generator object created
```

Conceptually:

```text
numbers
   │
   ▼
┌─────────────────┐
│ yield 1         │ ← Ready to start
│ yield 2         │
│ yield 3         │
└─────────────────┘
```

Now we can ask for the next value:

```python
print(next(numbers))
```

Conceptually:

```text
Start function
    ↓
Reach:
yield 1
    ↓
Give us:
1
    ↓
PAUSE ⏸️
```

Output:

```text
1
```

---

# 🔁 Calling `next()` Again

Now:

```python
print(next(numbers))
```

Python does **not** restart the function.

Instead:

```text
Generator remembers:

"I already yielded 1."

Continue from here.
        ↓
yield 2
        ↓
Give:
2
        ↓
PAUSE ⏸️
```

Then:

```python
print(next(numbers))
```

Output:

```text
3
```

Our generator's journey looks like:

```text
START
  │
  ▼
yield 1
  │
  ├── Give 1
  └── PAUSE ⏸️
          │
          ▼
       next()
          │
          ▼
       yield 2
          │
          ├── Give 2
          └── PAUSE ⏸️
                  │
                  ▼
               next()
                  │
                  ▼
               yield 3
                  │
                  ├── Give 3
                  └── PAUSE ⏸️
                          │
                          ▼
                       next()
                          │
                          ▼
                    Function ends
                          │
                          ▼
                    StopIteration 🛑
```

---

# 🤯 The Connection

Does this look familiar?

```text
next()
    ↓
Value

next()
    ↓
Value

next()
    ↓
Value

next()
    ↓
StopIteration
```

👀

That's because:

# ⚡ A GENERATOR IS AN ITERATOR

Python automatically handles the machinery.

Earlier, we manually created:

```text
__iter__()
__next__()
State
StopIteration
```

With a generator:

```python
def count():
    yield 1
    yield 2
    yield 3
```

Python handles that iterator machinery for us.

So:

```text
CUSTOM ITERATOR

You:
    ├── Track state
    ├── Create __iter__()
    ├── Create __next__()
    └── Raise StopIteration


GENERATOR

You:
    └── Use yield 😎
```

---

# 🧪 Practice — Easy

Create a generator:

```python
def football_positions():
    ...
```

It should yield:

```text
Goalkeeper
Defender
Midfielder
Forward
```

Then create the generator:

```python
positions = football_positions()
```

Use:

```python
next()
```

to retrieve the positions one at a time.

Do not use a `for` loop yet.

---

# 🧪 Practice — Easy 2

Create:

```python
def colors():
    ...
```

It should yield:

```text
Red
Green
Blue
```

Then call:

```python
next()
```

four times.

### Questions

1. What happens during the first three calls?
2. What happens during the fourth?
3. Why?

---

# 🧠 Generators Remember Their State

Consider:

```python
def match_minutes():
    yield 15
    yield 30
    yield 45
    yield 60
    yield 75
    yield 90
```

Now:

```python
minutes = match_minutes()
```

The generator begins here:

```text
yield 15  ← READY
yield 30
yield 45
yield 60
yield 75
yield 90
```

After:

```python
next(minutes)
```

we get:

```text
15
```

And the generator's position becomes:

```text
yield 15  ← Already used
yield 30  ← NEXT
yield 45
yield 60
yield 75
yield 90
```

It remembers.

This is a major difference from an ordinary function.

---

# 🧪 Practice — Where Is The Generator?

Consider:

```python
def numbers():
    yield 10
    yield 20
    yield 30
    yield 40
```

Then:

```python
values = numbers()

print(next(values))
print(next(values))
```

### Questions

1. What values have been produced?
2. What value comes next?
3. Has the function finished?
4. If you call `next(values)` two more times, what happens?

Explain it using the idea of:

```text
State
Pause
Resume
```

---

# 💤 Lazy Evaluation

Let's look at something more realistic.

Suppose we write:

```python
def get_players():
    players = []

    for number in range(1, 1_000_001):
        players.append(f"Player {number}")

    return players
```

This approach conceptually does:

```text
Create Player 1
Create Player 2
Create Player 3
...
Create Player 1,000,000
        ↓
Store everything
        ↓
Return everything
```

Even if we only want:

```text
Player 1
Player 2
Player 3
```

A generator can approach this differently:

```python
def get_players():
    for number in range(1, 1_000_001):
        yield f"Player {number}"
```

Now the generator can conceptually do:

```text
Need a player?
      │
      ▼
Create Player 1
      │
      ▼
Pause ⏸️

Need another?
      │
      ▼
Create Player 2
      │
      ▼
Pause ⏸️
```

It doesn't need to prepare every value before giving you the first one.

---

# 🧠 The Big Advantage

Lists generally work like:

```text
🍱 PREPARE EVERYTHING FIRST

[1, 2, 3, 4, 5, ...]
```

Generators can work like:

```text
🍳 COOK ON DEMAND

"One please."

→ Here.

"Another."

→ Here.

"Another."

→ Here.
```

😂

That's lazy evaluation.

And yes, in programming:

> **Being lazy can be a feature.**

---

# 🟡 Medium Practice — Number Generator

Create:

```python
def number_generator(limit):
    ...
```

It should yield numbers starting from:

```text
1
```

and stop at the provided limit.

Example:

```python
numbers = number_generator(5)
```

Should produce:

```text
1
2
3
4
5
```

You should be able to use:

```python
for number in numbers:
    print(number)
```

---

# 🟡 Medium Practice 2 — Even Numbers

Create:

```python
def even_numbers(limit):
    ...
```

Example:

```python
for number in even_numbers(10):
    print(number)
```

Expected:

```text
2
4
6
8
10
```

### Friendly Sensei Rule 🥋

Don't build a list first.

This:

```python
numbers = []

# Build everything

return numbers
```

is banned for this exercise. 😂🚫

Use:

```python
yield
```

---

# 🔴 Hard Practice — Player Filter

Suppose we have:

```python
players = [
    {"name": "Salah", "position": "RW"},
    {"name": "Rice", "position": "CM"},
    {"name": "Saka", "position": "RW"},
    {"name": "Palmer", "position": "AM"},
]
```

Create:

```python
def filter_position(players, position):
    ...
```

It should yield only players matching the requested position.

Example:

```python
for player in filter_position(players, "RW"):
    print(player["name"])
```

Expected:

```text
Salah
Saka
```

### Important

Don't create a new list containing the matching players.

Yield them one at a time.

```text
Check player
    ↓
Matches?
    │
    ├── Yes → yield
    │
    └── No  → continue
```

---

# ⚔️ Mini Challenge — Match Event Stream

Time to use what we just learned. 😎⚽

Imagine a football match producing events.

Create a generator:

```python
def match_events():
    ...
```

It should yield dictionaries such as:

```python
{
    "minute": 12,
    "event": "Goal",
    "player": "Salah"
}
```

Then more events:

```python
{
    "minute": 27,
    "event": "Yellow Card",
    "player": "Rice"
}
```

And so on.

Your generator might conceptually produce:

```text
MATCH START
     │
     ▼
12' Goal
     │
     ▼
PAUSE ⏸️
     │
next()
     │
     ▼
27' Yellow Card
     │
     ▼
PAUSE ⏸️
     │
next()
     │
     ▼
54' Substitution
     │
     ▼
...
```

---

## Requirements

Create at least:

* 1 Goal
* 1 Yellow Card
* 1 Substitution
* 1 Additional event of your choice

Each event should contain:

```text
minute
event
player
```

Then consume your generator using:

```python
for event in match_events():
    print(...)
```

Format the output however you like.

For example:

```text
12' — Goal — Salah
27' — Yellow Card — Rice
54' — Substitution — Palmer
```

### Bonus 🧠

Add:

```text
Team
```

to every event.

Then imagine how this could eventually become part of:

```text
⚽ Football Academy AI
        ↓
Match Simulation
        ↓
Live Event Stream
```

👀

---

# 🧩 Generator Exhaustion

Here's something important.

Consider:

```python
def numbers():
    yield 1
    yield 2
    yield 3
```

Then:

```python
values = numbers()

for number in values:
    print(number)
```

Output:

```text
1
2
3
```

Now try:

```python
for number in values:
    print(number)
```

What happens?

```text
...
```

Nothing.

Why?

Because the generator has already been consumed.

Conceptually:

```text
Generator

1 → USED
2 → USED
3 → USED

Nothing left 🏜️
```

Generators generally don't automatically rewind themselves.

Once consumed:

```text
🛑 Exhausted
```

If you need to start again:

```python
values = numbers()
```

You create a new generator.

---

# 🧪 Practice — Predict Before Running

Consider:

```python
def letters():
    yield "A"
    yield "B"
    yield "C"

alphabet = letters()

print(next(alphabet))

for letter in alphabet:
    print(letter)
```

### Question

What is printed?

Think about the generator's position.

Don't just guess.

Map it:

```text
A
B
C
```

Where is the generator after the first `next()`?

---

# 🧠 Generator Functions vs Normal Functions

Let's compare.

## Normal Function

```python
def get_numbers():
    return [1, 2, 3]
```

Calling:

```python
numbers = get_numbers()
```

gives:

```text
[1, 2, 3]
```

All values are ready.

---

## Generator Function

```python
def get_numbers():
    yield 1
    yield 2
    yield 3
```

Calling:

```python
numbers = get_numbers()
```

gives us conceptually:

```text
A generator ready to produce:

1
2
3
```

The values are produced as the generator advances.

---

# 🧪 Practice — `return` or `yield`?

For each situation, decide which makes more sense.

## Situation 1

A function calculates:

```text
total_price
```

and gives you one final answer.

```text
return
or
yield?
```

---

## Situation 2

A function reads through a huge source of records and processes them one record at a time.

```text
return
or
yield?
```

---

## Situation 3

A function checks whether a password is valid.

It produces one answer:

```text
True
or
False
```

```text
return
or
yield?
```

---

## Situation 4

A function can potentially produce an ongoing sequence of values.

```text
return
or
yield?
```

Explain your reasoning.

---

# ⚡ Generator Expressions

Remember list comprehensions?

```python
numbers = [number * 2 for number in range(10)]
```

That creates a list.

A generator expression looks similar:

```python
numbers = (number * 2 for number in range(10))
```

The difference is:

```text
[ ... ]

Creates a LIST
```

while:

```text
( ... )

Creates a GENERATOR
```

---

# 🧠 Compare Them

## List Comprehension

```python
squares = [number ** 2 for number in range(1, 6)]
```

Conceptually:

```text
Calculate everything:

1
4
9
16
25

Store:

[1, 4, 9, 16, 25]
```

---

## Generator Expression

```python
squares = (number ** 2 for number in range(1, 6))
```

Conceptually:

```text
Ready to calculate:

1² → when needed
2² → when needed
3² → when needed
...
```

The generator can be consumed:

```python
for square in squares:
    print(square)
```

---

# 🧪 Practice — Generator Expression

Create a generator expression that produces:

```text
1
4
9
16
25
```

Use:

```text
range()
**
```

Then:

1. Retrieve the first value using `next()`.
2. Retrieve the second value using `next()`.
3. Use a `for` loop to print the remaining values.

### Question

Why doesn't the `for` loop print the first two values again?

---

# 🟡 Medium — Filter With a Generator Expression

Given:

```python
scores = [45, 67, 89, 32, 91, 76]
```

Create a generator expression that produces only scores:

```text
>= 70
```

Expected:

```text
89
91
76
```

Do not create a list.

---

# 🔴 Hard — Transform and Filter

Given:

```python
players = [
    {"name": "Salah", "goals": 20},
    {"name": "Saka", "goals": 15},
    {"name": "Rice", "goals": 4},
    {"name": "Palmer", "goals": 18},
]
```

Create a generator expression that:

1. Filters players with at least `15` goals.
2. Produces only their names.

Expected:

```text
Salah
Saka
Palmer
```

Use a single generator expression.

---

# 🧠 A Very Important Distinction

Don't walk away thinking:

> **"Generators are always better than lists."**

Nope. 😂🥋

Use the right tool.

## A List Makes Sense When:

```text
You need all values available.

You need to access values repeatedly.

You need indexing.

You need the length immediately.

You need to reuse the collection.
```

Example:

```python
players[0]
players[1]
players[-1]
```

Lists are great for this.

---

## A Generator Makes Sense When:

```text
You can process values one at a time.

The data may be very large.

You don't need every value immediately.

You only need to make values when required.
```

The mental model:

```text
LIST

"Here's everything."
📦📦📦📦📦


GENERATOR

"Ask me when you're ready."
📦
   📦
      📦
         📦
```

---

# 🧪 Debugging Lab 🐛

Something is wrong with this code:

```python
def countdown(start):
    while start > 0:
        return start
        start -= 1
```

The developer expected:

```text
5
4
3
2
1
```

But something isn't right.

## Your Mission

1. Identify the problem.
2. Explain why it happens.
3. Rewrite the function as a generator.
4. Make it work with:

```python
for number in countdown(5):
    print(number)
```

---

# 🐛 Debugging Lab 2 — The Empty Generator

Consider:

```python
def get_numbers():
    for number in range(1, 6):
        yield number

numbers = get_numbers()

for number in numbers:
    print(number)

print("Again!")

for number in numbers:
    print(number)
```

The developer expected the numbers to print twice.

Instead:

```text
1
2
3
4
5

Again!
```

Then...

👻 Nothing.

### Your Mission

Explain:

1. Why this happened.
2. What "generator exhaustion" means.
3. How to fix the code if the developer needs to iterate over the values again.

---

# 🥋 Skill Check

No peeking. 😎

## Question 1

What is a generator?

---

## Question 2

What keyword is used to create a generator function?

```text
?
```

---

## Question 3

What is the biggest behavioral difference between:

```python
return
```

and:

```python
yield
```

?

---

## Question 4

Why can we use:

```python
next()
```

with a generator?

---

## Question 5

What does this mean?

```text
Lazy evaluation
```

---

## Question 6

What happens when a generator is exhausted?

---

## Question 7

What is the difference between:

```python
[number * 2 for number in range(5)]
```

and:

```python
(number * 2 for number in range(5))
```

?

---

## Question 8

When might a generator be a better choice than a list?

---

# 🧠 Explain It Like a Sensei

Explain this without drowning in technical jargon:

```text
FUNCTION
   │
   ▼
yield
   │
   ├── Produce a value
   │
   └── Pause ⏸️
          │
          ▼
       next()
          │
          ▼
       Resume
          │
          ▼
       yield
          │
          ▼
       Pause again ⏸️
```

If you can explain this naturally, you understand the heart of generators.

---

# ⚔️ Mini Challenge — Academy Training Stream

Let's put everything together. ⚽

The Football Academy has training sessions.

Each session produces players one at a time.

Suppose we have:

```python
players = [
    {
        "name": "Salah",
        "fitness": 92,
        "position": "RW"
    },
    {
        "name": "Rice",
        "fitness": 88,
        "position": "CM"
    },
    {
        "name": "Saka",
        "fitness": 95,
        "position": "RW"
    },
    {
        "name": "Palmer",
        "fitness": 76,
        "position": "AM"
    }
]
```

Create:

```python
def fit_players(players, minimum_fitness):
    ...
```

Your generator should:

```text
Check player
      │
      ▼
Fitness high enough?
      │
      ├── YES
      │     ↓
      │   yield player
      │
      └── NO
            ↓
         Continue
```

Example:

```python
for player in fit_players(players, 90):
    print(player["name"])
```

Expected:

```text
Salah
Saka
```

---

## 🔥 Upgrade

Now create another generator:

```python
def player_names(players):
    ...
```

It should receive a sequence of players and yield only:

```text
player["name"]
```

Now imagine chaining them:

```text
All Players
      │
      ▼
fit_players()
      │
      ▼
Only Fit Players
      │
      ▼
player_names()
      │
      ▼
Names
```

Try to make this work:

```python
fit = fit_players(players, 90)

names = player_names(fit)

for name in names:
    print(name)
```

🤯

Notice what happened.

We didn't need to create:

```text
List of fit players
        ↓
Then another list of names
```

Instead:

```text
Player
   ↓
Filter
   ↓
Transform
   ↓
Use
```

One item at a time.

Welcome to **generator pipelines**. 😎⚡

---

# 🏗️ Project Connection

This is where things start getting interesting.

Earlier, we had:

```text
Football Academy
      │
      ├── Players
      ├── Teams
      ├── Coaches
      └── Matches
```

Now we can imagine:

```text
⚽ MATCH EVENT STREAM

Match Data
    │
    ▼
⚡ Generator
    │
    ├── Event 1
    │
    ├── Event 2
    │
    ├── Event 3
    │
    └── ...
```

Or:

```text
ALL PLAYERS
      │
      ▼
⚡ Filter Generator
      │
      ▼
Eligible Players
      │
      ▼
⚡ Transform Generator
      │
      ▼
Player Names / Statistics
```

This isn't just a clever Python trick.

It's a way of thinking about data flowing through a system.

And that idea is going to show up again and again as we move toward:

```text
📊 Data Processing
      ↓
🤖 Machine Learning
      ↓
🧠 AI Systems
```

---

# 🧠 Batch Summary

You learned:

```text
⚡ GENERATOR

A special kind of iterator
that produces values
one at a time.
```

The key tool:

```python
yield
```

The mental model:

```text
yield
  ↓
Give value
  ↓
PAUSE ⏸️
  ↓
next()
  ↓
RESUME ▶️
```

And Python handles the messy iterator machinery:

```text
__iter__()
__next__()
State tracking
StopIteration
```

You also learned:

```text
🧠 Lazy Evaluation

Don't produce everything now.

Produce it when needed.
```

And:

```text
[ ... ]
    ↓
List Comprehension

( ... )
    ↓
Generator Expression
```

---

# 🏅 Batch Progress

```text
🟣 PART 6 — PYTHONIC FEATURES

🔁 Iterators
    ██████████  COMPLETE ✅

⚡ Generators
    ██████████  COMPLETE 🥋
                 ↑
              YOU ARE HERE

🎁 Decorators
    ░░░░░░░░░░  NEXT

🚪 Context Managers
    ░░░░░░░░░░  LOCKED

🏆 Part Boss Fight
    ░░░░░░░░░░  WAITING...
```

---

# 🚦 Exit Check

Before moving on, this sentence should make complete sense:

> **A generator is an iterator that can produce values one at a time, pausing after each `yield` and resuming when the next value is requested.**

If you're reading that and going:

```text
🤔 "Hmm... I think I need to fight yield again."
```

That's perfectly fine.

Generators can take a little hands-on repetition before they become intuitive.

But if you're reading it and going:

```text
😎 "Ohhhh. So Python is handling the iterator machinery for me."
```

Then...

# 🔓 GENERATORS — UNLOCKED ⚡

Take your time with the exercises, especially the **Academy Training Stream**.

Because the next batch is about to do something even more sneaky.

We're going to start passing functions around like ordinary objects.

# 🎁 NEXT UP — DECORATORS