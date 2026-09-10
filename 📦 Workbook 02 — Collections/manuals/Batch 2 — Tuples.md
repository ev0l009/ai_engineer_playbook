# 🤖 The AI Engineer Playbook
# 📦 Workbook 02 — Collections
## Batch 2 — Tuples

> *"Not everything should be editable.*
> *Some information should stay exactly as it was created."*
---

# 🎯 Learning Objectives
By the end of this batch you should be able to
✅ Create tuples
✅ Access tuple elements
✅ Understand immutability
✅ Pack and unpack tuples
✅ Return multiple values from functions
✅ Decide when to use a tuple instead of a list
---

# 🧭 Where You Are
```text
Phase 1 — Python Fluency

████████████████████░░░░ 50%

✔ Foundations
✔ Functions
🟢 Collections
    ✔ Lists
    ⏳ Tuples
⬜ Files
⬜ OOP
```
---

# 🤔 What is a Tuple?

A **tuple** is an ordered collection of items.
Just like a list...
But with one major difference.
A tuple **cannot be changed** after it is created.
Python calls this **immutable**.
---

# 🧠 Mental Model
Imagine writing a football match result.

```text
Liverpool 2 — 1 Chelsea
```

Once the match is over...
That result shouldn't suddenly become

```text
Liverpool 8 — 1 Chelsea
```

😂

It's history.
It should stay exactly the same.
That's a tuple.
---

# 📖 Creating Tuples

```python
player = ("James", 22, "CDM")
```

Tuples use

```python
(
)
```
Round brackets.

---

Another example

```python
coordinates = (7.3775, 3.9470)
```

---

# 📖 Accessing Items
Exactly like lists.

```python
player = ("James", 22, "CDM")

print(player[0])
```

Output

```text
James
```

---

Negative indexing also works.

```python
player[-1]
```

Output

```text
CDM
```

---

# 📖 Immutability

This is the biggest difference.

```python
player = ("James", 22, "CDM")

player[0] = "David"
```

Output

```text
TypeError
```

Why?

Because tuples cannot be modified.

---

# 🤔 Why Would Anyone Want This?

Great question.

Imagine storing

- GPS coordinates
- Birth dates
- RGB colours
- Database IDs
- Match results

Should these accidentally change?

Usually...

No.

Using tuples protects your data.

---

# 📖 Tuple Packing

Python automatically packs values into a tuple.

```python
player = "James", 22, "CDM"
```

Python understands

```python
("James", 22, "CDM")
```

---

# 📖 Tuple Unpacking

One of Python's nicest features.

```python
player = ("James", 22, "CDM")

name, age, position = player

print(name)
print(age)
print(position)
```

Output

```text
James

22

CDM
```

---

# 💡 Swapping Variables

Without tuples

```python
temp = a
a = b
b = temp
```

Python lets you do

```python
a, b = b, a
```

Behind the scenes...
Python uses tuple packing and unpacking.
Elegant.

---

# 📖 Returning Multiple Values

Functions can return tuples.

```python
def player_stats():

    goals = 8

    assists = 12

    return goals, assists
```

Using it

```python
goals, assists = player_stats()

print(goals)
```

Output

```text
8
```

---

# ⚽ Football Academy AI

Represent a player's basic profile.

```python
player = (
    "James",
    22,
    "CDM"
)
```

Store an academy location.

```python
academy_location = (
    6.5244,
    3.3792
)
```

Should the coordinates change every minute?

No.

A tuple makes sense.

---

# 📖 Tuple Methods

Tuples have very few methods.

```python
count()

index()
```

Example

```python
numbers = (4, 7, 7, 9)

print(numbers.count(7))
```

Output

```text
2
```

---

# 🆚 List vs Tuple

| Feature | List | Tuple |
|----------|------|-------|
| Mutable | ✅ | ❌ |
| Ordered | ✅ | ✅ |
| Indexing | ✅ | ✅ |
| Slicing | ✅ | ✅ |
| Add Items | ✅ | ❌ |
| Remove Items | ✅ | ❌ |

---

# 🐞 Debugging Lab

Predict what happens.

```python
player = (
    "James",
    22,
    "CDM"
)

player.append("Captain")
```

Question

Why does this fail?

---

Another one.

```python
numbers = (1)

print(type(numbers))
```

Is this a tuple?

No.

It's an integer.

To create a tuple with one item

```python
numbers = (1,)
```

Notice the comma.

This catches many beginners.

---

# 🏃 Practice

## Easy

1.

Create a tuple of five colours.

---

2.

Print the second colour.

---

3.

Print the last colour.

---

## Medium

Create a tuple

```python
player
```

Store

- name
- age
- position

Unpack it into three variables.

---

Write a function

```python
rectangle(length, width)
```

Return

- area
- perimeter

using one return statement.

---

## Hard

Create a function

```python
student_result()
```

Return

- average
- highest
- lowest

Unpack the returned tuple and display each value separately.

## 🎯 Mini Mission

Before we move to Dictionaries, try this:
Build a function called:

```python
match_summary(home_goals, away_goals)
```

It should return three values:

- The winner ("Home", "Away", or "Draw")
- Total goals
- Goal difference

Then unpack the returned tuple like this:

```python
winner, total_goals, goal_difference = match_summary(3, 1)
```

If you can do that comfortably, you've not only learned tuples—you've also started writing more elegant Python functions.

---

# 🤖 AI Engineer Lens

Tuples appear everywhere.

Coordinates

```python
(x, y)
```

Image size

```python
(width, height)
```

Tensor shape

```python
(batch, channels, height, width)
```

Dictionary items

```python
(key, value)
```

Multiple return values

```python
loss, accuracy
```

Even if you don't notice them...

You'll use tuples constantly.

---

# 💡 Chapter Summary

You learned

- Tuples are ordered.
- Tuples are immutable.
- Tuples support indexing and slicing.
- Packing creates tuples automatically.
- Unpacking makes code cleaner.
- Functions often return tuples.

---

# 🌱 Growth Log

Reflect before moving on.

- When would I choose a tuple instead of a list?

- Why is immutability useful?

- Can I explain tuple unpacking to someone else?

- Can I return multiple values from a function?

If your answer is **yes**, you're ready for dictionaries.

---

> 🚀 Coming Up

## 📦 Batch 3 — Dictionaries

You'll learn the collection that powers almost every real-world Python application.

Spoiler...

It might become your favorite collection.