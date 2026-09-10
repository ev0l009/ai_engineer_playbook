````markdown
# 🐍 PART 7 — PROFESSIONAL PYTHON
# 🏷️ BATCH 2 — STATIC TYPING

> 🎯 Mission:
> Move from "Python lets me do almost anything"
> to
> "Python lets me do almost anything — but I clearly communicate what SHOULD happen."

---

# 🗺️ PART 7 PROGRESS MAP

```text
PART 7 — PROFESSIONAL PYTHON
│
├── Batch 1 — Exception Handling        ✅
│
├── Batch 2 — Static Typing              🔥 YOU ARE HERE
│
├── Batch 3 — Documentation              ⬜
│
├── Batch 4 — Docstrings                 ⬜
│
├── Batch 5 — Pytest                     ⬜
│
└── 🥋 PART 7 BOSS FIGHT                 ⬜
````

### Exit Criterion

By the end of Part 7:

> "I can write clean, testable Python."

Static typing is one of the tools that gets us there.

---

# 🧠 THE BIG IDEA

Python is dynamically typed.

That means Python doesn't require you to declare:

```python
age: int
name: str
score: float
```

You can simply write:

```python
age = 20
name = "Valerian"
score = 95.5
```

Python figures out the types while the program runs.

That's convenient.

But as projects become larger...

```text
10 lines
    ↓
100 lines
    ↓
1,000 lines
    ↓
10,000+ lines
    ↓
Multiple developers
    ↓
🔥 "WHO WROTE THIS?!"
```

you need a way to communicate your intentions.

That's where:

# 🏷️ TYPE HINTS

come in.

---

# ⚔️ THE PROBLEM

Imagine this function:

```python
def calculate_score(points, bonus):
    return points + bonus
```

Looks fine.

But what are:

```text
points?
bonus?
```

Are they:

```python
int
float
str
```

Maybe:

```python
calculate_score(10, 5)
```

works.

But:

```python
calculate_score("10", 5)
```

doesn't.

And:

```python
calculate_score(10, "5")
```

doesn't.

The function doesn't clearly communicate what it expects.

Now imagine a project with 50 functions.

Then 200.

Then 1,000.

You don't want every developer guessing.

---

# 🏷️ TYPE HINTS

We can annotate variables:

```python
age: int = 21

name: str = "Valerian"

height: float = 1.75

is_active: bool = True
```

We can annotate function parameters:

```python
def greet(name: str):
    print(f"Hello {name}")
```

And return values:

```python
def add(a: int, b: int) -> int:
    return a + b
```

Read that as:

```text
add

a      → int
b      → int
returns → int
```

---

# 🧠 IMPORTANT

Type hints do NOT magically turn Python into a statically typed language.

This:

```python
age: int = "twenty"
```

doesn't automatically stop Python from running.

Python is still dynamically typed.

Type hints mainly communicate intent and allow external tools to detect mistakes.

Think:

```text
Python
   ↓
runs your program

Type checker
   ↓
examines your code
   ↓
finds suspicious type usage
```

Examples of type-checking tools include:

```text
mypy
Pyright
```

You don't need to master those tools yet.

You need to understand the type system they're checking.

---

# 🔥 LEVEL 1 — VARIABLE ANNOTATIONS

Basic form:

```python
variable: type = value
```

Examples:

```python
age: int = 21

name: str = "Alex"

price: float = 19.99

active: bool = True
```

---

# 🥋 PRACTICE 1 — ANNOTATE THE VARIABLES

Convert these into typed variables:

```python
age = 25
name = "Marcus"
height = 1.82
is_student = False
```

Expected structure:

```python
age: int = ...
name: str = ...
height: float = ...
is_student: bool = ...
```

### 🎯 Your mission

Write the complete code yourself.

Don't copy the answer immediately.

---

# 🔥 LEVEL 2 — FUNCTION PARAMETERS

Without type hints:

```python
def multiply(a, b):
    return a * b
```

With type hints:

```python
def multiply(a: int, b: int):
    return a * b
```

Better:

```python
def multiply(a: int, b: int) -> int:
    return a * b
```

Now the function communicates:

```text
a       → int
b       → int
return  → int
```

---

# 🧠 THE PATTERN

Memorize this:

```python
def function_name(parameter: type) -> return_type:
    ...
