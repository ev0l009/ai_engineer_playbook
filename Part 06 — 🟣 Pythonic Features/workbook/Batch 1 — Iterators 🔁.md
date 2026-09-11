# 🤖 The AI Engineer Playbook
## 🟣 Part 6 — Pythonic Features
### Batch 1 — Iterators 🔁

> *"Before you can understand generators, you need to understand the machinery underneath them."*

---

## 🎯 Learning Objectives

By the end of this batch, you should be able to:

- Explain what an iterable is
- Explain what an iterator is
- Understand the relationship between iterables and iterators
- Use `iter()`
- Use `next()`
- Understand `StopIteration`
- Explain how a `for` loop uses iterators
- Create a simple custom iterator
- Recognize when iterator-based thinking is useful

---

## 🧭 Where You Are

Phase 1 — Python Fluency 🐍

████████████████████████████████████████████████████

✅ Foundations
✅ Functions
✅ Collections
✅ Object-Oriented Programming
✅ Files & Python Ecosystem

🟣 Pythonic Features

    ⏳ Iterators
    ⬜ Generators
    ⬜ Decorators
    ⬜ Context Managers

🎯 Part Goal:
Understand and use Python's
more powerful language features.

---

# 🤔 The Problem

You've written this countless times:

```python
players = ["Messi", "Salah", "Mbappé"]

for player in players:
    print(player)
```

It looks incredibly simple.

Python sees:

```text
"Here is a list."

"Loop through it."

"Give me each player."

"Done."
```

But...

**How?**

How does Python know:

```text
First → Messi

Then → Salah

Then → Mbappé

Then → STOP
```

Something has to keep track of where you are.

Something has to know:

> "Give me the next item."

And something has to know:

> "There are no more items."

That "something" is an:

# 🔁 Iterator

---

# 🧠 The Big Idea

An iterator is an object that gives you items **one at a time**.

Think of it like a conveyor belt:

```text
              🔁 ITERATOR

        ┌───────────────────┐
        │ Messi             │
        │ Salah             │
        │ Mbappé            │
        └───────────────────┘
                 │
                 ▼
              next()
                 │
                 ▼
              "Messi"

                 │
                 ▼
              next()
                 │
                 ▼
              "Salah"

                 │
                 ▼
              next()
                 │
                 ▼
              "Mbappé"

                 │
                 ▼
              next()
                 │
                 ▼
          🛑 No more items
```

The iterator remembers its current position.

That's the key.

---

# 🧩 Iterable vs Iterator

This distinction is **very important**.

They sound almost identical.

They're not.

---

# 📦 Iterable

An **iterable** is something you can iterate over.

Examples:

```python
list
tuple
string
dictionary
set
```

For example:

```python
players = ["Messi", "Salah", "Mbappé"]
```

The list is an **iterable**.

It contains the data.

Conceptually:

```text
Iterable
    =
Something you can get an iterator from
```

---

# 🔁 Iterator

An iterator is the object that actually performs the step-by-step traversal.

You can get an iterator from an iterable using:

```python
iter()
```

For example:

```python
players = ["Messi", "Salah", "Mbappé"]

iterator = iter(players)
```

Now:

```text
players
   │
   │ iter()
   ▼
iterator
```

The list is the collection.

The iterator is the thing that walks through the collection.

---

# 🧠 A Simple Analogy

Imagine a book.

```text
📖 Book
```

The book contains:

```text
Page 1
Page 2
Page 3
Page 4
```

The book is like the **iterable**.

You can get a bookmark from it.

```text
📖 Book
    ↓
🔖 Bookmark
```

The bookmark tells you:

> "You're currently here."

Then you move:

```text
Page 1
   ↓
Page 2
   ↓
Page 3
   ↓
Page 4
```

The bookmark represents the iterator's current position.

So:

```text
Iterable
    =
The thing containing the items

Iterator
    =
The thing keeping track of where
you currently are
```

---

# 🛠️ `iter()`

Python provides:

```python
iter()
```

to obtain an iterator from an iterable.

Example:

```python
players = ["Messi", "Salah", "Mbappé"]

iterator = iter(players)
```

Now we have:

```text
players
   │
   │ iter()
   ▼
iterator
```

---

# 🛠️ `next()`

Once we have an iterator, we can ask it for the next item.

Python provides:

```python
next()
```

Example:

```python
players = ["Messi", "Salah", "Mbappé"]

iterator = iter(players)

print(next(iterator))
```

Output:

```text
Messi
```

Call it again:

