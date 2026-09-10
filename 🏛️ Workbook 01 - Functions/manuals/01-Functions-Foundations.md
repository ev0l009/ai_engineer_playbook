# Python Fluency Workbook 01 — Functions (Batch 1: Foundations)

> Goal: Build a solid understanding of Python functions and the Python-specific ideas you'll use throughout AI engineering.

## Progress

- 🟢 Functions (Current)
- ⚪ Files & Modules
- ⚪ Error Handling

---

# 1. Why Functions Exist

Functions let you **name a piece of reusable logic**.

Instead of repeating code:

```python
print("Hello")
print("Hello")
print("Hello")
```

you write:

```python
def greet():
    print("Hello")

greet()
greet()
greet()
```

Benefits:

- Reuse
- Readability
- Easier debugging
- Easier testing

> 🤖 AI Engineer Note:
> Functions are everywhere in Python libraries. Calls like `model.fit()` or `pd.read_csv()` are function (or method) calls.

---

# 2. Anatomy of a Function

```python
def add(a, b):
    return a + b
```

Breakdown:

- `def` → define a function
- `add` → function name
- `a, b` → parameters
- `return` → sends a value back

Flow:

```text
Call
 ↓
Parameters receive values
 ↓
Code runs
 ↓
Return value
```

---

# 3. Parameters vs Arguments

```python
def greet(name):      # parameter
    return f"Hello {name}"

greet("Valerian")     # argument
```

- **Parameter**: variable in the function definition.
- **Argument**: value passed into the function.

---

# 4. `print()` vs `return`

```python
def square(x):
    print(x*x)
```

prints the value.

```python
def square(x):
    return x*x
```

returns the value so it can be reused.

---

# 5. Quick Examples

```python
def is_even(n):
    return n % 2 == 0
```

```python
def full_name(first, last):
    return f"{first} {last}"
```

---

# 6. Think Like Python 🧠

Ask yourself:

- Why return a value instead of printing it?
- If another function needs the result, which should you use?

---

# 7. Common Mistakes

## Forgetting parentheses

```python
greet      # function object
greet()    # function call
```

## Printing instead of returning

```python
def add(a, b):
    print(a+b)
```

This cannot be reused in another calculation.

---

# 8. Checkpoint

Predict the output **before** running:

```python
def multiply(a, b):
    return a * b

x = multiply(4, 5)
print(x)
```

---

# 9. Exercises

## Easy

1. Write a function that returns the square of a number.
2. Write a function that returns the larger of two numbers.
3. Write a function that returns `True` if a number is positive.

## Medium

1. Write a function that counts vowels in a string.
2. Write a function that returns the average of a list.

## Hard

Write a function that receives a list of numbers and returns both the smallest and largest values.

---

# 10. Mini Challenge

Create a menu of functions:

- Celsius → Fahrenheit
- Fahrenheit → Celsius
- Kilometres → Miles

Call the correct function based on user input.

---

# 11. Stop Here ✅

Before Batch 2, make sure you can:

- Explain parameters vs arguments.
- Explain `print()` vs `return`.
- Write and call your own functions.
- Predict simple function outputs.

---

# Cheatsheet

| Concept | Meaning |
|---|---|
| `def` | Define a function |
| Parameter | Variable in the definition |
| Argument | Value passed in |
| `return` | Send a value back |
| `print()` | Display a value |