```

Example:

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

---

# 🥋 PRACTICE 2 — TYPE THESE FUNCTIONS

Add type hints.

### Easy

```python
def add(a, b):
    return a + b
```

Expected:

```text
a → ?
b → ?
return → ?
```

---

### Medium

```python
def calculate_price(price, tax):
    return price + (price * tax)
```

Think carefully about the types.

---

### Hard

```python
def create_player(name, age, rating):
    return {
        "name": name,
        "age": age,
        "rating": rating
    }
```

Don't just annotate the parameters.

Think about the return type too.

---

# 🔥 LEVEL 3 — COMMON COLLECTION TYPES

Modern Python allows:

```python
list[str]
```

instead of older syntax such as:

```python
List[str]
```

You can annotate:

```python
players: list[str] = [
    "Messi",
    "Salah",
    "Mbappe"
]
```

This means:

> `players` should be a list containing strings.

---

## More examples

```python
scores: list[int] = [10, 20, 30]

prices: list[float] = [10.5, 20.0, 15.75]

active: list[bool] = [True, False, True]
```

---

# 🧠 DICTIONARIES

```python
player_age: dict[str, int] = {
    "Messi": 39,
    "Salah": 34
}
```

Interpretation:

```text
key   → str
value → int
```

Another example:

```python
prices: dict[str, float] = {
    "ball": 25.50,
    "boots": 100.00
}
```

---

# 🧠 TUPLES

Tuples can describe the type of each position:

```python
player: tuple[str, int, float] = (
    "Salah",
    34,
    8.9
)
```

Meaning:

```text
position 1 → str
position 2 → int
position 3 → float
```

---

# 🧠 SETS

```python
unique_numbers: set[int] = {1, 2, 3, 4}
```

Or:

```python
countries: set[str] = {
    "Nigeria",
    "England",
    "Egypt"
}
```

---

# 🧪 COLLECTION TYPE CHEAT SHEET

```text
LIST
list[int]

DICTIONARY
dict[str, int]

TUPLE
tuple[str, int, float]

SET
set[str]
```

---

# 🥋 PRACTICE 3 — COLLECTION TYPING

Annotate these.

### 1

```python
players = ["Messi", "Salah", "Haaland"]
```

### 2

```python
scores = [10, 20, 30, 40]
```

### 3

```python
player_ratings = {
    "Salah": 9.2,
    "Haaland": 9.0
}
```

### 4

```python
positions = {"GK", "CB", "CM", "ST"}
```

### 5

```python
player = ("Salah", 34, 8.9)
```

---

# 🔥 LEVEL 4 — FUNCTION RETURNS WITH COLLECTIONS

Suppose:

```python
def get_players():
    return ["Salah", "Messi", "Haaland"]
```

We can write:

```python
def get_players() -> list[str]:
    return ["Salah", "Messi", "Haaland"]
```

Another:

```python
def get_scores() -> list[int]:
    return [10, 20, 30]
```

Another:

```python
def get_prices() -> dict[str, float]:
    return {
        "boots": 100.0,
        "ball": 25.0
    }
```

---

# 🧠 WHY THIS MATTERS

Imagine another developer sees:

```python
players = get_players()
```

Without typing, they must inspect the function.

With:

```python
def get_players() -> list[str]:
```

they immediately know:

```text
get_players()
     ↓
list
     ↓
strings
```

Less guessing.

Less confusion.

Less debugging.

---

# ⚔️ DEBUGGING LAB #1 — LYING TYPES

Look at this:

```python
def get_age() -> int:
    return "twenty"
```

### 🚨 What's wrong?

The annotation says:

```text
return → int
```

but the function actually returns:

```text
str
```

This is exactly the kind of mismatch a type checker can flag.

Fix it in one of two ways:

### Option A

Return an integer.

### Option B

Change the return annotation if the function genuinely should return text.

---

# 🥋 DEBUGGING LAB #2 — BROKEN COLLECTION

```python
players: list[str] = [
    "Messi",
    "Salah",
    10
]
```

Find the problem.

Hint:

```text
list[str]
```

means:

> Every element should be a string.

Fix the data.

---

# 🥋 DEBUGGING LAB #3 — WRONG DICTIONARY VALUE

```python
prices: dict[str, float] = {
    "boots": 100.0,
    "ball": "twenty"
}
```

What's wrong?

Break it down:

```text
dict[str, float]

