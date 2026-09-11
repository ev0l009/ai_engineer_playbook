# 🐍 PART 7 — PROFESSIONAL PYTHON
# 📜 BATCH 4 — DOCSTRINGS

> 🎯 Mission:
> Turn your functions, classes, and modules into self-explanatory
> pieces of software that other developers — and future you —
> can understand without reverse-engineering the code.

---

# 🗺️ PART 7 PROGRESS MAP

```text
PART 7 — PROFESSIONAL PYTHON
│
├── Batch 1 — Exception Handling        ✅
├── Batch 2 — Static Typing             ✅
├── Batch 3 — Documentation             ✅
├── Batch 4 — Docstrings                🔥 YOU ARE HERE
├── Batch 5 — Pytest                    ⬜
└── 🥋 PART 7 BOSS FIGHT                ⬜
````

---

# 🧠 THE BIG IDEA

You've already learned that documentation explains your project.

Now we're zooming in.

A **docstring** is documentation written directly inside Python code.

Example:

```python
def greet(name: str) -> str:
    """Return a greeting for the given name."""
    return f"Hello, {name}"
```

That string:

```python
"""Return a greeting for the given name."""
```

is a **docstring**.

It belongs to the function.

---

# ⚔️ THE PROBLEM

Compare these:

```python
def calculate(a, b):
    return a * b
```

and:

```python
def calculate(a: float, b: float) -> float:
    """Calculate the total cost from price and quantity."""
    return a * b
```

The second version gives us:

```text
Name
  ↓
calculate

Inputs
  ↓
a: float
b: float

Output
  ↓
float

Purpose
  ↓
Calculate total cost
```

That's much easier to understand.

---

# 🧠 COMMENTS ≠ DOCSTRINGS

This is a comment:

```python
# Calculate the total
total = price * quantity
```

This is a docstring:

```python
def calculate_total(price: float, quantity: int) -> float:
    """Calculate the total price."""
    return price * quantity
```

The key difference:

```text
COMMENT
    ↓
Usually explains a specific piece of implementation.

DOCSTRING
    ↓
Documents a Python object.
```

Python objects that commonly have docstrings include:

```text
Modules
Functions
Classes
Methods
```

---

# 🔥 WHY DOCSTRINGS MATTER

Docstrings can be used by:

```text
IDEs
Documentation generators
Developers
Python's introspection tools
```

For example, Python lets you inspect a function's documentation through:

```python
help(function_name)
```

And you can access its docstring through:

```python
function_name.__doc__
```

So unlike an ordinary comment, a docstring is actually attached to the object.

---

# 🧠 FIRST RULE

A docstring must be the first statement inside the object it documents.

Correct:

```python
def greet(name: str) -> str:
    """Return a greeting."""
    return f"Hello {name}"
```

Incorrect as a function docstring:

```python
def greet(name: str) -> str:
    print("Hello")
    """Return a greeting."""
```

The string isn't serving as the function's docstring there.

---

# 🥋 PRACTICE 1 — YOUR FIRST DOCSTRINGS

Add a useful docstring to each function.

### A

```python
def add(a: int, b: int) -> int:
    return a + b
```

### B

```python
def is_adult(age: int) -> bool:
    return age >= 18
```

### C

```python
def get_full_name(first: str, last: str) -> str:
    return f"{first} {last}"
```

Don't overthink them.

The docstring should explain the function's purpose.

---

# 🔥 WHAT MAKES A GOOD DOCSTRING?

A good docstring should answer:

```text
What does this thing do?
```

For example:

```python
def calculate_average(scores: list[int]) -> float:
    """Return the average of the given scores."""
    return sum(scores) / len(scores)
```

Notice how concise it is.

We don't need:

```text
This function is a function that takes a list...
```

😂

Say what matters.

---

# ⚠️ THE REDUNDANCY TRAP

Consider:

```python
def add(a: int, b: int) -> int:
    """Add two integers and return an integer."""
    return a + b
```

It's not terrible.

But the type hints already tell us:

```text
a → int
b → int
return → int
```

The docstring should focus on useful behavior.

Better:

```python
def add(a: int, b: int) -> int:
    """Return the sum of two numbers."""
    return a + b
```

---

# 🧠 DOCSTRINGS SHOULD EXPLAIN BEHAVIOR

Consider:

```python
def withdraw(balance: float, amount: float) -> float:
    """Withdraw money from an account."""
