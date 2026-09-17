# 🗡️ TRIAL 1 — EXCEPTION MASTER
Return a value from a function when it's required by another operation or process for print requires a value which is returned by the academy __len__ method to output the number of registered players

Return None when nothing is expected from a function. Trying to perform some operations on None would throw an AttributeError. In such cases where None must be returned, then every caller must check for it otherwise the outcome will most like be a confusing AttributeError far away from it's true source, hence the need to raise an exception to force resolution at the error source.

ValueError was not raised in this project because of the need for more meaningful high-level custom exceptions. But for say a function that parses to a float from a string will throw a ValueError if any of the characters are letters or if they are numbers but have more than one decimal point.

Raise a custom exception when you want to expose a high-level error interface with more meaningful message for example a PlayerNotFound error tells more than low-level default exceptions after a search operation fails

Let an exception propagate when the current process can't meaningfuly handle it and it can be handled better higher up the call stack for example, when trying to remove a non-existent player, you search for the missing player which raises an error. The function removing the player doesn't handle the exception but lets it propage to the call site with the try block which handles the exception.

## Elevation Trial 1
Trial 1 is complete. Here's the full set as it now stands, for your record:

Return a value — when the caller needs the result for further operations (e.g. __len__ for player count).
Return None — only when a genuine absence of a value is meaningful and safe (and even then, every caller must explicitly guard for it, or failures surface late and unclear).
Raise ValueError — in generic, domain-agnostic code that has no meaningful custom exception vocabulary of its own (e.g. a float-parsing utility).
Raise a custom exception — when the code belongs to a domain with meaning to add (e.g. PlayerNotFoundError says far more than a bare exception would).
Let an exception propagate — when the current function can't meaningfully handle the failure and a caller higher up the stack is better positioned to (e.g. remove_player not swallowing find_player's errors).


# 🗡️ TRIAL 3 — DOCUMENTATION MASTER
Let someone go through your project for this test.


# 🗡️ TRIAL 2 — TYPE MASTER
- def __len__(self) -> int: accepts the academy instance and returns the number of players as an int.

- def add_player(self, player: "Player") -> "Academy": expects a player object and returns an academy instance. Self also refers to the academy instance.

- def find_player(self, name: str) -> "Player": expects a string and returns a player object.

- def remove_player(self, name: str) -> "Academy": expects a string and returns an academy instance.

- def update_rating(self, name:str, new_rating: float | int) -> "Academy": accepts a string and a float or an integer and returns an academy instance.

- def average_rating(self) -> float: accepts no arguments and returns a float value.

- def top_player(self) -> "Player": expects no arguments and returns a player instance.

- def Player.__str__(self) -> str: accepts the player instance and returns a string

- def Academy.__init__(self, name: str) -> None: accepts the academy object and returns None

- def Player.__init__(self, name: str, age: int, position: str,rating: float | int) -> None: accepts the player instance, strings for name and position, integer for age, float or integer for rating and returns None

## None is mostly impossible except in Academy.__init__ and Player.__init__ where None is returned and that's more by python default design. None is defered as return value or even optional argument value because on failure an AttributeError would be thrown at the call site that would want to make use of the outcome of a success, so it's better to raise relevant exceptions and stop a delayed crash far from the source and also a potentially empty value.

## Any is not needed because its too ambiguous and every method clearly knows what to expect and return. This way, type checkers won't be silent even when wrong methods are called on an object, IDES can also give better suggestions related to specific object and clarity is gained.




# 🗡️ TRIAL 4 — PYTEST MASTER
|Test                                                                  |Category                                                |Why it exists (what regression would this catch?)                                                                                     |
|----------------------------------------------------------------------|--------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
|test_find_player_when_player_exists                                   |Happy path                                              |Confirms a player can be found after been added to the academy                                                                        |
|test_add_player_retrieve_added_player                                 |Happy path + parametrization                            |Confirms players can be added and each player's attribute is not misplaced with another player's                                      |
|test_player_empty_position_raises_invalid_player_error                |Invalid input + parametrization + expected exception    |Proves guard against empty strings works preventing preventing a scenario where when printing player info, position comes out blank   |
|test_remove_player_raises_player_not_found_error_for_missing_player   |Expected exception                                      |Proves an unregistered player cannot be removed from the academy                                                                      |




# 🗡️ TRIAL 5 — PROFESSIONAL JUDGMENT
Q1. Why shouldn't you catch every exception with `except Exception:`?
Ans => Because Exception catches all error types and so prevents appropriate handling of specific kinds of errors adequately. 


Q2. Why can incorrect type hints be worse than having no type hints?
Ans => Incorrect type hints are misleading and will lead to more confusion.


Q3. What makes a good custom exception?
Ans => A good custom exception should cover a specific expected error type


Q4. Why should documentation describe behavior rather than implementation?
Ans => To avoid redundancy. The code itself handles implementation, documentation should handle the why and what and not the how.


Q5. Why are edge cases so important in tests?
Ans => Absolute coverage as they test the extreme limits of expected valid data. 


Q6. What's the difference between "The code works." and "The code is production-ready."
Ans => A production-ready code doesn't just work but has comprehensive data type hinting, error handling, robust testing and documentation and so is more suited to be used by another developer or the public. A code that just works without enforing type hinting and documentation will be confusing and without proper error handling and testing could crash with all sorts of errors and run a very high risk compromised system with corrupted data and leaks