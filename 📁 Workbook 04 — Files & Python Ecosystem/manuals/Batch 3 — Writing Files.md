# 🤖 The AI Engineer Playbook
# 📁 Workbook 04 — Files & Python Ecosystem
## Batch 3 — Writing Files

> *"Reading lets your program learn. Writing lets your program remember."*

---

# 🎯 Learning Objectives

By the end of this batch you should be able to

✅ Create new files

✅ Write text to files

✅ Append new information

✅ Understand file modes

✅ Know when data is overwritten

---

# 🧭 Where You Are

```text
🤖 AI Engineer Playbook

Phase 1 — Python Fluency

█████████████████████████████████████████████░ 94%

✅ Foundations
✅ Functions
✅ Collections
✅ Object-Oriented Programming

🟢 Files & Python Ecosystem

    ✅ Thinking in Files
    ✅ Reading Files
    ⏳ Writing Files
    ⬜ Context Managers
    ⬜ Modules & Imports
    ⬜ Packages
```

---

# ✍️ Opening a File for Writing

Instead of

```python
"r"
```

we use

```python
"w"
```

Example

```python
file = open("players.txt", "w")
```

The `"w"` means

> Open this file for writing.

---

# 🚨 The Important Rule

If the file already exists...

```python
open("players.txt", "w")
```

will erase everything inside it.

Think of it like opening a notebook and replacing every page with a blank one.

---

# ✍️ Writing Text

Use

```python
write()
```

Example

```python
file = open("players.txt", "w")

file.write("James")

file.close()
```

Contents

```text
James
```

---

# Writing Multiple Lines

```python
file = open("players.txt", "w")

file.write("James\n")
file.write("David\n")
file.write("Samuel\n")

file.close()
```

Contents

```text
James
David
Samuel
```

Notice the

```text
\n
```

Without it...

everything appears on one line.

---

# 🤔 Why Doesn't `write()` Add New Lines?

Because Python writes exactly what you tell it to write.

If you don't include

```text
\n
```

Python won't invent it.

---

# 📝 `writelines()`

You can also write a collection of strings.

```python
players = [

    "James\n",

    "David\n",

    "Samuel\n"
]

file = open("players.txt", "w")

file.writelines(players)

file.close()
```

Output

```text
James
David
Samuel
```

---

# ➕ Append Mode

Sometimes you don't want to erase the file.

You only want to add more.

Use

```python
"a"
```

Example

```python
file = open("players.txt", "a")

file.write("Musa\n")

file.close()
```

Now the file becomes

```text
James
David
Samuel
Musa
```

Nothing was erased.

---

# 🧠 File Modes

| Mode | Meaning |
|------|---------|
| `"r"` | Read only |
| `"w"` | Write (overwrite) |
| `"a"` | Append |
| `"r+"` | Read and write |

For now...

You'll mostly use

- `"r"`
- `"w"`
- `"a"`

---

# ⚽ Football Academy AI

Imagine signing a new player.

```python
file = open("academy.txt", "a")

file.write("Adebayo\n")

file.close()
```

Tomorrow

the player is still there.

That's persistence.

---

# 🐞 Common Beginner Mistakes

## Forgetting the Newline

```python
file.write("James")
file.write("David")
```

Output

```text
JamesDavid
```

---

## Accidentally Using `"w"`

Suppose the file contains

```text
James
David
Samuel
```

You run

```python
file = open("players.txt", "w")

file.write("Musa")
```

Now the file contains only

```text
Musa
```

Everything else is gone.

---

## Forgetting to Close

```python
file = open(...)

file.write(...)
```

No

```python
close()
```

Not recommended.

---

# 🧠 Combining Reading and Writing

A common workflow

```text
Read Players

↓

Modify List

↓

Write Updated List
```

That's exactly what many real applications do.

---

# 🤖 AI Engineer Lens

Machine learning often saves results to files.

Examples

```python
predictions.txt

metrics.csv

results.json

training.log
```

Writing files is just as important as reading them.

---

# 🏃 Practice

## Easy

Create

```text
notes.txt
```

Write

```text
Learning Python is fun!
```

---

## Medium

Create

```text
shopping.txt
```

Write

```text
Rice
Beans
Milk
```

Append

```text
Bread
```

Read the file afterwards to verify the result.

---

## Hard

Create

```text
academy.txt
```

Write four player names.

Read them back into a list.

Append one new player.

Read again.

Print the updated list.

---

# ⚔️ Mini Project

Build a simple

```text
Player Registration System
```

Menu

```text
1. Register Player

2. Show Players

3. Exit
```

Registering a player should

↓

Append to

```text
academy.txt
```

Showing players should

↓

Read the file

↓

Print every player.

Congratulations.

You've just built persistent storage.

---

# 💡 Chapter Summary

You learned

- `"w"` overwrites files.
- `"a"` appends data.
- `write()` writes strings.
- `writelines()` writes multiple strings.
- Newlines must be added manually.
- Reading and writing are often used together.

---

# 🌱 Growth Log

Reflect honestly.

- When should I use `"a"` instead of `"w"`?

- Why is `\n` important when writing text?

- What would happen if I accidentally opened an important file with `"w"`?

If yes...

You're ready for one of Python's nicest features.

---

> 🚀 Coming Up

## 🛡️ Batch 4 — Context Managers (`with`)

You'll finally understand why almost every experienced Python developer writes

```python
with open(...) as file:
```

instead of manually calling `close()`.