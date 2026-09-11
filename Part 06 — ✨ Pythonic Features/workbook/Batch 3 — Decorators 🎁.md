# 🤖 The AI Engineer Playbook
# 🟣 Part 6 — Pythonic Features
## Batch 3 — Decorators 🎁

> *"Sometimes you don't want to change what a function does. You just want to give it extra powers."*

---

# 🎯 Learning Objectives

By the end of this batch, you should be able to:

- Understand that functions are objects
- Store functions in variables
- Pass functions to other functions
- Return functions from functions
- Understand higher-order functions
- Explain what a decorator does
- Create basic decorators
- Understand the `@decorator` syntax
- Decorate functions with arguments
- Return values from decorated functions
- Use `*args` and `**kwargs` in decorators
- Understand why `functools.wraps` is useful
- Recognize practical uses of decorators

---

# 🧭 Where You Are
## 🤖 AI Engineer Playbook
### Phase 1 — Python Fluency 🐍

████████████████████████████████████████████████████

✅ Foundations
✅ Functions
✅ Collections
✅ Object-Oriented Programming
✅ Files & Python Ecosystem

🟣 Pythonic Features

    ✅ Iterators
    ✅ Generators
    🎁 Decorators  ← YOU ARE HERE
    ⬜ Context Managers

🎯 Part Goal:
Understand and use Python's
more powerful language features.

---

# 🧠 Before We Begin

You may have seen something like this:

```python
@something
def greet():
    print("Hello")
```

And thought:

```text
🤨 What is that?

Why is there an @ symbol?

Is this Python black magic?
```

😂

Not black magic.

Just functions.

A decorator is built from a few ideas:

```text
FUNCTIONS
    ↓
Functions are objects
    ↓
Functions can be passed around
    ↓
Functions can return other functions
    ↓
Higher-order functions
    ↓
🎁 DECORATORS
```

So before touching `@`, we're going to dismantle the machine and see what's inside.

---

# 🧱 Step 1 — Functions Are Objects

You've been using functions like this:

```python
def greet():
    print("Hello")
```

Then:

```python
greet()
```

Output:

```text
Hello
```

Normal.

But in Python, a function is also an object.

That means you can do something interesting:

```python
def greet():
    print("Hello")

message = greet
```

Notice carefully:

```python
message = greet
```

NOT:

```python
message = greet()
```

These are very different.

---

## Calling the Function

This:

```python
greet()
```

means:

```text
Run the function.
```

But this:

```python
greet
```

refers to:

```text
The function itself.
```

So:

```python
message = greet
```

means:

```text
message
   │
   ▼
points to
   │
   ▼
greet function
```

Now:

```python
message()
```

Output:

```text
Hello
```

🤯

You didn't create a second function.

You created another reference to the same function.

---

# 🧪 Practice — Function Alias

Create:

```python
def celebrate():
    print("🎉 Goal!")
```

Then store the function in:

```python
action
```

Finally call:

```python
action()
```

Expected:

```text
🎉 Goal!
```

---

# 🧠 The Big Idea

A function can be treated like a value.

Just like:

```python
number = 10
```

or:

```python
name = "Valerian"
```

you can have:

```python
action = celebrate
```

Conceptually:

```text
VARIABLE
    │
    ▼
FUNCTION OBJECT

action ───────────┐
                  ▼
              celebrate()
```

This is the first key.

---

# 🧪 Predict Before Running

What happens here?

```python
def score_goal():
    print("GOOOAL!")

celebration = score_goal

celebration()
```

Answer before you test it.

Then explain:

> Why did `celebration()` work?

---

# 🚨 Common Mistake

Look at these:

```python
action = greet
```

and:

```python
action = greet()
```

They are NOT the same.

## Version 1

```python
action = greet
```

Means:

```text
Store the function.
```

## Version 2

```python
action = greet()
```

Means:

```text
Run greet()
    ↓
Take its returned result
    ↓
Store that result
```

