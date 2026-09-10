# ./helpers.py
from exceptions import InvalidPlayerError
from exceptions import AcademyError

def require_non_empty(value: str, field_name: str) -> None:
  if not value.strip():
    raise InvalidPlayerError(f"{field_name} cannot be empty.")
def validate_rating(value: float | int):
  if not isinstance(value,int) and not isinstance(value,float):
    raise InvalidPlayerError("Player rating must be of type float or int.")
  if value < 0 or value > 10:
    raise InvalidPlayerError("Player rating must be in the range 0-10.")


def check_empty_player_list(player_list: dict[str, "Player"]):
  if not player_list:
    raise AcademyError("No registered players.")


def validate_age(value: float):
  if not isinstance(value,int):
    raise InvalidPlayerError("Invalid age argument.")
  if value < 0:
    raise InvalidPlayerError("Player age cannot be less than 0.")
