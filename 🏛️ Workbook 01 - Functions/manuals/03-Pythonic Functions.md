# 🐍 Python Fluency Workbook 01
# Batch 3 — Pythonic Functions

> *"Writing functions is programming.*
> *Understanding functions is thinking like a Python programmer."*

---

# 🎯 Learning Objectives

By the end of this chapter, you should be able to:

- ✅ Explain what **first-class functions** are.
- ✅ Pass functions as arguments.
- ✅ Return functions from functions.
- ✅ Know when to use `lambda`.
- ✅ Know when **not** to use `lambda`.
- ✅ Write readable function annotations.
- ✅ Write useful docstrings.
- ✅ Recognize these concepts in AI libraries.

---

# 📌 Where You Are

```text
Python Fluency

███████████████░░░░░░░░ 75%

✔ Foundations
✔ Mastering Functions
🟢 Pythonic Functions
⬜ Function Lab
```

---

# 📖 1. Functions Are Objects

## 🤔 Mental Model

Most programming languages treat functions as something special.

Python doesn't.

Python treats functions like almost everything else.

They're objects.

If that sounds strange...

Think about this.

You can do this:

```python
name = "Valerian"
```

Now `name` refers to a string object.

You can also do this:

```python
def greet():
    return "Hello!"

say_hi = greet
```

Now `say_hi` refers to a **function object**.

Exactly the same idea.

---

## 💻 Example

```python
def greet():
    return "Hello!"

say_hi = greet

print(say_hi())
```

Output

```text
Hello!
```

Notice something important.

We wrote

```python
say_hi = greet
```

NOT

```python
say_hi = greet()
```

Why?

Because

```python
greet
```

means

> "Give me the function."

while

```python
greet()
```

means

> "Run the function."

This tiny difference becomes incredibly important later.

---

## ⚠️ Common Beginner Mistake

```python
def greet():
    return "Hello"

print(greet)
```

Output?

Not

```text
Hello
```

Instead something like

```text
<function greet at 0x...>
```

Why?

Because you printed the function itself.

You never called it.

---

# 🧠 Think Like Python

Imagine functions are TV remotes.

```python
remote = turn_on_tv
```

You now own the remote.

Nothing happened.

The TV only turns on when you press the button.

```python
remote()
```

The parentheses are the button.

---

# 📖 2. Higher-Order Functions

A function is called **higher-order** if it:

- receives another function
- returns another function

---

## 💻 Example

```python
def double(x):
    return x * 2

def apply(func, value):
    return func(value)

print(apply(double, 5))
```

Output

```text
10
```

Python passed the entire function into another function.

---

## 🤖 AI Engineer Note

Later you'll see code like

```python
sorted(players, key=my_function)
```

or

```python
dataset.map(transform)
```

or

```python
model.apply(weights_init)
```

Those APIs work because Python treats functions as values.

---

# 📖 3. Lambda Functions

## What is a Lambda?

A lambda is simply an anonymous function.

Instead of

```python
def square(x):
    return x * x
```

you write

```python
square = lambda x: x * x
```

Same idea.

Different syntax.

---

## ⚡ Syntax

```python
lambda parameters: expression
```

Think of it as

```python
def

↓

one line

↓

returns automatically
```

---

## 💻 Example

```python
double = lambda x: x * 2

print(double(8))
```

Output

```text
16
```

---

# 🤔 Should I Use Lambda Everywhere?

No.

In fact...

Most experienced Python developers **don't**.

Lambda shines when the function is:

- tiny
- used once
- improves readability

---

Good

```python
players.sort(key=lambda player: player["goals"])
```

Bad

```python
lambda player:
    if ...
```

If it takes more than one line...

Use `def`.

---

# 📖 4. Function Annotations

Annotations tell readers what types are expected.

```python
def add(a: int, b: int) -> int:
    return a + b
```

Notice

```python
a: int
```

means

> "I expect an integer."

while

```python
-> int
```

means

> "I return an integer."

---

## 🤔 Important

Python **does not enforce** annotations.

This works.

```python
add("Hello", "World")
```

It won't stop you.

Annotations are mainly for:

- humans
- IDEs
- static analysis tools

---

# 📖 5. Docstrings

A docstring explains **what** a function does.

Example

```python
def average(numbers):
    """
    Returns the average of a list of numbers.
    """
    return sum(numbers) / len(numbers)
```

Later you can do

```python
help(average)
```

and Python will display the documentation.

Very useful.

---

# 🔬 Under the Hood

When Python sees

```python
def greet():
```

it creates a **function object** in memory.

The variable

```python
greet
```

simply points to that object.

That's why this works.

```python
copy = greet
```

Both names point to the same function.

Exactly like this.

```text
greet ─────┐
           │
           ▼
      Function Object
           ▲
           │
copy ──────┘
```

---

# 🐞 Debugging Lab

Without running the code...

Predict the output.

```python
def hello():
    return "Hi"

x = hello

print(x)
print(x())
```

Questions

1. Why are the outputs different?

2. Which line actually calls the function?

---

# 🏃 Practice

### Easy

1. Write a lambda that triples a number.

2. Write a lambda that returns `True` if a number is even.

3. Write a function with annotations.

---

### Medium

Given

```python
players = [
    ("Ada", 4),
    ("Grace", 9),
    ("Linus", 6)
]
```

Sort them by score using `lambda`.

---

Write a function that accepts another function and applies it twice.

---

### Hard

Create a function

```python
benchmark(func, value)
```

that

- receives another function
- runs it
- returns the result

---

# 🥋 Boss Fight

Imagine you're writing software for a football academy.

Each player has

```python
{
    "name": "...",
    "goals": ...,
    "assists": ...,
    "age": ...
}
```

Build reusable functions that

- sort by goals
- sort by assists
- sort by age

Use

- regular functions
- lambda functions

Compare both solutions.

Which do you prefer?

Why?

---

# 💭 Reflection

Try answering without looking back.

1. Why are functions called **first-class objects**?

2. What's the difference between

```python
greet
```

and

```python
greet()
```

3. When is `lambda` better than `def`?

4. Why do annotations exist if Python ignores them?

5. Why are docstrings important?

---

# 💡 Chapter Summary

You learned that

- Functions are objects.
- Functions can be passed around.
- Lambda creates anonymous functions.
- Annotations improve readability.
- Docstrings improve documentation.
- Python's flexibility with functions is one reason AI libraries feel so expressive.

---

# ✅ Before Moving to Batch 4

You should now be comfortable with:

- ✔ First-class functions
- ✔ Higher-order functions
- ✔ Lambda
- ✔ Function annotations
- ✔ Docstrings
- ✔ Best practices

If you can explain these concepts **without looking at the notes**, you're ready for the Function Lab.

---

> 🚀 **Coming Up:** Batch 4 — Function Lab
>
> This is where you'll combine everything you've learned into realistic mini-projects, debugging challenges, interview-style questions, and one final "Boss Fight" before we move on to Files & Modules.
