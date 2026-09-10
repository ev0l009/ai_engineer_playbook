# 🥋 PART 7 — PROFESSIONAL PYTHON
# ⚔️ BOSS FIGHT: THE PRODUCTION GAUNTLET

> "Knowing the tools is one thing.
> Knowing when, where, and WHY to use them together is professional Python."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    🏯 BOSS ARENA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

You are now responsible for a small production-style Python service.

Your mission:

    Take a messy Football Academy system
    and turn it into code that is:

        🛡️ Safe
        🧠 Typed
        📖 Documented
        🧪 Tested
        🧹 Maintainable

You are NOT being asked to simply make the program "work."

You must make it behave like professional Python.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# 👹 THE BOSS

                    ┌─────────────────────┐
                    │   ACADEMY MANAGER    │
                    │                     │
                    │  💥 Buggy           │
                    │  💥 Untyped         │
                    │  💥 Undocumented    │
                    │  💥 Untested        │
                    │                     │
                    └──────────┬──────────┘
                               │
                         YOUR MISSION
                               │
                               ▼
                    ┌─────────────────────┐
                    │  PRODUCTION READY   │
                    │                     │
                    │  🛡️ Exceptions      │
                    │  🔤 Static Types    │
                    │  📖 Documentation   │
                    │  📝 Docstrings      │
                    │  🧪 Pytest          │
                    │                     │
                    └─────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# 🧩 THE SCENARIO

Football Academy FC stores information about its players.

Each player has:

    - name
    - age
    - position
    - rating

The academy needs a small service that can:

    1. Add players
    2. Find players
    3. Remove players
    4. Update ratings
    5. Calculate average rating
    6. Return the highest-rated player

But the existing implementation is terrible.

It has:

    ❌ inconsistent exceptions
    ❌ missing type hints
    ❌ misleading behavior
    ❌ poor documentation
    ❌ missing docstrings
    ❌ weak tests
    ❌ duplicated logic
    ❌ edge cases nobody considered


Your job is to fix it.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# 🗺️ PROJECT STRUCTURE

Build the project like this:

academy_manager/
│
├── academy/
│   ├── __init__.py
│   ├── models.py
│   ├── service.py
│   └── exceptions.py
│
├── tests/
│   ├── test_models.py
│   └── test_service.py
│
├── README.md
└── pyproject.toml


You don't necessarily need to implement every file immediately.

The goal is to think like someone maintaining a real Python project.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# 🧱 PART 1 — DESIGN THE DOMAIN

Create a Player model.

It should contain:

    name: str
    age: int
    position: str
    rating: float


Example:

    Player(
        name="Victor",
        age=21,
        position="Midfielder",
        rating=8.4
    )


## RULES

A player:

    - must have a non-empty name
    - must have a positive age
    - must have a valid rating
    - rating must be between 0 and 10
    - position must not be empty


### 💀 BOSS QUESTION

Where should validation happen?

Option A:

    Inside every service method.

Option B:

    Inside the Player model.

Option C:

    Randomly wherever convenient.

Choose deliberately.

Explain WHY.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# 🛡️ PART 2 — EXCEPTION DESIGN

Do NOT simply throw generic exceptions everywhere.

Create meaningful custom exceptions.

For example:

    AcademyError

Then more specific errors beneath it.

Possible design:

    AcademyError
        ├── PlayerNotFoundError
        ├── DuplicatePlayerError
        └── InvalidPlayerError


You decide the final hierarchy.

## RULE

Your exceptions should communicate WHAT went wrong.

Bad:

    raise Exception("bad")

Better:

    raise PlayerNotFoundError(...)

Best:

    raise PlayerNotFoundError(
        f"Player '{name}' does not exist."
    )


### 🧠 THINK

Why is a custom exception better than returning:

    None

or:

    False

for every failure?


Explain your reasoning.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# ⚔️ PART 3 — BUILD THE SERVICE

Create an AcademyService.

It should support:

    add_player(player)
    get_player(name)
    remove_player(name)
    update_rating(name, rating)
    average_rating()
    top_player()


The service should maintain the academy's players.

You decide the internal data structure.