key   → str
value → float
```

The key is fine.

The value isn't.

Fix it.

---

# 🔥 LEVEL 5 — NONE

One of the most important situations in real programs:

Sometimes a value exists.

Sometimes it doesn't.

Example:

```python
player_name = None
```

We can express:

```text
str OR None
```

using:

```python
str | None
```

Example:

```python
player_name: str | None = None
```

This means:

```text
player_name can contain:

str
OR
None
```

---

# 🧠 WHY THIS IS USEFUL

Imagine searching for a player:

```python
def find_player(name: str) -> str | None:
    ...
```

The function is saying:

```text
I might find the player.
If I do → str

If I don't → None
```

That's valuable information.

---

# 🥋 PRACTICE 4 — OPTIONAL RESULTS

What should these return types be?

### 1

```python
def find_user(username: str):
    ...
```

It returns either a username or `None`.

---

### 2

```python
def find_score(player: str):
    ...
```

It returns either an integer score or `None`.

---

### 3

```python
def find_price(product: str):
    ...
```

It returns either a float or `None`.

Write the correct annotations.

---

# 🔥 LEVEL 6 — TYPE ALIASES

Sometimes a type becomes complicated.

Instead of repeating:

```python
dict[str, int]
```

everywhere, you can give it a name.

Example:

```python
PlayerScores = dict[str, int]
```

Then:

```python
scores: PlayerScores = {
    "Salah": 20,
    "Haaland": 18
}
```

This makes code easier to read.

---

# 🧠 THINK LIKE A PROFESSIONAL

Compare:

```python
def update_scores(
    scores: dict[str, int]
) -> dict[str, int]:
    ...
```

with:

```python
PlayerScores = dict[str, int]

def update_scores(
    scores: PlayerScores
) -> PlayerScores:
    ...
```

The second version communicates a concept:

```text
PlayerScores
```

rather than merely exposing the implementation.

---

# 🥋 PRACTICE 5 — CREATE YOUR OWN ALIASES

Create type aliases for:

```text
Player ratings
Product prices
Player names
Student scores
```

For example:

```python
PlayerRatings = ...
```

Then use each alias in a variable annotation.

---

# ⚠️ LEVEL 7 — ANY

There is another type:

```python
Any
```

It basically means:

> "This could be anything."

Example:

```python
from typing import Any

value: Any = 10
value = "hello"
value = [1, 2, 3]
```

Very flexible.

But...

# 🚨 DON'T ABUSE IT

If everything is:

```python
Any
```

you've basically told the type checker:

> "Bro, don't worry about it."

😂

And that defeats much of the point of static typing.

Prefer precise types whenever possible.

Use `Any` when the data genuinely cannot reasonably be typed more precisely.

---

# 🧠 TYPE HINTS ARE COMMUNICATION

This is the deeper lesson.

Typing isn't just about satisfying a tool.

It's about communicating intent.

Compare:

```python
def process(data):
    ...
```

with:

```python
def process(data: list[str]) -> dict[str, int]:
    ...
```

The second function tells you much more before you even read its body.

That's professional Python.

---

# 🔥 LEVEL 8 — TYPE NARROWING

Consider:

```python
def print_name(name: str | None):
    if name is not None:
        print(name.upper())
```

Before the condition:

```text
name → str | None
```

After:

```python
if name is not None:
```

inside that branch, Python/type-checking tools can understand:

```text
name → str
```

This is called:

# TYPE NARROWING

You're taking a broad possibility:

```text
str | None
```

and narrowing it:

```text
str
```

---

# 🧠 WHY DOES THIS MATTER?

Because some operations only make sense for certain types.

For example:

```python
name.upper()
```

makes sense for:

```text
str
```

but not:

```text
None
```

So we check first.

---

# 🥋 PRACTICE 6 — NARROW THE TYPE

Write a function:

```python
def greet_player(name: str | None):
```

It should:

```text
if name exists:
    print the player's name in uppercase

otherwise:
    print "Unknown player"
```

Use type narrowing.

---

# ⚔️ DEBUGGING LAB #4 — NONE TRAP

What's wrong here?

```python
def get_player_name() -> str | None:
    return None


name = get_player_name()

