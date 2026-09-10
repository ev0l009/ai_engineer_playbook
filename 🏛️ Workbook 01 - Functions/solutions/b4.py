players = [
  { 'name': 'Val', 'age': 26, 'position': 'DMF', 'goals': 9, 'assists': 12 },
  { 'name': 'Justice', 'age': 25, 'position': 'CF', 'goals': 29, 'assists': 6 },
  { 'name': 'Mike', 'age': 32, 'position': 'CM', 'goals': 9, 'assists': 6 },
  { 'name': 'Leo', 'age': 23, 'position': 'LWF', 'goals': 18, 'assists': 14 },
  { 'name': 'Kofi', 'age': 28, 'position': 'CB', 'goals': 3, 'assists': 2 },
  { 'name': 'Santi', 'age': 21, 'position': 'AMF', 'goals': 11, 'assists': 15 },
  { 'name': 'Tariq', 'age': 27, 'position': 'RB', 'goals': 2, 'assists': 8 },
]

# show players
def players_list():
  '''
  Prints a list of all registered players
  '''
  print('PLAYERS LIST:\n')
  for player in players:
    print(f'Name: {player['name']}\nAge: {player['age']}\nPosition: {player['position']}\nGoals: {player['goals']}\nAssists: {player['assists']}\n')

# add player
def add_player(
    name: str,
    age: int,
    pos: str,
    goals: int,
    assists: int
  ):
  '''
  Rgisters a new player to the list of players. Requires \nname(string), age(integer), pos - position(string), \ngoals(integer), assists(integer)
  '''
  players.append({
    'name': name,
    'age': age,
    'position': pos,
    'goals': goals,
    'assists': assists
  })
  players_list()
add_player(
  name = 'Joe',
  age = 23,
  pos = 'CF',
  goals = 12,
  assists = 23
)

# remove player
def remove_player(name, age, pos):
  '''
  Un registers a player from the list of players. Requires args name(string), age(integer), position - pos(str)
  '''
  print('REMOVE PLAYER:')
  for player in players:
    found_player = False
    if player['name'] == name and player['age'] == age and player['position'] == pos:
      found_player = True
      players.remove(player)
      break
    if found_player == False:
      print('Could\'nt find this player')
  players_list()
remove_player(name = 'Val', age = 26, pos = 'DMF')

# find player(s)/show_player(s):
def find_player(name = None, age = None, pos = None, goals = None, assists = None):
  '''
  Search for player(s). Optional args name(str), age(int), pos(str), goals(int), assists(int). Returns the whoke player list if no argument is passed and return an err for no player found.
  '''
  if name == None and age == None and pos == None and goals == None and assists == None:
    players_list()
    return
  found_player = False
  print('PLAYER SEARCH')
  for player in players:
    if name == player['name'] or age == player['age'] or pos == player['position'] or goals == player['goals'] or assists == player['assists']:
      found_player = True
      print(f'Name: {player['name']}\nAge: {player['age']}\nPosition: {player['position']}\nGoals: {player['goals']}\nAssists: {player['assists']}\n')  
  if found_player == False:
    print('Couldn\'t find player')
find_player('Joe')
find_player('Val')

# count players
def count_players():
  '''
  Returns the total number of registered players
  '''
  print(f'\nTOTAL NUMBER OF REGISTERED PLAYERS: {len(players)}')
count_players()

# Top Scorer
def top_scorer(players: list[dict]) -> list[dict]:
  '''
  Shows the top scorer(s)
  '''
  if len(players) == 0:
    print('No registered players')
    return
  players.sort(key=lambda player: player['goals'], reverse=True)
  top_scorers = players[0]
  top_scorers_list = []
  for player in players:
    if player['goals'] == top_scorers['goals']:
      top_scorers_list.append({
        'name': player['name'],
        'goals': player['goals']
      })
  return top_scorers_list

# Most Assists
def most_assists(players: list[dict]) -> list[dict]:
  '''
  Shows the player(s) with the most assists
  '''
  if len(players) == 0:
    print('No registered players')
    return
  players.sort(key=lambda player: player['assists'], reverse=True)
  most_assists = players[0]
  most_assists_list = []
  for player in players:
    if player['assists'] == most_assists['assists']:
      most_assists_list.append({
        'name': player['name'],
        'assists': player['assists']
      })
  return most_assists_list