For example:

```python
def get_name():
    return "Salah"

player = get_name()
```

Now:

```text
player
```

contains:

```text
"Salah"
```

Not the function.

---

# 🥋 Skill Check — Spot the Difference

Explain the difference between:

```python
a = function
```

and:

```python
a = function()
```

Use your own words.

This distinction is going to matter a LOT.

---

# 📦 Step 2 — Passing Functions Around

Since functions are objects...

we can pass them into other functions.

Consider:

```python
def greet():
    print("Hello!")

def execute(function):
    function()
```

Now:

```python
execute(greet)
```

What happens?

Conceptually:

```text
execute(greet)
       │
       ▼
greet function is passed in
       │
       ▼
execute()
       │
       ▼
function()
       │
       ▼
greet()
       │
       ▼
Hello!
```

Notice again:

```python
execute(greet)
```

We passed the function.

We didn't run it yet.

---

# 🧠 Higher-Order Functions

A function that can:

```text
Accept another function
```

or:

```text
Return another function
```

is called a:

# 🏗️ Higher-Order Function

For example:

```python
def execute(function):
    function()
```

`execute()` is a higher-order function because it receives another function.

---

# 🧪 Practice — Football Action

Create:

```python
def attack():
    print("⚽ Attack started!")
```

Then create:

```python
def run_action(action):
    ...
```

Pass:

```python
attack
```

into:

```python
run_action()
```

Your output should be:

```text
⚽ Attack started!
```

---

# 🧠 Why Is This Useful?

Imagine:

```python
def train():
    print("Training...")

def rest():
    print("Resting...")

def recover():
    print("Recovering...")
```

Now:

```python
def perform(activity):
    activity()
```

You can do:

```python
perform(train)
perform(rest)
perform(recover)
```

The structure stays the same.

Only the behavior changes.

```text
perform()
    │
    ├── train()
    │
    ├── rest()
    │
    └── recover()
```

That's powerful.

---

# 🔴 Hard Practice — Command Runner

Create three functions:

```python
def show_players():
    ...

def show_teams():
    ...

def show_stats():
    ...
```

Then create:

```python
def run_command(command):
    ...
```

Use it like:

```python
run_command(show_players)
run_command(show_teams)
run_command(show_stats)
```

### Bonus

Create a dictionary:

```python
commands = {
    "players": show_players,
    "teams": show_teams,
    "stats": show_stats
}
```

Then try:

```python
commands["players"]()
```

🤯

Functions inside dictionaries.

We'll come back to this kind of pattern in real applications.

---

# 🧱 Step 3 — Functions Can Return Functions

We've passed functions into other functions.

Now let's go in the other direction.

A function can also return a function.

Example:

```python
def outer():
    def inner():
        print("Hello!")

    return inner
```

Now:

```python
result = outer()
```

What is `result`?

Not:

```text
Hello!
```

Instead:

```text
result
    │
    ▼
inner function
```

Because:

```python
return inner
```

returns the function itself.

Not:

```python
return inner()
```

which would run it.

Now:

```python
result()
```

Output:

```text
Hello!
```

---

# 🤯 The Shape of It

```text
outer()
   │
   ▼
Creates inner()
   │
   ▼
Returns inner function
   │
   ▼
result
   │
   ▼
result()
   │
   ▼
inner() runs
```

This is the second major ingredient for decorators.

---

# 🧪 Practice — Function Factory

Create:

```python
def create_greeting():
    ...
```

Inside it, create:

```python
def greet():
    print("Welcome to Football Academy!")
```

Return:

```python
greet
```

Then:

```python
message = create_greeting()

message()
```

Expected:

```text
Welcome to Football Academy!
```

---

# 🧠 Step 4 — Functions Inside Functions

Python allows this:

```python
def outer():
    def inner():
        print("Inside!")

    inner()
```

Calling:

```python
outer()
```

produces:

```text
Inside!
```

