# 🤖 The AI Engineer Playbook
# 📁 Workbook 04 — Files & Python Ecosystem
## Batch 4 — Context Managers (`with`)

> *"Good programmers close files. Great programmers make sure they always close."*

---

# 🎯 Learning Objectives

By the end of this batch you should be able to

✅ Explain what a context manager is

✅ Use the `with` statement

✅ Understand why `with` is safer than manually calling `close()`

✅ Write cleaner, more Pythonic file-handling code

---

# 🧭 Where You Are

```text
🤖 AI Engineer Playbook

Phase 1 — Python Fluency

██████████████████████████████████████████████░ 96%

✅ Foundations
✅ Functions
✅ Collections
✅ Object-Oriented Programming

🟢 Files & Python Ecosystem

    ✅ Thinking in Files
    ✅ Reading Files
    ✅ Writing Files
    ⏳ Context Managers
    ⬜ Modules & Imports
    ⬜ Packages
```

---

# 🤔 The Problem

So far we've written code like this.

```python
file = open("players.txt", "r")

content = file.read()

print(content)

file.close()
```

Works perfectly.

Until...

Something goes wrong.

---

# 🚨 Imagine This

```python
file = open("players.txt", "r")

content = file.read()

print(10 / 0)

file.close()
```

What happens?

Python stops here.

```python
print(10 / 0)
```

with

```text
ZeroDivisionError
```

The program crashes.

`file.close()` is never reached.

The file stays open longer than intended.

---

# 🛡️ The Better Way

Python gives us

```python
with
```

Example

```python
with open("players.txt", "r") as file:

    content = file.read()

    print(content)
```

Notice something?

No

```python
file.close()
```

Python closes the file automatically.

Even if an error occurs.

---

# 🧠 What Does `with` Mean?

Think of borrowing a library book.

Without `with`

```text
Borrow Book

↓

Read Book

↓

Remember to Return Book
```

You might forget.

---

With `with`

```text
Borrow Book

↓

Read Book

↓

Library Automatically Takes It Back
```

No forgetting.

---

# 🧩 Breaking It Down

```python
with open("players.txt", "r") as file:
```

Let's read it from left to right.

---

### `with`

"I'm entering a managed block."

---

### `open(...)`

Open the file.

---

### `as`

Store the opened file in a variable.

---

### `file`

The variable you'll use inside the block.

---

### `:`

Everything indented below belongs to this context.

When the block ends...

The file is automatically closed.

---

# 📖 Reading with `with`

```python
with open("players.txt", "r") as file:

    print(file.read())
```

Done.

No manual cleanup needed.

---

# ✍️ Writing with `with`

```python
with open("notes.txt", "w") as file:

    file.write("Learning Python!")
```

File closes automatically.

---

# ➕ Appending with `with`

```python
with open("players.txt", "a") as file:

    file.write("Adebayo\n")
```

Exactly the same idea.

---

# 🧠 Scope Reminder

Notice this.

```python
with open("players.txt") as file:

    content = file.read()

print(content)
```

This works because `content` was created outside the file object itself.

But this...

```python
print(file.read())
```

outside the `with` block is a problem.

The file has already been closed.

---

# ⚽ Football Academy AI

Loading players

```python
with open("academy.txt", "r") as file:

    for player in file:

        print(player.strip())
```

Saving a new player

```python
with open("academy.txt", "a") as file:

    file.write("James\n")
```

Simple.

Clean.

Safe.

---

# 🤖 AI Engineer Lens

You'll see `with` everywhere.

Examples:

```python
with open(...)
```

```python
with sqlite3.connect(...)
```

```python
with requests.Session() as session:
```

```python
with lock:
```

It's much bigger than files.

It's Python's way of saying:

> "I'll clean this up automatically."

---

# 🐞 Common Beginner Mistakes

## Forgetting the Colon

Wrong

```python
with open("players.txt", "r") as file
```

Correct

```python
with open("players.txt", "r") as file:
```

---

## Bad Indentation

Wrong

```python
with open("players.txt") as file:

print(file.read())
```

Correct

```python
with open("players.txt") as file:

    print(file.read())
```

---

## Using the File Afterwards

```python
with open("players.txt") as file:

    pass

file.read()
```

The file has already been closed.

---

# 🏃 Practice

## Easy

Read

```text
notes.txt
```

using `with`.

Print the contents.

---

## Medium

Create

```text
journal.txt
```

Write three lines using `with`.

Read them back.

---

## Hard

Create

```text
academy.txt
```

Append two new players using `with`.

Read the file.

Print every player.

---

# ⚔️ Mini Project

Update your

```text
Player Registration System
```

Replace every occurrence of

```python
open(...)
```

and

```python
close()
```

with

```python
with open(...)
```

Your program should behave exactly the same.

The code should simply be cleaner and safer.

---

# 💡 Chapter Summary

You learned

- `with` creates a managed block.
- Files are closed automatically.
- It works for reading, writing, and appending.
- It's safer if errors occur.
- It's the preferred Python style.

---

# 🌱 Growth Log

Reflect honestly.

- Why is `with` safer than manually calling `close()`?

- What happens when execution leaves a `with` block?

- Can I explain what `as file` does?

If yes...

You're officially writing file-handling code the Pythonic way.

---

> 🚀 Coming Up

## 📦 Batch 5 — Modules & Imports

You'll finally answer questions like:

- What exactly is a module?
- Why do we write `import math`?
- What's the difference between

```python
import math
```

and

```python
from math import sqrt
```

You'll also start organizing your own code into reusable files.