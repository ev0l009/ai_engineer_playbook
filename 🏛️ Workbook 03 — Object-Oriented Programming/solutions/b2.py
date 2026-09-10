# 🏃 Practice
## Easy
# Create a `Book` class with attributes title and author. Create one object. Print both attributes.
class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
deep_blue = Book('Deep Blue', 'Val')
print(deep_blue.author)
print(deep_blue.title)

print()
## Medium
# Create a `Car` class with attributes brand, model and year. Add the method `start()` and the output should be `Toyota Corolla has started.`
class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year
  def start(self):
    print(f'{self.brand} {self.model} has started.')
corolla = Car(brand='Toyota', model='Corolla', year = 2016)
corolla.start()

print()
## Hard
# Create a `FootballPlayer` class with the attributes name, age, position and goals. Add the methods score_goal(), assist() and display_profile(). Create three players. Simulate a match. Display the updated profiles.
class FootballPlayer:
  def __init__(self, name, age, position):
    self.name = name
    self.age = age
    self.position = position
    self.goals = 0
    self.assists = 0

  def score_goal(self):
    self.goals += 1
    print(f'{self.name} shoots and scores. GOAL!!!')

  def assist(self):
    self.assists += 1
    print(f'{self.name} plays a forward pass...')

  def display_profile(self):
    print(f'==================\n  {self.name.upper()} \n==================')
    print(f'Name: {self.name}')
    print(f'Age: {self.age}')
    print(f'Position: {self.position}')
    print(f'Goal(s): {self.goals}')
    print(f'Assist(s): {self.assists}')
    print()

val = FootballPlayer('Valerian', 27, 'CDM')
justice = FootballPlayer('Justice', 26, 'CF')
joe = FootballPlayer('Joseph', 27, 'SS')

val.assist()
joe.score_goal()
val.assist()
justice.score_goal()
joe.assist()
justice.score_goal()

val.display_profile()
justice.display_profile()
joe.display_profile()

'''
🥋 Boss Mini-Challenge
Before moving on, build this entirely on your own:
class FootballTeam:
Requirements:
Attributes:
name
coach
points (starts at 0)
players (starts as an empty list)
Methods:
add_player(player_name)
win_match() → adds 3 points
draw_match() → adds 1 point
display_team()
Create two different teams and verify that each object maintains its own players and points.
'''
class FootballTeam:
  def __init__(self, name: str, coach: str):
    self.name = name
    self.coach = coach
    self.players = []
    self.points = 0
  def add_player(self, player_name: str):
    self.players.append(player_name)
  def win_match(self):
    self.points += 3
  def draw_match(self):
    self.points += 1
  def display_team(self):
    print(f'==================\n  {self.name.upper()} \n==================')
    print(f'Coach: {self.coach}')
    print(f'Points: {self.points}')
    print('Squad List:')
    if not self.players:
      print('  There are no players yet. Please add some.')
    else:
      for index, player in enumerate(self.players):
        print(f'  {index+1}. {player}')

volt = FootballTeam( 'Volt Academy', 'Emmanuel' )
volt.add_player('Val')
volt.add_player('Justice')
volt.add_player('Joe')
volt.draw_match()
volt.win_match()
volt.display_team()

blaze = FootballTeam( 'Blaze Academy', 'Justice' )
blaze.add_player('Mike')
blaze.add_player('Richy')
blaze.add_player('Cletus')
blaze.draw_match()
blaze.draw_match()
blaze.display_team()

deep_blue = FootballTeam( 'Deep blue Academy', 'Jerry' )
deep_blue.add_player('Solomon')
deep_blue.add_player('Charles')
deep_blue.add_player('Frank')
deep_blue.display_team()