# Youngest player(s)
def youngest_player(players: list[dict]) -> list[dict]:
  '''
  Shows youngest player(s)
  '''
  if len(players) == 0:
    print('No registered players')
    return
  players.sort(key=lambda player: player['age'])
  youngest_player = players[0]
  youngest_players_list = []
  for player in players:
    if player['age'] == youngest_player['age']:
      youngest_players_list.append({
        'name': player['name'],
        'age': player['age']
      })
  return youngest_players_list

# Average age
def average_age(players: list[dict]) -> float:
  '''
  Shows average age of all players
  '''
  if len(players) == 0:
    print('No registered players')
    return
  age_sum = 0
  for player in players:
    age_sum += player['age']
  average = age_sum/len(players)
  return average

# Average goals
def average_goals(players: list[dict]) -> float:
  '''
  Shows the average goals
  '''
  if len(players) == 0:
    print('No registered players')
    return
  total_goals = 0
  for player in players:
    total_goals += player['goals']
  average = total_goals/len(players)
  return average

# Academy Summary:
def academy_summary(players_list: list[dict]):
  '''
  Displays the Academy Summary
  '''
  print('================')
  print('ACADEMY SUMMARY:')
  print('================\n')

  print('TOP SCORER(S):')
  top_scorers_list = top_scorer(players_list)
  for player in top_scorers_list:
    print(f'{player['name']}: {player['goals']} goals')

  print('\nMOST ASSIST(S):')
  most_assists_list = most_assists(players_list)
  for player in most_assists_list:
    print(f'{player['name']}: {player['assists']} assists')

  print('\nYOUNGEST PLAYER(S):')
  youngest_players_list = youngest_player(players_list)
  for player in youngest_players_list:
    print(f'{player['name']}: {player['age']} yrs old')

  avg_age = average_age(players_list)
  print(f'\nAVERAGE AGE: {avg_age:.2f}')

  avg_goals = average_goals(players_list)
  print(f'\nAVERAGE GOALS: {avg_goals:.2f}')
academy_summary(players)

# 🥋 Boss Fight
def age_key(player): # A bit too much this method
  return player['age']
players.sort(
  key=age_key
)

# Easier/cleaner cus of lamda's anonymity and explicit return meaning less lines of code
players.sort(key=lambda player: player['age'])

# 🐞 Debugging Lab
def add_player(player, squad=[]):
    squad.append(player)
    return squad # Can't quite recall why tho 

# Correct implementation
def add_player(player, squad=None):
    squad.append(player)
    return squad

# is_even()
def is_even(num:int)->bool:
    return num%2==0

# factorial()
def factorial(num:int)->int:
  result = num
  while num>1:
    result *= num-1
    num = num - 1
  return result

# power()
def power(index, base):
  return base**index

# largest()
def largest(*args: tuple[int]) -> int:
  largest_number = args[0]
  for val in args:
    if val > largest_number:
      largest_number = val
  return largest_number

# smallest()
def smallest(*args: tuple[int]) -> int:
  smallest_number = args[0]
  for val in args:
    if val < smallest_number:
      smallest_number = val
  return smallest_number

# average()
def average(*args: tuple[int]) -> float:
  total = 0
  for val in args:
    total += val
  avg = total/len(args)
  return avg

# median()
def median(*args: tuple[int]) -> float:
  if len(args) == 0:
    return
  sorted_data = sorted(args)
  print(sorted_data)
  if len(sorted_data)%2 != 0:
    return sorted_data[int(len(sorted_data)/2)]
  if len(sorted_data)%2 == 0:
    return (sorted_data[int((len(sorted_data)-1)/2)] + sorted_data[int(((len(sorted_data)-1)/2)+1)])/2

# count_vowels()
def count_vowels(s:str)->int:
  if len(s) == 0:
    return
  count = 0
  for char in s:
    if char in ('a','e','i','o','u'):
      count += 1
  return count

# reverse_string()
def reverse_string(s: str) -> str:
  rvsd_str = ''
  for char in reversed(s):
    rvsd_str += char
  return rvsd_str

# is_palindrome()
def is_palindrome(s: str) -> str:
  rvsd_str = ''
  for char in reversed(s):
    rvsd_str += char
  return s == rvsd_str