```

That's okay.

But perhaps this function rejects insufficient funds.

Then that behavior matters:

```python
def withdraw(balance: float, amount: float) -> float:
    """Withdraw an amount from the balance.

    Raises ValueError if the amount exceeds the balance.
    """
```

Now the reader knows something important.

---

# 🔥 DOCSTRINGS + EXCEPTION HANDLING

This connects directly to Batch 1.

Suppose:

```python
def withdraw(balance: float, amount: float) -> float:
    """Withdraw money from an account.

    Raises:
        ValueError: If the withdrawal exceeds the balance.
    """
    if amount > balance:
        raise ValueError("Insufficient funds")

    return balance - amount
```

Now the contract is clear:

```text
Input
  ↓
balance, amount

Output
  ↓
float

Possible failure
  ↓
ValueError
```

This is professional documentation.

---

# 🧠 DOCSTRING AS A CONTRACT

Think of a documented function as having a contract:

```text
┌──────────────────────────────┐
│          FUNCTION            │
├──────────────────────────────┤
│ What does it do?             │
│ What does it accept?         │
│ What does it return?         │
│ What can go wrong?           │
│ What assumptions exist?      │
└──────────────────────────────┘
```

Type hints handle a lot of:

```text
What types go in/out?
```

Docstrings handle:

```text
What does the operation actually mean?
```

Together:

```text
TYPE HINTS + DOCSTRINGS
          ↓
      Clear API
```

---

# 🧠 PARAMETERS

When a function has several parameters, a docstring can explain what they mean.

For example:

```python
def calculate_discount(
    price: float,
    percentage: float
) -> float:
    """Calculate a discounted price.

    Args:
        price: The original price.
        percentage: The discount percentage.

    Returns:
        The price after applying the discount.
    """
```

This style is commonly used in Python projects.

---

# 🧩 THE STRUCTURE

A detailed docstring can contain:

```text
Summary
   ↓
Args
   ↓
Returns
   ↓
Raises
```

For example:

```python
def withdraw(
    balance: float,
    amount: float
) -> float:
    """Withdraw money from an account.

    Args:
        balance: Current account balance.
        amount: Amount to withdraw.

    Returns:
        The remaining account balance.

    Raises:
        ValueError: If amount is greater than balance.
    """
```

---

# 🧠 DO YOU ALWAYS NEED ALL FOUR?

No.

Don't write:

```python
Args:
Returns:
Raises:
Notes:
Examples:
Warnings:
...
```

for a function like:

```python
def add(a: int, b: int) -> int:
```

That would be ridiculous.

😂

Use the level of documentation appropriate to the complexity.

---

# 📏 DOCSTRING DETAIL LEVELS

## Level 1 — Simple

```python
def add(a: int, b: int) -> int:
    """Return the sum of two numbers."""
```

Perfectly reasonable.

---

## Level 2 — Parameters and return

```python
def calculate_tax(price: float, rate: float) -> float:
    """Calculate tax for a given price and rate.

    Args:
        price: The original price.
        rate: The tax rate as a decimal.

    Returns:
        The calculated tax amount.
    """
```

Useful when the meaning isn't obvious.

---

## Level 3 — Complex behavior

```python
def withdraw(balance: float, amount: float) -> float:
    """Withdraw money from an account.

    Args:
        balance: Current account balance.
        amount: Amount to withdraw.

    Returns:
        Remaining balance after the withdrawal.

    Raises:
        ValueError: If amount is negative or exceeds balance.
    """
```

Now we're documenting behavior that matters.

---

# 🥋 PRACTICE 2 — DOCUMENT THE CONTRACT

Write a detailed docstring for:

```python
def withdraw(
    balance: float,
    amount: float
) -> float:
    if amount < 0:
        raise ValueError("Amount cannot be negative")

    if amount > balance:
        raise ValueError("Insufficient funds")

    return balance - amount
```

Your docstring should communicate:

```text
Purpose
Arguments
Return value
Possible exception
```

---

# 🔥 DOCSTRINGS FOR CLASSES

Functions aren't the only objects that can have docstrings.

Classes can too.

Example:

```python
class Player:
    """Represent a football player."""

    def __init__(
        self,
        name: str,
        age: int,
        rating: float
    ):
        self.name = name
        self.age = age
        self.rating = rating
