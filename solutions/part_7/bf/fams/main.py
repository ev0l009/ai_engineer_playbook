from models.academy import Academy
from models.player import Player

from exceptions import InvalidPlayerError
from exceptions import PlayerAlreadyExistsError
from exceptions import PlayerNotFoundError
from exceptions import AcademyError
academy = Academy('Val Academy')
val = Player("Val",29,"CDM",7.5)
joe = Player("Joe",25,"CF",7.8)
jude = Player("Jude",24,"CAM",8.2)


try:
   Player("Jude",24,"CAM",8.2)
except InvalidPlayerError as err:
   print(err)
else:
   print(val.rating)


try:
  academy.add_player(Player("Val",29,"CDM",7.5))
  academy.add_player(Player("Joe",25,"CF",7.8))
  academy.add_player(Player("Jude",24,"CAM",8.2))
except PlayerAlreadyExistsError as err:
  print(f'Registeration Error: {err}')
except InvalidPlayerError as err:
  print(f'Registeration Error: {err}')
else:
  print('Player registeration successful')
academy.add_player(Player("Val",29,"CDM",7.5)) # Running this raises an uncaught error, was just testing this as well


print()
try:
   player = academy.find_player("Val")
except InvalidPlayerError as err:
   print(f'Error: {err}')
except PlayerNotFoundError as err:
   print(err)
except AcademyError as err:
   print(err)
else:
   print(player.name)


print()
try:
   academy.remove_player('Joe')
except InvalidPlayerError as err:
   print(f'Error: {err}')
except PlayerNotFoundError as err:
   print(err)
else:
   print(f"Player successfully unregistered.")
print(academy.find_player('Joe')) #Output: PlayerNotFoundError: 'Joe' is not a registered player.


try:
   academy.update_rating("Val",97.8)
except InvalidPlayerError as err:
   print(f'Rating update Error: {err}')
except PlayerNotFoundError as err:
   print(err)
else:
   print("Player rating updated successfully ")
   print(academy.find_player("Val").rating) #Output: 9.8


try:
   average_rating = academy.average_rating()
except AcademyError as err:
   print(err)
else:
   print(f'Average rating: {average_rating:.2f}')


try:
  player = academy.top_player()
except AcademyError as err:
  print(err)
else:
  print(f"Top player: {player.name}\nRating: {player.rating}")