```python
print(next(iterator))
```

Output:

```text
Salah
```

Again:

```python
print(next(iterator))
```

Output:

```text
Mbappé
```

And again:

```python
print(next(iterator))
```

Now Python has a problem.

There is nothing left.

So it raises:

```text
StopIteration
```

---

# 🛑 StopIteration

`StopIteration` is Python's way of saying:

> **"There are no more items."**

The sequence looks like:

```text
next(iterator)
      ↓
   "Messi"

next(iterator)
      ↓
   "Salah"

next(iterator)
      ↓
   "Mbappé"

next(iterator)
      ↓
StopIteration
```

This is a fundamental part of Python's iterator protocol.

---

# 🧠 The Iterator Protocol

A Python iterator fundamentally follows this idea:

```text
Give me the next item
        ↓
next()
        ↓
Return item

OR

No more items
        ↓
StopIteration
```

An iterator provides a `__next__()` operation.

And an iterator can also produce itself through `__iter__()`.

We'll see those methods when we build our own iterator.

For now, remember:

```text
iter()
    ↓
Get iterator

next()
    ↓
Get next item

StopIteration
    ↓
No more items
```

---

# 🔍 Let's Look Under the Hood

When you write:

```python
for player in players:
    print(player)
```

Python is doing something conceptually similar to:

```python
iterator = iter(players)

while True:
    try:
        player = next(iterator)
        print(player)
    except StopIteration:
        break
```

This isn't the exact internal implementation you should memorize.

The important idea is:

```text
for loop
   ↓
iter()
   ↓
next()
   ↓
next()
   ↓
next()
   ↓
StopIteration
   ↓
loop ends
```

💡 **This is the big connection.**

You've been using iterators every time you've used many ordinary `for` loops.

---

# 🤯 Aha Moment

You might have thought:

```python
for player in players:
    print(player)
```

was simply:

> "Python loops through the list."

But now we can think more precisely:

```text
for
 ↓
Get iterator
 ↓
Ask for next item
 ↓
Run loop body
 ↓
Ask for next item
 ↓
Run loop body
 ↓
...
 ↓
StopIteration
 ↓
Stop
```

That's a much deeper understanding of Python.

---

# 🧩 Which Things Are Iterable?

You've already learned many of these.

## Lists

```python
players = ["Salah", "Palmer", "Saka"]
```

Iterable? ✅

---

## Tuples

```python
scores = (10, 20, 30)
```

Iterable? ✅

---

## Strings

```python
name = "Valerian"
```

Iterable? ✅

You can iterate over:

```text
V
a
l
e
r
i
a
n
```

---

## Dictionaries

```python
player = {
    "name": "Salah",
    "goals": 20
}
```

Iterable? ✅

By default, iterating over a dictionary gives you its keys.

```python
for item in player:
    print(item)
```

Conceptually:

```text
name
goals
```

---

## Sets

```python
positions = {"GK", "DF", "MF", "FW"}
```

Iterable? ✅

---

# 🧪 Practice — Easy

## Challenge 1

Create a list:

```python
players = ["Salah", "Saka", "Palmer"]
```

Create an iterator from it.

Then use `next()` to retrieve every player one at a time.

Your goal:

```text
Salah
Saka
Palmer
```

Do **not** use a `for` loop.

---

# 🧪 Practice — Easy 2

Create:

```python
word = "Python"
```

Turn it into an iterator.

Use `next()` repeatedly to produce:

```text
P
y
t
h
o
n
```

Again:

> No `for` loop.

You're manually experiencing what iteration feels like.

---

# 🟡 Medium Practice

Create:

```python
numbers = [10, 20, 30, 40, 50]
```

Create an iterator.

Then retrieve only the first three values using:

```python
next()
```

Your program should produce:

```text
10
20
30
```

Do not retrieve the remaining values.

Then think:

> Where is the iterator now?

---

# 🟡 Medium Practice 2

Suppose:
```python
colors = ["red", "green", "blue"]
```
Create an iterator.

Call:

```python
next()
```

once.

Then call it again.

Then stop.

Answer:

What value would the iterator return if you called `next()` one more time?

---

# 🔴 Hard Practice

Consider:

```python
numbers = [1, 2, 3]
iterator = iter(numbers)
```

You then execute:

```python
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
```

### Questions:

1. What are the first three outputs?
2. What happens on the fourth call?
3. Why?
4. What exception is raised?

Don't just answer:

```text
"StopIteration."
```

Explain the **state of the iterator**.

---