```

The class docstring explains what the class represents.

---

# 🧠 CLASS DOCSTRING

A useful class docstring might explain:

```text
What does this object represent?
What is its purpose?
What important behavior does it provide?
```

For example:

```python
class Wallet:
    """Represent a user's wallet and its current balance."""
```

Simple.

Clear.

Useful.

---

# 🥋 PRACTICE 3 — CLASS DOCSTRINGS

Add appropriate class docstrings to:

```python
class Player:
    ...
```

```python
class Wallet:
    ...
```

```python
class Product:
    ...
```

Think about what each object represents.

---

# 🔥 METHOD DOCSTRINGS

Methods can have docstrings too:

```python
class Wallet:
    """Represent a user's wallet."""

    def deposit(self, amount: float) -> None:
        """Add money to the wallet."""
        ...
```

And:

```python
    def withdraw(self, amount: float) -> None:
        """Remove money from the wallet."""
        ...
```

Notice the hierarchy:

```text
Wallet
│
├── class docstring
│
├── deposit()
│   └── method docstring
│
└── withdraw()
    └── method docstring
```

---

# 📦 MODULE DOCSTRINGS

A module is simply a Python file.

You can document the entire module by putting a docstring at the top:

```python
"""Utilities for working with football players."""

class Player:
    ...
```

The module docstring tells the reader:

> "What is this file responsible for?"

---

# 🧠 THREE LEVELS

Lock this in:

```text
MODULE
  ↓
"What is this file for?"

CLASS
  ↓
"What does this object represent?"

FUNCTION / METHOD
  ↓
"What does this operation do?"
```

That's a very useful mental model.

---

# 🥋 PRACTICE 4 — DOCUMENT THE WHOLE MODULE

Imagine this file:

```python
class Player:
    ...

def find_player(players, name):
    ...

def calculate_average_rating(players):
    ...
```

Write a module-level docstring describing the purpose of the file.

Then add docstrings to the class and functions.

---

# 🔥 DOCSTRING STYLE

There are several conventions for writing docstrings.

You may encounter:

```text
Google style
Sphinx style
NumPy style
```

You don't need to memorize every format right now.

The important thing is:

```text
Pick a consistent style.
```

For this curriculum, we'll primarily use the clean:

```text
Summary

Args:
Returns:
Raises:
```

style.

---

# 🧠 WHY CONSISTENCY MATTERS

Imagine this:

```text
function A → Google style
function B → random style
function C → no documentation
function D → 40-line essay
function E → emojis only
```

😂

That's not a professional codebase.

Consistency makes documentation predictable.

---

# ⚔️ DEBUGGING LAB #1 — DOCSTRING IN THE WRONG PLACE

What's wrong?

```python
def greet(name: str) -> str:
    print("Starting greeting")
    """Return a greeting for the user."""
    return f"Hello {name}"
```

Explain why Python doesn't treat that string as the function's docstring.

Then fix it.

---

# ⚔️ DEBUGGING LAB #2 — USELESS DOCSTRING

Improve this:

```python
def calculate_total(price: float, quantity: int) -> float:
    """This function calculates the total."""
    return price * quantity
```

Ask:

```text
What useful information is missing?
```

You don't necessarily need a huge docstring.

Make it better without making it bloated.

---

# ⚔️ DEBUGGING LAB #3 — MISSING RAISES

Consider:

```python
def divide(a: float, b: float) -> float:
    """Divide a by b.

    Args:
        a: The numerator.
        b: The denominator.

    Returns:
        The result of the division.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b
```

What's missing from the documentation?

Add the appropriate `Raises` section.

---

# ⚔️ DEBUGGING LAB #4 — WRONG DOCUMENTATION

```python
def find_player(
    players: list[str],
    name: str
) -> str | None:
    """Return the player's rating."""
```

But the function actually returns:

```text
player name
OR
None
```

What's wrong?

The code and documentation disagree.

Fix the docstring.

---

# 🧠 DOCUMENTATION MUST MATCH CODE

This is critical.

Bad:

```python
def get_rating(player: str) -> float:
    """Return the player's age."""
```

The type hints say:

```text
float
```

The documentation says:

```text
age
```

The implementation might say:

```text
rating
```

Three different stories.

💀

Professional code should have:

```text
Implementation
      ↕
Type hints
      ↕