print(name.upper())
```

The function explicitly says:

```text
str OR None
```

Yet we're immediately assuming:

```text
str
```

Fix the code by checking whether `name` is `None`.

---

# 🔥 LEVEL 9 — TYPING HIGHER-ORDER FUNCTIONS

You've already learned higher-order functions.

Now combine that knowledge with static typing.

Suppose:

```python
def double(number: int) -> int:
    return number * 2
```

And:

```python
def apply_operation(
    number: int,
    operation
):
    return operation(number)
```

We can describe the operation more clearly.

Using `Callable`:

```python
from collections.abc import Callable

def apply_operation(
    number: int,
    operation: Callable[[int], int]
) -> int:
    return operation(number)
```

Read it as:

```text
operation:

takes → int
returns → int
```

This connects two things you've already learned:

```text
Higher-Order Functions
        +
Static Typing
        ↓
Callable
```

---

# 🧠 BREAKDOWN

```python
Callable[[int], int]
```

means:

```text
Callable
   │
   ├── accepts an int
   │
   └── returns an int
```

So:

```python
def double(number: int) -> int:
    return number * 2
```

fits.

---

# 🥋 PRACTICE 7 — TYPED CALLBACK

Create:

```python
def square(number: int) -> int:
    ...
```

Then create:

```python
def apply_operation(
    number: int,
    operation: Callable[[int], int]
) -> int:
    ...
```

Call it with:

```python
square
```

---

# 🧩 MINI PROJECT — TYPED FOOTBALL ACADEMY

Now we're going to upgrade part of the Football Academy.

Current version:

```python
players = []

def add_player(name, age, position, rating):
    ...
```

That's functional.

But now we're professional.

---

# 🎯 MISSION

Create a typed player system.

Your function should communicate:

```text
name     → str
age      → int
position → str
rating   → float
```

Start with:

```python
players: list[dict[str, ...]] = []
```

You'll need to determine the appropriate value type for the dictionary.

Then create:

```python
def add_player(...):
    ...
```

with complete annotations.

---

# 🚨 CHALLENGE — SEARCH FUNCTION

Create:

```python
def find_player(name: str) -> ...:
```

It should:

```text
search players
    ↓
if found
    ↓
return player

if not found
    ↓
return None
```

Your return type should reflect that.

---

# 🚨 CHALLENGE — FILTER FUNCTION

Create:

```python
def get_high_rated_players(...) -> ...:
```

It should return all players whose rating is:

```text
>= 8.0
```

Type the parameters and return value.

---

# 🚨 CHALLENGE — UPDATE FUNCTION

Create:

```python
def update_rating(...):
```

It should:

```text
receive player name
receive new rating
find player
update rating if player exists
```

Think carefully about:

```text
What can be None?
What definitely exists?
What should the function return?
```

---

# 🧠 PROFESSIONAL DESIGN QUESTION

Suppose you have:

```python
players: list[dict[str, object]]
```

This is technically broad.

You could store:

```python
str
int
float
```

inside the dictionary.

But the type information isn't very specific.

Later, when your projects become more advanced, you'll learn better ways to model structured data.

For now, understand the principle:

> The more accurately you describe your data, the more useful static typing becomes.

Don't chase complexity prematurely.

---

# 🐛 DEBUGGING LAB #5 — TYPE CHECKER THINKING

Consider:

```python
def add_score(score: int, bonus: int) -> int:
    return score + bonus


result = add_score("10", 5)
```

Python may not complain until runtime.

But a type checker can look at:

```python
add_score("10", 5)
```

and say:

```text
🚨 Expected int
🚨 Received str
```

That's one of the biggest benefits of static typing.

It catches problems BEFORE you run the program.

---

# 🧠 STATIC TYPING WORKFLOW

Think:

```text
Write code
   ↓
Add type hints
   ↓
Type checker analyzes code
   ↓
Potential mistakes discovered
   ↓
Fix mistakes
   ↓
Run program
   ↓
Test behavior
```

Typing doesn't replace testing.

Testing doesn't replace typing.

They complement each other.

And that's going to become VERY important in the next stages of Part 7.

---

# 🧪 STATIC TYPING VS TESTING

Imagine:

```python
def add(a: int, b: int) -> int:
    return a + b
