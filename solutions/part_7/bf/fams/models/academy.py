# ./models/academy.py

"""Contains the academy model and academy methods."""

# These helper functions are needed to validate arguments before academy actions are executed
from helpers import check_empty_player_list
from helpers import require_non_empty
from helpers import validate_rating

# These custom exceptions are needed to expose a more meaningful high-level interface
from exceptions import PlayerAlreadyExistsError
from exceptions import PlayerNotFoundError

# Required in type hinting for the player object
from models.player import Player

class Academy:
  """Creates an academy instance and contains academy actions.
  
  Methods:
    - `__init__`: initializes an academy instance.
        
        Usage:
        academy = Academy("My Football Academy")
    
    - `add_player`: adds a player object to the academy players.
    
        Usage:
        val = Player("Val", 28, "CDM", 7.8)
        academy.add_player(val)
        
    - `find_player`: searches for a player by name.
    
        Usage:
        academy.find_player("Val")

    - `remove_player`: removes a player from the academy.

        Usage:
        academy.remove_player("Val")
    
    - `update_rating`: updates a player's ratings.

        Usage:
        academy.update_rating("Val", 9.5)
    
    - `average_rating`: returns the average rating of all players in the academy.
    
        Usage:
        academy.average_rating()
        
    - `top_player`: returns highest-rated player in the academy.
    
        Usage:
        academy.top_player()"""
  
  def __init__(self, name: str) -> None:
    """Validates name argument and initializes academy object.
    
    Arg:
      - name (`str`): name of academy
    
    Returns None
    
    Raises:
      - AcademyError - Name cannot be empty."""
    require_non_empty(name, "Academy Name", case="academy")
    self.name = name
    self.players: dict[str, Player] = {}

  def add_player(self, player: "Player") -> "Academy":
    """Adds a player object to the academy.
    
    Arg:
      - player (`Player`): player object
    
    Returns self or academy instance
    
    Raises:
      - PlayerAlreadyExistsError - player already exists
    """
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
  
  def update_rating(self, name:str, new_rating: float) -> "Academy":
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