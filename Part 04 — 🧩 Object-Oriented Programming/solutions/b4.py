# 🏃 Practice
## Easy
# Create `Animal` with the method `move()` and create `Bird`. Override `move()`. Print `Bird flies.`.
class Animal:
  def __init__(self, name):
    self.name=name
  def move(self):
    print(f'{self.name} is roaming...')
class Bird(Animal):
  def move(self):
    print(f'{self.name} is flying...')
parrot = Bird('Parrot')
parrot.move()

print()
## Medium
# Create `Employee` with method `work()`. Create `Developer`. Override `work()`. Create `Designer`. Override `work()`. Store both objects in a list. Loop through them. Call `work()`.
class Employee:
  def __init__(self, name):
    self.name=name
  def work(self):
    print(f'{self.name} is working...')
class Developer(Employee):
  def work(self):
    print(f'{self.name} is debugging...')
class Designer(Employee):
  def work(self):
    print(f'{self.name} is designing...')
employees = [
  Developer('Valerian'),
  Designer('Charlie')
]
for employee in employees:
  employee.work()

print()
## Hard
# Create `Player` with method `play()`. Create Goalkeeper, Defender, Midfielder, Forward. Override `play()`. Each should describe how that position contributes during a match. Store them in one list. Loop through the list. Call `play()`.
class Player:
  def __init__(self, name):
    self.name=name
  def play(self):
    print(f'{self.name} is playing...')
class Goalkeeper(Player):
  def play(self):
    print(f'{self.name} makes a good save...')
class Defender(Player):
  def play(self):
    print(f'{self.name} attempts a tackle and clears his box...')
class Midfielder(Player):
  def play(self):
    print(f'{self.name} retrieves the ball and plays a through pass forward...')
class Forward(Player):
  def play(self):
    print(f'{self.name} controls and places it beyond the reach of the keeper! GOAL!!!')
players=[
  Goalkeeper('Solo'),
  Defender('Success'),
  Midfielder('Valerian'),
  Forward('Justice')
]
for player in players:
  player.play()

print()
# 🎯 Boss Mini-Challenge
# Build a simple football simulation.
# Create these classes:
# - Player
# - Goalkeeper
# - Defender
# - Midfielder
# - Forward
# Each class should implement:
# # play()
# But each should describe its role differently.
# Then write a function:
# def kickoff(team):
#     for player in team:
#         player.play()
class Player:
  def __init__(self, name):
    self.name=name
  def play(self):
    print(f'{self.name} is playing...')
class Goalkeeper(Player):
  def play(self):
    print(f'{self.name} makes a brilliant save!')
class Defender(Player):
  def play(self):
    print(f'{self.name} tackles and clears the box...')
class Midfielder(Player):
  def play(self):
    print(f'{self.name} dribbles up the left flank and crosses...')
class Forward(Player):
  def play(self):
    print(f'{self.name} attempts a volley... GOAL!!!')
team=[
  Goalkeeper('De Gea'),
  Defender('Ferdinand'),
  Midfielder('Rooney'),
  Forward('Saha')
]
def kickoff(team: list):
  for player in team:
    player.play()
kickoff(team)