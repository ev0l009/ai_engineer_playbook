# 🤖 The AI Engineer Playbook
# 📁 Workbook 04 — Files & Python Ecosystem
## Batch 6 — Packages

> *"Modules organize code. Packages organize modules."*

---

# 🎯 Learning Objectives

By the end of this batch, you should be able to:

- Explain what a Python package is
- Understand the relationship between modules and packages
- Organize modules into folders
- Understand the role of `__init__.py`
- Import code from modules inside packages
- Use package-style project structures
- Begin thinking about larger Python applications

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
    ✅ Imports & Modules
    ⏳ Packages
    ⬜ PyPI
    ⬜ Virtual Environments
    ⬜ PATH
    ⬜ Git Integration

🎯 Exit Goal:
Can organize multi-file Python projects
```

---

# 🧠 The Big Idea

In the previous batch, you learned that:

> A **module** is a Python file.

For example:

```text
player.py
```

```text
storage.py
```

```text
utils.py
```

But what happens when your project gets bigger?

Imagine this:

```text
football_academy/

├── main.py
├── player.py
├── goalkeeper.py
├── defender.py
├── midfielder.py
├── forward.py
├── storage.py
├── loader.py
├── validator.py
├── formatter.py
├── helpers.py
└── menu.py
```

😭😭😭

Everything is in one folder.

The files are modules...

but the project is starting to become messy.

So we need another level of organization.

That level is called a **package**.

---

# 📦 What Is a Package?

At a beginner-friendly level:

> A **package** is a folder used to organize related Python modules.

Imagine this:

```text
football_academy/

├── main.py
│
├── models/
│   ├── player.py
│   ├── goalkeeper.py
│   └── academy.py
│
├── services/
│   ├── storage.py
│   └── loader.py
│
└── utils/
    ├── validator.py
    └── formatter.py
```

Now the project is much easier to understand.

---

# 🧩 Module vs Package

Let's make the distinction crystal clear.

## Module

A Python file.

```text
player.py
```

---

## Package

A folder containing related Python modules.

```text
models/

├── player.py
├── goalkeeper.py
└── academy.py
```

So:

```text
player.py
    ↓
Module

models/
    ↓
Package
```

---

# 🏗️ Why Packages Exist

Imagine walking into a library.

Would you prefer this?

```text
📚
Every book in one giant room.
```

Or this?

```text
📚 Library

├── Fiction
├── Science
├── History
└── Technology
```

Packages work like categories.

They group related code together.

For example:

```text
models/
```

contains:

```text
Things that represent our data.
```

While:

```text
services/
```

contains:

```text
Things that perform actions.
```

And:

```text
utils/
```

contains:

```text
Helpful reusable functions.
```

---

# ⚽ Football Academy AI — The Growing Project

Let's organize our Football Academy project.

```text
football_academy/

├── main.py
│
├── models/
│   ├── __init__.py
│   ├── player.py
│   └── academy.py
│
├── services/
│   ├── __init__.py
│   └── storage.py
│
└── utils/
    ├── __init__.py
    └── helpers.py
```

Don't panic at the strange new file:

```text
__init__.py
```

We're getting there. 😎

---

# 🧠 The Role of `__init__.py`

Traditionally, a file called:

```text
__init__.py
```

was used to explicitly mark a directory as a Python package.

For learning and for many projects, you'll still commonly see:

```text
models/
├── __init__.py
└── player.py
```

Modern Python can also support namespace packages without an `__init__.py` in some situations.

But for now, our mental model is simple:

> `__init__.py` is a package-related file that helps define and initialize a regular Python package.

You don't need to put anything inside it yet.

An empty file is completely fine:

```text
__init__.py
```

---

# 🧩 Importing From a Package

Suppose we have:

```text
football_academy/

├── main.py
│
└── models/
    ├── __init__.py
    └── player.py
```

Inside:

```text
player.py
```

we write:

```python
class Player:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return f"{self.name} - {self.position}"
```

Now inside:

```text
main.py
```

we can write:

```python
from models.player import Player
```

Let's break that down.

```text
models
   ↓
package

player
   ↓
module

Player
   ↓
class
```

So:

```python
from models.player import Player
```

means:

> Go into the `models` package, find the `player` module, and import the `Player` class.

---

# 🧠 Reading Imports From Left to Right

Look at:

```python
from models.player import Player
```

Think:

```text
from
    models/
        player.py
            Player
```

Or visually:

```text
models/
    └── player.py
            └── Player
```

That import path describes where Python should look.

---

# 📦 Another Example

Project:

```text
project/

