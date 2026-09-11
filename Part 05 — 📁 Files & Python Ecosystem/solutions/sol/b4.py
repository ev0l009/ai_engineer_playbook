## Easy
# Read
# ```text
# notes.txt
# ```
# using `with`.
# Print the contents.
with open('notes.txt', 'r') as file:
    print(file.read())

## Medium
# Create
# ```text
# journal.txt
# ```
# Write three lines using `with`.
# Read them back.
with open('journal.txt', 'w') as file:
    file.write('Line 1\nLine 2\nLine 3')
with open('journal.txt', 'r') as file:
    for line in file:
        print(line.strip())

## Hard
# Create
# ```text
# academy.txt
# ```
# Append two new players using `with`.
# Read the file.
# Print every player.
with open('academy.txt', 'a') as file:
    file.write('\nJayce\nReuben')
with open('academy.txt', 'r') as file:
    for line in file:
        print(line.strip())

## Mini Project
# Update your
# ```text
# Player Registration System
# ```
# Replace every occurrence of
# ```python
# open(...)
# ```
# and
# ```python
# close()
# ```
# with
# ```python
# with open(...)
# ```
# Your program should behave exactly the same.
# The code should simply be cleaner and safer.
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

def load_players(db):
    players = []
    with open(db, 'r') as file:
        for line in file:
            player = line.strip().lower()
            players.append(player)
    return players
def save_player(db, new_player):
  with open(db, 'a') as file:
    file.write(f'\n{new_player}')

def register_player(db):
  print('\nREGISTER PLAYER')
  new_player = input('Enter player name: ')
  if not new_player.strip():
    print("Invalid player name.")
    return
  players=load_players(db)
  if new_player.lower() in players:
    print('Player already exists...')
    return
  save_player(db, new_player)
  print('Player successfully registered...')

def show_players(db):
  print('\nSHOW PLAYERS LIST')
  with open(db, 'r') as file:
    for index, player in enumerate(file):
        print(f'{index+1}. {player.strip().capitalize()}')

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