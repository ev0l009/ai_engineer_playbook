# 🐍 Python Fluency Workbook 01
# Batch 4 — Function Lab

> *"Knowledge isn't proven by reading.*
> *It's proven by building."*

---

# 🏁 Final Mission

Congratulations.

You've reached the Function Lab.

This isn't another lesson.

This is where everything you've learned comes together.

Imagine you've just landed your first internship.

Your team leader doesn't care that you know what a function is.

They care whether you can use functions to build software.

Today...

You're going to do exactly that.

---

# 🎯 Learning Objectives

By the end of this lab you should be able to

✅ Break large problems into small functions

✅ Design reusable functions

✅ Pass data between functions

✅ Decide when to return values

✅ Choose between `def` and `lambda`

✅ Read function-heavy code confidently

---

# ⚽ Project

# Football Academy Manager

Your academy has hired you to build a small management system.

You'll improve it as you progress through Python.

Today's version will only use functions.

Later...

We'll add files.

Then classes.

Then pandas.

Then machine learning.

This project grows with you.

---

# 🧩 Phase One

Create functions for

```text
Add Player

Remove Player

Find Player

Show Players

Count Players
```

Hints

```python
players = []
```

Every action should be its own function.

---

# 🧩 Phase Two

Each player should contain

```python
{
    "name": "...",
    "age": ...,
    "position": "...",
    "goals": ...,
    "assists": ...
}
```

Example

```python
{
    "name": "Valerian",
    "age": 26,
    "position": "CDM",
    "goals": 8,
    "assists": 15
}
```

---

# 🧩 Phase Three

Create functions

```text
Top Scorer

Most Assists

Youngest Player

Average Age

Average Goals
```

Every calculation should have its own function.

Avoid writing everything inside `main()`.

---

# 🧩 Phase Four

Create

```python
academy_summary(players)
```

Output

```text
Players: 18

Average Age: 21.4

Top Scorer: Daniel

Most Assists: Ibrahim

Youngest: James
```

Only one function should print this.

All calculations should come from other functions.

Think reusable.

---

# 🥋 Boss Fight

Without looking at previous chapters...

Write

```python
sort_players(players, key_function)
```

Example

```python
sort_players(players, goals_key)

sort_players(players, assists_key)

sort_players(players, youngest_key)
```

Now...

Rewrite it using lambda.

Example

```python
sort_players(
    players,
    lambda player: player["goals"]
)
```

Question

Which version is easier to read?

Why?

---

# 🐞 Debugging Lab

What is wrong here?

```python
def add_player(player, squad=[]):
    squad.append(player)
    return squad
```

Question

Why might this create strange bugs?

Rewrite it correctly.

---

# 🔍 Read the Code

Without running it...

Predict the output.

```python
def multiply(x):
    return x * 2

def calculate(func, value):
    return func(value)

print(
    calculate(multiply, 8)
)
```

---

Now this one.

```python
def hello():
    return "Hello"

say = hello

print(say)

print(say())
```

Why are the outputs different?

---

# ⚔️ Code Duel

Version A

```python
players.sort(
    key=lambda p: p["goals"]
)
```

Version B

```python
def goal_key(player):
    return player["goals"]

players.sort(
    key=goal_key
)
```

Questions

Which is shorter?

Which is clearer?

Which would you choose if the logic became longer?

---

# 🤖 AI Engineer Lens

Believe it or not...

Everything you've learned in this workbook appears in AI.

Examples

Training

```python
train(model)
```

Prediction

```python
predict(image)
```

Loss

```python
loss(prediction, target)
```

Sorting

```python
sorted(
    predictions,
    key=lambda x: x.score
)
```

Data Processing

```python
dataset.map(transform)
```

Evaluation

```python
accuracy(y_true, y_pred)
```

AI code is filled with functions.

Mastering them now makes later topics much easier.

---

# 💼 Interview Corner

Explain in your own words.

1.

What's the difference between

```python
print()
```

and

```python
return
```

---

2.

Why are functions called first-class objects?

---

3.

When would you choose

```python
lambda
```

instead of

```python
def
```

---

4.

Why shouldn't large functions be replaced with lambda?

---

5.

What problem does

```python
*args
```

solve?

---

6.

What problem does

```python
**kwargs
```

solve?

---

7.

Why is this dangerous?

```python
def add(item, basket=[]):
```

---

# 🏃 Practice Challenge

Create these functions.

```
is_even()

factorial()

power()

largest()

smallest()

average()

median()

count_vowels()

reverse_string()

is_palindrome()
```

No copying from Google.

Build them yourself.

---

# 🧠 Reflection

Can you now explain...

Without looking...

✔ Parameters

✔ Arguments

✔ Return values

✔ Scope

✔ Mutable objects

✔ Lambda

✔ First-class functions

✔ Annotations

✔ Docstrings

If you can explain them...

You've learned them.

If not...

Review before moving on.

---

# 📋 Functions Cheatsheet

## Define

```python
def greet():
    pass
```

---

## Return

```python
return value
```

---

## Default Argument

```python
def greet(name="Friend"):
```

---

## Variable Arguments

```python
*args

**kwargs
```

---

## Lambda

```python
lambda x: x * 2
```

---

## Annotation

```python
def add(a:int,b:int)->int:
```

---

## Docstring

```python
"""
Description
"""
```

---

# 🏆 Graduation

Congratulations.

You now understand one of the most important concepts in Python.

Functions.

Everything that follows—

Files

Modules

Exceptions

Classes

Decorators

Generators

NumPy

Pandas

scikit-learn

PyTorch

—all build upon what you've learned here.

Take your time.

Practise.

Experiment.

Write bad functions.

Rewrite them.

That's how good Python developers are made.

---

# 🌉 Next Stop

## Python Fluency Workbook 02

# Files & Modules

Soon you'll learn how to make your programs remember things.

Instead of

```python
players = []
```

disappearing every time your program closes...

You'll save them to

```text
players.txt
```

then

```text
players.csv
```

Eventually...

Those files become datasets.

Those datasets become machine learning models.

Your AI journey continues there.

🚀
