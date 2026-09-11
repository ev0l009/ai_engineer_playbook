# 🤖 The AI Engineer Playbook
# 🏛️ Workbook 03 — Object-Oriented Programming
## Batch 5 — Magic (Dunder) Methods

> *"Make your classes feel like native Python objects."*

---

# 🎯 Learning Objectives

By the end of this batch you should be able to

✅ Explain what magic (dunder) methods are

✅ Understand when Python calls them automatically

✅ Implement

- `__str__`
- `__repr__`
- `__len__`
- `__eq__`

✅ Recognize other common dunder methods

---

# 🧭 Where You Are

```text
🤖 AI Engineer Playbook

Phase 1 — Python Fluency

█████████████████████████████████████░ 85%

✅ Foundations
✅ Functions
✅ Collections

🟢 Object-Oriented Programming

    ✅ Thinking in Objects
    ✅ Classes & Constructors
    ✅ Inheritance
    ✅ Polymorphism
    ⏳ Magic Methods
```

---

# 🤔 What Are Magic Methods?

You've already met one.

```python
__init__()
```

Remember...

You never called it yourself.

```python
player = Player(...)
```

Python called it automatically.

That's what magic methods are.

They are **special methods that Python automatically uses in certain situations.**

---

# Why "Dunder"?

```text
Double UNDERscore

↓

DUNDER
```

Example

```python
__init__

__str__

__len__

__eq__
```

---

# 🧠 Think About Built-in Objects

Suppose we have

```python
players = [
    "James",
    "David",
    "Samuel"
]
```

You can write

```python
len(players)
```

Output

```text
3
```

Why does this work?

Because Python secretly does

```python
players.__len__()
```

Interesting...

---

# Your Own Class

```python
class Team:

    pass
```

Now

```python
team = Team()

len(team)
```

Python says

```text
TypeError
```

Why?

Because your class doesn't know how to answer

"What is your length?"

---

# ⭐ __len__()

Let's teach it.

```python
class Team:

    def __init__(self):

        self.players = []

    def __len__(self):

        return len(self.players)
```

Now

```python
team = Team()

print(len(team))
```

Output

```text
0
```

After

```python
team.players.append("James")

team.players.append("David")
```

```python
print(len(team))
```

Output

```text
2
```

Awesome.

---

# ⭐ __str__()

Imagine this.

```python
player = Player("James")

print(player)
```

Output

```text
<__main__.Player object at 0x000001...>
```

😅

Not very useful.

Let's improve it.

---

```python
class Player:

    def __init__(self, name):

        self.name = name

    def __str__(self):

        return f"Player: {self.name}"
```

Now

```python
print(player)
```

Output

```text
Player: James
```

Much nicer.

---

# ⭐ __repr__()

`__repr__` is similar to `__str__`.

The idea is:

```text
__str__

↓

Friendly

```

```text
__repr__

↓

Developer-focused
```

Example

```python
class Player:

    def __repr__(self):

        return f"Player(name='{self.name}')"
```

Now

```python
player
```

might display

```text
Player(name='James')
```

Useful while debugging.

---

# ⭐ __eq__()

Suppose

```python
player1 = Player("James")

player2 = Player("James")
```

Now

```python
print(player1 == player2)
```

Output

```text
False
```

Wait...

Why?

Because Python compares the objects'

memory addresses.

Not their contents.

---

Let's change that.

```python
class Player:

    def __eq__(self, other):

        return self.name == other.name
```

Now

```python
player1 == player2
```

Output

```text
True
```

Now equality means something useful.

---

# ⚽ Football Academy AI

Let's combine everything.

```python
class Player:

    def __init__(self, name, position):

        self.name = name
        self.position = position

    def __str__(self):

        return f"{self.name} ({self.position})"

    def __eq__(self, other):

        return self.name == other.name
```

Usage

```python
james = Player(
    "James",
    "CDM"
)

print(james)
```

Output

```text
James (CDM)
```

---

# ⭐ More Magic Methods

You don't need to memorize these yet.

Just know they exist.

| Method | Purpose |
|---------|----------|
| `__init__` | Create an object |
| `__str__` | Human-readable string |
| `__repr__` | Developer representation |
| `__len__` | Used by `len()` |
| `__eq__` | Used by `==` |
| `__add__` | Used by `+` |
| `__contains__` | Used by `in` |
| `__getitem__` | Used by indexing `[]` |
| `__iter__` | Allows iteration (`for`) |

---

# 🧠 Why This Matters

Magic methods let your own classes behave like Python's built-in types.

Instead of feeling like something separate...

Your classes become first-class Python objects.

---

# 🤖 AI Engineer Lens

You won't write dunder methods every day...

But you'll constantly use classes that rely on them.

Example

```python
dataset[0]
```

works because the dataset class implements

```python
__getitem__()
```

---

```python
for batch in dataloader:
```

works because it implements

```python
__iter__()
```

---

```python
len(dataset)
```

works because it implements

```python
__len__()
```

Frameworks like PyTorch and pandas use these methods heavily.

---

# 🏃 Practice

## Easy

Create a

```python
Book
```

class.

Implement

```python
__str__()
```

Print the object.

---

## Medium

Create a

```python
Playlist
```

class.

Store songs in a list.

Implement

```python
__len__()
```

Verify

```python
len(playlist)
```

works.

---

## Hard

Create a

```python
FootballTeam
```

class.

Attributes

- team_name
- players

Implement

- `__str__`
- `__len__`

Create two teams.

Print both.

Display their sizes using `len()`.

---

# 🐞 Debugging Lab

Predict the output.

```python
class Book:

    def __str__(self):

        return "Python"

book = Book()

print(book)
```

Output?

```text
Python
```

---

Another one.

```python
class Team:

    pass

team = Team()

print(len(team))
```

Why does it fail?

Because `__len__()` hasn't been implemented.

---

# 💡 Chapter Summary

You learned

- Magic methods are special methods called automatically by Python.
- `__init__` initializes objects.
- `__str__` controls printable output.
- `__repr__` helps with debugging.
- `__len__` supports `len()`.
- `__eq__` customizes equality.

---

# 🌱 Growth Log

Reflect honestly.

- Why is `__str__` better than printing the default object?

- When would I use `__eq__`?

- Can I explain why `len(team)` works after implementing `__len__`?

If your answer is **yes**, you've completed the OOP workbook.

---

🎯 Final Boss Challenge — Football Academy AI (OOP Edition)
Build a mini Football Academy system with the following classes:
FootballAcademy
        │
        ├── stores players
        │
        ▼
      Player
        │
        ├── Goalkeeper
        ├── Defender
        ├── Midfielder
        └── Forward
Requirements
Player
Attributes:
name
age
position
Methods:
train()
play()
__str__()
Child Classes

Each should:

Inherit from Player
Use super()
Override play()
Add one unique method

Examples:

Goalkeeper → save_penalty()
Defender → block_shot()
Midfielder → through_ball()
Forward → finish_chance()
FootballAcademy

Should:

Store players
Add players
Remove players
Display all players
Return the number of players using __len__()

# 🏅 Badge Unlocked

🏛️ **Object Architect**

You can now design object-oriented programs using:

✅ Classes

✅ Objects

✅ Constructors

✅ Inheritance

✅ Polymorphism

✅ Magic Methods

This is a major milestone in becoming a Python developer.