Hint:

    Think about the operations you need frequently.

Do NOT choose a structure just because you already know how to use it.

Choose it because it fits the problem.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# 🔤 PART 4 — STATIC TYPING AUDIT

Now pretend you inherited this:

    def add_player(player):
        ...

    def get_player(name):
        ...

    def update_rating(name, rating):
        ...

    def average_rating():
        ...

    def top_player():
        ...


Your job:

Add appropriate type annotations.

For every public function/method, think about:

    INPUT TYPE
    RETURN TYPE
    POSSIBLE NONE
    POSSIBLE EXCEPTIONS


Example conceptually:

    def get_player(...) -> Player:
        ...


But ask yourself:

    What happens when the player doesn't exist?

Should it be:

    -> Player

or:

    -> Player | None

?

There is no automatic correct answer.

The behavior of your function determines the correct type.

🔥 IMPORTANT:

Your type hints must describe reality.

Do NOT use:

    Any

just to make the type checker happy.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# 📖 PART 5 — DOCUMENTATION BATTLE

Now imagine another developer joins your project.

They should be able to understand:

    - what the project does
    - how to install it
    - how to run it
    - how to test it
    - how the architecture is organized
    - what the public API does


Your README must contain at minimum:

    # Academy Manager

    ## Overview

    ## Project Structure

    ## Installation

    ## Usage

    ## Running Tests

    ## Design Notes


Do NOT write documentation that simply repeats the code.

Documentation should explain the system.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# 📝 PART 6 — DOCSTRING AUDIT

Every important public component should have a useful docstring.

At minimum:

    - module docstrings
    - public classes
    - public methods
    - public functions


For example:

    class AcademyService:
        """
        Manage player records for the football academy.
        """

But don't stop there.

For meaningful methods, document:

    Args
    Returns
    Raises


Example structure:

    def update_rating(...) -> None:
        """
        Update a player's rating.

        Args:
            name: Name of the player.
            rating: New rating between 0 and 10.

        Raises:
            PlayerNotFoundError:
                If the player does not exist.
            InvalidPlayerError:
                If the rating is outside the valid range.
        """


🔥 CRITICAL:

Your docstring must match the ACTUAL behavior.

If the function raises PlayerNotFoundError,
the documentation should not claim it returns None on failure.

Code and documentation must agree.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# 🧪 PART 7 — BUILD THE TEST SUITE

Now we enter the real arena.

Your test suite must test BEHAVIOR.

Not implementation details.


Create tests for:

────────────────────────────────────────────
PLAYER VALIDATION
────────────────────────────────────────────

    ✓ valid player
    ✓ empty name
    ✓ invalid age
    ✓ empty position
    ✓ rating below 0
    ✓ rating above 10


────────────────────────────────────────────
ADD PLAYER
────────────────────────────────────────────

    ✓ adding a player
    ✓ retrieving the player
    ✓ duplicate player


────────────────────────────────────────────
GET PLAYER
────────────────────────────────────────────

    ✓ existing player
    ✓ missing player


────────────────────────────────────────────
REMOVE PLAYER
────────────────────────────────────────────

    ✓ existing player
    ✓ missing player


────────────────────────────────────────────
UPDATE RATING
────────────────────────────────────────────

    ✓ valid update
    ✓ invalid rating
    ✓ missing player


────────────────────────────────────────────
STATISTICS
────────────────────────────────────────────

    ✓ average rating
    ✓ top player
    ✓ multiple players
    ✓ boundary cases
    ✓ empty academy


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# 🧪 PART 8 — PYTEST REQUIREMENTS

Your tests must demonstrate:

    assert
    pytest.raises
    fixtures
    parametrization

For example, validation tests are excellent candidates
for parametrization.

Conceptually:

    @pytest.mark.parametrize(
        "rating",
        [-1, 10.1, 100]
    )
    def test_invalid_rating(rating):
        ...


Don't blindly parametrize everything.

Use parametrization when multiple inputs test
the SAME behavior.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# 🏗️ PART 9 — FIXTURES

Create at least one useful fixture.

For example:

    a standard AcademyService

or:

    a collection of test players


