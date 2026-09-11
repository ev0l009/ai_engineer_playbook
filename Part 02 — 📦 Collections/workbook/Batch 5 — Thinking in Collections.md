# 🤖 The AI Engineer Playbook
# 📦 Workbook 02 — Collections
## Batch 5 — Thinking in Collections

> *"Great programmers don't memorize collections.*
> *They choose the right one."*

---

# 🎯 Mission

After this chapter, someone should be able to describe a problem...

…and you should immediately have an idea of which collection fits best.

This is exactly how experienced developers think.

---

# 🧠 Mental Model

Think of collections as different kinds of storage.

```text
            📦 Collections

          ┌───────────────┐
          │     List      │
          └───────────────┘
               Ordered
               Editable
             Duplicate OK

                     │

                     ▼

          ┌───────────────┐
          │     Tuple     │
          └───────────────┘
              Ordered
             NOT Editable

                     │

                     ▼

          ┌───────────────┐
          │  Dictionary   │
          └───────────────┘
             Key → Value

                     │

                     ▼

          ┌───────────────┐
          │      Set      │
          └───────────────┘
          Unique Values
           No Duplicates
```

Each one exists because it solves a different problem.

---

# 📋 Decision Tree

Ask yourself four questions.

## 1.

Do I need labels?

```text
Yes
```

↓

Use a

# Dictionary

Example

```python
player = {
    "name": "James",
    "position": "CDM",
    "goals": 8
}
```

---

## 2.

Do I need duplicates?

```text
Yes
```

↓

List

Example

```python
scores = [2,2,3,5]
```

---

## 3.

Must the data never change?

```text
Yes
```

↓

Tuple

Example

```python
coordinates = (
    6.5244,
    3.3792
)
```

---

## 4.

Do I only care about unique values?

↓

Set

Example

```python
positions = {
    "GK",
    "CB",
    "CDM"
}
```

---

# ⚽ Football Examples

## Squad

```python
players = [
    "James",
    "David",
    "Musa"
]
```

List

Why?

Players join.

Players leave.

---

## Academy Coordinates

```python
location = (
    6.5244,
    3.3792
)
```

Tuple

Why?

Coordinates don't change.

---

## Player Information

```python
player = {
    "name":"James",
    "age":22,
    "position":"CDM"
}
```

Dictionary

Why?

Every value has a label.

---

## Registered Jersey Numbers

```python
numbers = {
    4,
    7,
    8,
    10
}
```

Set

Why?

No duplicates allowed.

---

# 🤖 AI Examples

Training images

```python
images = [...]
```

↓

List

---

Image dimensions

```python
(height, width)
```

↓

Tuple

---

Model configuration

```python
config = {
    "epochs":20,
    "batch_size":32,
    "learning_rate":0.001
}
```

↓

Dictionary

---

Unique labels

```python
labels = {
    "Cat",
    "Dog",
    "Bird"
}
```

↓

Set

---

# 🚨 Common Beginner Mistakes

## Mistake 1

Using a list for everything.

```python
player = [
    "James",
    22,
    "CDM",
    8
]
```

Six months later...

```python
player[2]
```

What was index 2 again?

🤔

Use a dictionary.

---

## Mistake 2

Trying to change tuples.

```python
player[0] = "David"
```

❌

---

## Mistake 3

Indexing sets.

```python
players[0]
```

❌

Sets are unordered.

---

## Mistake 4

Using a dictionary when labels don't matter.

```python
numbers = {
    0:10,
    1:20,
    2:30
}
```

Just use a list.

---

# 🧠 Quick Decision Quiz

What would you choose?

---

A football squad?

↓

List

---

A player's profile?

↓

Dictionary

---

GPS coordinates?

↓

Tuple

---

Unique positions?

↓

Set

---

A shopping cart?

↓

List

---

An API response?

↓

Dictionary

---

RGB colour?

↓

Tuple

---

Unique hashtags?

↓

Set

---

# ⚔️ Boss Fight

Create a Football Academy System.

Requirements

Store

Academy Name

↓

String

---

Academy Location

↓

Tuple

---

Players

↓

List

---

Each Player

↓

Dictionary

---

Available Positions

↓

Set

---

Functions

- Add Player
- Remove Player
- Find Player
- Display Squad
- Count Players
- Show Available Positions

Everything you've learned in Functions and Collections comes together here.

---

# 🤖 AI Engineer Lens

Most AI projects combine collections.

Example

```python
dataset = [

    {
        "image":"cat01.jpg",
        "label":"Cat"
    },

    {
        "image":"dog02.jpg",
        "label":"Dog"
    }

]
```

Notice

Dataset

↓

List

Each record

↓

Dictionary

Unique labels

↓

Set

Image size

↓

Tuple

That's not a coincidence.

That's exactly how engineers think.

---

# 📄 Collections Cheatsheet

| Need | Use |
|------|------|
| Ordered editable sequence | List |
| Ordered fixed sequence | Tuple |
| Labelled information | Dictionary |
| Unique values | Set |

---

# 🥋 Collections Skill Check

I can...

✅ Create all four collections

✅ Access data correctly

✅ Modify mutable collections

✅ Explain immutability

✅ Use key-value pairs

✅ Remove duplicates

✅ Choose the correct collection

---

# 🌱 Growth Log

Reflect honestly.

- Which collection feels most natural?

- Which one challenged me most?

- Could I explain the difference between all four without notes?

- Could I redesign one of my previous Python projects using better collections?

If yes...

Congratulations.

You've graduated from the Collections Workbook.

---

# 🏅 Badge Unlocked

📦 Collection Architect

You now know how professional Python developers organize information.

That's a huge milestone.

---

# 🚀 Next Workbook

📁 Files & Modules

You'll finally make your programs remember things even after they close.

No more losing data every time the script stops.

Your Football Academy AI is about to become a real application.