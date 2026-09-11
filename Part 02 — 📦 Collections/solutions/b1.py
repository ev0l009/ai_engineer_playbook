# EASY
# 1. Create a list of five favourite foods.
fav_foods = ['egusi', 'jollof', 'beans', 'cake', 'fish']

# 2. Print the first item.
print(fav_foods[0])

# 3. Print the last item.
print(fav_foods[-1])

# 4. Replace one item.
fav_foods[3] = 'fried rice'

# 5. Add another item.
fav_foods.append('Fried yams')

# MEDIUM
# Create 'top_scorers', add ten players, remove two. print the final list.

top_scorers = []
top_scorers.append('Mike')
top_scorers.append('Val')
top_scorers.append('Justice')
top_scorers.append('Joe')
top_scorers.append('Richy')
top_scorers.append('Charles')
top_scorers.append('Ricky')
top_scorers.append('Solomon')
top_scorers.append('Festus')
top_scorers.append('Phil')

top_scorers.remove('Festus')
top_scorers.pop(3)

# print(top_scorers)

# Create a shopping list that allow users to add, remove, display using functions.
shopping_list: list[str] = ['car','rope']

def add_to_list(s: str, l: list):
  l.append(s)
  return l

def remove_from_list(key, l: list):
  if type(key) is int and key < len(l) and key >= len(l)*-1:
    l.pop(key)
  if type(key) is str:
    l.remove(key)
  return l

def display_list(l: list):
  print(l)

display_list(shopping_list)


# HARD
# Create a squad manager menu. It should have these features implemented; add player, remove player, show squad, count players, exit. Everything must use functions.

squad = ['Val', 'Justice', 'Ezzy']
def squad_manager(player_list: list):
  opt = '0'
  while opt != '5':
    if opt == '0':
      opt = get_menu_opt()

    elif opt == '1':
      add_player(player_list)
      opt = '0'
    elif opt == '2':
      remove_player(player_list)
      opt = '0'
    elif opt == '3':
      show_squad(player_list)
      opt = '0'
    elif opt == '4':
      count_players(player_list)
      opt = '0'

  print('\nExiting...')

def count_players(l: list):
  print(f'\nTotal players in squad: {len(l)}')
  print('Returning to menu...\n')

def show_squad(l: list):
  print('\nCURRENT SQUAD:')
  if not l:
      print('Squad is empty.')
  else:
      for idx, player in enumerate(l, 1):
          print(f'{idx}. {player}')
  print('\nReturning to menu...\n')

def add_player(l: list) -> list:
  print('\nADD PLAYER:')
  val = input('Player Name: ')
  if val == '':
    print('Operation Failed: Couldn\'t add this player\nReturning to menu...\n')
    return l
  l.append(val)
  print('\nAdding player successful.\nReturning to menu...\n')
  return l

def remove_player(l: list) -> list:
  print('\nREMOVE PLAYER:')
  val = input('Player Name: ')
  if val == '':
    print("Operation Failed: Couldn't remove this player\nReturning to menu...\n")
    return l

  if val in l:
    l.remove(val)
    print('\nPlayer removal successful.\nReturning to menu...\n')
  else:
    print(f'\nPlayer "{val}" not found in squad.\nReturning to menu...\n')
  return l

def get_menu_opt() -> str:
  print('--------------------\n SQUAD MANAGER MENU \n--------------------')
  attempts = 3
  while attempts > 0:
    opt = input('1. Add player\n2. Remove player\n3. Show squad\n4. Count player\n5. Exit\nSelect an option: ')
    if opt in ('1','2','3','4','5'):
      return opt

    attempts -= 1
    
    if attempts > 0:
      print(f'\nInvalid input. Attempts left: {attempts}')
      continue
  
  print('\nToo many invalid attempts.')
  return '5'

squad_manager(squad)