Conceptually:

```text
outer()
   │
   └── inner()
           │
           └── print()
```

The inner function belongs to the scope of `outer()`.

And usually:

```python
inner()
```

cannot be called directly from outside:

```python
outer()
inner()  # ❌
```

Because `inner` exists inside `outer`'s scope.

---

# 🧠 The Decorator Recipe

Now we have all the ingredients.

```text
1️⃣ Functions are objects

2️⃣ Functions can be passed to functions

3️⃣ Functions can return functions

4️⃣ Functions can be nested

        ↓

🎁 DECORATORS
```

Let's build one manually.

---

# 🎁 Our First Decorator

Suppose we have:

```python
def greet():
    print("Hello!")
```

We want to add extra behavior.

For example:

```text
Before:
"Preparing greeting..."

Run:
"Hello!"

After:
"Greeting complete!"
```

We could edit the function:

```python
def greet():
    print("Preparing greeting...")
    print("Hello!")
    print("Greeting complete!")
```

But what if we have:

```text
greet()
attack()
train()
save_player()
```

and we want to add similar behavior to all of them?

Copying:

```python
print("Starting...")
```

and:

```python
print("Finished...")
```

into every function gets repetitive.

So instead...

we can wrap the function.

---

# 🎁 Building the Wrapper

Start with:

```python
def decorate(function):
    def wrapper():
        print("Before function")

        function()

        print("After function")

    return wrapper
```

Let's slow this down.

---

## Step 1 — Receive a Function

```python
def decorate(function):
```

We can do:

```python
decorate(greet)
```

So:

```text
function
    │
    ▼
greet
```

---

## Step 2 — Create a New Function

Inside:

```python
def decorate(function):
```

we create:

```python
def wrapper():
```

This wrapper will add behavior around the original function.

```text
wrapper()

Before
   ↓
Original Function
   ↓
After
```

---

## Step 3 — Return the Wrapper

Finally:

```python
return wrapper
```

So now:

```python
new_greet = decorate(greet)
```

Conceptually:

```text
greet
  │
  ▼
decorate()
  │
  ▼
Creates wrapper()
  │
  ▼
new_greet
```

Now:

```python
new_greet()
```

Output:

```text
Before function
Hello!
After function
```

🎉

You just created a decorator.

---

# 🤯 What Just Happened?

Let's map it.

```python
def greet():
    print("Hello!")
```

Then:

```python
new_greet = decorate(greet)
```

Python does:

```text
ORIGINAL FUNCTION

greet()
    │
    ▼
decorate(greet)
    │
    ▼
WRAPPER CREATED

wrapper():
    Before
    ↓
    greet()
    ↓
    After
```

Then:

```python
new_greet()
```

actually runs:

```text
wrapper()
```

Which runs:

```text
Before
   ↓
greet()
   ↓
After
```

This is the heart of a decorator.

# 🎁 A decorator wraps a function and adds behavior.

---

# 🧪 Practice — Training Decorator

Create:

```python
def training_decorator(function):
    ...
```

Your wrapper should print:

```text
🏃 Training session starting...
```

Then run the original function.

Then print:

```text
💪 Training session complete!
```

Use it with:

```python
def train_player():
    print("Player is training.")
```

Expected:

```text
🏃 Training session starting...
Player is training.
💪 Training session complete!
```

Use the manual approach first:

```python
decorated_function = training_decorator(train_player)

decorated_function()
```

No `@` yet.

We earn the magic syntax. 🥋

---

# ⚡ The `@` Syntax

Remember:

```python
decorated_function = training_decorator(train_player)
```

Python gives us shorthand.

Instead of writing that manually:

```python
@training_decorator
def train_player():
    print("Player is training.")
```

Conceptually, Python does:

```text
@training_decorator

def train_player()
        │
        ▼
training_decorator(train_player)
        │
        ▼
wrapper returned
        │
        ▼
train_player now refers to wrapper
```

So this:

```python
@training_decorator
def train_player():
    print("Player is training.")
```

is conceptually similar to:

```python
def train_player():
    print("Player is training.")

train_player = training_decorator(train_player)
```

🤯

The `@` is just cleaner syntax.

---

# 🧠 The Big Idea

Decorators let us say:

```text
Original Function

        +

Extra Behavior
```

Without rewriting the original function's body.

Conceptually:

```text
              🎁 DECORATOR

                    │
                    ▼

        ┌──────────────────────┐
        │      BEFORE          │
        └──────────┬───────────┘
                   │
                   ▼
              FUNCTION
                   │
                   ▼
        ┌──────────────────────┐
        │       AFTER          │
        └──────────────────────┘
```

---

# 🧪 Practice — Logging Decorator

Create:

```python
def logger(function):
    ...
```

It should print:

```text
Running function...
```

before the original function.

And:

```text
Function finished.
```

afterwards.

Use it like:

```python
@logger
def save_player():
    print("Player saved.")
```

Expected:

```text
Running function...
Player saved.
Function finished.
```

---

# 🐛 Debugging Lab — Where Did My Function Go?

Look at this:

```python
def decorator(function):
    def wrapper():
        print("Before")
        function()
        print("After")

    return wrapper


def greet():
    print("Hello!")


greet = decorator(greet)

greet()
```

A beginner says:

> "Wait... `greet` was a function. Then we replaced it. Did we delete the original?! 😭"

## Your Mission

Explain what is happening.

Use this map:

```text
Original greet
      │
      ▼
Passed into decorator
      │
      ▼
wrapper remembers original function
      │
      ▼
wrapper returned
      │
      ▼
greet now points to wrapper
```

Is the original function actually lost immediately?

What allows `wrapper()` to still call it?

---

# 🧠 Decorators and Arguments

Our current decorator works with:

```python
def greet():
    ...
```

But what about:

```python
def greet(name):
    print(f"Hello, {name}")
```

If we use:

```python
@logger
```

our old wrapper:

```python
def wrapper():
```

accepts no arguments.

So this could cause a problem.

We need the wrapper to accept whatever arguments the original function needs.

Enter:

```python
*args
```

and:

```python
**kwargs
```

---

# 🧠 Flexible Wrappers

```python
def decorator(function):
    def wrapper(*args, **kwargs):
        print("Before")

        result = function(*args, **kwargs)

        print("After")

        return result

    return wrapper
```

This is the standard flexible pattern.

Let's break it down.

---

## `*args`

Allows positional arguments.

Example:

```python
def example(*args):
    print(args)
```

Could receive:

```python
example("Salah", 20, "Forward")
```

Conceptually:

```text
args

(
    "Salah",
    20,
    "Forward"
)
```

---

## `**kwargs`

Allows keyword arguments.

Example:

```python
def example(**kwargs):
    print(kwargs)
```

Could receive:

```python
example(
    name="Salah",
    goals=20
)
```

Conceptually:

```text
kwargs

{
    "name": "Salah",
    "goals": 20
}
```

---

# 🧠 Why Decorators Use Them

Imagine:

```python
def greet():
    ...

def welcome(name):
    ...

def create_player(name, position, age):
    ...
```

A generic decorator shouldn't care exactly how many arguments each function needs.

So:

```python
def wrapper(*args, **kwargs):
```

basically says:

> "Give me whatever arguments you have. I'll pass them to the original function."

```text
Arguments
    │
    ▼
wrapper(*args, **kwargs)
    │
    ▼
function(*args, **kwargs)
```

---

# 🧪 Practice — Decorator With Arguments

Create:

```python
def announcer(function):
    ...
```

Then:

```python
@announcer
def introduce_player(name, position):
    print(f"{name} plays as a {position}.")
```

Calling:

```python
introduce_player("Saka", "RW")
```

Should produce something like:

```text
📢 Player announcement!
Saka plays as a RW.
📢 End of announcement.
```

