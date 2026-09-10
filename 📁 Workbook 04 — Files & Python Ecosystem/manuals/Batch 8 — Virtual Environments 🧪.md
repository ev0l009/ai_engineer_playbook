# 🤖 The AI Engineer Playbook
# 📁 Workbook 04 — Files & Python Ecosystem
## Batch 8 — Virtual Environments 🧪

> *"Every project deserves its own workspace."*

---

# 🎯 Learning Objectives

By the end of this batch, you should be able to:

- Explain what a virtual environment is
- Understand the problem virtual environments solve
- Create a virtual environment
- Activate and deactivate one
- Install packages inside a virtual environment
- Understand project dependencies
- Recognize why different projects may need isolated environments
- Understand the relationship between `python`, `pip`, and a virtual environment
- Start every serious Python project with its own environment

---

# 🧭 Where You Are

```text
🤖 AI Engineer Playbook

Phase 1 — Python Fluency 🐍

█████████████████████████████████████████████████░

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
    ✅ Packages
    ✅ PyPI & pip
    ⏳ Virtual Environments
    ⬜ PATH
    ⬜ Git Integration

🎯 Exit Goal:
Can organize multi-file Python projects
```

---

# 🤔 The Problem

Let's imagine you have two Python projects.

```text
📁 Project A
```

Project A uses:

```text
pandas version 2.x
```

Then you start another project.

```text
📁 Project B
```

But Project B needs:

```text
pandas version 1.x
```

Now imagine both projects share the same Python installation.

You do this:

```text
Install pandas 2.x
```

Project A:

```text
😎 Works!
```

Then you change it:

```text
Install pandas 1.x
```

Project B:

```text
😎 Works!
```

But Project A:

```text
💀 Something broke.
```

Why?

Because both projects are fighting over the same shared environment.

---

# 🧠 The Big Idea

A **virtual environment** gives a Python project its own isolated space.

Instead of this:

```text
                    GLOBAL PYTHON
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ↓              ↓              ↓

      Project A      Project B      Project C

      Same packages
      Same versions
      Same environment

              😬
```

We can have this:

```text
Project A
    │
    └── 🧪 Virtual Environment A
            └── Its own packages


Project B
    │
    └── 🧪 Virtual Environment B
            └── Its own packages


Project C
    │
    └── 🧪 Virtual Environment C
            └── Its own packages
```

Now each project can manage its own dependencies.

Much cleaner. 😌

---

# 🧩 What Exactly Is a Virtual Environment?

Think of your main Python installation as a large apartment building.

```text
🏢 Python Installation
```

Inside that building, you could throw every package from every project together.

Eventually:

```text
NumPy
Pandas
Flask
PyTorch
scikit-learn
requests
Some random package from six months ago
Another package you forgot about

😵‍💫
```

Instead, virtual environments give each project its own apartment.

```text
🏢 Python Installation

    ├── 🏠 Project A Environment
    │       ├── pandas
    │       └── numpy
    │
    ├── 🏠 Project B Environment
    │       ├── flask
    │       └── requests
    │
    └── 🏠 Project C Environment
            ├── torch
            └── numpy
```

Each project gets its own controlled space.

---

# 🧠 The Important Mental Model

A virtual environment is **not another programming language**.

It is also not a replacement for Python.

You still write normal Python:

```python
print("Hello")
```

What changes is the environment surrounding your project.

Think:

```text
Python Program
      +
Python Interpreter
      +
Installed Packages
```

A virtual environment helps control which packages belong to a particular project.

---

# 🏗️ Your First Virtual Environment

Suppose you have a project:

```text
my_project/
```

Open your terminal inside that project directory.

Then run:

```bash
python -m venv venv
```

Let's slow that down.

```text
python
   │
   └── Run Python

-m
   │
   └── Run a Python module

venv
   │
   └── The virtual environment module

venv
   │
   └── Name of the environment folder
```

So:

```bash
python -m venv venv
```

roughly means:

> Use Python to run the `venv` module and create a virtual environment called `venv`.

---

# 📁 What Happens Next?

Your project may now look something like this:

```text
my_project/

├── main.py
│
└── venv/
```

Inside that environment folder are files and directories used to manage the isolated Python environment.

Conceptually:

```text
my_project/

├── main.py
│
└── venv/
    │
    ├── Python-related environment files
    │
    ├── package management tools
    │
    └── installed packages
```