The fixture should remove unnecessary setup duplication.

But don't create fixtures merely because pytest has fixtures.

Ask:

    "Does this make my tests clearer?"


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# 💀 PART 10 — EDGE CASE GAUNTLET

This is where amateurs get eliminated.

What should happen when:

    1. The academy has zero players?

    2. average_rating() is called?

    3. top_player() is called?

    4. Two players have the same rating?

    5. A player's name is an empty string?

    6. A player's name contains only spaces?

    7. The same player is added twice?

    8. update_rating() receives 10?

    9. update_rating() receives 0?

    10. update_rating() receives 10.01?

    11. A player is removed and then requested?

YOU must define the behavior.

There is no hiding behind:

    "I didn't think of that."


Professional programmers think about failure states.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# 🐞 DEBUGGING LAB — BROKEN CODE

The following pseudo-code contains several design problems.

Study it carefully:

    class Academy:

        def __init__(self):
            self.players = []

        def add(self, player):
            self.players.append(player)

        def find(self, name):
            for player in self.players:
                if player.name == name:
                    return player

        def average(self):
            total = 0
            for player in self.players:
                total += player.rating

            return total / len(self.players)

        def update(self, name, rating):
            player = self.find(name)
            player.rating = rating

        def top(self):
            return max(self.players, key=lambda p: p.rating)


Now identify EVERYTHING wrong with it.

Think about:

    🛡️ Exceptions
    🔤 Typing
    📖 Documentation
    🧪 Testing
    🧠 Design
    💀 Edge cases


Do not immediately rewrite it.

First diagnose it.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# 🔎 DEBUGGING LAB — DIAGNOSIS TABLE

Fill this in:

| Problem | Why it's dangerous | Professional fix |
|---------|--------------------|------------------|
| ?       | ?                  | ?                |
| ?       | ?                  | ?                |
| ?       | ?                  | ?                |
| ?       | ?                  | ?                |
| ?       | ?                  | ?                |


Try to find at least 8 problems.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# 🧠 PART 11 — BEHAVIOR VS IMPLEMENTATION

Suppose your service internally uses:

    dict

Your test should generally NOT say:

    assert isinstance(service.players, dict)

Why?

Because that tests implementation.

Instead test behavior:

    add player
    retrieve player
    update player
    remove player


If you later change:

    dict

to:

    database

your behavior tests should still make sense.


🔥 PROFESSIONAL TESTING PRINCIPLE:

    Test what the system DOES.

    Not how the system happens to do it.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# 🧹 PART 12 — REFACTORING CHALLENGE

Now perform a professional refactor.

Your final project should demonstrate:

    ✓ clear naming
    ✓ sensible modules
    ✓ meaningful exceptions
    ✓ accurate type hints
    ✓ useful docstrings
    ✓ README documentation
    ✓ isolated tests
    ✓ fixtures
    ✓ parametrization
    ✓ edge-case handling


And remove:

    ✗ duplicated logic
    ✗ meaningless exceptions
    ✗ unexplained magic values
    ✗ misleading names
    ✗ unnecessary Any
    ✗ tests coupled to implementation


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# 🥋 FINAL BOSS — THE FIVE TRIALS

You cannot claim victory until you can complete all five.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🗡️ TRIAL 1 — EXCEPTION MASTER

Explain:

    When should you:

        return a value

        return None

        raise ValueError

        raise a custom exception

        let an exception propagate

Your answer must use examples from AcademyService.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🗡️ TRIAL 2 — TYPE MASTER

For every public method in your service:

    1. Write the signature.
    2. Explain the parameter types.
    3. Explain the return type.
    4. Explain whether None is possible.
    5. Explain why Any is or isn't necessary.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🗡️ TRIAL 3 — DOCUMENTATION MASTER

Write:

    1. Module docstring
    2. Class docstring
    3. Method docstrings
    4. README outline


Then perform the ultimate test:

    Could another developer use your API
    without reading the implementation?

If not:

    improve the documentation.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🗡️ TRIAL 4 — PYTEST MASTER