Your decorator should work with the function's arguments.

---

# 🧠 Decorators and Return Values

Consider:

```python
def add(a, b):
    return a + b
```

If we decorate it:

```python
@logger
def add(a, b):
    return a + b
```

Our wrapper must not accidentally swallow the result.

Bad:

```python
def wrapper(*args, **kwargs):
    function(*args, **kwargs)
```

The original function returns something...

but the wrapper doesn't return it.

Better:

```python
def wrapper(*args, **kwargs):
    result = function(*args, **kwargs)

    return result
```

Or simply:

```python
def wrapper(*args, **kwargs):
    return function(*args, **kwargs)
```

when no extra work is needed afterward.

---

# 🧪 Practice — Preserve the Result

Create:

```python
def tracker(function):
    ...
```

It should print:

```text
Calculating...
```

before the function.

Then call the original function.

Then return its result.

Use:

```python
@tracker
def calculate_score(goals, assists):
    return goals * 4 + assists * 3
```

Example:

```python
score = calculate_score(5, 2)
```

Your variable:

```python
score
```

must still contain the calculated value.

---

# 🐛 Debugging Lab — The Missing Return

What's wrong here?

```python
def logger(function):
    def wrapper(*args, **kwargs):
        print("Running...")
        function(*args, **kwargs)

    return wrapper


@logger
def multiply(a, b):
    return a * b


result = multiply(5, 4)

print(result)
```

The developer expected:

```text
Running...
20
```

But the result isn't `20`.

## Your Mission

1. Explain why.
2. Fix the decorator.
3. Explain why decorators must sometimes return the original function's result.

---

# 🧠 `functools.wraps`

Here's a slightly sneaky issue.

Consider:

```python
def logger(function):
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper
```

Then:

```python
@logger
def train_player():
    """Train a football player."""
    print("Training...")
```

Because the decorator replaces the function with `wrapper`, Python can lose some useful metadata.

For example:

```text
Function name
Documentation
Other metadata
```

So Python provides:

```python
from functools import wraps
```

Then:

```python
def logger(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper
```

The key idea:

```text
@wraps(function)

helps preserve useful information
about the original function.
```

For example:

```text
Original function name
Original docstring
```

---

# 🧠 Don't Memorize This Yet

At first, you'll often see decorators written like:

```python
from functools import wraps


def decorator(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        result = function(*args, **kwargs)

        return result

    return wrapper
```

You don't need to stare at it like:

```text
😵‍💫 "I must memorize every character immediately."
```

Nope.

Understand the structure:

```text
DECORATOR
    │
    ├── Receives function
    │
    ├── Creates wrapper
    │
    ├── Wrapper does extra work
    │
    ├── Wrapper calls original function
    │
    └── Returns wrapper
```

The syntax will become familiar through use.

---

# 🧪 Practice — Timing Mindset

Create a decorator:

```python
def announce(function):
    ...
```

It should print:

```text
▶ Starting...
```

Then run the function.

Then:

```text
⏹ Finished.
```

Use it with at least two functions:

```python
@announce
def train():
    print("Training players.")


@announce
def rest():
    print("Players are resting.")
```

Notice:

```text
Same extra behavior

Different original functions
```

That is exactly why decorators exist.

---

# 🧠 Practical Uses of Decorators

Decorators are useful when many functions need the same extra behavior.

Examples:

```text
📝 Logging
```

```text
"Function started"

Run function

"Function finished"
```

---

```text
🔐 Authentication
```

Conceptually:

```text
User requests action
       │
       ▼
Decorator checks permission
       │
       ├── Allowed → Run function
       │
       └── Denied  → Stop
```

---

```text
⏱ Timing
```

```text
Start timer
     ↓
Run function
     ↓
Stop timer
     ↓
Show duration
```

---

```text
💾 Caching
```

