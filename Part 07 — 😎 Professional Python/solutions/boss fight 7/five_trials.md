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