Documentation
```

all agreeing.

---

# 🔥 DOCSTRINGS AND IDEs

Modern editors can use docstrings to show information while you're coding.

Imagine calling:

```python
calculate_discount(
```

Your editor may display:

```text
calculate_discount(price, percentage)

Calculate a discounted price.

price:
    The original price.

percentage:
    The discount percentage.
```

You don't need to open another file.

The documentation travels with the code.

That's one reason docstrings are so useful.

---

# 🧠 DOCSTRINGS + AUTOCOMPLETION

The bigger ecosystem looks like:

```text
Type hints
    ↓
IDE understands types

Docstrings
    ↓
IDE understands meaning

Together
    ↓
Better developer experience
```

This is one of the reasons professional Python code feels much nicer to work with.

---

# 🥋 PRACTICE 5 — BUILD A DOCUMENTED API

Create these functions:

```python
def add_player(
    name: str,
    age: int,
    rating: float
) -> None:
    ...
```

```python
def find_player(
    name: str
) -> dict[str, object] | None:
    ...
```

```python
def get_rating(
    name: str
) -> float | None:
    ...
```

For each function:

```text
[ ] Add a useful summary
[ ] Document parameters where useful
[ ] Document return behavior
[ ] Document exceptions if applicable
[ ] Keep the documentation concise
```

---

# 🚀 MINI PROJECT — DOCUMENT THE FOOTBALL ACADEMY

Take a section of your Football Academy project.

At minimum, document:

```text
1 module
1 class
3 functions/methods
```

For example:

```text
players.py
│
├── module docstring
│
├── Player
│   └── class docstring
│
├── add_player()
│   └── function docstring
│
├── find_player()
│   └── function docstring
│
└── remove_player()
    └── function docstring
```

Don't just write descriptions.

Document the actual behavior.

---

# 🔥 HARD MODE — DOCUMENTATION AUDIT

Take an older project of yours.

Find five functions.

For each one, ask:

```text
1. Does it have a docstring?

2. Does the docstring explain what it does?

3. Are the parameters clear?

4. Is the return behavior clear?

5. Are important exceptions documented?

6. Does the documentation still match the code?

7. Could I understand this function six months from now?
```

Give each function a score:

```text
0 — undocumented
1 — barely useful
2 — acceptable
3 — clear
4 — professional
```

Then improve the weakest one.

---

# 🧠 WHEN NOT TO WRITE A HUGE DOCSTRING

This:

```python
def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
```

is enough.

You don't need:

```text
Args:
    a: First integer...
    b: Second integer...

Returns:
    An integer representing...
    
Examples:
    ...

Notes:
    Addition is...
    
Implementation:
    ...
```

😂

Documentation has a cost.

The goal is:

```text
Maximum useful information
        ↓
Minimum unnecessary noise
```

---

# ⚔️ THE DOCSTRING DECISION TREE

When documenting a function, ask:

```text
Does the function need explanation?
        │
        ├── NO
        │    ↓
        │  Keep it concise.
        │
        └── YES
             ↓
        What needs explaining?
             │
             ├── Purpose
             │
             ├── Parameters
             │
             ├── Return behavior
             │
             ├── Exceptions
             │
             └── Important assumptions
```

Don't document for the sake of documentation.

Document for the reader.

---

# 🧠 DOCSTRINGS AND PUBLIC APIs

Docstrings become especially important when code is intended for other developers.

For example:

```text
Your private helper
    ↓
Small amount of documentation may be enough.

Public library function
    ↓
Clear documentation becomes much more important.
```

If you're publishing a Python package, users shouldn't have to inspect your implementation to understand how to use your API.

---

# 🥋 SKILL CHECK — ROUND 1

Answer from memory.

### 1.

What is a docstring?

### 2.

Where must a function's docstring appear?

### 3.

What's the difference between a comment and a docstring?

### 4.

What Python objects commonly have docstrings?

### 5.

How can you inspect an object's documentation interactively?

### 6.

When should a docstring mention exceptions?

### 7.

Why shouldn't every docstring be extremely detailed?

---

# 🥋 SKILL CHECK — ROUND 2

Write the docstring for:

```python
def calculate_average(scores: list[int]) -> float:
    ...
```

Then write one for:

```python
class Player:
    ...
```

Then write a module-level docstring for:

```text
statistics.py
```

which contains functions for calculating football player statistics.

---

# 🥋 SKILL CHECK — ROUND 3

Improve this:

```python
def transfer_player(player, team):
    """Transfer a player."""
```

Suppose the function:

```text
- receives a Player object
- receives a team name
- changes the player's team
- raises ValueError if the team name is empty
```

Write a professional docstring.

---

# 🥋 HARD MODE — FULL API DOCUMENTATION

Document this:

```python
class Wallet:
    """..."""

    def __init__(self, owner: str, balance: float):
        ...

    def deposit(self, amount: float) -> None:
        ...

    def withdraw(self, amount: float) -> None:
        ...

    def get_balance(self) -> float:
        ...
```

Assume:

```text
deposit()
    raises ValueError for non-positive amounts

withdraw()
    raises ValueError for non-positive amounts
    raises ValueError for insufficient funds
```

Your mission:

```text
[ ] Class docstring
[ ] Constructor documentation where useful
[ ] deposit() docstring
[ ] withdraw() docstring
[ ] get_balance() docstring
[ ] Arguments documented
[ ] Returns documented
[ ] Exceptions documented
```

---

# 🔥 FINAL CHALLENGE — MAKE CODE EXPLAIN ITSELF

Take this:

```python
class Player:
    def __init__(self, name, age, rating):
        self.name = name
        self.age = age
        self.rating = rating

    def improve_rating(self, amount):
        self.rating += amount

    def is_elite(self):
        return self.rating >= 9.0
```

Your mission:

### Step 1

Add type hints.

### Step 2

Add a class docstring.

### Step 3

Add method docstrings.

### Step 4

Think about what assumptions should be documented.

### Step 5

Ask yourself:

> Could another developer understand this class without reading every implementation detail?

---

# 🧠 THE PROFESSIONAL CONNECTION

Look at what you've accumulated in Part 7:

```text
Exception Handling
       ↓
"We can deal with failures."

Static Typing
       ↓
"We can communicate expected types."

Documentation
       ↓
"We can explain the project."

Docstrings
       ↓
"We can explain individual code objects."

Pytest
       ↓
"We can verify behavior."
```

We're building a complete professional workflow.

---

# 🧩 THE FIVE-LAYER MODEL

```text
                 PROFESSIONAL PYTHON
                         │
        ┌────────────────┼────────────────┐
        ↓                ↓                ↓
   Type Safety      Documentation      Reliability
        │                │                │
   Type Hints        READMEs           Pytest
                         │
                     Docstrings
                         │
                         ↓
                    Understanding
```

And that is much closer to how real software engineering works.

---

# 🏆 BATCH COMPLETION CHECKLIST

Before moving on:

```text
[ ] I know what a docstring is
[ ] I know where a docstring belongs
[ ] I understand comments vs docstrings
[ ] I can document functions
[ ] I can document parameters
[ ] I can document return values
[ ] I can document exceptions
[ ] I can document classes
[ ] I can document methods
[ ] I can document modules
[ ] I understand concise vs detailed docstrings
[ ] I know documentation must match behavior
[ ] I understand how IDEs can use docstrings
[ ] I can document part of an existing project
```

---

# 🗺️ PART 7 STATUS

```text
PART 7 — PROFESSIONAL PYTHON
│
├── Batch 1 — Exception Handling        ✅
├── Batch 2 — Static Typing             ✅
├── Batch 3 — Documentation             ✅
├── Batch 4 — Docstrings                🔥 COMPLETE
├── Batch 5 — Pytest                    ⬜ NEXT
└── 🥋 PART 7 BOSS FIGHT                ⬜
```

---

# 🧠 SENSEI'S FINAL WORD

This batch looks deceptively simple.

There's not much syntax.

But there's a major engineering principle underneath it:

> **Code is written for computers. Documentation is written for humans.**

And good professional Python respects both.

You've now gone from:

```text
"Here's some code."
```

to:

```text
"Here's code that tells you:

    what it expects,
    what it does,
    what it returns,
    what can go wrong,
    and how it fits into the project."
```

That's a very different standard.

And next...

# 🧪 BATCH 5 — PYTEST

This one is going to be more hands-on.

We're moving from:

```text
"Does this code look right?"
```

to:

```text
"PROVE IT."
```

Tests.

Assertions.

Test functions.

Test organization.

Fixtures.

Testing failures.

And eventually:

```text
CODE
  ↓
TEST
  ↓
BREAK IT
  ↓
FIX IT
  ↓
CONFIDENCE
```

Then...

# 🥋 PART 7 BOSS FIGHT

No badge yet.

We've still got one final weapon to forge.