```text
Need result?
    │
    ├── Already calculated?
    │       ↓
    │      Yes → Reuse result
    │
    └── No
          ↓
      Run function
          ↓
      Store result
```

You'll see decorators everywhere in more advanced Python frameworks.

---

# ⚔️ Mini Challenge — Football Academy Access Control

Let's build a simple example.

Create:

```python
def require_admin(function):
    ...
```

For now, keep it simple.

Your decorator should print:

```text
🔐 Checking permissions...
```

Then run the original function.

Then:

```text
✅ Action completed.
```

Use it with:

```python
@require_admin
def add_player(name):
    print(f"{name} added to the academy.")
```

Calling:

```python
add_player("Salah")
```

should produce:

```text
🔐 Checking permissions...
Salah added to the academy.
✅ Action completed.
```

---

## 🔥 Upgrade

Now imagine:

```python
current_user = {
    "name": "Coach Alex",
    "role": "admin"
}
```

Modify the decorator so that:

```text
role == "admin"
```

allows the function to run.

Otherwise:

```text
❌ Access denied.
```

Conceptually:

```text
Request
   │
   ▼
require_admin
   │
   ├── Admin?
   │      │
   │      ├── YES → Run function
   │      │
   │      └── NO → Access denied
   │
   ▼
Done
```

---

# 🔥 Hard Challenge — Universal Action Decorator

Create a decorator:

```python
def academy_action(function):
    ...
```

Requirements:

```text
Before:
▶ Starting academy action...

Run original function

After:
🏁 Academy action complete!
```

It must:

* Work with functions that have no arguments
* Work with functions that have positional arguments
* Work with functions that have keyword arguments
* Preserve return values

Test it with:

```python
@academy_action
def train():
    print("Players are training.")
```

Then:

```python
@academy_action
def register_player(name, position):
    return f"{name} registered as {position}"
```

And:

```python
@academy_action
def update_fitness(name, fitness=100):
    return f"{name}'s fitness is now {fitness}"
```

Your decorator should handle all three.

🥋 **This is the real decorator workout.**

---

# 🐛 Debugging Lab — Argument Explosion

Look at this decorator:

```python
def logger(function):

    def wrapper():
        print("Running...")
        return function()

    return wrapper
```

Then:

```python
@logger
def greet(name):
    print(f"Hello, {name}")
```

Calling:

```python
greet("Valerian")
```

causes a problem.

## Your Mission

1. Why does this fail?
2. What does `wrapper()` currently accept?
3. How can `*args` fix positional arguments?
4. Why might we also use `**kwargs`?

Rewrite the decorator correctly.

---

# 🧠 The Decorator Blueprint

At this stage, this structure should start feeling familiar:

```python
from functools import wraps


def decorator(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        # Before

        result = function(*args, **kwargs)

        # After

        return result

    return wrapper
```

Read it like this:

```text
Receive function
       │
       ▼
Create wrapper
       │
       ├── Receive arguments
       │
       ├── Do something BEFORE
       │
       ├── Run original function
       │
       ├── Do something AFTER
       │
       └── Return original result
       │
       ▼
Return wrapper
```

🎁

That's your decorator blueprint.

---

# 🧪 Comprehension Check

Complete this sentence:

> A decorator is a function that takes another function and ______________________________.

Then:

> The wrapper is responsible for ______________________________.

Then:

> `*args` and `**kwargs` are useful because ______________________________.

Then:

> We return `result` when ______________________________.

---

# 🥋 Skill Check

## Question 1

Why are functions able to be passed into other functions in Python?

---

## Question 2

What makes a function a higher-order function?

---

## Question 3

Explain this:

```python
new_function = decorator(original_function)
```

---

## Question 4

What does this syntax:

```python
@decorator
```

conceptually do?

---

## Question 5

Why do decorators often use:

```python
*args
```

and:

```python
**kwargs
```

?

---

## Question 6

Why might a decorator need:

```python
return result
```

?

---

## Question 7

What problem does:

