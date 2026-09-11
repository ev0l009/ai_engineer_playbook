# 🤖 The AI Engineer Playbook
# 🏛️ Workbook 03 — Object-Oriented Programming
## Batch 2 — Classes, Objects & Constructors

> *"A class defines what something is.*
> *An object is that thing brought to life."*

---

# 🎯 Learning Objectives

By the end of this batch you should be able to

✅ Create your own classes

✅ Create objects (instances)

✅ Understand constructors (`__init__`)

✅ Understand `self`

✅ Add attributes to objects

✅ Create methods

---

# 🧭 Where You Are

```text
🤖 AI Engineer Playbook

Phase 1 — Python Fluency

████████████████████████████████░░░░ 70%

✅ Foundations
✅ Functions
✅ Collections

🟢 Object-Oriented Programming

    ✅ Thinking in Objects
    ⏳ Classes & Constructors
    ⬜ Inheritance
    ⬜ Polymorphism
    ⬜ Magic Methods
```

---

# 🏗️ Creating Your First Class

In Python, classes are created with the `class` keyword.

```python
class Player:
    pass
```

Congratulations.

You've just created a class.

But...

It doesn't do anything yet.

---

# 🤔 What is `pass`?

Python expects every class and function to contain code.

Sometimes we're not ready yet.

```python
class Player:
    pass
```

`pass` simply means

> "I'll implement this later."

---

# 👤 Creating an Object

Having a class isn't enough.

You must create an object from it.

```python
class Player:
    pass

james = Player()
```

Congratulations again.

`james` is now an object.

---

Think of it like this.

```text
Player Class

        │

        ▼

James Object
```

---

# 📦 What Can This Object Do?

Right now...

Nothing.

It has no data.

No actions.

Let's fix that.

---

# 🏗️ Constructors

Every time Python creates an object...

it asks

> "How should I build it?"

The answer is the constructor.

In Python, constructors are written as

```python
__init__
```

Pronounced

> "dunder init"

(Dunder = Double Under)

---

# Your First Constructor

```python
class Player:

    def __init__(self):
        print("Player created!")
```

Now

```python
james = Player()
```

Output

```text
Player created!
```

Notice something.

You never called

```python
__init__()
```

Python did it automatically.

---

# 🧠 Why Does `__init__` Exist?

Imagine building a football player.

Every player needs

- Name
- Age
- Position

Instead of adding them one by one...

We provide them immediately.

---

```python
class Player:

    def __init__(self, name, age, position):

        self.name = name
        self.age = age
        self.position = position
```

Now we can create players properly.

```python
james = Player(
    "James",
    22,
    "CDM"
)
```

---

# 🤔 Meet `self`

This confuses almost everyone.

Let's simplify it.

Suppose you have two players.

```python
james = Player("James",22,"CDM")

david = Player("David",24,"CB")
```

Where should James' name be stored?

Inside James.

Where should David's name be stored?

Inside David.

That's exactly what `self` means.

> **The object currently being created or used.**

---

Imagine Python secretly doing this.

```text
James.name

James.age

James.position
```

and

```text
David.name

David.age

David.position
```

Each object owns its own data.

---

# 📦 Attributes

Anything attached to `self`

becomes an attribute.

```python
self.name = name
```

creates

```python
james.name
```

and

```python
david.name
```

Each object gets its own copy.

---

# 🏃 Accessing Attributes

```python
print(james.name)
```

Output

```text
James
```

---

```python
print(james.position)
```

Output

```text
CDM
```

---

# ✏️ Updating Attributes

Objects can change.

```python
james.age = 23
```

Now

```python
print(james.age)
```

Output

```text
23
```

---

# ⚙️ Adding Methods

Objects don't just store information.

They perform actions.

```python
class Player:

    def __init__(self, name):

        self.name = name

    def celebrate(self):

        print(self.name, "celebrates!")
```

Usage

```python
james = Player("James")

james.celebrate()
```

Output

```text
James celebrates!
```

---

Notice

Methods always receive

```python
self
```

as the first parameter.

Python supplies it automatically.

---

# ⚽ Football Academy AI

Let's build a better player.

```python
class Player:

    def __init__(self, name, age, position):

        self.name = name
        self.age = age
        self.position = position
        self.goals = 0

    def score_goal(self):

        self.goals += 1

    def display(self):

        print("Name:", self.name)
        print("Age:", self.age)
        print("Position:", self.position)
        print("Goals:", self.goals)
```

Usage

```python
james = Player(
    "James",
    22,
    "CDM"
)

james.score_goal()
james.score_goal()

james.display()
```

Output

```text
Name: James
Age: 22
Position: CDM
Goals: 2
```

Now our player isn't just data.

It's an object with behavior.

---

# 🐞 Debugging Lab

Predict the error.

```python
class Player:

    def __init__(name):

        self.name = name
```

What's wrong?

Hint:

Where did `self` go?

---

Another one.

```python
class Player:

    def __init__(self, name):

        self.name = name

player = Player()
```

Why does this fail?

Because the constructor expects

```python
name
```

but none was supplied.

---

# 🏃 Practice

## Easy

Create a

```python
Book
```

class.

Attributes

- title
- author

Create one object.

Print both attributes.

---

## Medium

Create a

```python
Car
```

class.

Attributes

- brand
- model
- year

Method

```python
start()
```

Output

```text
Toyota Corolla has started.
```

---

## Hard

Create a

```python
FootballPlayer
```

class.

Attributes

- name
- age
- position
- goals

Methods

- score_goal()
- assist()
- display_profile()

Create three players.

Simulate a match.

Display the updated profiles.

---

# 🤖 AI Engineer Lens

Almost every library you use later will be built around classes.

For example:

```python
model = RandomForestClassifier()
```

```python
model.fit(X_train, y_train)
```

```python
predictions = model.predict(X_test)
```

`RandomForestClassifier` is a class.

`model` is an object.

You're learning the exact same concepts used by professional ML libraries.

---

# 💡 Chapter Summary

You learned

- `class` defines a new type.
- Objects are created from classes.
- `__init__` runs automatically.
- `self` refers to the current object.
- Attributes store object data.
- Methods define object behavior.

---

# 🌱 Growth Log

Reflect honestly.

- Why is `__init__` useful?

- What does `self` actually represent?

- Can two objects from the same class have different attribute values?

- Why are methods written inside the class instead of as standalone functions?

If your answer is **yes**, you're ready for inheritance.

---

> 🚀 Coming Up

## 🧬 Batch 3 — Inheritance & `super()`

You'll learn how one class can build upon another, reducing repetition and creating cleaner, more powerful designs.