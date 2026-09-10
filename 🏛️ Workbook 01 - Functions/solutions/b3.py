# 1. Write a lambda that cubes a number.
cube = lambda x: x**3
print(cube(2))

# 2. Sort a list of names by length.
names = [
  'Paul', 'Valerian', 'Jerry', 'Jesse', 'Eve', 'Stephen'
]
names.sort(key=lambda name: len(name))
print(names)

# 3. Write a function that accepts another function and a number, then applies it three times.
def apply_thrice(func, val):
  return func(func(func(val)))
def add_five(x):
  return x + 5
print(apply_thrice(add_five, 10))

# 4. Write a function with annotations.
def add_nums(*nums: int) -> int:
  '''
  Returns the sum of variable numbers of integers
  '''
  total = 0
  for num in nums:
    total += num
  return total
print(add_nums(2,5,7,1))
help(add_nums)

# Given a list of dictionaries representing football players, sort them by: * goals * assists * age
players = [
  { 'name': 'Valerian', 'age': 26, 'goals': 8, 'assists': 15 },
  { 'name': 'Justice', 'age': 25, 'goals': 19, 'assists': 6 },
  { 'name': 'Jerry', 'age': 29, 'goals': 10, 'assists': 9 },
  { 'name': 'Success', 'age': 19, 'goals': 4, 'assists': 8 },
  { 'name': 'Mike', 'age': 32, 'goals': 15, 'assists': 8 },
]

players.sort(key = lambda player: player['goals'])
print(players)
players.sort(key = lambda player: player['assists'])
print(players)
players.sort(key = lambda player: player['age'])
print(players)

