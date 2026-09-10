# ./models/player.py

'''Contains the player model and player actions'''

# These helper functions are needed to validate arguments before player initialization
from helpers import require_non_empty
from helpers import validate_age
from helpers import validate_rating

class Player:
  '''Creates a player object and holds player actions.
  
  Methods:
    - __init__: validates and initializes player

        Usage:
        val = Player("Val", 23, "CDM", 7.5)

    - __str__: returns player info in formatted and easy-to-read format.

        Usage:
        print(val)'''
  
  def __init__(self, name: str, age: int, position: str,rating: float | int) -> None:
    '''Validates required arguments and initializes a player
    
    Args:
      - name (`str`): player's name
      - age (`int`): player's age and must be an integer greater than or equal to 0.
      - position (`str`): player's position
      - rating (`float | int`): player's rating and must be a float or integer with the range of 0-10.
    
    Returns None
    
    Raises:
      - InvalidPlayerError - empty name or position string
      - InvalidPlayerError - invalid rating(must be an int or float from 0-10)
      - InvalidPlayerError - invalid age(must be int greater than or equal to 0.)'''

    # Order matters: first invalid field is the one reported to the caller.
    # All checks run before any attribute is set, so init never leaves
    # a partially-constructed Player on failure.
    require_non_empty(name, "Name")
    validate_age(age)
    require_non_empty(position, "Position")
    validate_rating(rating)

    self.name = name
    self.age = age
    self.position = position
    self.rating = float(rating)

  def __str__(self):
    '''returns player in an easy-to-read format.
    
    Returns: str - formatted player info'''
    return (
      f"==================\n"
      f"   Player Info:\n"
      f"==================\n"
      f"Name: {self.name}\n"
      f"Age: {self.age}\n"
      f"Position: {self.position}\n"
      f"Rating: {self.rating}"
    )