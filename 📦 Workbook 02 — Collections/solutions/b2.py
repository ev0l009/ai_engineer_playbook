# Easy
# 1. Create a tuple of five colours.
colors = 'rose', 'peach', 'purple', 'biege', 'sandgold'

# 2. Print the second colour.
print(colors[1])

# 3. Print the last colour.
print(colors[-1])

## Medium
# Create a tuple `player`, store name. age and position. Unpack it into three variables.
player = 'Val', 25, 'CDM'
name, age, position = player

# Write a function `rectangle(length, width)`. Return area, perimeter using one return statement.
def rectangle(length: float, width: float) -> tuple(float):
  area = length*width
  perimeter = 2*(l+b)
  return area, perimeter

## Hard
# Create a function `student_result()`. Return average, highest, lowest. Unpack the returned tuple and display each value.
def student_result() -> tuple(float):
  return 77.8, 92, 60

average, highest, lowest = student_result()

# Mini Mission
# Build a function called `match_summary(home_goals, away_goals)`. It should return three values, the winner ("Home", "Away", or "Draw"), total goals, goal difference.
# Then unpack the returned tuple like this:
# winner, total_goals, goal_difference = match_summary(3, 1)
def match_summary(home_goals: int, away_goals: int) -> tuple(str, int, int):
  winner = 'Home'
  if home_goals == away_goals:
    winner = 'Draw'
  elif home_goals < away_goals:
    winner = 'Away'
  
  total_goals = home_goals + away_goals

  goal_difference = home_goals - away_goals
  if goal_difference < 0:
    goal_difference *= -1
  
  return winner, total_goals, goal_difference