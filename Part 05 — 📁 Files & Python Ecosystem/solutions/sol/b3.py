# 🏃 Practice
## Easy
# Create `notes.txt`. Write `Learning Python is fun!`
file=open('notes.txt', 'w')
file.write('Learning Python is fun!')
file.close()

print()
## Medium
# Create `shopping.txt`. Write
# ```text
# Rice
# Beans
# Milk
# ```
# Append
# ```text
# Bread
# ```
# Read the file afterwards to verify the result.
file=open('shopping.txt', 'w')
file.write('Rice\n')
file.write('Beans\n')
file.write('Milk\n')
# Very much tempted to go like `Rice\nBeaans\nMilk`...
file.close()

file=open('shopping.txt', 'a')
file.write('Bread')
file.close()

file=open('shopping.txt', 'r')
for line in file:
  print(line.strip())
file.close()

print()
## Hard
# Create `academy.txt`. Write four player names. Read them back into a list. Append one new player. Read again. Print the updated list.
file=open('academy.txt', 'w')
file.write('Val\nJustice\nJoe\nMike')
file.close()

file=open('academy.txt', 'r')
players=[]
for line in file:
  player=line.strip()
  players.append(player)
file.close()

file=open('academy.txt', 'a')
file.write('\nJerry')
file.close()

file=open('academy.txt', 'r')
for line in file:
  player=line.strip()
  if player not in players:
    players.append(player)

print(players)

print()
# ⚔️ Mini Project
# Build a simple `Player Registration System`
# Menu
# 1. Register Player
# 2. Show Players
# 3. Exit
# Registering a player should
# ↓
# Append to
# academy.txt
# Showing players should
# ↓
# Read the file
# ↓
# Print every player.
# Congratulations.
# You've just built persistent storage.

db_path='academy.txt'
def player_reg_sys(db):
  opt = '0'
  while opt != '3':
    if opt == '0':
      opt=get_menu_opt()
    elif opt == '1':
      register_player(db)
      opt = '0'
    elif opt == '2':
      show_players(db)
      opt = '0'
  print('\nExiting...')

def register_player(db):
  print('\nREGISTER PLAYER')
  new_player = input('Enter player name: ')

  file=open(db, 'r')
  lines = file.readlines()
  players = []
  for line in lines:
    player=line.strip()
    players.append(player)
  file.close()

  if new_player in players:
    print('Player already exists...')
    return

  file=open(db, 'a')
  file.write(f'\n{new_player}')
  file.close()
  print('Player successfully registered...')

def show_players(db):
  print('\nSHOW PLAYERS LIST')
  file=open(db, 'r')
  for index, line in enumerate(file):
    player = line.strip()
    print(f'{index+1}. {player}')
  file.close()
  return

def get_menu_opt()->str:
  print('\nPLAYER REGISTERATION SYSTEM.')
  attempts = 3
  while attempts:
    opt = input('1. Register Player\n2. Show Players\n3. Exit\nSelct an option:  ')
    if opt in ('1','2','3'):
      return opt
    attempts -= 1
    if attempts > 0:
      print(f'\nInvalid entry, {attempts} chances left...')
  print('Too many invalid attempts...')
  return '3'

player_reg_sys(db_path)