## 🟢 Easy
# Import:
# ```python
# math
# ```
# Use it to calculate:
# ```python
# sqrt(81)
# ```
# Then import:
# ```python
# random
# ```
# Generate a random number between:
# ```text
# 1 and 100
# ```
import math
import random

print(math.sqrt(81))
print(random.randint(1,100))

print()
## 🟡 Medium
# Create:
# ```text
# greetings.py
# ```
# Add:
# ```python
# def greet(name):
#     return f"Hello, {name}!"
# ```
# Create:
# ```text
# main.py
# ```
# Import the module and call `greet()`.
# Try both:
# ```python
# import greetings
# ```
# and:
# ```python
# from greetings import greet
# ```
# /main.py
from files.sol.sol.greetings import greet
print(greet('Val'))
# or 
import files.sol.sol.greetings as greetings
print(greetings.greet('Val'))
# /greetings.py
def greet(name):
    return f"Hello, {name}!"

print()
## 🔴 Hard
# Create this structure:
# ```text
# academy/
# │
# ├── main.py
# ├── players.py
# └── utils.py
# ```
# ### `players.py`
# Create:
# ```python
# def create_player(name, position):
# ```
# Return a dictionary.
# ---
# ### `utils.py`
# Create:
# ```python
# def display_player(player):
# ```
# Print the player's information.
# ---
# ### `main.py`
# Import both functions.
# Create a player.
# Display the player.
# academy/main.py
import players
import utils

player=players.create_player('Val', 'CDM')
utils.display_player(player)
# academy/players.py
def create_player(name: str, position: str) -> dict:
    return {
        "name": name,
        "position": position
    }
# academy/utils.py
def display_player(player):
    print('Player Info:')
    print(f'Player Name: {player["name"]}')
    print(f'Position: {player["position"]}')