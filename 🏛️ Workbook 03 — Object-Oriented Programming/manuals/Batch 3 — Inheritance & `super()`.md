# 🤖 The AI Engineer Playbook
# 🏛️ Workbook 03 — Object-Oriented Programming
## Batch 3 — Inheritance & `super()`

> *"Why write the same code twice when one class can build upon another?"*

---

# 🎯 Learning Objectives

By the end of this batch you should be able to

✅ Explain inheritance

✅ Create parent and child classes

✅ Reuse code through inheritance

✅ Understand method overriding

✅ Use `super()`

✅ Decide when inheritance is appropriate

---

# 🧭 Where You Are

```text
🤖 AI Engineer Playbook

Phase 1 — Python Fluency

██████████████████████████████████░░ 75%

✅ Foundations
✅ Functions
✅ Collections

🟢 Object-Oriented Programming

    ✅ Thinking in Objects
    ✅ Classes & Constructors
    ⏳ Inheritance
    ⬜ Polymorphism
    ⬜ Magic Methods
```

---

# 🤔 The Problem

Imagine your academy has

- Goalkeepers
- Defenders
- Midfielders
- Forwards

You might write

```python
class Goalkeeper:
```

```python
class Defender:
```

```python
class Midfielder:
```

```python
class Forward:
```

Each one has

- name
- age
- position
- display_profile()

That's a lot of repeated code.

---

# 🧠 The Better Question

Instead of asking

> "What makes a goalkeeper?"

Ask

> "Is a goalkeeper also a player?"

Of course.

A goalkeeper **is a Player**.

A defender **is a Player**.

A midfielder **is a Player**.

A forward **is a Player**.

So why not reuse the Player class?

That's inheritance.

---

# 🏛️ Parent Class

```python
class Player:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def display(self):

        print(self.name, self.age)
```

This is our parent (or base) class.

---

# 👶 Child Class

A goalkeeper is a specialized player.

```python
class Goalkeeper(Player):
    pass
```

That's it.

`Goalkeeper` now inherits everything from `Player`.

---

# 🏃 Creating Objects

```python
keeper = Goalkeeper("David", 26)

keeper.display()
```

Output

```text
David 26
```

Even though `Goalkeeper` doesn't define `display()`!

It inherited it.

---

# 📚 Mental Model

Think of a family tree.

```text
           Player

          /   |   \

 Goalkeeper Defender Forward
```

Children inherit characteristics from their parent.

---

# ⚙️ Adding New Abilities

Goalkeepers can dive.

Players generally can't.

```python
class Goalkeeper(Player):

    def dive(self):

        print(self.name, "dives!")
```

Now

```python
keeper.display()

keeper.dive()
```

Output

```text
David 26

David dives!
```

The child class has

- everything from the parent
- plus its own features

---

# 🤔 What About Constructors?

Suppose we want

Goalkeepers to also have

```text
clean_sheets
```

We could write

```python
class Goalkeeper(Player):

    def __init__(self, name, age):

        self.name = name
        self.age = age
        self.clean_sheets = 0
```

This works...

But we've copied code from `Player`.

Not ideal.

---

# 🌟 Enter `super()`

`super()` lets us reuse the parent's constructor.

```python
class Goalkeeper(Player):

    def __init__(self, name, age):

        super().__init__(name, age)

        self.clean_sheets = 0
```

Now

- `Player` handles `name` and `age`
- `Goalkeeper` only adds `clean_sheets`

Much cleaner.

---

# 📚 What Does `super()` Mean?

Think of it like this.

The child says:

> "Hey Parent...

Can you do your part first?

Then I'll finish the rest."

That's exactly what

```python
super().__init__()
```

does.

---

# ⚽ Football Academy AI

Let's build it.

```python
class Player:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def introduce(self):

        print(self.name, "-", self.age)
```

---

```python
class Goalkeeper(Player):

    def __init__(self, name, age):

        super().__init__(name, age)

        self.clean_sheets = 0

    def save_penalty(self):

        print(self.name, "saved a penalty!")
```

---

Usage

```python
keeper = Goalkeeper("David", 25)

keeper.introduce()

keeper.save_penalty()
```

Output

```text
David - 25

David saved a penalty!
```

---

# 🐞 Debugging Lab

Predict the error.

```python
class Goalkeeper(Player):

    def __init__(self):

        self.clean_sheets = 0
```

Now

```python
keeper = Goalkeeper()

print(keeper.name)
```

Why does this fail?

Because the parent constructor never ran.

---

Another one.

```python
class Goalkeeper(Player):

    def __init__(self, name):

        super().__init__()
```

What's missing?

The parent's constructor expects

```python
name

age
```

Both must be passed.

---

# 🏃 Practice

## Easy

Create

```python
Animal
```

Attributes

- name

Method

```python
speak()
```

Create

```python
Dog(Animal)
```

Add

```python
bark()
```

---

## Medium

Create

```python
Vehicle
```

Attributes

- brand

Method

```python
start()
```

Create

```python
Car(Vehicle)
```

Add

```python
honk()
```

---

## Hard

Create

```python
Player
```

Attributes

- name
- age

Methods

- train()
- display()

Create

```python
Defender
Midfielder
Forward
Goalkeeper
```

Each should inherit from Player.

Give each class one unique method.

Examples

```text
tackle()

through_ball()

shoot()

save()
```

---

# 🤖 AI Engineer Lens

Inheritance appears in many libraries.

Example

```python
NeuralNetwork
```

↓

```python
CNN
```

↓

```python
ResNet
```

Each specialized model inherits common behavior from a more general one.

The same idea appears in game engines, web frameworks, and GUI toolkits.

---

# 💡 Chapter Summary

You learned

- Inheritance lets one class reuse another.
- Parent classes hold shared behavior.
- Child classes extend that behavior.
- `super()` calls the parent implementation.
- Inheritance reduces duplication.

---

# 🌱 Growth Log

Reflect honestly.

- Why is inheritance useful?

- When should I use `super()`?

- Why shouldn't I copy the parent's constructor?

- Can I explain the relationship between `Player` and `Goalkeeper`?

If your answer is **yes**, you're ready for polymorphism.

---

> 🚀 Coming Up

## 🎭 Batch 4 — Polymorphism

You'll discover how different classes can respond to the same method call in different ways—one of the most elegant ideas in object-oriented programming.