from models.academy import Academy
from models.player import Player

from exceptions import AcademyError
from exceptions import InvalidPlayerError

# try:
#     Academy("")
# except AcademyError as err:
#     print(err)

try:
    Player("",27,"CDM",8.0)
except InvalidPlayerError as err:
    print(err)