You generally don't need to manually edit the internals.

For now:

> Python manages the environment. You use it.

---

# 🔌 Creating vs Activating

This is important.

Creating an environment:

```bash
python -m venv venv
```

does **not** automatically mean you're using it.

You need to activate it.

Think:

```text
Create 🏗️
    ↓
Environment exists

Activate 🔌
    ↓
Terminal starts using that environment
```

---

# ▶️ Activating a Virtual Environment

The activation command depends on your operating system and shell.

A common pattern is:

## Windows Command Prompt

```bash
venv\Scripts\activate
```

## Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

## macOS / Linux

```bash
source venv/bin/activate
```

Once activated, your terminal will often show the environment name.

For example:

```text
(venv) C:\my_project>
```

That:

```text
(venv)
```

is your visual clue.

It usually means:

> You're currently working inside the `venv` virtual environment.

---

# 🧠 The Environment Switch

Before activation:

```text
Terminal
    ↓
Using your regular/default Python environment
```

After activation:

```text
Terminal
    ↓
(venv)
    ↓
Using the project's virtual environment
```

This affects commands such as:

```bash
python
```

and:

```bash
pip
```

because your shell is now configured to prefer the Python and package tools associated with the activated environment.

---

# 📦 Installing Packages Inside the Environment

Let's say you've activated your environment:

```text
(venv)
```

Now you run:

```bash
python -m pip install requests
```

The package is installed into the environment associated with that Python interpreter.

Conceptually:

```text
my_project/
├── main.py
└── venv/
    └── Installed packages
            └── requests
```

Your project can now use:

```python
import requests
```

---

# 🧠 Why `python -m pip` Is Useful

Earlier, we learned:

```bash
pip install package_name
```

But now you may prefer:

```bash
python -m pip install package_name
```

Why?

Because you're explicitly saying:

```text
Use THIS Python
        ↓
Run ITS pip
        ↓
Install the package there
```

That can help reduce confusion when multiple Python installations or environments exist.

A useful mental model is:

```text
python
   ↓
Which interpreter?

python -m pip
   ↓
Use that interpreter's package manager
```

---

# 🔍 Checking the Environment

Once your environment is activated, you can run:

```bash
python -m pip list
```

You might initially see only a few packages.

That's because your new environment starts relatively isolated.

Then:

```bash
python -m pip install requests
```

Afterward:

```bash
python -m pip list
```

You should see `requests` and its required dependencies in that environment.

The exact output and versions can vary.

---

# 🧪 Experiment: Two Separate Environments

Imagine this setup:

```text
projects/

├── project_a/
│   └── venv/
│
└── project_b/
    └── venv/
```

You activate:

```text
project_a/venv
```

and install:

```text
requests
```

Then:

```text
Project A Environment

requests
```

But Project B's environment doesn't automatically receive it.

```text
Project B Environment

No requests yet
```

That's isolation.

And that's the whole point.

---

# 🐞 Debugging Lab 1 — "I Installed It, But Python Can't Find It!"

You activate one environment:

```text
(venv_a)
```

Then install:

```bash
python -m pip install pandas
```

Later, you switch to:

```text
(venv_b)
```

And write:

```python
import pandas
```

Python says:

```text
ModuleNotFoundError
```

🤔

The likely explanation:

```text
pandas was installed in:

venv_a

But your program is now using:

venv_b
```

Remember:

```text
Different environment
        =
Different package collection
```

---

# 🐞 Debugging Lab 2 — "Why Does It Work in One Project?"

Imagine:

```text
Project A
    │
    └── venv
         └── pandas installed
```

You open:

```text
Project B
```

Then write:

```python
import pandas
```

And get:

```text
ModuleNotFoundError
```

You might think:

> "But I already installed pandas!"

Yes.

But you installed it in:

```text
Project A's environment
```

Not necessarily in:

```text
Project B's environment.
```

The solution is usually to activate Project B's environment and install the required dependency there.

---

# 🐞 Debugging Lab 3 — "I Created `venv`, So Why Isn't It Being Used?"

You run:

```bash
python -m venv venv
```

Great.

The environment exists.

But then you immediately run:

```bash
pip install something
```

without activating the environment.

Depending on your setup, that command may use a different `pip` than you intended.

This is why the normal workflow is:

```text
Create environment
        ↓
Activate environment
        ↓
Install packages
        ↓
Run project
```

Or, when appropriate, explicitly use the environment's interpreter to run `pip`.

---

# 🔌 Deactivating the Environment

When you're done working inside a virtual environment:

```bash
deactivate
```

Your terminal prompt should return to its normal state.

Conceptually:

```text
(venv) Terminal

deactivate

        ↓

Normal Terminal
```

You haven't deleted anything.

You simply stopped using that environment in the current shell.

The environment still exists in your project folder.

---

# 🧠 The Complete Workflow

Here is the lifecycle you'll use repeatedly.

## Step 1 — Create a Project

```text
my_project/

└── main.py
```

---

## Step 2 — Create an Environment

```bash
python -m venv venv
```

Now:

```text
my_project/

├── main.py
│
└── venv/
```

---

## Step 3 — Activate It

Use the command appropriate for your operating system and shell.

For example:

```text
(venv)
```

appears in the terminal prompt.

---

## Step 4 — Install Dependencies

```bash
python -m pip install requests
```

---

## Step 5 — Write Your Program

```python
import requests

print("My project is ready!")
```

---

## Step 6 — Work

```text
Write code
    ↓
Install required packages
    ↓
Run program
    ↓
Build cool stuff 😎
```

---

## Step 7 — Deactivate When Finished

```bash
deactivate
```

---

# 📋 The Workflow Map

```text
📁 Create Project
        │
        ▼
🧪 Create Virtual Environment
        │
        ▼
🔌 Activate Environment
        │
        ▼
📦 Install Dependencies
        │
        ▼
💻 Write Code
        │
        ▼
▶️ Run Project
        │
        ▼
🔌 Deactivate When Finished
```

Eventually, this will become second nature.

---

# 🤖 AI Engineer Lens

Virtual environments become especially important in AI.

Imagine one project uses:

```text
PyTorch
NumPy
Pandas
```

Another project uses:

```text
TensorFlow
scikit-learn
```

Another uses:

```text
FastAPI
Transformers
LangChain
```

These projects can have many dependencies.

Sometimes they need:

```text
Different versions
```

or:

```text
Specific compatible combinations
```

Without isolation:

```text
Dependency chaos 😭
```

With environments:

```text
AI Project A 🧪
    ├── torch
    ├── numpy
    └── pandas


AI Project B 🧪
    ├── tensorflow
    └── numpy


AI API 🧪
    ├── fastapi
    └── other dependencies
```

This is normal professional practice.

---

# 🧠 A New Concept — Dependencies

A **dependency** is software your project needs in order to work.

For example:

```text
My Program
    │
    ├── requests
    ├── pandas
    └── numpy
```

Your project depends on those packages.

Therefore:

```text
requests
pandas
numpy
```

are dependencies.

Later, you'll learn how to record these dependencies so another developer can recreate your environment.

The idea looks like:

```text
Your Project
        +
Dependency List
        ↓
Another Person
        ↓
Recreates Environment
        ↓
Runs Project
```

That's coming soon.

---

# 🏃 Practice

## 🟢 Easy — Create Your First Environment

Create a folder:

```text
virtual_env_practice/
```

Inside it, create:

```text
main.py
```

Then create a virtual environment:

```bash
python -m venv venv
```

Activate it.

Your goal:

```text
See (venv) appear in your terminal.
```

Then deactivate it:

```bash
deactivate
```

---

# 🟡 Medium — Install a Package

Inside your project:

1. Create a virtual environment.
2. Activate it.
3. Install:

```text
requests
```

using:

```bash
python -m pip install requests
```

Then create:

```text
main.py
```

Write:

```python
import requests

print("requests is available!")
```

The point is not to master `requests`.

The point is:

```text
Environment
    ↓
Install
    ↓
Import
    ↓
Use
```

---

# 🔴 Hard — Two Projects, Two Environments

Create two separate projects.

```text
python_projects/

├── project_one/
│   ├── main.py
│   └── venv/
│
└── project_two/
    ├── main.py
    └── venv/
```

For each project:

1. Create its own virtual environment.
2. Activate it.
3. Install a different package.

For example:

```text
Project One
    ↓
requests


Project Two
    ↓
rich
```

Then investigate:

```bash
python -m pip list
```

inside each environment.

