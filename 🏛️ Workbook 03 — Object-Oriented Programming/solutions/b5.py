# 🏃 Practice
## Easy
# Create a Book class. Implement __str__(). Print the object.
class Book:
  def __init__(self, name):
    self.name=name
  def __str__(self):
    return f'Title: {self.name}'
deep_blue=Book('Deep Blue')
print(deep_blue)

print()
## Medium
# Create a Playlist class. Store songs in a list. Implement __len__(). Verify len(playlist) works.
class Playlist:
  def __init__(self):
    self.songs=[]
  def __len__(self):
    return len(self.songs)
rap_songs=Playlist()
rap_songs.songs.append('Money Trees')
rap_songs.songs.append('Twinnem')
rap_songs.songs.append('Zeus')
rap_songs.songs.append('My Bad')
print(len(rap_songs))

print()
## Hard
# Create a FootballTeam class. Attributes team_name, players. Implement `__str__`, `__len__`. Create two teams. Print both. Display their sizes using `len()`.
class FootballTeam:
  def __init__(self, team_name):
    self.team_name=team_name
    self.players=[]
  def __str__(self):
    return f'Team Name: {self.team_name}'
  def __len__(self):
    return len(self.players)
volt=FootballTeam('Volt Academy')
raiders=FootballTeam('Blue Raiders')
print(volt)
print(raiders)
volt.players.append('Val')
volt.players.append('Justice')
volt.players.append('Joe')
raiders.players.append('Jerry')
print(len(volt))
print(len(raiders))


print()
# 🎯 Final Boss Challenge — Football Academy AI (OOP Edition)
# Build a mini Football Academy system with the following classes:
# FootballAcademy
#         │
#         ├── stores players
#         │
#         ▼
#       Player
#         │
#         ├── Goalkeeper
#         ├── Defender
#         ├── Midfielder
#         └── Forward
# Requirements
# Player
# Attributes:
# name
# age
# position
# Methods:
# train()
# play()
# __str__()
# Child Classes
# Each should:
# Inherit from Player
# Use super()
# Override play()
# Add one unique method
# Examples:
# Goalkeeper → save_penalty()
# Defender → block_shot()
# Midfielder → through_ball()
# Forward → finish_chance()
# FootballAcademy
# Should:
# Store players
# Add players
# Remove players
# Display all players
# Return the number of players using __len__()
class FootballAcademy:
  def __init__(self, name):
    self.name=name
    self.players=[]
  def add_player(self, player):
    self.players.append(player)
  def remove_player(self, player):
    if player in self.players:
      self.players.remove(player)
  def display_all_players(self):
    print(f'\n{self.name.upper()} PLAYERS.\n')
    for player in self.players:
      print(f'Name: {player.name}')
      print(f'Age: {player.age}')
      print(f'Position: {player.position}')
      print()
  def __len__(self):
    return len(self.players)

class Player:
  def __init__(self, name, age, position):
    self.name=name
    self.age=age
    self.position=position
  def train(self):
    print(f'{self.name} is training...')
  def play(self):
    print(f'{self.name} is training...')
  def __str__(self):
    return f'Player name: {self.name}'

class Goalkeeper(Player):
  def __init__(self,name,age,position):
    super().__init__(name,age,position)
    self.saves=0
  def save(self):
    self.save += 1

class Defender(Player):
  def __init__(self,name,age,position):
    super().__init__(name,age,position)
    self.shots_blocked=0
  def block_shot(self):
    self.shots_blocked += 1

class Midfielder(Player):
  def __init__(self,name,age,position):
    super().__init__(name,age,position)
    self.through_passes=0
  def through_pass(self):
    self.through_passes += 1

class Forward(Player):
  def __init__(self,name,age,position):
    super().__init__(name,age,position)
    self.shots=0
  def shoot(self):
    self.shots += 1

val = Midfielder('Val', 26, 'CDM')
justice = Forward('Justice', 27, 'CF')
volt = FootballAcademy('Volt Academy')
volt.add_player(player=val)
volt.add_player(player=justice)
volt.remove_player(val)
print(len(volt))
for player in volt.players:
  print(player)
volt.display_all_players()