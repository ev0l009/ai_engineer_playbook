# 🧱 PART 1 — DESIGN THE DOMAIN
class Player:
  def __init__(self, name: str, age: int, position: str,rating: float | int) -> None:
     require_non_empty(name, "Name")
     validate_age(age)
     require_non_empty(position, "Position")
     validate_rating(rating)
     self.name = name
     self.age = age
     self.position = position
     self.rating = float(rating)


# helpers
def require_non_empty(value: str, field_name: str) -> None:
  if not value.strip():
     raise InvalidPlayerError(f"{field_name} cannot be empty.")
 def validate_rating(value: float | int):
  if not isinstance(value,int) and not isinstance(value,float):
     raise InvalidPlayerError("Player rating must be of type float or int.")
  if value < 0 or value > 10:
     raise InvalidPlayerError("Player rating must be in the range 0-10.")


def check_empty_player_list(player_list: dict[str, Player]):
  if not player_list:
     raise AcademyError("No registered players.")


def validate_age(value: float):
  if not isinstance(value,int):
     raise InvalidPlayerError("Invalid age argument.")
  if value < 0:
     raise InvalidPlayerError("Player age cannot be less than 0.")


# 🛡️ PART 2 — EXCEPTION DESIGN
class AcademyError(Exception):
  pass


class RegistrationError(AcademyError):
  pass


class PlayerNotFoundError(AcademyError):
  pass


class PlayerAlreadyExistsError(RegistrationError):
  pass


class InvalidPlayerError(AcademyError):
  pass


class Academy:
  def __init__(self, name: str) -> None:
     self.name = name
     self.players: dict[str, Player] = {}


  # def add_player(self, player: "Player") -> "Academy":
  #    try:
  #       self.find_player(player.name)
  #    except AcademyError:
  #       pass
  #    else:
  #       raise PlayerAlreadyExistsError(f"{player.name} already exists.")
  #    self.players[player.name.lower()] = player
  #    return self


  def add_player(self, player: "Player") -> "Academy":
     key = player.name.lower()
     if key in self.players:
         raise PlayerAlreadyExistsError(f"{player.name} already exists.")
     self.players[key] = player
     return self
   def find_player(self, name: str) -> "Player":
     check_empty_player_list(self.players)
     require_non_empty(name, "Name")
     key = name.lower()
     if key in self.players:
         return self.players[key]
     raise PlayerNotFoundError(f"'{name}' is not a registered player.")
   def remove_player(self, name: str) -> "Academy":
     player = self.find_player(name)
     self.players.pop(player.name.lower())
     return self
   def update_rating  (self, name:str, new_rating: float) -> "Academy":
     validate_rating(new_rating)
     player = self.find_player(name)
     player.rating = new_rating
     return self
   def average_rating(self) -> float:
      check_empty_player_list(self.players)
      total_ratings = 0
      for player in self.players.values():
          total_ratings += player.rating
      return total_ratings/len(self.players)
   def top_player(self) -> "Player":
     check_empty_player_list(self.players)
     players = list(self.players.values())
     current = players[0]
     for player in players:
         if player.rating > current.rating:
             current = player
     return current
    
academy = Academy('Val Academy')
val = Player("Val",29,"CDM",7.5)
joe = Player("Joe",25,"CF",7.8)
jude = Player("Jude",24,"CAM",8.2)


# try:
#    Player("Jude",24,"CAM",8.2)
# except InvalidPlayerError as err:
#    print(err)
# else:
#    print(val.rating)


try:
  academy.add_player(Player("Val",29,"CDM",7.5))
  academy.add_player(Player("Joe",25,"CF",7.8))
  academy.add_player(Player("Jude",24,"CAM",8.2))
except PlayerAlreadyExistsError as err:
  print(f'Registeration Error: {err}')
except InvalidPlayerError as err:
  print(f'Registeration Error: {err}')
else:
  print('Player registeration successful')
# academy.add_player(Player("Val",29,"CDM",7.5)) # Running this raises an uncaught error, was just testing this as well


# print()
# try:
#    player = academy.find_player("Val")
# except InvalidPlayerError as err:
#    print(f'Error: {err}')
# except PlayerNotFoundError as err:
#    print(err)
# except AcademyError as err:
#    print(err)
# else:
#    print(player.name)


# print()
# try:
#    academy.remove_player('Joe')
# except InvalidPlayerError as err:
#    print(f'Error: {err}')
# except PlayerNotFoundError as err:
#    print(err)
# else:
#    print(f"Player successfully unregistered.")
# print(academy.find_player('Joe')) #Output: PlayerNotFoundError: 'Joe' is not a registered player.


# try:
#    academy.update_rating("Val",97.8)
# except InvalidPlayerError as err:
#    print(f'Rating update Error: {err}')
# except PlayerNotFoundError as err:
#    print(err)
# else:
#    print("Player rating updated successfully ")
#    print(academy.find_player("Val").rating) #Output: 9.8


# try:
#    average_rating = academy.average_rating()
# except AcademyError as err:
#    print(err)
# else:
#    print(f'Average rating: {average_rating:.2f}')


try:
  player = academy.top_player()
except AcademyError as err:
  print(err)
else:
  print(f"Top player: {player.name}\nRating: {player.rating}")


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
 |_ main.py
 |_ test.py
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
- All tests files are available in`/tests`. Use `pytest -v` to run tests


## Design notes
The academy stores players as dicts and this is preferred because of efficiency in targeting by key instead of looping through every item.

