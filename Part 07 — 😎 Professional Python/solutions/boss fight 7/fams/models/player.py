# ./models/player.py

'''Contains the player model and player actions'''

# These helper functions are needed to validate arguments before player initialization
from helpers import require_non_empty
from helpers import validate_age
from helpers import validate_rating

from exceptions import InvalidPlayerError

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
      - rating (`float | int`): player's rating and must be a float or integer within the valid range (see MIN_RATING/MAX_RATING in helpers module).
    
    Returns None
    
    Raises:
      - InvalidPlayerError - empty name or position string
      - InvalidPlayerError - invalid rating must be an int or float within the valid range (see MIN_RATING/MAX_RATING in helpers module).
      - InvalidPlayerError - invalid age(must be int greater than or equal to 0.)'''

    # Order matters: first invalid field is the one reported to the caller.
    # All checks run before any attribute is set, so init never leaves
    # a partially-constructed Player on failure.
    require_non_empty(name, "Player Name", error = InvalidPlayerError)
    validate_age(age)
    require_non_empty(position, "Player Position", error = InvalidPlayerError)
    validate_rating(rating)

    self.name = name
    self.age = age
    self.position = position
    self.rating = float(rating)

  def __str__(self) -> str:
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