```

Static typing can help detect:

```python
add("5", 10)
```

But static typing doesn't prove:

```text
Does add() actually calculate what we intended?
```

A test can check that:

```text
add(2, 3)
    ↓
5
```

So:

```text
Static Typing
    ↓
"What TYPES are flowing through my program?"

Testing
    ↓
"Does my program BEHAVE correctly?"
```

Professional Python uses both.

---

# 🥋 PRACTICE 8 — TYPE OR BEHAVIOR?

For each problem, decide whether static typing, testing, or both would help.

### A

```text
A function expects an int but receives a string.
```

### B

```text
A function returns 7 when you expected 10.
```

### C

```text
A function should return None when a player isn't found.
```

### D

```text
A function accepts a list of strings but receives integers.
```

Think before checking your answers.

---

# 🧠 COMMON MISTAKES

## ❌ Mistake 1 — Thinking annotations enforce types

```python
age: int = "hello"
```

Type hints aren't runtime enforcement.

---

## ❌ Mistake 2 — Using Any everywhere

```python
def process(data: Any) -> Any:
```

This throws away useful information.

---

## ❌ Mistake 3 — Forgetting None

Bad:

```python
def find_player(name: str) -> str:
    return None
```

If `None` is a legitimate result, represent it:

```python
def find_player(name: str) -> str | None:
    return None
```

---

## ❌ Mistake 4 — Typing only variables

This:

```python
players: list[str] = [...]
```

is useful.

But this:

```python
def get_players() -> list[str]:
```

also communicates the function contract.

Use annotations where they improve clarity.

---

## ❌ Mistake 5 — Making types unreadably complicated

Don't turn a simple program into:

```text
🤯🤯🤯
```

just to demonstrate typing.

The goal is:

```text
clarity
```

not:

```text
type-hint gymnastics
```

---

# 🧠 THE PROFESSIONAL PYTHON RULE

A good type annotation should answer:

> "What kind of thing should this be?"

A good function annotation should answer:

> "What goes in, and what comes out?"

If your annotation makes the code harder to understand without providing useful information...

rethink it.

---

# 🥋 SKILL CHECK — ROUND 1

Without looking back, explain:

### 1.

What is dynamic typing?

### 2.

What is a type hint?

### 3.

Does a type hint automatically prevent incorrect values?

### 4.

What does this mean?

```python
scores: list[int]
```

### 5.

What does this mean?

```python
dict[str, float]
```

### 6.

What does this mean?

```python
str | None
```

### 7.

Why should `Any` be used carefully?

### 8.

What is type narrowing?

---

# 🥋 SKILL CHECK — ROUND 2

Type these functions completely.

### Challenge A

```python
def calculate_total(price, quantity):
    return price * quantity
```

Requirements:

```text
price → float
quantity → int
return → float
```

---

### Challenge B

```python
def get_names():
    return ["Alex", "Sam", "Jordan"]
```

---

### Challenge C

```python
def find_score(scores, player):
    return scores.get(player)
```

Assume:

```text
scores → dictionary of str → int
player → str
return → int OR None
```

---

# 🥋 SKILL CHECK — ROUND 3

Fix every typing problem:

```python
players: list[str] = [
    "Salah",
    "Messi",
    10
]


def get_age() -> int:
    return "34"


def find_player(name: str) -> str:
    return None


def add_score(a: int, b: int) -> int:
    return a + b


result = add_score("10", 5)
```

Don't just fix the code.

Explain WHY each mistake was a problem.

---

# 🥋 HARD MODE — DESIGN CHALLENGE

Design a typed mini inventory system.

You need:

```text
products
add_product()
find_product()
get_price()
```

Each product should contain:

```text
name
price
quantity
```

Requirements:

```text
name     → str
price    → float
quantity → int
```

Your system should support:

```text
adding products
finding products
retrieving prices
handling missing products
```

Every function must have:

```text
parameter annotations
return annotations
```

No untyped functions.

---

# 🔥 FINAL STATIC TYPING CHALLENGE

You inherit this code:

```python
players = []


def add_player(name, age, rating):
    players.append({
        "name": name,
        "age": age,
        "rating": rating
    })


def find_player(name):
    for player in players:
        if player["name"] == name:
            return player

    return None


def get_rating(name):
    player = find_player(name)

    if player:
        return player["rating"]

    return None