├── main.py
│
├── utils/
│   ├── __init__.py
│   └── helpers.py
```

Inside:

```text
helpers.py
```

```python
def greet(name):
    return f"Hello, {name}!"
```

Inside:

```text
main.py
```

```python
from utils.helpers import greet


print(greet("Valerian"))
```

Output:

```text
Hello, Valerian!
```

The pattern is:

```python
from package.module import thing
```

This is one of the most important patterns in Python project organization.

---

# 🔍 The Full Structure

Let's look at a slightly bigger project.

```text
football_academy/

├── main.py
│
├── models/
│   ├── __init__.py
│   ├── player.py
│   └── academy.py
│
├── services/
│   ├── __init__.py
│   └── storage.py
│
└── utils/
    ├── __init__.py
    └── helpers.py
```

---

## `models/player.py`

```python
class Player:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return f"{self.name} ({self.position})"
```

---

## `models/academy.py`

```python
class FootballAcademy:

    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def show_players(self):

        for player in self.players:
            print(player)
```

---

## `services/storage.py`

```python
def save_player(player):

    with open("players.txt", "a") as file:
        file.write(
            f"{player.name},{player.position}\n"
        )
```

---

## `utils/helpers.py`

```python
def display_title():

    print("⚽ FOOTBALL ACADEMY ⚽")
```

---

# 🚀 Bringing Everything Together

Inside:

```text
main.py
```

we can write:

```python
from models.player import Player
from models.academy import FootballAcademy
from services.storage import save_player
from utils.helpers import display_title


display_title()

academy = FootballAcademy()

player = Player(
    "James",
    "Midfielder"
)

academy.add_player(player)

save_player(player)

academy.show_players()
```

Now look at what happened.

`main.py` acts like the **conductor**.

```text
          🎼 main.py
              │
      ┌───────┼────────┐
      ↓       ↓        ↓

   models   services   utils
```

Each part of the program has its own responsibility.

---

# 🧠 The Problem Packages Solve

Without packages:

```text
football_academy/

├── main.py
├── player.py
├── academy.py
├── storage.py
├── loader.py
├── validator.py
├── formatter.py
├── menu.py
├── config.py
├── helpers.py
├── statistics.py
└── ...
```

😵‍💫

With packages:

```text
football_academy/

├── main.py
│
├── models/
│   ├── player.py
│   └── academy.py
│
├── services/
│   ├── storage.py
│   └── loader.py
│
├── utils/
│   ├── validator.py
│   └── formatter.py
│
└── config/
    └── settings.py
```

😌

Packages help your project communicate its structure.

---

# 🧩 Package Names

Package names usually follow Python naming conventions.

Prefer:

```text
models
services
utils
data_processing
machine_learning
```

Avoid:

```text
My Package
My-Package
MyPackage
```

A common style is:

```text
lowercase_with_underscores
```

---

# 🐞 Debugging Lab 1

Look at this structure:

```text
project/

├── main.py
│
└── models/
    ├── __init__.py
    └── player.py
```

Inside `player.py`:

```python
class Player:
    pass
```

Which import is correct?

### Option A

```python
from player import Player
```

### Option B

```python
from models import Player
```

### Option C

```python
from models.player import Player
```

The answer is:

```python
from models.player import Player
```

Why?

Because:

```text
models
    ↓
player
    ↓
Player
```

Python follows the package → module → item path.

---

# 🐞 Debugging Lab 2

Project:

```text
project/

├── main.py
│
└── utils/
    ├── __init__.py
    └── helpers.py
```

Inside:

```text
helpers.py
```

```python
def calculate_age(birth_year):
    return 2026 - birth_year
```

Someone writes:

```python
from utils import calculate_age
```

This will not normally work with the structure shown, because `calculate_age` lives inside:

```text
utils/helpers.py
```

The direct import is:

```python
from utils.helpers import calculate_age
```

Later, you'll also see packages expose selected names through `__init__.py`, but that's an additional organizational technique—not something you need to rely on yet.

---

# 🧠 `__init__.py` Can Do More

So far:

```text
__init__.py
```

has been empty.

But it can contain Python code.

For example:

```text
models/

├── __init__.py
├── player.py
└── academy.py
```

Inside:

```python
# models/__init__.py

