# main.py

"""Service entry point"""

# Required to create academy and player objects
from models.academy import Academy
from models.player import Player

# These custom exceptions are needed to expose a more meaningful high-level error interface
from exceptions import InvalidPlayerError
from exceptions import PlayerAlreadyExistsError
from exceptions import PlayerNotFoundError
from exceptions import AcademyError

empty_academy = Academy("Empty Acade")
academy = Academy('Val Academy')
val = Player("Val",29,"CDM",7.5)
joe = Player("Joe",25,"CF",7.8)
jude = Player("Jude",24,"CAM",8.2)
print(val)

print()
try:
   Player("Val",24,"CAM",8.2)
except InvalidPlayerError as err:
   print(err)
else:
   print(val.rating)

print()
try:
  academy.add_player(Player("",29,"CDM",7.5)).add_player(Player("Joe",25,"CF",7.8)).add_player(Player("Jude",24,"CAM",8.2))
except InvalidPlayerError as err:
  print(f'Error: {err}')
except PlayerAlreadyExistsError as err:
  print(f'Error: {err}')
else:
  print('Players registration successful')


print()
try:
   player = academy.find_player("Jude")
except InvalidPlayerError as err:
   print(f'Error: {err}')
except PlayerNotFoundError as err:
   print(err)
except AcademyError as err:
   print(err)
else:
   print(player)


print()
try:
   empty_academy.remove_player('Joe')
except InvalidPlayerError as err:
   print(f'Error: {err}')
except PlayerNotFoundError as err:
   print(err)
except AcademyError as err:
   print(err)
else:
   print(f"Player successfully unregistered.")
# print(academy.find_player('Joe')) 
# Output: PlayerNotFoundError: 'Joe' is not a registered player.

print()
try:
   academy.update_rating("Val",9.8)
except InvalidPlayerError as err:
   print(f'Rating update Error: {err}')
except PlayerNotFoundError as err:
   print(err)
except AcademyError as err:
   print(err)
else:
   print("Player rating updated successfully ")
   print(academy.find_player("Val"))

print()
try:
   average_rating = academy.average_rating()
except AcademyError as err:
   print(err)
else:
   print(f'Average rating: {average_rating:.2f}')

print()
try:
  player = academy.top_player()
except AcademyError as err:
  print(err)
else:
  print(f"Top player: {player.name}\nRating: {player.rating}")
