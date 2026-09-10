from helpers import check_empty_player_list
from helpers import require_non_empty
from helpers import validate_rating
from exceptions import PlayerAlreadyExistsError
from exceptions import PlayerNotFoundError
from models.player import Player

class Academy:
  def __init__(self, name: str) -> None:
    self.name = name
    self.players: dict[str, Player] = {}

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