# 🔴 Hard Practice 2 — Iterator State

Consider:

```python
numbers = [10, 20, 30, 40]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
```

Now imagine another piece of code receives the same iterator:

```python
other = iterator
```

Then:

```python
print(next(other))
```

### Question:

What gets printed?

And why?

---

# ⚔️ Mini Challenge — Manual Loop

Now we're going to recreate a `for` loop manually.

Given:

```python
players = ["Salah", "Saka", "Palmer"]
```

Your goal is to use:

```python
iter()
next()
```

and exception handling to print every player.

Conceptually, you're trying to reproduce:

```python
for player in players:
    print(player)
```

without actually using `for`.

Your program should eventually stop cleanly when there are no more players.

### Rules

You may use:

```text
iter()
next()
try
except
print()
```

You may NOT use:

```text
for
```

or:

```text
while
```

The challenge is to experience the iterator protocol directly.

---

# 🧠 Think About It

Why does Python use:

```text
StopIteration
```

instead of returning something like:

```text
None
```

when the iterator runs out?

Imagine your iterable contains:

```python
[10, 20, None, 40]
```

If Python used `None` to mean:

> "We're finished."

How would it distinguish that from the actual value:

```python
None
```

This is one reason an exception such as `StopIteration` is useful.

---

# 🧩 Iterable vs Iterator — Test Yourself

Which is which?

```python
players = ["Salah", "Saka", "Palmer"]

iterator = iter(players)
```

### `players`

Is it:

```text
Iterable
Iterator
Both
```

### `iterator`

Is it:

```text
Iterable
Iterator
Both
```

Think carefully.

---

# 🧠 The Deeper Detail

Here's something subtle.

An iterator is itself iterable.

That means an iterator implements both concepts:

```text
Iterable behavior
        +
Iterator behavior
```

This is why an iterator can provide:

```python
__iter__()
```

which returns itself.

And:

```python
__next__()
```

which gives the next value.

So the conceptual relationship is:

```text
Iterable
   │
   │ iter()
   ▼
Iterator
   │
   │ next()
   ▼
Value
```

And:

```text
Iterator
   ├── __iter__()
   └── __next__()
```

This becomes extremely important when we build custom iterators.

---

# 🛠️ Building Our Own Iterator

Now we're getting serious. 😎

Let's create an object that counts upward.

We want:

```text
1
2
3
4
5
```

using:

```python
next()
```

We can create a class:

```python
class Counter:
    def __init__(self, limit):
        self.current = 1
        self.limit = limit
```

So:

```python
counter = Counter(5)
```

contains:

```text
current = 1
limit = 5
```

Now we need Python to understand:

> "This object knows how to provide the next value."

We implement:

```python
__iter__()
```

and:

```python
__next__()
```

---

# 🧠 `__iter__()`

An iterator should be able to return itself when Python asks for its iterator.

That looks like:

```python
def __iter__(self):
    return self
```

So conceptually:

```text
iter(counter)
      ↓
counter
```

---

# 🧠 `__next__()`

Now we define what happens when Python asks:

```python
next(counter)
```

Conceptually:

```text
If current <= limit:

    return current

    then increase current

Otherwise:

    raise StopIteration
```

A complete example:

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

Now:

```python
counter = Counter(5)
```

We can do:

```python
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
```

Conceptually:

```text
1
2
3
4
5
```

And the next call raises:

```text
StopIteration
```

---

# 🤯 What We Just Built

We created an object that participates in Python's iterator protocol.

```text
Counter
   │
   ├── __iter__()
   │
   └── __next__()
```

And now Python can understand:

```python
for number in Counter(5):
    print(number)
```

The `for` loop can use the iterator protocol automatically.

That's pretty cool.

---

# 🧪 Practice — Build Your Own Counter

Create a class:

```python
class Countdown:
    ...
```

It should count:

```text
5
4
3
2
1
```

Then stop.

### Requirements

Your class should implement:

```python
__init__()
__iter__()
__next__()
```

You should use:

```python
StopIteration
```

when the countdown finishes.

---

# 🟡 Medium — Even Numbers Iterator

Create:

```python
class EvenNumbers:
    ...
```

It should produce:

```text
2
4
6
8
10
```

when given a limit of `10`.

For example:

```python
numbers = EvenNumbers(10)
```

Then:

```python
for number in numbers:
    print(number)
```

should produce:

```text
2
4
6
8
10
```

### Challenge

Make the limit configurable.

So:

```python
EvenNumbers(6)
```

produces:

