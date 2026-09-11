# 🤖 The AI Engineer Playbook
# 📁 Workbook 04 — Files & Python Ecosystem
## Batch 5 — Imports & Modules

> *"A program doesn't have to live in one file."*

````md
# 🤖 The AI Engineer Playbook
# 📁 Workbook 04 — Files & Python Ecosystem
## Batch 5 — Imports & Modules

> *"A program doesn't have to live in one file."*

---

# 🎯 Learning Objectives

By the end of this batch, you should be able to:

- Explain what a module is
- Import Python's built-in modules
- Use `import`
- Use `from ... import`
- Use aliases with `as`
- Create your own modules
- Import code from another Python file
- Begin organizing a multi-file project

---

# 🧭 Where You Are

```text
🤖 AI Engineer Playbook

Phase 1 — Python Fluency

███████████████████████████████████████████████░

✅ Foundations
✅ Functions
✅ Collections
✅ Object-Oriented Programming

🟢 Files & Python Ecosystem

    ✅ Thinking in Files
    ✅ Reading Files
    ✅ Writing Files
    ✅ Context Managers
    ⏳ Imports & Modules
    ⬜ Packages
    ⬜ PyPI
    ⬜ Virtual Environments
    ⬜ PATH
    ⬜ Git Integration
````

---

# 🤔 The Problem

Imagine your Football Academy project keeps growing.

You have:

* `Player`
* `Goalkeeper`
* `Defender`
* `Midfielder`
* `Forward`
* `FootballAcademy`
* Functions for saving data
* Functions for loading data
* Menu functions

You could put everything inside:

```text
main.py
```

Eventually...

```text
main.py

1,000+ lines 😭
```

Finding things becomes annoying.

Changing one part of the program becomes harder.

This is where **modules** come in.

---

# 📦 What Is a Module?

A Python module is simply:

> **A Python file containing reusable Python code.**

For example:

```text
players.py
```

is a module.

Inside it:

```python
class Player:
    pass
```

Another file:

```text
main.py
```

can use that code.

---

# 🧠 The Big Idea

Imagine this project:

```text
football_academy/
│
├── main.py
├── players.py
└── storage.py
```

### `players.py`

Contains:

```python
class Player:
    pass
```

### `storage.py`

Contains:

```python
def save_players():
    pass
```

### `main.py`

Brings everything together.

This means:

```text
players.py
      ↓
   Player

storage.py
      ↓
save_players()

        ↓

      main.py
```

---

# ⭐ Your First Import

Python already comes with many useful modules.

For example:

```python
import math
```

Now you can use functions inside the `math` module.

```python
print(math.sqrt(25))
```

Output:

```text
5.0
```

---

# 🔍 Breaking It Down

```python
import math
```

means:

> "Python, bring the `math` module into this file so I can use it."

Then:

```python
math.sqrt(25)
```

means:

> "Use the `sqrt()` function from the `math` module."

The dot is important.

```text
module.function()
```

Example:

```python
math.sqrt()
math.ceil()
math.floor()
```

---

# 📚 Another Example

Python has a module called:

```python
random
```

Import it:

```python
import random
```

Then:

```python
number = random.randint(1, 10)

print(number)
```

Python generates a random number between `1` and `10`.

---

# 🤔 Why Not Just Do This?

```python
sqrt(25)
```

Why write:

```python
math.sqrt(25)
```

The reason is **organization and clarity**.

Imagine you import multiple modules that all contain functions with the same name.

Using:

```python
module.function()
```

helps Python—and you—know exactly where that function came from.

---

# 📦 `from ... import`

Sometimes you don't want the entire module.

You only want something specific.

Instead of:

```python
import math

print(math.sqrt(25))
```

You can write:

```python
from math import sqrt

print(sqrt(25))
```

Now you can use:

```python
sqrt()
```

directly.

---

# 🧠 Compare Them

## Option 1

```python
import math

math.sqrt(25)
```

## Option 2

```python
from math import sqrt

sqrt(25)
```

Both work.

The difference is how you access the imported functionality.

---

# ⚠️ A Small Warning

You might see:

```python
from math import *
```

This imports everything.

For example:

```python
from math import *
```

Now many names suddenly appear in your file.

This can cause confusion and name collisions.

For now:

❌ Avoid this.

Prefer:

```python
import math
```

or:

```python
from math import sqrt
```

---

# 🏷️ Import Aliases

Sometimes module names are long.

You can rename them temporarily using:

```python
as
```

Example:

```python
import math as m
```

Now:

```python
print(m.sqrt(25))
```

You can also alias imported items:

```python
from math import sqrt as square_root

print(square_root(25))
```

---

# 🧰 Useful Standard Library Modules

Python comes with a large collection of built-in modules called the **Standard Library**.

A few examples:

| Module       | Useful For                    |
| ------------ | ----------------------------- |
| `math`       | Mathematical operations       |
| `random`     | Random values                 |
| `datetime`   | Dates and time                |
| `os`         | Operating system interactions |
| `json`       | Working with JSON data        |
| `pathlib`    | Working with file paths       |
| `statistics` | Statistical calculations      |

You don't need to memorize them.

Just remember:

> Before building something from scratch, check whether Python already provides a tool for it.

---

# 🏗️ Creating Your Own Module

Now for the important part.

Suppose you create:

```text
players.py
```

Inside:

```python
def create_player(name, age):
    return {
        "name": name,
        "age": age
    }
```

Then you create:

```text
main.py
```

Both files are in the same folder:

```text
project/
│
├── main.py
└── players.py
```

Inside `main.py`:

```python
import players
```

Now you can write:

```python
player = players.create_player("James", 25)

