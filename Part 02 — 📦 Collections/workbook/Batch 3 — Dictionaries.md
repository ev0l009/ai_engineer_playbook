# 🤖 The AI Engineer Playbook
# 📦 Workbook 02 — Collections
## Batch 3 — Dictionaries

> *"Good programmers don't just store data.*
> *They give it meaning."*

---

# 🎯 Learning Objectives

By the end of this batch you should be able to

✅ Create dictionaries

✅ Access values using keys

✅ Add and update data

✅ Remove items

✅ Iterate through dictionaries

✅ Work with nested dictionaries

✅ Know when a dictionary is the right choice

---

# 🧭 Where You Are

```text
Phase 1 — Python Fluency

██████████████████████░░ 60%

✔ Foundations
✔ Functions
🟢 Collections
    ✔ Lists
    ✔ Tuples
    ⏳ Dictionaries
⬜ Files
⬜ OOP
```

---

# 🤔 What is a Dictionary?

A **dictionary** stores information as **key-value pairs**.

Think of a real dictionary.

You don't open it and read every page.

You search for a **word**.

Python dictionaries work the same way.

```text
Key  --------->  Value

"name" -------> "James"

"age" --------> 22

"position" ---> "CDM"
```

---

# 🧠 Mental Model

Imagine every football player has an ID card.

```text
------------------------

Name: James

Age: 22

Position: CDM

Goals: 8

Assists: 12

------------------------
```

Each label is a **key**.

The information beside it is the **value**.

---

# 📖 Creating Dictionaries

```python
player = {
    "name": "James",
    "age": 22,
    "position": "CDM"
}
```

Dictionaries use

```python
{
}
```

Curly braces.

---

# 📖 Accessing Values

Use the key.

```python
print(player["name"])
```

Output

```text
James
```

---

Another example

```python
print(player["position"])
```

Output

```text
CDM
```

---

# 📖 Adding New Data

```python
player["goals"] = 8
```

Now the dictionary becomes

```python
{
    "name": "James",
    "age": 22,
    "position": "CDM",
    "goals": 8
}
```

---

# 📖 Updating Values

```python
player["age"] = 23
```

Simple.

---

# 📖 Removing Items

By key

```python
del player["age"]
```

---

Or

```python
player.pop("position")
```

---

# 📖 Membership

```python
if "goals" in player:
    print("Found")
```

Notice

We're checking for **keys**, not values.

---

# 📖 Useful Methods

## Keys

```python
player.keys()
```

Returns

```text
name

age

position
```

---

## Values

```python
player.values()
```

Returns

```text
James

22

CDM
```

---

## Items

```python
player.items()
```

Returns

```text
("name", "James")

("age", 22)

("position", "CDM")
```

Very useful for loops.

---

# 📖 Looping Through Dictionaries

Keys

```python
for key in player:
    print(key)
```

---

Values

```python
for value in player.values():
    print(value)
```

---

Keys and Values

```python
for key, value in player.items():
    print(key, value)
```

Output

```text
name James

age 22

position CDM
```

---

# 📖 Nested Dictionaries

Dictionaries can contain dictionaries.

```python
academy = {

    "James": {

        "position": "GK",

        "goals": 0

    },

    "David": {

        "position": "CB",

        "goals": 2

    }

}
```

Access

```python
academy["James"]["position"]
```

Output

```text
GK
```

---

# ⚽ Football Academy AI

Instead of

```python
player = (
    "James",
    22,
    "CDM"
)
```

You now have

```python
player = {
    "name": "James",
    "age": 22,
    "position": "CDM",
    "goals": 8,
    "assists": 12
}
```

Which version is easier to understand six months from now?

Exactly.

---

# 🐞 Debugging Lab

What happens?

```python
player = {
    "name": "James"
}

print(player["age"])
```

Output?

```text
KeyError
```

Why?

Because `"age"` doesn't exist.

Safer approach

```python
print(player.get("age"))
```

This returns `None` instead of raising an error.

You can also provide a default value:

```python
print(player.get("age", "Unknown"))
```

Output

```text
Unknown
```

---

# 🏃 Practice

## Easy

1.

Create a dictionary describing your favorite football player.

Include

- name
- club
- position

---

2.

Print the player's name.

---

3.

Add the player's jersey number.

---

## Medium

Create

```python
book
```

Store

- title
- author
- pages
- year

Print every key and value.

---

Create

```python
student
```

Update the student's score.

---

## Hard

Create a football academy.

Each player should be stored as a dictionary.

Store all players inside another dictionary.

Display every player's

- name
- position
- goals

using loops.

---

# 🤖 AI Engineer Lens

Dictionaries are everywhere in AI.

Model configuration

```python
config = {
    "learning_rate": 0.001,
    "epochs": 20,
    "batch_size": 32
}
```

Dataset records

```python
sample = {
    "image": image,
    "label": "Cat"
}
```

API responses

```python
{
    "prediction": "Dog",
    "confidence": 0.98
}
```

JSON data is essentially a dictionary.

Master dictionaries...

and you'll be comfortable reading a huge amount of Python code.

---

# 💡 Chapter Summary

You learned

- Dictionaries store key-value pairs.
- Keys are used to access values.
- Dictionaries are mutable.
- `.keys()`, `.values()`, and `.items()` are essential tools.
- Nested dictionaries model complex data.
- `.get()` helps avoid `KeyError`.

---

# 🌱 Growth Log

Reflect before moving on.

- Why is a dictionary better than a tuple for storing player details?

- When should I use `.get()` instead of square brackets?

- Can I loop through both keys and values?

- Could I model a football academy with nested dictionaries?

If your answer is **yes**, you're ready for the final collection.

---

> 🚀 Coming Up

## 📦 Batch 4 — Sets

You'll discover the collection that automatically removes duplicates and makes searching for unique values incredibly efficient.