```text
2
4
6
```

---

# 🔴 Hard — Range Iterator

Python already has:

```python
range()
```

but we're going to build a simplified version.

Create:

```python
class MyRange:
    ...
```

It should support:

```python
MyRange(5)
```

producing:

```text
0
1
2
3
4
```

Your iterator must:

* Start at `0`
* Stop before the limit
* Return one number at a time
* Raise `StopIteration` at the correct moment

---

# ⚔️ Mini Project — Player Iterator

Now let's bring this back into the Football Academy. ⚽

Imagine:

```python
players = [
    {"name": "Salah", "position": "RW"},
    {"name": "Saka", "position": "RW"},
    {"name": "Palmer", "position": "AM"},
    {"name": "Rice", "position": "CM"},
]
```

Build an iterator:

```python
class PlayerIterator:
    ...
```

It should allow you to process players one at a time.

For example:

```python
players = PlayerIterator(player_data)

for player in players:
    print(player["name"])
```

Expected:

```text
Salah
Saka
Palmer
Rice
```

### Your iterator should:

* Store the collection
* Track the current position
* Implement `__iter__()`
* Implement `__next__()`
* Raise `StopIteration` when finished

---

# 🥋 Skill Check

Try these without looking back.

## Question 1

What is the difference between:

```text
Iterable
```

and:

```text
Iterator
```

---

## Question 2

What does this do?

```python
iter(players)
```

---

## Question 3

What does this do?

```python
next(iterator)
```

---

## Question 4

What happens when an iterator has no more values?

---

## Question 5

Why does this work?

```python
for player in players:
    print(player)
```

even though you never explicitly wrote:

```python
iter()
```

or:

```python
next()
```

---

## Question 6

What are the two important methods involved in the iterator protocol?

---

## Question 7

Why does `__next__()` eventually raise:

```python
StopIteration
```

?

---

# 🧠 Explain It Like a Sensei

Without using technical jargon, explain this:

```text
Iterable
      ↓
iter()
      ↓
Iterator
      ↓
next()
      ↓
Value
      ↓
next()
      ↓
Value
      ↓
...
      ↓
StopIteration
```

If you can explain that naturally, you've got the heart of this batch.

---

# 🏗️ Project Connection

We aren't rebuilding the Football Academy yet.

But notice what just happened.

Earlier, we had:

```text
⚽ Football Academy

Players
Teams
Matches
Statistics
```

Now we've added another possible tool:

```text
PlayerIterator
```

Later, when our academy contains:

```text
10 players
100 players
10,000 players
```

we'll encounter situations where processing everything at once isn't necessarily the best approach.

That leads us toward one of the major reasons Python's iterator system matters:

```text
Data
 ↓
Process one item
 ↓
Process next item
 ↓
Process next item
 ↓
...
```

This idea becomes even more important with:

# ⚡ Generators

And generators are where iterator-based thinking becomes much more powerful.

---

# 💡 Chapter Summary

You learned:

```text
Iterable
    =
Something that can provide an iterator
```

```text
Iterator
    =
An object that produces values one at a time
```

```python
iter()
```

gets an iterator.

```python
next()
```

asks for the next value.

```text
StopIteration
```

signals that there are no more values.

And a `for` loop is built around this iterator protocol.

Conceptually:

```text
for
 ↓
iter()
 ↓
next()
 ↓
next()
 ↓
next()
 ↓
StopIteration
 ↓
Done
```

---

# 🏅 Batch Progress

```text
🟣 PART 6 — PYTHONIC FEATURES

🔁 Iterators

    ✅ Iterable vs Iterator
    ✅ iter()
    ✅ next()
    ✅ StopIteration
    ✅ Iterator protocol
    ✅ How for loops use iterators
    ✅ Custom iterators

    🥋 Practice
    🥋 Mini Challenge
    🥋 Skill Check

        ↓

⚡ NEXT BATCH

GENERATORS
```

---

# 🚦 Exit Check

Before moving on, you should be comfortable answering:

> **"What happens underneath a Python `for` loop?"**

A strong answer looks roughly like:

```text
Python obtains an iterator from the iterable,
then repeatedly asks that iterator for the next
value until the iterator raises StopIteration.
```

If that sentence makes sense rather than just sounding like Python wizardry...

# 🔓 ITERATORS — UNLOCKED

And now we're ready for the fun part.

# ⚡ Generators

Because once you understand:

```text
iter()
next()
StopIteration
```

the strange-looking:

```python
yield
```

starts making a LOT more sense.