```

Your mission:

# 🛠️ MAKE IT PROFESSIONAL

Add appropriate type annotations to:

```text
players
add_player()
find_player()
get_rating()
```

Then answer:

```text
1. What is the type of players?

2. What is the return type of find_player()?

3. What is the return type of get_rating()?

4. Why must find_player() account for None?

5. Why must get_rating() account for None?

6. What would happen if someone called:

   get_rating("Unknown Player")

7. Which parts could a type checker help us catch?
```

---

# 🧠 DEBUGGING LAB — FINAL BOSS PREVIEW

You're not fighting the Part 7 boss yet.

But here's a taste.

Imagine this:

```python
def get_player_rating(name: str) -> float:
    player = find_player(name)

    return player["rating"]
```

The problem?

```text
find_player()
        ↓
player OR None
        ↓
player["rating"]
```

What happens if:

```text
player = None
```

💥

This is where the skills you've already learned start connecting:

```text
Exception Handling
       +
Static Typing
       +
Functions
       +
Collections
       ↓
Professional Python
```

---

# 🧠 THE BIG IDEA — LOCK IT IN

Static typing is NOT:

```text
"Python suddenly becomes Java."
```

It is:

```text
"Let's clearly describe what our code expects."
```

You use:

```python
name: str
age: int
rating: float
active: bool
```

Functions:

```python
def add(a: int, b: int) -> int:
```

Collections:

```python
list[str]
dict[str, int]
tuple[str, int]
set[str]
```

Optional values:

```python
str | None
```

Type aliases:

```python
PlayerScores = dict[str, int]
```

Higher-order functions:

```python
Callable[[int], int]
```

And remember:

```text
Type hints
    ↓
communicate intent

Type checkers
    ↓
find suspicious type usage

Tests
    ↓
verify behavior
```

---

# 🏆 BATCH 2 COMPLETION CHECKLIST

Before moving on, you should be able to check these confidently:

```text
[ ] I understand dynamic typing
[ ] I understand type hints
[ ] I can annotate variables
[ ] I can annotate function parameters
[ ] I can annotate return values
[ ] I can type lists
[ ] I can type dictionaries
[ ] I can type tuples
[ ] I can type sets
[ ] I understand str | None
[ ] I understand type narrowing
[ ] I understand type aliases
[ ] I understand why Any should be used carefully
[ ] I can type higher-order functions with Callable
[ ] I understand what a type checker does
[ ] I understand that type hints don't enforce runtime types
[ ] I understand typing vs testing
[ ] I can add typing to an existing project
```

---

# 🗺️ PART 7 STATUS

```text
PART 7 — PROFESSIONAL PYTHON
│
├── Batch 1 — Exception Handling
│      └── ✅ COMPLETE
│
├── Batch 2 — Static Typing
│      └── 🔥 CURRENT BATCH
│
├── Batch 3 — Documentation
│      └── ⬜ NEXT
│
├── Batch 4 — Docstrings
│      └── ⬜
│
├── Batch 5 — Pytest
│      └── ⬜
│
└── 🥋 PART 7 BOSS
       └── ⬜
```

---

# ⚔️ SENSEI'S FINAL WORD

You've now added another layer to your Python.

Earlier:

```text
"I can make Python work."
```

Now:

```text
"I can tell Python users and developer tools
what my code is supposed to accept and return."
```

That's a serious upgrade.

And here's the important part:

You're not learning static typing in isolation.

You're building toward:

```text
Exception Handling
       ↓
Static Typing
       ↓
Documentation
       ↓
Docstrings
       ↓
Pytest
       ↓
🥋 PROFESSIONAL PYTHON
```

Then we take those professional Python skills back into your projects.

Football Academy.

Wallet.

Terminal applications.

And eventually...

```text
Python
   ↓
DSA
   ↓
Data
   ↓
Math
   ↓
ML
   ↓
Deep Learning
   ↓
LLMs
   ↓
MLOps
   ↓
🔥 AI ENGINEER
```

# 🐍 KEEP FORGING.

The code isn't just going to work.

It's going to become:

```text
READABLE
TYPED
TESTABLE
MAINTAINABLE
PROFESSIONAL
```

🥋 **Static Typing training complete when YOU can solve the challenges without the notes.**

No Part 7 boss yet.

We're still hunting.

```
```
