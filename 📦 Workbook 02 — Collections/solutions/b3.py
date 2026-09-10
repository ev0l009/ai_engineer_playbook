# ⚔️ Boss Fight
academy_name = 'Evol Football Academy'
academy_location = (23.454, 66.674)
squad_A = [
  {
    'name': 'Val',
    'age': 27,
    'position': 'CDM',
  },
  {
    'name': 'Justice',
    'age': 26,
    'position': 'CF',
  }
]
covered_positions = {'CF', 'CDM'}

def football_academy_sys(academy_name, academy_location, player_list, covered_positions):
  opt = '0'
  while opt != '7':
    if opt == '0':
      opt = get_menu_opt()
    elif opt == '1':
      add_player(player_list)
      opt = '0'
    elif opt == '2':
      remove_player(player_list)
      opt = '0'
    elif opt == '3':
      find_player(player_list)
      opt = '0'
    elif opt == '4':
      display_squad(player_list)
      opt = '0'
    elif opt == '5':
      count_players(player_list, academy_name)
      opt = '0'
    elif opt == '6':
      show_available_pos(covered_positions)
      opt = '0'
    elif opt == '7':
      break
  print('\nGoodbye...')

def show_available_pos(s: set):
  all_positions = {'GK','CB','LB','RB','DMF','CM','RMF','LMF','AMF','CF','SS'}
  available_pos = all_positions - s
  for pos in available_pos:
    print(pos, end='  ')

def count_players(l: list, academy_name: str):
  print('------------------------\n  Squad Count  \n------------------------')
  print(f'\nThe {academy_name} currently has {len(l)} players in its squad.')

def display_squad(l: list):
  print('------------------------\n  All Players  \n------------------------')
  if not l:
    print('There are no players in your squad.')
    return
  for player in l:
    print()
    print(f'Name: {player['name']}')
    print(f'Age: {player['age']}')
    print(f'Position: {player['position']}')
    print()
  print('Exiting...')

def find_player(l: list):
  print('------------------------\n  Find Player(s)  \n------------------------')
  name = input('Player Name: ')
  position = input('Player position: ')
  age = input('Player age: ')
  count = 0
  found = False
  for player in l:
    if player['name'] == name or player['position'] == position or player['age'] == age:
      found = True
      print()
      print(f'Name: {player['name']}')
      print(f'Age: {player['age']}')
      print(f'Position: {player['position']}')
    print()
  if found is False:
    print('No player found')
  print('Exting...')
  
def remove_player(l: list) -> list:
  print('------------------------\n  Unregister Player  \n------------------------')
  name = input('Player Name: ')
  position = input('Player position: ')
  for player in l:
    if player['name'] == name and player['position'] == position:
      l.remove(player)
      print('Player unregistered. Exiting...')
      return l
  print('Operation failed. Exiting...')
  return l

def add_player(l: list) -> list:
  print('------------------------\n  Player Registeration  \n------------------------')
  player = {
    'name': input('Player Name: '),
    'age': int(input('Player age: ')),
    'position': input('Player position: '),
  }
  if not isinstance(player['name'], str) or not isinstance(player['age'], int) or not isinstance(player['position'], str):
    print('Invalid credentials. Exting...')
    return l
  if player in l:
    print('Player already exists. Exiting...')
    return l
  l.append(player)
  print('Player Registeration Successful. Returning to menu...')
  return l

def get_menu_opt():
  print('\n==========================\n Football Academy System  \n==========================')
  attempts = 3
  while attempts > 0:
    print('1. Add player\n2. Remove player\n3. Find player\n4. Display squad\n5. Count players\n6. Show available positions\n7. Exit')
    opt = input('Select an option: ')
    if opt in ('1','2','3','4','5','6','7'):
      return opt
    attempts -= 1
    if attempts > 0:
      print(f'\nInvalid option. Tries left: {attempts}\n')
      continue
  print('\nToo many invalid attempts.')
  return '7'

football_academy_sys(academy_name, academy_location, squad_A, covered_positions)