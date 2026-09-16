# Football Academy Management System(FAMS)
## Overview
FAMS is a backend management service built for football managers and coaches to enable them handle various tasks including player registration, removal, update, squad assessments.


## Features
- Player registration
- Player search by name
- Player removal
- Update player rating
- Access to team average rating
- Get highest rated player


## Project Structure
fams
    |
    |_ models
    |   |
    |   |_ academy.py
    |   |
    |   |_ player.py
    | 
    |_ main.py
    |
    |_ test_main.py
    |
    |_ helpers.py
    |
    |_ exceptions.py
    |
    |_ README.md


## Installation
- Clone repo
- Prepare and activate virtual environment
- Run `pip install pytest`
- Run `python3 main.py`


## Usage
### Methods
- `Player`: initializes a player object and required to run academy methods.

#### Example
```python
try:
   val = Player("Val",24,"CAM",8.2)
except InvalidPlayerError as err:
   print(err) # raise errors if any
else:
   print(val) # Output: Player info
```


- `Academy`: initializes the academy object and required to run Academy methods.

#### Example
```python
try:
    academy = Academy("My Football Academy")
except AcademyError as err:
   print(err) # raise errors if any
else:
    print(academy.name) # Output: My Football Academy
```


- `add_player`: adds a player to the academy

#### Example
```python
try:
    (
        academy
            .add_player(Player("Val",29,"CDM",7.5))
            .add_player(Player("Joe",25,"CF",7.8))
            .add_player(Player("Jude",24,"CAM",8.2))
    )
except InvalidPlayerError as err:
  print(f'Error: {err}')
except PlayerAlreadyExistsError as err:
  print(f'Error: {err}')
else:
  print('Players registration successful')
# → Academy object (supports chaining as shown above)
```


- `find_player`: searches for a player and returns the player object if found

#### Example
```python
try:
   player = academy.find_player("Jude")
except InvalidPlayerError as err:
   print(f'Error: {err}')
except PlayerNotFoundError as err:
   print(err)
except AcademyError as err:
   print(err)
else:
   print(player) # Prints player info or raises relevant errors
```


- `remove_player`: removes a player from academy

#### Example
```python
try:
   academy.remove_player('Val')
except InvalidPlayerError as err:
   print(f'Error: {err}')
except PlayerNotFoundError as err:
   print(err)
except AcademyError as err:
   print(err)
else:
   print(f"Player successfully unregistered.")
```


- `update_rating`: updates a player's rating

#### Example
```python
try:
   academy.update_rating("Val",9.8)
except InvalidPlayerError as err:
   print(f'Rating update Error: {err}')
except PlayerNotFoundError as err:
   print(err)
except AcademyError as err:
   print(err)
else:
   print("Player rating updated successfully ")
   print(academy.find_player("Val").rating)
```


- `average_rating`: returns the average rating of players in the academy

#### Example
```python
try:
   average_rating = academy.average_rating()
except AcademyError as err:
   print(err)
else:
   print(f'Average rating: {average_rating:.2f}')
```


- `top_player`: returns the player with the highest rating

#### Example
```python
try:
  player = academy.top_player()
except AcademyError as err:
  print(err)
else:
  print(f"Top player: {player.name}\nRating: {player.rating}")
```

## Exceptions
```text
AcademyError
    |
    |_ RegistrationError
    |   |
    |   |_PlayerAlreadyExistsError
    |
    |_ PlayerNotFoundError
    |
    |_ InvalidPlayerError
```
- AcademyError - Generic academy error
- RegistrationError - Academy sub-error raised during failed registration operations.
- PlayerNotFoundError - Academy sub-error raised when searching for an unregistered player.
- PlayerAlreadyExistsError - Registration sub-error raised when attempting to register already registered player.
- InvalidPlayerError - Academy sub-error raised when an invalid player argument is passed.

## Testing
- All test files are available in `test_main.py`. Use `pytest -v` to run tests


## Design notes
The academy stores players as dicts and this is preferred because of efficiency in targeting by key instead of looping through every item.