```python
@wraps(function)
```

help with?

---

## Question 8

Give two real-world uses for decorators.

---

# 🧠 Explain It Like You're Teaching Someone

Explain decorators using this idea:

```text
🎁 ORIGINAL FUNCTION

      ↓

📦 WRAPPER

      ↓

Extra behavior
      +
Original behavior
```

Your explanation should answer:

> "Why not just put the extra code inside every function?"

If you can answer that naturally...

you understand decorators.

---

# 🏗️ Project Connection — Football Academy AI

Imagine the Football Academy system has many actions:

```text
Add Player
Update Player
Delete Player
View Statistics
Create Training Session
```

Maybe every important action needs:

```text
📝 Logging
```

Instead of:

```python
def add_player():
    print("Logging...")
    # action


def delete_player():
    print("Logging...")
    # action


def update_player():
    print("Logging...")
    # action
```

We can conceptually use:

```text
            🎁 logger
                │
        ┌───────┼───────┐
        ▼       ▼       ▼
    add_player delete  update
```

Each function keeps its main responsibility.

The decorator handles the shared behavior.

This idea becomes extremely useful in larger applications.

Later, when we get to things like:

```text
🌐 APIs
🤖 AI Applications
🔐 Authentication
📊 Logging
⏱ Performance Monitoring
```

you'll see this pattern again.

---

# 🧠 Batch Summary

You learned the path:

```text
FUNCTIONS ARE OBJECTS
        │
        ▼
Can be stored in variables
        │
        ▼
Can be passed to functions
        │
        ▼
Can be returned from functions
        │
        ▼
HIGHER-ORDER FUNCTIONS
        │
        ▼
🎁 DECORATORS
```

A decorator:

```text
Receives a function
        ↓
Creates a wrapper
        ↓
Adds extra behavior
        ↓
Runs original function
        ↓
Returns the wrapper
```

The common flexible structure:

```python
from functools import wraps


def decorator(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        # Before

        result = function(*args, **kwargs)

        # After

        return result

    return wrapper
```

And:

```python
@decorator
def function():
    ...
```

is conceptually similar to:

```python
def function():
    ...

function = decorator(function)
```

🤯

The `@` symbol is not magic.

It's just a cleaner doorway into the decorator pattern.

---

# 🏅 Batch Progress

```text
🟣 PART 6 — PYTHONIC FEATURES

🔁 Iterators
    ██████████  COMPLETE ✅

⚡ Generators
    ██████████  COMPLETE ⚡

🎁 Decorators
    ██████████  COMPLETE 🥋
                 ↑
              YOU ARE HERE

🚪 Context Managers
    ░░░░░░░░░░  NEXT

🏆 Part Boss Fight
    ░░░░░░░░░░  APPROACHING...
```

---

# 🏅 Decorator Badge Unlocked

```text
╔══════════════════════════════════╗
║                                  ║
║       🎁 DECORATOR APPRENTICE     ║
║                                  ║
║   "I wrap functions with style." ║
║                                  ║
╚══════════════════════════════════╝
```

😂😎

---

# 🚦 Exit Check

Before moving on, this should make sense:

> **A decorator takes a function, wraps it with another function, and allows extra behavior to be added without rewriting the original function.**

And this:

```python
@decorator
def my_function():
    ...
```

should no longer feel like:

```text
🧙 Ancient Python sorcery
```

but more like:

```text
😎 "Ah. Python is passing my function
into the decorator and replacing it
with the wrapper."
```

---

# 🚪 NEXT UP — Context Managers

And then we're entering one of Python's cleanest ideas:

```python
with something:
    ...
```

We'll explore why Python can say:

```text
Open resource
    ↓
Use resource
    ↓
Automatically clean up
```

Even when things go wrong. 👀

But first...

**Decorator dojo cleared.** 🥋🎁

Take a breath, shake off the `*args` and `**kwargs` dust...

Because **Context Managers** are next. 🚪🐍