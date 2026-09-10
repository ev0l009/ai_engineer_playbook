# ./models/player.py

'''Creates a player.'''

# These helper functions are need to validate arguments before player initialization
import helpers


class Player:
  '''Initializes a player and performs other player actions
  
  Args:
    - name (`str`): player's name
    - age (`int`): player's age and must be an integer greater than or equal to 0.
    - position (`str`): player's position
    - rating (`float | int`): player's rating and must be a float or integer with the range of 0-10.
  
  
  Returns the a Player object, string or None depending on action
  
  Raises:
    -  '''
  def __init__(self, name: str, age: int, position: str,rating: float | int) -> None:
    helpers.require_non_empty(name, "Name")
    helpers.validate_age(age)
    helpers.require_non_empty(position, "Position")
    helpers.validate_rating(rating)
    self.name = name
    self.age = age
    self.position = position
    self.rating = float(rating)
  def __str__(self):
    return f"==================\n   Player Info:\n==================\nName: {self.name}\nAge: {self.age}\nPosition: {self.position}\nRating: {self.rating}"