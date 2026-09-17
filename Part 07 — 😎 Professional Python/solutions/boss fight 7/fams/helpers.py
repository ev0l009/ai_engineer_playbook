# ./helpers.py

"""Helpful validation functions used across the academy system."""

# required imports so relevant custom exceptions can be raised
from exceptions import InvalidPlayerError
from exceptions import AcademyError

MIN_RATING = 0
MAX_RATING = 10

def require_non_empty(value: str, field_name: str, error: type[Exception]) -> None:
  """checks that value is not an empty string

  Args:
    - value (`str`): value to check
    - field_name (`str`): name of field to be used in error message
    - error (`type[Exception]`): expected error class, not an instance.
    
  Returns None
  
  Raises: 
    Exception: Field cannot be empty. (See exceptions module.)"""
  if not value.strip():
    raise error(f"{field_name} cannot be empty.")

def validate_rating(value: float | int) -> None:
  """checks that value is either a float or an int
  
  Args:
    - value (`int | float`): value to check
    
  Returns None
  
  Raises:
    - InvalidPlayerError - player rating must be an int or a float
    - InvalidPlayerError - player rating must be within the valid range (see MIN_RATING/MAX_RATING in this module).""" 
  if type(value) is not int and type(value) is not float:
    raise InvalidPlayerError("Player rating must be of type float or int.")
  if value < MIN_RATING or value > MAX_RATING:
    raise InvalidPlayerError(f"Player rating must be in the range {MIN_RATING}-{MAX_RATING}.") 


def require_non_empty_academy(player_list: dict[str, "Player"]) -> None:
  """checks that players dict is not empty

  Args:
    - player_list (`dict[str, "Player"]`): dictionary containing academy player objects
    
  Returns None
  
  Raises:
    - AcademyError - Academy players dict is empty""" 
  if not player_list:
    raise AcademyError("No registered players.")


def validate_age(value: int) -> None:
  """checks that value is an int
  
  Args:
    - value (`int`): value to check
    
  Returns None
  
  Raises:
    - InvalidPlayerError - player age must be an int
    - InvalidPlayerError - player age must be equal to or greater than 0"""
  if type(value) is not int:
    raise InvalidPlayerError("Invalid age argument.")
  if value < 0:
    raise InvalidPlayerError("Player age cannot be less than 0.")
