# 🏃 Practice
## 🟢 Easy — Your First Package
# Create a project folder with two items: a main.py file and a greetings folder. Inside the greetings folder, add an __init__.py file and a hello.py file. In hello.py, define a function called greet that takes a name and returns the string "Hello, {name}!" using an f-string. In main.py, import the greet function from the greetings folder and call it.

# projects/main.py
from greetings.hello import greet
print(greet('Val'))
# OR
from files.sol.sol.greetings import greet
print(greet('Val'))

# projects/greetings/__init__.py
# Empty for the first main.py option
# OR
from .hello import greet
# for the second

# projects/greetings/hello.py
def greet(name):
    return f"Hello, {name}!"


## 🟡 Medium — Organize Your Utilities
# Create a project folder with a main.py file and a utils folder. Inside the utils folder, add an __init__.py file, a calculator.py file, and a formatter.py file. In calculator.py, define a function called add that takes two arguments a and b and returns their sum. In formatter.py, define a function called format_name that takes a name, strips any leading or trailing whitespace, and converts it to title case. In main.py, import both the add function from the calculator module and the format_name function from the formatter module, then use them in your code.

# project/main.py
from utils import add
from utils import format_name

print(add(2,5))
print(format_name('Val Alora'))

# project/utils/__init__.py
from .calculator import add
from .formatter import format_name

# project/utils/calculator.py
def add(a, b):
    return a + b

# project/utils/formatter.py
def format_name(name):
    return name.strip().title()


## 🔴 Hard — Mini Football Package
# Create a football_project folder with a main.py file, a models folder, and a utils folder. Inside the models folder, add an __init__.py file and a player.py file. Inside the utils folder, add an __init__.py file and a display.py file.

# In models/player.py, define a Player class with three attributes: name, position, and age. Add a __str__() method to the class that returns a readable string representation of the player.

# In utils/display.py, create a function called display_player that takes a player object as an argument and prints that player.

# In your main.py file, import the Player class from the models.player module and import the display_player function from the utils.display module. Then create a new Player instance with a name, position, and age of your choice. Finally, call the display_player function and pass the player instance to it to display the player's information.
class Player:
    def __init__(self, name: str, position: str, age: int) -> None:
        self.name=name
        self.position=position
        self.age=age
    def __str__(self) -> str:
        return f"PLAYER INFO\nName: {self.name}\nAge: {self.age}\nPosition: {self.position}"

# project/models/__init__.py
from .player import Player

# project/utils/display.py
def display_player(player: "Player") -> None:
    print(player)

# project/utils/__init__.py
from .display import display_player

# project/main.py
from models import Player
from utils import display_player

player=Player('Val', 'CDM', 26)
display_player(player)