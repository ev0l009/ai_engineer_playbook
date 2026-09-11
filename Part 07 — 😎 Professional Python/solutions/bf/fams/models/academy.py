# ./models/academy.py

"""Manages players data for the football academy."""

# These helper functions are needed to validate arguments before academy actions are executed
from helpers import check_empty_player_list
from helpers import require_non_empty
from helpers import validate_rating

# These custom exceptions are needed to expose a more meaningful high-level error interface
from exceptions import PlayerAlreadyExistsError
from exceptions import PlayerNotFoundError

# Required for type hinting for the player object
from models.player import Player

class Academy:
  """
    Creates an academy instance and contains academy actions.
  
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
          academy.top_player()
  """
  
  def __init__(self, name: str) -> None:
    """
      Validates name argument and initializes academy object.
      
      Arg:
        - name (`str`): name of academy
      
      Returns None
      
      Raises:
        - AcademyError - Name cannot be empty.
    """
    require_non_empty(name, "Academy Name", case="academy")
    self.name = name
    self.players: dict[str, Player] = {}

  def add_player(self, player: "Player") -> "Academy":
    """
      Adds a player object to the academy.
      
      Arg:
        - player (`Player`): player object
      
      Returns academy - self, enabling self chaining
      
      Raises:
        - PlayerAlreadyExistsError - player already exists
    """
    key = player.name.lower()
    if key in self.players:
      raise PlayerAlreadyExistsError(f"{player.name} already exists.")
    self.players[key] = player
    return self
  
  def find_player(self, name: str) -> "Player":
    """
      Searches for a player by name.
      
      Arg:
        - name (`str`): name of player
        
      Returns the player object
      
      Raises:
        - AcademyError - academy player list is empty.
        - InvalidPlayerError - name cannot be empty.
        - PlayerNotFoundError - players does not exist in academy records.
    """

    check_empty_player_list(self.players)
    require_non_empty(name, "Name")
    key = name.lower()
    if key in self.players:
      return self.players[key]
    raise PlayerNotFoundError(f"'{name}' is not a registered player.")
  
  def remove_player(self, name: str) -> "Academy":
    """
      Removes player from academy records.
      
      Arg:
        - name (`str`): name of player
      
      Returns Academy - self, enabling self chaining.
      
      Raises:
        - Calls `find_player` which raises AcademyError if academy player list is empty
        - Calls `find_player` which raises InvalidPlayerError if player name is empty
        - Calls `find_player` which raises PlayerNotFoundError if player is not registered.
    """
    player = self.find_player(name)
    self.players.pop(player.name.lower())
    return self
  
  def update_rating(self, name:str, new_rating: float) -> "Academy":
    """
      Updates player's rating.
        
      Args:
        - name (`str`): name of player
        - new_rating (`float`): new player rating
      
      Returns Academy - self, enabling self chaining.
      
      Raises:
        - Calls validate_rating which raises InvalidPlayerError if rating is not within the range of 0-10.
        - Calls `find_player` which raises AcademyError if academy player list is empty
        - Calls `find_player` which raises InvalidPlayerError if player name is empty
        - Calls `find_player` which raises PlayerNotFoundError if player is not registered.
    """
    validate_rating(new_rating)
    player = self.find_player(name)
    player.rating = new_rating
    return self
  
  def average_rating(self) -> float:
    """
      Calculate the average rating of all players in the academy.
      
      Returns:
        - Average rating of all players(`float`)
      
      Raises:
        - Calls `check_empty_player_list` which raises AcademyError if academy has no registered players.
    """
    check_empty_player_list(self.players)
    total_ratings = 0
    for player in self.players.values():
      total_ratings += player.rating
    return total_ratings/len(self.players)
  
  def top_player(self) -> "Player":
    """
      Gets the player with the highest rating.
          
      Returns:
        - Highest rated player object(`Player`)
      
      Raises:
        - Calls `check_empty_player_list` which raises AcademyError if academy has no registered players.
    """
    check_empty_player_list(self.players)
    players = list(self.players.values())
    current = players[0]
    for player in players:
        if player.rating > current.rating:
          current = player
    return current