from .player import Player
from .academy import FootballAcademy
```

The `.` means:

> This current package.

Now code outside the package may be able to write:

```python
from models import Player
from models import FootballAcademy
```

Instead of:

```python
from models.player import Player
from models.academy import FootballAcademy
```

This is useful...

but don't worry about memorizing it right now.

The important concept is:

> A package can control and organize what it exposes.

---

# 🤖 AI Engineer Lens

Later, you'll use packages constantly.

For example:

```python
import numpy
```

```python
import pandas
```

```python
import sklearn
```

```python
import torch
```

These are all larger pieces of Python software organized into packages and subpackages.

You'll eventually write imports like:

```python
from sklearn.model_selection import train_test_split
```

Read it like this:

```text
sklearn
    ↓
model_selection
    ↓
train_test_split
```

That same idea is exactly what you're learning right now with:

```python
from models.player import Player
```

The scale is different.

The concept is the same.

---

# 🏃 Practice

## 🟢 Easy — Your First Package

Create:

```text
project/

├── main.py
│
└── greetings/
    ├── __init__.py
    └── hello.py
```

Inside:

```text
hello.py
```

create:

```python
def greet(name):
    return f"Hello, {name}!"
```

Inside:

```text
main.py
```

import and call `greet()`.

---

## 🟡 Medium — Organize Your Utilities

Create:

```text
project/

├── main.py
│
└── utils/
    ├── __init__.py
    ├── calculator.py
    └── formatter.py
```

### `calculator.py`

Create:

```python
def add(a, b):
    return a + b
```

### `formatter.py`

Create:

```python
def format_name(name):
    return name.strip().title()
```

Import both functions into:

```text
main.py
```

Use them.

---

## 🔴 Hard — Mini Football Package

Create:

```text
football_project/

├── main.py
│
├── models/
│   ├── __init__.py
│   └── player.py
│
└── utils/
    ├── __init__.py
    └── display.py
```

---

### `models/player.py`

Create a `Player` class with:

```text
name
position
age
```

Add a `__str__()` method.

---

### `utils/display.py`

Create:

```python
def display_player(player):
```

Print the player.

---

### `main.py`

Import:

```text
Player
```

and:

```text
display_player
```

Then:

1. Create a player.
2. Display the player.

---

# ⚔️ Mini Challenge — Organize an Existing Project

Take one of your previous programs.

For example:

```text
Contact Book
```

or:

```text
Football Academy
```

Try moving it from this:

```text
project/

└── main.py
```

to something like:

```text
project/

├── main.py
│
├── models/
│   ├── __init__.py
│   └── contact.py
│
├── services/
│   ├── __init__.py
│   └── storage.py
│
└── utils/
    ├── __init__.py
    └── helpers.py
```

You don't need to create the "perfect" structure.

Ask yourself:

> Which pieces of code belong together?

That's the beginning of software architecture.

---

# 🧠 The Big Idea — One More Time

Here's the full progression.

```text
FUNCTION
A reusable piece of code.

        ↓

MODULE
A Python file containing code.

        ↓

PACKAGE
A folder organizing related modules.

        ↓

PROJECT
Multiple packages and files
working together.
```

That is the organizational ladder you're climbing.

---

# 💡 Chapter Summary

You learned:

- A **module** is a Python file.
- A **package** organizes related modules.
- Packages help larger projects stay clean.
- `__init__.py` is commonly used with regular Python packages.
- Imports can follow this pattern:

```python
from package.module import thing
```

- Packages allow you to group code by responsibility.

---

# 🌱 Growth Log

Ask yourself:

- What is the difference between a module and a package?
- Why would a project use packages instead of putting every file in one folder?
- Can I read this import?

```python
from models.player import Player
```

- What does the folder structure tell me about a project's organization?

If you can answer those...

You've taken another major step toward organizing real Python applications.

---

# 📈 Progress Update

```text
🤖 AI Engineer Playbook

Phase 1 — Python Fluency

████████████████████████████████████████████████░

🟢 Files & Python Ecosystem

    ✅ Thinking in Files
    ✅ Reading Files
    ✅ Writing Files
    ✅ Context Managers
    ✅ Imports & Modules
    ⏳ Packages
    ⬜ PyPI
    ⬜ Virtual Environments
    ⬜ PATH
    ⬜ Git Integration

🎯 EXIT CRITERIA:
Can organize multi-file Python projects
```

---

# 🚀 Coming Up

## 🌐 Batch 7 — PyPI & `pip`

So far, you've used:

```text
Your code
        +
Python's Standard Library
```

But the Python ecosystem is much bigger.

Soon you'll be able to install tools created by other developers.

The next progression:

```text
Standard Library
        ↓
Third-Party Packages
        ↓
PyPI
        ↓
pip install
        ↓
Use the package
```

You'll finally understand where commands like this come from:

```bash
pip install pandas
```

And more importantly...

you'll understand what actually happens after you run it. 🚀