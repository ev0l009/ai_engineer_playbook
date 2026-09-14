# Football Academy Management System(FAMS)
## Overview
FAMS is a backend management service built for football managers and coaches to enable them handle various tasks including player registeration, removal, update, squad assessments.


## Features
- Player registration
- Player search by name
- Player removal
- Update player rating
- Access to team average rating
- Get highest rated player


## Project Structure
fams
    |_ models
    |   |_ academy.py
    |   |_ player.py
    |_ main.py
    |_ test_main.py
    |_ helpers.py
    |_ exceptions.py
    |_ Readme.md


## Installation
- Clone repo
- Prepare and activate virtual environment
- Run `pip install pytest`
- Run `python3 main.py`


## Usage
### Methods
- `Player`: initializes a player object


#### Example
```python
val = Player("Val", 29, "CDM", 2.9)
print(val.name) # Output: Val
print(val.position) # Output: CDM
print(val.rating) # Output: 2.9
```


- `add_player`: adds a player to the academy


#### Example
```python
academy.add_player(val)
# → Academy object (supports chaining, e.g. academy.add_player(a).add_player(b))
```


- `find_player`: searches for a player and returns the player object if found


#### Example
```python
player = academy.find_player("Val")
print(player.name) # Output: Val
print(player.age) # Output: 29
```


- `remove_player`: removes a player from academy


#### Example
```python
academy.remove_player("Val")
academy.find_player("Val") # Raises as error as "Val" has been removed from the academy.
```


- `update_rating`: updates a player's rating


#### Example
```python
academy.update_rating("Val", 9.7)
val = academy.find_player("Val")
print(val.rating) # Output: 9.7
```


- `average_rating()`: returns the average rating of players in the academy


#### Example
```python
academy.average_rating()
# Average rating: 7.8
```


- `top_player()`: returns the player with the highest rating


#### Example
```python
academy.top_player()
# Top player: Val with rating 7.8
```


## Testing
- All tests files are available in`test_main.py`. Use `pytest -v` to run tests


## Design notes
The academy stores players as dicts and this is preferred because of efficiency in targeting by key instead of looping through every item.