Notice how the environments can have different installed packages.

---

# ⚔️ Mini Challenge — The Dependency Detective

Read this situation.

```text
You have two projects.

Project A:

Needs:
pandas
numpy
matplotlib


Project B:

Needs:
fastapi
requests
```

Answer these questions:

### 1. Should both projects share one virtual environment?

Explain why or why not.

---

### 2. Where should you install Project A's packages?

```text
Global Python?

or

Project A's environment?
```

---

### 3. What happens if Project B needs a different version of `requests` than another project?

---

### 4. Complete the architecture:

```text
Project A
    │
    └── __________________
            │
            ├── pandas
            ├── numpy
            └── matplotlib


Project B
    │
    └── __________________
            │
            ├── fastapi
            └── requests
```

---

# 🧠 The Big Idea — One More Time

The relationship looks like this:

```text
Your Computer
        │
        ▼
🐍 Python
        │
        ├──────────────┐
        │              │
        ▼              ▼

📁 Project A       📁 Project B
     │                  │
     ▼                  ▼

🧪 Environment A   🧪 Environment B
     │                  │
     ▼                  ▼

📦 Packages A      📦 Packages B
```

Each project gets control over its own dependencies.

---

# 🧩 Common Commands Cheat Sheet

## Create an Environment

```bash
python -m venv venv
```

---

## Activate — Windows Command Prompt

```bash
venv\Scripts\activate
```

---

## Activate — Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

---

## Activate — macOS / Linux

```bash
source venv/bin/activate
```

---

## Install a Package

```bash
python -m pip install package_name
```

---

## Check Installed Packages

```bash
python -m pip list
```

---

## Deactivate

```bash
deactivate
```

---

# ⚠️ A Note About Command Variations

Depending on your operating system and Python installation, you may encounter variations such as:

```bash
python3 -m venv venv
```

instead of:

```bash
python -m venv venv
```

The exact command used to invoke Python can vary.

The core idea remains:

```text
Use your Python interpreter
        ↓
Run the venv module
        ↓
Create an isolated environment
```

Don't panic if your system uses a slightly different command.

Understand the system first.

Memorization comes later.

---

# 💡 Chapter Summary

You learned:

- A virtual environment is an isolated Python environment.
- Projects can have their own dependencies.
- Different environments can contain different packages and versions.
- Create one with:

```bash
python -m venv venv
```

- Activate it before working.
- Install packages inside the intended environment.
- `python -m pip` helps tie package management to a specific Python interpreter.
- Use:

```bash
deactivate
```

to leave an activated environment.
- Virtual environments help prevent dependency conflicts.

---

# 🌱 Growth Log

Before moving on, ask yourself:

### Can I explain this?

> Why shouldn't every Python project necessarily share the same packages?

### Can I explain this?

```text
Global Python
        ↓
Project
        ↓
Virtual Environment
        ↓
Dependencies
```

### Can I do this?

```text
Create
    ↓
Activate
    ↓
Install
    ↓
Code
    ↓
Deactivate
```

If yes...

Then you've crossed an important line.

You're no longer just writing Python files.

You're beginning to understand how **Python projects are actually managed**. 🧪😎

---

# 📈 Progress Update

```text
🤖 AI Engineer Playbook

Phase 1 — Python Fluency 🐍

██████████████████████████████████████████████████░

🟢 Files & Python Ecosystem

    ✅ Thinking in Files
    ✅ Reading Files
    ✅ Writing Files
    ✅ Context Managers
    ✅ Imports & Modules
    ✅ Packages
    ✅ PyPI & pip
    ⏳ Virtual Environments
    ⬜ PATH
    ⬜ Git Integration

🎯 EXIT CRITERIA:
Can organize multi-file Python projects
```

---

# 🚀 Coming Up

## 🛣️ Batch 9 — PATH

Soon we're going to investigate one of those things that confuses almost every developer at some point:

```text
You type:

python

Terminal says:

❌ Command not found
```

But...

```text
Python is installed. 🤨
```

So why can't the terminal find it?

The answer leads us to:

```text
PATH
```

And once you understand it, this becomes much less mysterious:

```text
Terminal
    │
    ▼
"Find this command"
    │
    ▼
Search PATH locations
    │
    ├── Found it 😎
    │
    └── Didn't find it 😭
```

Next up:

# 🛣️ Understanding PATH