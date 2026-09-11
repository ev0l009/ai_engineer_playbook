# ./helpers.py

"""Helpful validation functions used across the academy system."""

# required imports so relevant custom exceptions can be raised
from exceptions import InvalidPlayerError
from exceptions import AcademyError

def require_non_empty(value: str, field_name: str, case = 'player') -> None:
  """checks that value is not an empty string

  Args:
    - value (`str`): value to check
    - field_name (`str`): name of field to be used in error message
    
  Returns None
  
  Raises:
    - InvalidPlayerError - string must not be an empty string"""
  if not value.strip():
    if case == 'player':
      raise InvalidPlayerError(f"{field_name} cannot be empty.")
    else:
      raise AcademyError(f"{field_name} cannot be empty.")

  
def validate_rating(value: float | int):
  """checks that value is either a float or an int
  
  Args:
    - value (`int | float`): value to check
    
  Returns None
  
  Raises:
    - InvalidPlayerError - player rating must be an int or a float
    - InvalidPlayerError - player rating must be within the range 0-10.""" 
  if not isinstance(value,int) and not isinstance(value,float):
    raise InvalidPlayerError("Player rating must be of type float or int.")
  if value < 0 or value > 10:
    raise InvalidPlayerError("Player rating must be in the range 0-10.")


def check_empty_player_list(player_list: dict[str, "Player"]):
  """checks that players dict is not empty

  Args:
    - player_list (`dict[str, "Player"])`): dictionary containing academy player objects
    
  Returns None
  
  Raises:
    - AcademyError - Academy players dict is empty""" 
  if not player_list:
    raise AcademyError("No registered players.")


def validate_age(value: int):
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
