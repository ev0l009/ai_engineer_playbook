# 🤖 The AI Engineer Playbook
## 📦 Workbook 02 — Collections
### Batch 1 — Lists

> *"Programs don't just solve problems.*
> *They organize information."*

---

## 🎯 Learning Objectives

By the end of this batch you should be able to

✅ Create lists

✅ Access elements using indexes

✅ Modify lists

✅ Add and remove items

✅ Slice lists

✅ Understand mutability

✅ Work with nested lists

✅ Choose when a list is the right collection

---

# 🧭 Where You Are

```text
Phase 1 — Python Fluency

██████████████████░░░░░░ 45%

✔ Foundations
✔ Functions
🟢 Collections
⬜ Files
⬜ OOP
```

---

# 🤔 What is a List?

A **list** is an ordered collection of items.

Think of it like a football team's squad list.

```text
1. Goalkeeper

2. Left Back

3. Center Back

4. Right Back

...
```

Each player has a position in the list.

Python calls that position an **index**.

---

# 🧠 Mental Model

Imagine a train.

```text
+---------+---------+---------+---------+

| James   | David   | Musa    | Ibrahim |

+---------+---------+---------+---------+

     0         1         2         3
```

Every carriage has a number.

Python uses those numbers to find data.

---

# 📖 Creating Lists

```python
players = ["James", "David", "Musa"]
```

Lists use

```python
[
]
```

Square brackets.

---

Lists can store almost anything.

```python
numbers = [5, 9, 13]

names = ["Ada", "Grace"]

mixed = [5, "Hello", True, 3.14]
```

Although Python allows mixed types...

Most good programs keep lists consistent.

---

# 📖 Accessing Items

```python
players = ["James", "David", "Musa"]

print(players[0])
```

Output

```text
James
```

Remember

Python starts counting from **zero**.

```text
James     David     Musa

 0          1         2
```

---

# 📖 Negative Indexing

Python can count backwards.

```python
players[-1]
```

returns

```text
Musa
```

```text
James     David     Musa

-3         -2        -1
```

Very useful when you need the last item.

---

# 📖 Changing Items

Lists are **mutable**.

That means they can change.

```python
players = ["James", "David", "Musa"]

players[1] = "Samuel"

print(players)
```

Output

```text
['James', 'Samuel', 'Musa']
```

---

# 📖 Adding Items

Add to the end.

```python
players.append("Daniel")
```

Result

```text
['James', 'David', 'Musa', 'Daniel']
```

---

Insert at a position.

```python
players.insert(1, "Victor")
```

Result

```text
['James', 'Victor', 'David', 'Musa']
```

---

# 📖 Removing Items

Remove by value.

```python
players.remove("David")
```

---

Remove by position.

```python
players.pop()
```

Removes the last item.

Or

```python
players.pop(1)
```

Removes index 1.

---

Delete completely.

```python
del players[0]
```

---

# 📖 Length

```python
len(players)
```

Returns

```text
3
```

---

# 📖 Membership

```python
if "James" in players:
    print("Found")
```

Output

```text
Found
```

---

# 📖 Slicing

Take part of a list.

```python
numbers = [10,20,30,40,50]
```

```python
numbers[1:4]
```

Output

```text
[20,30,40]
```

Remember

The end index is **not included**.

Think

```text
start ≤ index < end
```

---

Examples

```python
numbers[:3]

numbers[2:]

numbers[:]

numbers[-3:]
```

Practice predicting each output before running it.

---

# 📖 Nested Lists

Lists can contain other lists.

```python
academy = [

    ["James", "GK"],

    ["David", "CB"],

    ["Musa", "CDM"]

]
```

Access

```python
academy[2][1]
```

Output

```text
CDM
```

---

# ⚽ Football Academy AI

Store your first squad.

```python
players = [
    "James",
    "David",
    "Musa",
    "Ibrahim",
    "Samuel"
]
```

Write functions that

- show all players
- add a player
- remove a player
- count players

Notice something?

You're combining **Functions** with **Lists**.

That's how real learning works.

---

# 🐞 Debugging Lab

What's wrong?

```python
players = [
    "James",
    "David",
    "Musa"
]

print(players[3])
```

Question

Why does this fail?

How would you fix it?

---

# 🏃 Practice

## Easy

1. Create a list of five favourite foods.
2. Print the first item.
3. Print the last item.
4. Replace one item.
5. Add another item.
---

## Medium

Create

```python
top_scorers
```

Add ten players.

Remove two.

Print the final list.

---

Create a shopping list.

Allow users to

- add
- remove
- display

using functions.

---

## Hard

Create a squad manager.

Menu

```text
1 Add Player

2 Remove Player

3 Show Squad

4 Count Players

5 Exit
```

Everything must use functions.

---

# 🤖 AI Engineer Lens

Lists appear everywhere in AI.

Examples

Training data

```python
images = [...]
```

Predictions

```python
predictions = [...]
```

Labels

```python
labels = [...]
```

Mini-batches

```python
batch = images[:32]
```

Even when using NumPy or PyTorch, you'll often start with Python lists.

---

# 💡 Chapter Summary

You learned

- Lists are ordered.
- Lists are mutable.
- Python starts indexing at zero.
- Negative indexes count backwards.
- Slicing extracts part of a list.
- Lists can contain other lists.

---

# 🌱 Growth Log

Reflect before moving on.

- What felt easiest today?

- Which list method do I think I'll use the most?

- Can I explain why Python starts at index 0?

- Could I build a simple contact list using only functions and lists?

If your answer is **yes**, you're ready for Batch 2.

---

> 🚀 Coming Up

## 📦 Batch 2 — Tuples

You'll discover why Python has another collection that looks almost identical to a list... but behaves very differently.