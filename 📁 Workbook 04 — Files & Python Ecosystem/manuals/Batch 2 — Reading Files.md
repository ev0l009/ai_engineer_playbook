# 🤖 The AI Engineer Playbook
# 📁 Workbook 04 — Files & Python Ecosystem
## Batch 2 — Reading Files

> *"Every AI model, game, and application begins by reading data."*

---

# 🎯 Learning Objectives

By the end of this batch you should be able to

✅ Open a file

✅ Read an entire file

✅ Read one line at a time

✅ Read all lines into a list

✅ Understand the file cursor

✅ Close files properly

---

# 🧭 Where You Are

```text
🤖 AI Engineer Playbook

Phase 1 — Python Fluency

████████████████████████████████████████████░ 93%

✅ Foundations
✅ Functions
✅ Collections
✅ Object-Oriented Programming

🟢 Files & Python Ecosystem

    ✅ Thinking in Files
    ⏳ Reading Files
    ⬜ Writing Files
    ⬜ Context Managers
    ⬜ Modules & Imports
    ⬜ Packages
```

---

# 📄 Our Example File

Suppose we have a file called

```text
players.txt
```

Contents

```text
James
David
Samuel
Musa
```

That's it.

Just plain text.

---

# 🏗 Opening a File

Python uses

```python
open()
```

Example

```python
file = open("players.txt", "r")
```

Let's break it down.

```python
open(...)
```

↓

Open a file.

---

```python
"players.txt"
```

↓

The file name (or path).

---

```python
"r"
```

↓

Read mode.

We only want to read.

Not modify.

---

The variable

```python
file
```

now represents the opened file.

Think of it like opening a book.

You now have access to its pages.

---

# 📖 Reading Everything

To read the whole file:

```python
file = open("players.txt", "r")

content = file.read()

print(content)

file.close()
```

Output

```text
James
David
Samuel
Musa
```

---

# 🧠 Why `close()`?

Imagine borrowing a library book.

You should return it.

Similarly,

```python
file.close()
```

tells Python

"I'm done with this file."

We'll soon learn a better way.

---

# 📄 Reading One Line

Sometimes a whole file is too much.

Use

```python
readline()
```

Example

```python
file = open("players.txt", "r")

print(file.readline())
```

Output

```text
James
```

Call it again.

```python
print(file.readline())
```

Output

```text
David
```

Again.

```text
Samuel
```

Again.

```text
Musa
```

---

# 🤯 The File Cursor

Imagine your finger following a book.

```text
James
^

Read line

↓

David
^

Read line

↓

Samuel
^

Read line

↓

Musa
```

Python remembers where it stopped.

That remembered position is called the **file cursor**.

---

# 📚 Reading All Lines

Instead of one string,

you can get a list.

```python
file = open("players.txt", "r")

lines = file.readlines()

print(lines)
```

Output

```python
[
    "James\n",
    "David\n",
    "Samuel\n",
    "Musa\n"
]
```

Notice the

```text
\n
```

That's the newline character.

It marks the end of each line.

---

# 🧹 Removing `\n`

Use

```python
strip()
```

Example

```python
for line in lines:

    print(line.strip())
```

Output

```text
James
David
Samuel
Musa
```

Much cleaner.

---

# 📖 Reading Line by Line

Instead of using `readlines()`, you can iterate directly over the file.

```python
file = open("players.txt", "r")

for line in file:
    print(line.strip())

file.close()
```

This is memory-efficient because Python reads one line at a time instead of loading the whole file into memory.

---

# 🚨 Common Beginner Mistakes

## Forgetting to Close

```python
file = open("players.txt")
```

No

```python
close()
```

Not ideal.

---

## Wrong File Name

```python
open("player.txt")
```

But the file is actually

```text
players.txt
```

Result

```text
FileNotFoundError
```

---

## Reading Twice

```python
print(file.read())

print(file.read())
```

Output

```text
James
David
Samuel
Musa
```

Then...

```text

```

(Empty!)

Why?

Because the cursor is already at the end of the file.

---

# 🧠 Resetting the Cursor

Use

```python
seek()
```

Example

```python
file.seek(0)
```

This moves the cursor back to the beginning.

Now you can read the file again.

---

# ⚽ Football Academy AI

Suppose

```text
players.txt
```

contains

```text
James
David
Samuel
```

Reading it

```python
file = open("players.txt", "r")

for player in file:
    print(player.strip())

file.close()
```

Output

```text
James
David
Samuel
```

Imagine replacing `print()` with

```python
academy.add_player(...)
```

You've just loaded your academy from disk.

---

# 🤖 AI Engineer Lens

Almost every AI project starts like this.

```python
file = open("train.csv", "r")
```

or

```python
with open("config.json") as file:
```

Before a model can learn...

It must read data.

---

# 🐞 Debugging Lab

Predict the output.

```python
file = open("players.txt")

print(file.readline())

print(file.readline())
```

If the file contains

```text
James
David
```

Output?

```text
James
David
```

---

Another one.

```python
file = open("players.txt")

print(file.read())

print(file.readline())
```

Why is the second output empty?

Because `read()` already moved the cursor to the end.

---

# 🏃 Practice

## Easy

Create

```text
fruits.txt
```

Contents

```text
Apple
Banana
Orange
```

Read the whole file.

---

## Medium

Read the file one line at a time.

Print each fruit.

---

## Hard

Create

```text
academy.txt
```

Contents

```text
James
David
Samuel
Musa
```

Read the file.

Store each name in a list.

Print the list.

---

# 💡 Chapter Summary

You learned

- `open()` opens files.
- `"r"` means read mode.
- `read()` reads everything.
- `readline()` reads one line.
- `readlines()` returns a list.
- The file cursor tracks your reading position.
- `seek(0)` resets the cursor.
- `close()` releases the file.

---

# Experiment...
file.read()

file.readline()

file.readlines()

for line in file:
  print(line.strip())

Know and understand their differences.

# 🌱 Growth Log

Reflect honestly.

- When should I use `read()` instead of `readline()`?

- Why does `read()` followed by another `read()` return an empty string?

- What does `strip()` remove?

- Why is iterating over the file often better than `readlines()` for large files?

If yes...

You're ready to write to files.

---

> 🚀 Coming Up

## ✍️ Batch 3 — Writing Files

You'll learn how to create new files, overwrite existing ones, append new data, and finally save your Football Academy AI permanently.