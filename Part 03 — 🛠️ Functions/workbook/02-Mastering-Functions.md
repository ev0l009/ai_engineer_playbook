# Python Fluency Workbook 01 — Functions
## Batch 2 — Mastering Functions

# Scope & the LEGB Rule

Variables live in different scopes.

- **L**ocal
- **E**nclosing
- **G**lobal
- **B**uilt-in

```python
x = 10

def show():
    x = 5
    return x

print(show())  # 5
print(x)       # 10
```

Python looks for names in LEGB order.

---

# Mutable vs Immutable

Immutable objects (int, str, tuple) create new values.

```python
def add_one(n):
    n += 1
    return n
```

The original integer is unchanged.

Mutable objects (list, dict, set) can be modified.

```python
def add_item(items):
    items.append("Python")

langs = ["Go"]
add_item(langs)
print(langs)
```

Why? Because both names reference the same list object.

---

# Object References

Python passes object references.

```python
def rename(names):
    names[0] = "Ada"

people = ["Grace", "Linus"]
rename(people)
```

Predict the final value of `people` before running it.

---

# Default Arguments

Safe:

```python
def greet(name="Friend"):
    return f"Hello {name}"
```

Dangerous:

```python
def add(item, basket=[]):
    basket.append(item)
    return basket
```

Every call shares the same default list.

Correct pattern:

```python
def add(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket
```

---

# Keyword Arguments

```python
def introduce(name, age):
    return f"{name} is {age}"

introduce(age=26, name="Valerian")
```

Keyword arguments improve readability.

---

# *args

Collect extra positional arguments.

```python
def total(*numbers):
    return sum(numbers)
```

---

# **kwargs

Collect extra keyword arguments.

```python
def profile(**info):
    return info
```

---

# Common Mistakes

- Changing mutable arguments accidentally.
- Using mutable default parameters.
- Confusing local and global variables.

---

# Checkpoint

Explain:

1. Why did the list change but the integer didn't?
2. Why is `basket=[]` a bug?

---

# Exercises

## Easy

- Write `maximum(*numbers)`.
- Write `greet(name="Friend")`.

## Medium

- Build a function that accepts any number of exam scores and returns the average.
- Build a function that accepts arbitrary keyword arguments for a football player profile.

## Hard

Write a menu system where each menu action is implemented as its own function and user choices are passed between functions.

---

# Stop Here

Before Batch 3 you should be comfortable explaining:

- LEGB
- Mutable vs immutable
- Object references
- Default arguments
- *args and **kwargs
