# 🤖 The AI Engineer Playbook
# 📦 Workbook 02 — Collections
## Batch 4 — Sets

> *"Sometimes the most important information isn't what's repeated...*
> *it's what's unique."*

---

# 🎯 Learning Objectives

By the end of this batch you should be able to

✅ Create sets

✅ Add and remove items

✅ Understand uniqueness

✅ Perform set operations

✅ Check membership efficiently

✅ Know when a set is the right choice

---

# 🧭 Where You Are

```text
Phase 1 — Python Fluency

████████████████████████░ 80%

✔ Foundations
✔ Functions
🟢 Collections
    ✔ Lists
    ✔ Tuples
    ✔ Dictionaries
    ⏳ Sets
⬜ Thinking in Collections
```

---

# 🤔 What is a Set?

A **set** is an unordered collection of **unique** items.

Unlike lists...

Sets automatically remove duplicates.

---

# 🧠 Mental Model

Imagine a football tournament.

Players register.

```text
James
David
James
Musa
David
Samuel
```

The organizers only care who registered.

Not how many times.

Final registration:

```text
James
David
Musa
Samuel
```

That's a set.

---

# 📖 Creating Sets

```python
positions = {
    "GK",
    "CB",
    "CDM",
    "ST"
}
```

---

You can also create a set from a list.

```python
numbers = [1,2,2,3,3,3,4]

unique = set(numbers)

print(unique)
```

Output

```text
{1, 2, 3, 4}
```

Duplicates disappear automatically.

---

# 📖 Empty Sets

This catches beginners.

```python
empty = {}
```

This is **NOT** a set.

It's an empty dictionary.

Correct way:

```python
empty = set()
```

---

# 📖 Sets Are Unordered

```python
players = {
    "James",
    "David",
    "Musa"
}

print(players)
```

The order isn't guaranteed.

Don't expect

```text
James
David
Musa
```

every time.

---

# 📖 Adding Items

```python
players.add("Samuel")
```

---

Adding an existing value

```python
players.add("James")
```

Nothing happens.

Sets don't allow duplicates.

---

# 📖 Removing Items

```python
players.remove("David")
```

If the value doesn't exist...

Python raises a `KeyError`.

---

Safer option

```python
players.discard("David")
```

If it isn't present...

Nothing happens.

---

# 📖 Membership

```python
if "James" in players:
    print("Found")
```

Membership checks with sets are typically very fast.

---

# 📖 Set Operations

Suppose two football teams train together.

```python
team_a = {"James", "David", "Musa"}

team_b = {"David", "Samuel", "Musa"}
```

---

## Union

Everyone involved.

```python
team_a | team_b
```

Result

```text
{"James", "David", "Musa", "Samuel"}
```

---

## Intersection

Who appears in both teams?

```python
team_a & team_b
```

Result

```text
{"David", "Musa"}
```

---

## Difference

Who is only in Team A?

```python
team_a - team_b
```

Result

```text
{"James"}
```

---

## Symmetric Difference

Who appears in exactly one team?

```python
team_a ^ team_b
```

Result

```text
{"James", "Samuel"}
```

---

# ⚽ Football Academy AI

Track all positions in your academy.

```python
positions = {
    "GK",
    "CB",
    "LB",
    "RB",
    "CDM",
    "CM",
    "CAM",
    "LW",
    "RW",
    "ST"
}
```

Suppose players choose positions.

A set guarantees you don't accidentally store

```text
CDM
CDM
CDM
```

three times.

---

# 🐞 Debugging Lab

Predict the output.

```python
numbers = {1,2,2,3,3,4}

print(numbers)
```

Why doesn't it print six numbers?

---

Another one.

```python
players = {"James"}

print(players[0])
```

Why does this fail?

Because sets **do not support indexing**.

They are unordered.

---

# 🏃 Practice

## Easy

1.

Create a set of five colours.

---

2.

Add another colour.

---

3.

Remove one colour.

---

4.

Check if `"Blue"` exists.

---

## Medium

Create a list

```python
scores = [4,5,5,6,7,7,8,8]
```

Convert it into a set.

Print the result.

---

Create two sets of football players.

Display

- Union
- Intersection
- Difference

---

## Hard

Create a football registration system.

Allow users to

- Register players
- Prevent duplicate registrations
- Display all registered players

Use a **set**.

---

# 🤖 AI Engineer Lens

Sets are useful in AI for tasks like

Removing duplicate labels

```python
labels = {
    "Cat",
    "Dog",
    "Bird"
}
```

Finding unique words in text

```python
unique_words = set(words)
```

Comparing datasets

Checking whether an item has already been processed

Although you'll use lists and dictionaries more often, sets are invaluable whenever **uniqueness** matters.

---

# 🆚 List vs Tuple vs Dictionary vs Set

| Feature | List | Tuple | Dictionary | Set |
|---------|------|--------|------------|-----|
| Ordered | ✅ | ✅ | ✅* | ❌ |
| Mutable | ✅ | ❌ | ✅ | ✅ |
| Indexing | ✅ | ✅ | By key | ❌ |
| Duplicate Values | ✅ | ✅ | Keys: ❌ Values: ✅ | ❌ |
| Best Use | Sequence | Fixed data | Labeled data | Unique data |

\* Dictionaries preserve insertion order in modern Python, but values are still accessed by **key**, not by position.

---

# 💡 Chapter Summary

You learned

- Sets store unique items.
- Sets are unordered.
- Sets do not support indexing.
- Sets automatically remove duplicates.
- Set operations model real-world relationships.
- Membership testing is a common use case.

---

# 🌱 Growth Log

Reflect before moving on.

- When would I choose a set instead of a list?

- Why can't sets use indexes?

- Which set operation feels most intuitive?

- Could I remove duplicates from a list without writing a loop?

If your answer is **yes**, you're ready for the final batch.

---

> 🚀 Coming Up

## 🧠 Batch 5 — Thinking in Collections

This is where everything comes together.

You'll stop thinking:

> "How do I use a list?"

and start thinking:

> "Which collection solves this problem best?"