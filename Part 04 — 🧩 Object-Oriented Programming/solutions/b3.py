# 🏃 Practice
## Easy
# Create `Animal` with attribute name and method `speak()`. Create `Dog(Animal)`. Add `bark()`
class Animal:
  def __init__(self, name: str):
    self.name = name
  def speak(self):
    print('I should be human to speak right?')
class Dog(Animal):
  def bark(self):
    print('Woof! woof!!')
bingo = Dog('Bingo')
bingo.speak()
bingo.bark()

print()
## Medium
# Create `Vehicle` with attribute brand and method `start()`. Create `Car(Vehicle)`. Add `honk()`.
class Vehicle:
  def __init__(self, brand):
    self.brand = brand
  def start(self):
    print('Engines revving!')
class Car(Vehicle):
  def honk(self):
    print('Honk! Honk!!')
corolla = Car('Corolla')
corolla.honk()
corolla.start()

print()
## Hard
# Create `Player` with attributes name, age and methods train(), display(). Create `Defender, Midfielder, Forward, Goalkeeper`. Each should inherit from Player. Give each class one unique method; `tackle(), through_ball(), shoot(), save()`.
class Player:
  def __init__(self, name: str, age: int):
    self.name = name
    self.age = age
  def train(self):
    print(f'{self.name}\'s training in session!')
  def display(self):
    print(f'{self.name} - {self.age}')
class Defender(Player):
  # Honestly, even without the __init__, Defender already has access to the attributes in Player. Wouldn't that mean super() is only useful only when Defender has to initialize it's own attributes or is it conventional to use super() regardless when creating a subclass.
  def tackle(self):
    print(f'{self.name} attempts a tackle!')
class Midfielder(Player):
  def through_ball(self):
    print(f'{self.name} plays a through pass forward')
class Forward(Player):
  def shoot(self):
    print(f'{self.name} shoots and scores!')
class Goalkeeper(Player):
  def save(self):
    print(f'{self.name} makes a fingertip save!!')

paul = Defender('Paul', 26)
paul.tackle()
val = Midfielder('Val', 27)
val.train()
solo = Goalkeeper('Solo', 30)
solo.save()
justice = Forward('Justice', 25)
justice.display()

print()
# 🥋 Boss Mini-Challenge
# Build a small academy hierarchy.
# Player
# should have:
# - name
# - age
# - train()
# Create these subclasses:
# - Goalkeeper
# - Defender
# - Midfielder
# - Forward
# Each subclass should:
# - Call the parent constructor with super().
# - Add one unique attribute (for example, clean_sheets, tackles, assists, or goals).
# - Add one unique method.
# - Then create one object from each class and demonstrate that:
# All of them can train() (inherited behavior).
# Each can perform its own specialized action.
class Player:
  def __init__(self, name: str, age: int):
    self.name = name
    self.age = age
  def train(self):
    print(f'{self.name}\'s training in session...')
class Goalkeeper(Player):
  def __init__(self, name, age):
    super().__init__(name, age)
    self.clean_sheets = 0
  def dive(self):
    print(f'{self.name} makes a brave save!')
class Midfielder(Player):
  def __init__(self, name, age):
    super().__init__(name, age)
    self.assists = 0
  def through_ball(self):
    print(f'{self.name} plays a lovely pass forward...')
class Defender(Player):
  def __init__(self, name, age):
    super().__init__(name, age)
    self.tackles = 0
  def tackle(self):
    print(f'{self.name} attempts a tackle...')
class Forward(Player):
  def __init__(self, name, age):
    super().__init__(name, age)
    self.goals = 0
  def shoot(self):
    self.goals += 1
    print(f'{self.name} shoots and scores!')
  def check_goals(self):
    print(f'{self.name} has {self.goals} goal(s).')

gk = Goalkeeper('James', 21)
gk.train()
gk.dive()
cdm = Midfielder('Val', 22)
cdm.train()
cdm.through_ball()
cb = Defender('John', 23)
cb.train()
cb.tackle()
ss = Forward('Joe', 20)
ss.train()
ss.shoot()
ss.shoot()
ss.check_goals()