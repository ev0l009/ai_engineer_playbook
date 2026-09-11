# 🤖 The AI Engineer Playbook
# 🏛️ Workbook 03 — Object-Oriented Programming
## Batch 4 — Polymorphism

> *"One interface. Many behaviors."*

---

# 🎯 Learning Objectives

By the end of this batch you should be able to

✅ Explain polymorphism

✅ Override inherited methods

✅ Understand method overriding

✅ Recognize duck typing in Python

✅ Write flexible object-oriented code

---

# 🧭 Where You Are

```text
🤖 AI Engineer Playbook

Phase 1 — Python Fluency

████████████████████████████████████░ 80%

✅ Foundations
✅ Functions
✅ Collections

🟢 Object-Oriented Programming

    ✅ Thinking in Objects
    ✅ Classes & Constructors
    ✅ Inheritance
    ⏳ Polymorphism
    ⬜ Magic Methods
```

---

# 🤔 What Does "Polymorphism" Mean?

The word comes from Greek.

```text
Poly = Many

Morph = Forms
```

Literally

> **Many Forms**

In programming...

It means

**different objects can respond to the same message in different ways.**

---

# 🧠 Imagine Training Day

Every player trains.

But...

A goalkeeper trains differently from a striker.

Yet we still say

```text
train()
```

The action is the same.

The behavior is different.

That's polymorphism.

---

# 🏛️ Parent Class

```python
class Player:

    def __init__(self, name):
        self.name = name

    def train(self):
        print(self.name, "is training.")
```

---

# 👶 Child Classes

A goalkeeper trains differently.

```python
class Goalkeeper(Player):

    def train(self):
        print(self.name, "is practicing saves.")
```

---

A defender trains differently.

```python
class Defender(Player):

    def train(self):
        print(self.name, "is practicing tackles.")
```

---

A forward trains differently.

```python
class Forward(Player):

    def train(self):
        print(self.name, "is practicing finishing.")
```

---

# 🎭 Method Overriding

Notice something?

Every class has

```python
train()
```

But each one behaves differently.

This is called

**Method Overriding**.

The child class replaces the parent's implementation.

---

# 🏃 Using Polymorphism

```python
players = [

    Goalkeeper("David"),

    Defender("James"),

    Forward("Samuel")

]
```

Now

```python
for player in players:

    player.train()
```

Output

```text
David is practicing saves.

James is practicing tackles.

Samuel is practicing finishing.
```

One loop.

One method call.

Three different behaviors.

That's the power of polymorphism.

---

# 🤯 Why Is This Powerful?

Imagine adding

```python
Midfielder
```

Do we need to change the loop?

No.

Just define

```python
train()
```

inside `Midfielder`.

The loop already works.

Your code grows without becoming messy.

---

# 🦆 Duck Typing

Python has a famous idea.

> **"If it walks like a duck and quacks like a duck... it's a duck."**

Python doesn't care what class an object belongs to.

It cares whether the object can do what's being asked.

---

Example

```python
class Dog:

    def speak(self):
        print("Woof!")
```

```python
class Cat:

    def speak(self):
        print("Meow!")
```

Now

```python
animals = [

    Dog(),

    Cat()

]

for animal in animals:

    animal.speak()
```

Output

```text
Woof!

Meow!
```

We never asked

```python
if animal is Dog
```

or

```python
if animal is Cat
```

We simply called

```python
speak()
```

If the object supports it...

Python is happy.

That's duck typing.

---

# ⚽ Football Academy AI

Imagine match day.

```python
team = [

    Goalkeeper("David"),

    Defender("James"),

    Midfielder("Musa"),

    Forward("Samuel")

]
```

Every player warms up.

```python
for player in team:

    player.train()
```

No `if` statements.

No complicated checks.

Every object knows how to train itself.

Beautiful.

---

# 🚫 Without Polymorphism

You might write

```python
if player.position == "GK":

    ...

elif player.position == "CB":

    ...

elif player.position == "ST":

    ...
```

Every time you add a new position...

You edit this code again.

That violates one of the biggest software engineering goals:

> **Open for extension, closed for modification.**

Polymorphism avoids that.

---

# 🐞 Debugging Lab

Predict the output.

```python
class Animal:

    def speak(self):

        print("Some sound")

class Dog(Animal):

    pass

dog = Dog()

dog.speak()
```

Output?

```text
Some sound
```

Why?

Because `Dog` inherited the method and didn't override it.

---

Now

```python
class Dog(Animal):

    def speak(self):

        print("Woof!")
```

Output?

```text
Woof!
```

---

# 🏃 Practice

## Easy

Create

```python
Animal
```

Method

```python
move()
```

Create

```python
Bird
```

Override

```python
move()
```

Print

```text
Bird flies.
```

---

## Medium

Create

```python
Employee
```

Method

```python
work()
```

Create

```python
Developer
```

Override

```python
work()
```

Create

```python
Designer
```

Override

```python
work()
```

Store both objects in a list.

Loop through them.

Call

```python
work()
```

---

## Hard

Create

```python
Player
```

Method

```python
play()
```

Create

- Goalkeeper
- Defender
- Midfielder
- Forward

Override

```python
play()
```

Each should describe how that position contributes during a match.

Store them in one list.

Loop through the list.

Call

```python
play()
```

---

# 🤖 AI Engineer Lens

Polymorphism appears everywhere.

Imagine different machine learning models.

```python
LinearRegression

DecisionTree

RandomForest

NeuralNetwork
```

Each one has

```python
fit()
```

and

```python
predict()
```

You can write

```python
model.fit(data)

model.predict(test)
```

without caring which model you're using.

That's polymorphism in action.

---

# 💡 Chapter Summary

You learned

- Polymorphism means one interface, many behaviors.
- Child classes can override inherited methods.
- The same method call can produce different results.
- Duck typing focuses on behavior rather than exact type.
- Polymorphism reduces long chains of `if`/`elif` statements.

---

# 🌱 Growth Log

Reflect honestly.

- Why is overriding useful?

- Why didn't our loop need to know each player's type?

- Can I explain duck typing without mentioning ducks?

- Can I think of another real-world example where different things respond differently to the same action?

If your answer is **yes**, you're ready for the final OOP chapter.

---

# 🏅 OOP Progress

```text
🏛️ Object-Oriented Programming

████████████████████░░░░ 80%

✅ Thinking in Objects
✅ Classes & Constructors
✅ Inheritance
✅ Polymorphism
⏳ Magic Methods

↓

🏅 Object Architect
```

---

> 🚀 Coming Up

## ✨ Batch 5 — Magic (Dunder) Methods

You'll finally understand why Python methods like

- `__init__`
- `__str__`
- `__repr__`
- `__len__`
- `__eq__`

have double underscores—and how they make your own classes behave like built-in Python objects.