print(player)
```

Output:

```python
{'name': 'James', 'age': 25}
```

🎉

You've just imported your own code from another file.

---

# 🧠 Another Approach

Instead of importing the whole module:

```python
import players
```

You can import a specific function:

```python
from players import create_player
```

Then:

```python
player = create_player("James", 25)
```

No:

```python
players.
```

needed.

---

# ⚽ Football Academy AI

Let's begin organizing our project.

```text
football_academy/
│
├── main.py
├── player.py
└── storage.py
```

---

## `player.py`

```python
class Player:

    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def __str__(self):
        return f"{self.name} ({self.position})"
```

---

## `storage.py`

```python
def save_player(player):

    with open("players.txt", "a") as file:
        file.write(f"{player.name},{player.age},{player.position}\n")
```

---

## `main.py`

```python
from player import Player
from storage import save_player


player = Player(
    "James",
    24,
    "Midfielder"
)

save_player(player)
```

Look at what happened.

`main.py` doesn't need to know **how** the player is saved.

It simply says:

```python
save_player(player)
```

The storage logic lives somewhere else.

This is one of the biggest benefits of modules.

---

# 🧩 Separation of Responsibilities

Each file gets a job.

```text
player.py

↓

Player-related code
```

```text
storage.py

↓

Saving and loading
```

```text
main.py

↓

Running the application
```

Instead of:

```text
Everything Everywhere All at Once.py 😭
```

---

# 🐞 Debugging Lab

## What is wrong here?

Project:

```text
project/
│
├── main.py
└── player.py
```

`player.py`

```python
def greet():
    print("Hello!")
```

`main.py`

```python
import player

greet()
```

This fails.

Why?

Because you imported the **module**.

You need:

```python
player.greet()
```

Or:

```python
from player import greet

greet()
```

---

# ⚠️ Common Beginner Mistake

Suppose you have:

```text
random.py
```

Then you write:

```python
import random
```

Python may import **your file** instead of Python's actual `random` module.

The same problem can happen with names like:

```text
math.py
json.py
os.py
```

Avoid naming your own files after standard library modules.

---

# 🧠 `if __name__ == "__main__"` — Preview

You may eventually see this:

```python
if __name__ == "__main__":
    main()
```

Don't worry about mastering it yet.

For now, the important idea is:

> Python can tell the difference between a file being run directly and a file being imported.

We'll revisit this properly when it becomes useful for project organization.

---

# 🏃 Practice

## 🟢 Easy

Import:

```python
math
```

Use it to calculate:

```python
sqrt(81)
```

Then import:

```python
random
```

Generate a random number between:

```text
1 and 100
```

---

## 🟡 Medium

Create:

```text
greetings.py
```

Add:

```python
def greet(name):
    return f"Hello, {name}!"
```

Create:

```text
main.py
```

Import the module and call `greet()`.

Try both:

```python
import greetings
```

and:

```python
from greetings import greet
```

---

## 🔴 Hard

Create this structure:

```text
academy/
│
├── main.py
├── players.py
└── utils.py
```

### `players.py`

Create:

```python
def create_player(name, position):
```

Return a dictionary.

---

### `utils.py`

Create:

```python
def display_player(player):
```

Print the player's information.

---

### `main.py`

Import both functions.

Create a player.

Display the player.

---

# ⚔️ Mini Challenge — Split the Code

Take a small program you've already written.

Maybe your:

* Contact Book
* Wallet App
* Player Registration System
* Football Academy project

Try splitting it into at least two files.

For example:

```text
project/
│
├── main.py
└── helpers.py
```

Move some helper functions into:

```text
helpers.py
```

Then import them into:

```text
main.py
```

The goal isn't to create a complicated structure.

The goal is to experience this:

```text
One Program

↓

Multiple Python Files

↓

Imports connect them
```

---

# 🤖 AI Engineer Lens

You'll constantly import modules in AI and data projects.

For example:

```python
import numpy as np
```

```python
import pandas as pd
```

```python
import matplotlib.pyplot as plt
```

Later, those lines will become completely normal.

For now, understand the pattern:

```text
Import code

↓

Give it a name

↓

Use the functionality
```

---

# 💡 Chapter Summary

You learned:

* A module is a Python file containing reusable code.
* `import module` imports the module.
* Access module contents using:

```python
module.item
```

* `from module import item` imports something specific.
* `as` creates an alias.
* Python includes many useful standard library modules.
* You can create your own modules.
* Modules help organize large programs.

---

# 🌱 Growth Log

Ask yourself:

* What is the difference between a module and a function?
* What is the difference between:

```python
import math
```

and:

```python
from math import sqrt
```

* Why might a project use multiple Python files?
* Why is separating `Player` code from file storage useful?

If you can explain those...

You're ready for the next level.

---

# 🚀 Coming Up

## 📦 Batch 6 — Packages

You've learned how Python files can work together.

Next, we'll organize **multiple modules into folders**.

Something like this:

```text
football_academy/

├── main.py

├── models/
│   ├── player.py
│   └── academy.py

├── services/
│   └── storage.py

└── utils/
    └── helpers.py
```

That's where your projects start looking less like individual scripts...

and more like actual software. 🏗️

````

---

## 🎯 Your key takeaway from this batch

Don't overcomplicate modules in your head.

At the beginner level:

> **A module is just a `.py` file that you can import code from.**

So if you have:

```text
calculator.py
````

and inside:

```python
def add(a, b):
    return a + b
```

Another file can do:

```python
from calculator import add

print(add(2, 3))
```

That's the core idea.

**One Python file can borrow and reuse code from another Python file.**

Once that clicks, **Packages** are basically the next organizational step:

> **Modules → organized into folders → Packages.**

And that's exactly where we're heading next. 😎🚀