Design a test suite containing:

    ✓ happy paths
    ✓ boundary cases
    ✓ invalid inputs
    ✓ expected exceptions
    ✓ fixtures
    ✓ parametrization
    ✓ isolated tests


Then explain:

    Why each test exists.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🗡️ TRIAL 5 — PROFESSIONAL JUDGMENT

Answer these without searching:

────────────────────────────────────────────

Q1.

Why shouldn't you catch every exception with:

    except Exception:

?

────────────────────────────────────────────

Q2.

Why can incorrect type hints be worse than
having no type hints?

────────────────────────────────────────────

Q3.

What makes a good custom exception?

────────────────────────────────────────────

Q4.

Why should documentation describe behavior
rather than implementation?

────────────────────────────────────────────

Q5.

Why are edge cases so important in tests?

────────────────────────────────────────────

Q6.

What's the difference between:

    "The code works."

and:

    "The code is production-ready."

────────────────────────────────────────────


# 🏆 BOSS SUBMISSION

Your submission should contain:

    1️⃣ Architecture decision

    2️⃣ Exception hierarchy

    3️⃣ Player model

    4️⃣ AcademyService design

    5️⃣ Type annotations

    6️⃣ Broken-code diagnosis

    7️⃣ Fixed implementation

    8️⃣ Test plan

    9️⃣ Pytest tests

    🔟 Documentation strategy

    1️⃣1️⃣ Answers to the five trials


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# 🧠 BONUS ROUND — CODE REVIEW

Imagine I am your senior engineer.

I ask:

    "Why did you design it this way?"

You must be able to defend:

    - your data structure
    - your exception hierarchy
    - your validation location
    - your return types
    - your test cases
    - your fixture design
    - your parametrization choices
    - your documentation decisions


If your answer is:

    "Because that's how Python does it."

❌ FAIL.

If your answer is:

    "Because this behavior makes the API clearer,
     safer, and easier to maintain."

🔥 GOOD.

Professional Python is not memorizing syntax.

It's making deliberate engineering decisions.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# 📊 BOSS GRADING

Total: 100 XP

    🛡️ Exception Handling       20 XP
    🔤 Static Typing             15 XP
    📖 Documentation             10 XP
    📝 Docstrings                10 XP
    🧪 Pytest                    25 XP
    🧠 Design Decisions          10 XP
    🐞 Debugging                 10 XP

Ranks:

    0–49    🥉 Apprentice
    50–69   🥈 Professional Trainee
    70–84   🥇 Python Professional
    85–94   ⚔️ Senior Python Warrior
    95–100  👑 PROFESSIONAL PYTHON MASTER


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# 🏯 PART 7 EXIT CRITERION

You officially clear Part 7 when you can confidently say:

    "I can write Python that is not only functional,
     but typed, documented, tested, and resilient."


That means:

    Exception Handling       ✅
    Static Typing            ✅
    Documentation            ✅
    Docstrings               ✅
    Pytest                   ✅
    Integration              ⚔️ THIS BOSS


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# 🗺️ CURRENT JOURNEY

PHASE 1 — PYTHON FLUENCY
│
├── Part 1 Foundations              ✅
├── Part 2 Functions                ✅
├── Part 3 Collections              ✅
├── Part 4 OOP                     ✅
├── Part 5 Files & Ecosystem       ✅
├── Part 6 Pythonic Features       ✅
│
└── Part 7 Professional Python
    ├── Exception Handling         ✅
    ├── Static Typing              ✅
    ├── Documentation              ✅
    ├── Docstrings                 ✅
    ├── Pytest                     ✅
    └── ⚔️ BOSS                    🔥 NOW


                    ↓
              DEFEAT THE BOSS
                    ↓

PHASE 2 — DATA STRUCTURES
                    │
                    ▼
               🧠 DSA


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# 👹 THE FINAL MESSAGE

You've learned the individual weapons.

Now prove you can fight with all of them at once.

No new topic.

No tutorial hand-holding.

No "here's exactly how to do it."

You already know the tools.

This fight is about engineering judgment.

                    🥋
              ENTER THE ARENA.
                    ⚔️

           PROFESSIONAL PYTHON BOSS

                 YOUR MOVE.