# ./models/player.py

'''Creates a player.'''

# These helper functions are need to validate arguments before player initialization
from helpers import require_non_empty
from helpers import validate_age
from helpers import validate_rating


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