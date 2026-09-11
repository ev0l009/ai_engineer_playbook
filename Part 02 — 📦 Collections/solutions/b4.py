## Easy
# 1. Create a set of five colours.
colors = {'blue','orange','biege','red','brown'}

# 2. Add another colour.
colors.add('yellow')

# 3. Remove one colour.
colors.discard('blue')

# 4. Check if `"Blue"` exists.
if 'blue' in colors:
  print('Found')
else:
  print('Not found')

## Medium
# Create a list `scores = [4,5,5,6,7,7,8,8]`. Convert it into a set. Print the result.
scores = [4,5,5,6,7,7,8,8]
print(set(scores))

# Create two sets of football players. Display Union, Intersection, Difference
players_A = {'Jude', 'Val', 'Justice', 'Charles'}
players_B = {'Jerry', 'Val', 'Lucas', 'Charles'}

print(players_A | players_B)
print(players_A & players_B)
print(players_A - players_B)
print(players_A ^ players_B)

## Hard
# Create a football registration system. Allow users to Register players, Prevent duplicate registrations, Display all registered players. Use a **set**.
registered_players = set()

def football_registeration_sys(l: set):
  opt = '0'
  attempts = 2
  while attempts > 0:
    if opt == '0':
      print('\n=============================\nFootball Registeration System\n=============================\nWelcome to the FRS.')
      opt = input('1. Register player\n2. Show players\n3. Exit\nSelect an option: ')
    elif opt == '1':
      register_player(registered_players)
      opt = '0'
    elif opt == '2':
      show_players(l)
      opt = '0' 
    elif opt == '3':
      print()
      break
    else:
      attempts -= 1
      if attempts > 0:
        print(f'Invalid attempt\nTries left: {attempts}')
      opt= '0'
      continue
  if opt != '3':
    print('\nToo may invalid attempts.')
  print('Exiting...')

def show_players(l: set):
  if not l:
    print('\nThere are no players. Please register.\n')
  idx = 0
  for player in l:
    print(f'{idx+1}. {player}')

def register_player(l: set) -> set:
  val = input('Player name: ')
  if val in l:
    print('This player already exists.\nNo updates made\nReturning to menu')
    return l
  l.add(val)
  print('Player successfully registered')
  return l

football_registeration_sys(registered_players)