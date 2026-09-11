# 🧪 Practice
# Easy
# Create a generator function called `football_positions` that yields the following positions in order: Goalkeeper, Defender, Midfielder, Forward. Then create the generator object by calling the function and assigning it to a variable called `positions`. Use the `next` function to retrieve each position one at a time. Do not use a `for` loop.
def football_positions():
    yield "Goalkeeper"
    yield "Defender"
    yield "Midfielder"
    yield "Forward"
positions=football_positions()
print(next(positions))
print(next(positions))
print(next(positions))
print(next(positions))

print()
# Create a generator function called `colors` that yields the strings Red, Green, and Blue in that order. Then call `next` on the generator four times. Answer the following questions: What happens during the first three calls? What happens during the fourth call? Why does that happen?
def colors():
    yield 'Red'
    yield 'Green'
    yield 'Blue'
my_colors=colors()
print(next(my_colors))
print(next(my_colors))
print(next(my_colors))
# The first three calls prints Red, Green and Blue. The forth calls raise the StopIteration error. This happens cus generator are still iterators and gives such errors after exhausting it's items

# Consider this generator function called numbers that yields the values 10, 20, 30, and 40. You then create a generator object called values and call next on it twice. Answer these questions: What values have been produced so far? What value comes next? Has the function finished running? If you call next on values two more times, what happens? Explain your answers using the concepts of state, pause, and resume in the context of generator execution.
# Ans => 10 and 20 have been produced. 30 comes next. The functions hasn't finished. Calling next(values) two more times yields 30 and 40.
# Calling next(value) for the first sets the state to 10. At this point the function pauses. On the next call, the function resumes and sets its state to the next value. This keeps on until it exhausts its items.

print()
# 🟡 Medium Practice — Number Generator
# Create a generator function called number_generator that takes a limit argument. It should yield numbers starting from 1 up to and including the provided limit. For example, calling number_generator(5) and then iterating over it with a for loop should produce 1, 2, 3, 4, and 5.
def number_generator(limit):
    for num in range(1, limit+1):
        yield num
numbers=number_generator(5)
for number in numbers:
    print(number)

print()
# Create a generator function called even_numbers that takes a limit argument. It should yield even numbers starting from 2 up to and including the given limit. For example, when you iterate over even_numbers(10) with a for loop, the output should be 2, 4, 6, 8, and 10. Remember not to build a list first—do not collect the numbers in a list and return it. Instead, use the yield keyword to produce each number one at a time as a generator.
def even_numbers(limit):
    for num in range(2,limit+1,2):
        yield num
for number in even_numbers(10):
    print(number)

print()
# Hard
# Create a generator function called filter_position that takes a list of player dictionaries and a position string as arguments. It should yield only the players whose position matches the requested position. For example, when you iterate over filter_position(players, "RW") and print each player's name, the output should be Salah and Saka. Do not create a new list containing the matching players—instead, yield each matching player one at a time as you check through the list.
players = [
    {"name": "Salah", "position": "RW"},
    {"name": "Rice", "position": "CM"},
    {"name": "Saka", "position": "RW"},
    {"name": "Palmer", "position": "AM"},
]
def filter_position(players,position):
    for player in players:
        if player['position']==position:
            yield player
for player in filter_position(players,'RW'):
    print(player['name'])

print()
# ⚔️ Mini Challenge — Match Event Stream
# Create a generator function called match_events that yields a sequence of football match events, each represented as a dictionary. Your generator should produce at least four events: one Goal, one Yellow Card, one Substitution, and one additional event of your choice, such as a Shot on Target or a Foul. Each event dictionary must include the keys minute, event, and player, with appropriate values. Then consume your generator using a for loop and print each event in a readable format, such as "12' — Goal — Salah". Optionally, you can also add a Team key to each event to specify which team is involved, and consider how this event stream could eventually be used in a match simulation system.

def match_events():
    print('MATCH START')
    yield {
        "minute": 14,
        "event": "Yellow Card",
        "player": "Casemiro",
        "team": "RMA"
    }
    yield {
        "minute": 38,
        "event": "Goal",
        "player": "Salah",
        "team": "LIV"
    }
    yield {
        "minute": 65,
        "event": "Substitution",
        "player": "Nuñez",
        "team": "LIV"
    }
    yield {
        "minute": 88,
        "event": "Red Card",
        "player": "Van Dijk",
        "team": "LIV"
    }
for ev in match_events():
    print(f"{ev['minute']}' - {ev['team']} - {ev['event']} - {ev['player']}")

print()
# Consider the generator function called letters that yields A, B, and C. You create a generator object called alphabet and call next on it once. Then you iterate over the remaining items using a for loop. What is printed in total? Think about the generator's position after the first next call. Where is it in the sequence, and what values will the for loop retrieve from that point onward?
# Ans => The first next call prints A then the generator pauses. The loop then prints the remain items B and C. After the first next(), the generator is at A, subsequent calls prints the next value B.

# 🧪 Practice — `return` or `yield`?
# For each situation, decide which makes more sense.

# Should a function that calculates a total price and gives you one final answer use `return` or `yield`?
# Ans => return

# A function reads through a huge source of records and processes them one record at a time.
# Ans => yield

# A function checks whether a password is valid.
# Ans => return

# A function can potentially produce an ongoing sequence of values.
# Ans => All values may not be needed at once, and since the sequence of value could possible increase(is ongoing), yield is best used.

print()
# 🧪 Practice — Generator Expression
# Create a generator expression that produces the squares of numbers from 1 to 5, which are 1, 4, 9, 16, and 25. Use the range function and the exponentiation operator to generate the squares. Then retrieve the first value using next, retrieve the second value using next again, and finally use a for loop to print the remaining values. Why doesn't the for loop print the first two values again?
squares = (number**2 for number in range(1,6))
print(next(squares))
print(next(squares))
for square in squares:
    print(square)
# It has already passed them in the iteration when the first two next() calls were made

print()
# 🟡 Medium — Filter With a Generator Expression
# Given a list of scores containing 45, 67, 89, 32, 91, and 76, create a generator expression that produces only the scores that are greater than or equal to 70. The expected output is 89, 91, and 76. Do not create a list—use a generator expression instead.
scores = [45, 67, 89, 32, 91, 76]
valid_scores=(score for score in scores if score>=70)
for score in valid_scores:
    print(score)

print()

players = [
    {"name": "Salah", "goals": 20},
    {"name": "Saka", "goals": 15},
    {"name": "Rice", "goals": 4},
    {"name": "Palmer", "goals": 18},
]
player_names_=(player['name'] for player in players if player['goals']>=15)
for player in player_names_:
    print(player)

# 🧪 Debugging Lab 🐛
# Identify the problem with this code:
# ```python
# def countdown(start):
#     while start > 0:
#         return start
#         start -= 1
# ```
# The developer expected it to produce 5, 4, 3, 2, 1, but something isn't right. Explain why the problem happens, then rewrite the function as a generator so that it works correctly with a for loop, such as for number in countdown(5): print(number).
# Ans > Well the countdown function ends after the return. Yield would be best used in this situation as it allows the state to be changed subsequently and the function can yield the values on call without ending until all the values are exhausted.
def count_down(start):
    while start > 0:
        yield start
        start -= 1
for num in count_down(5):
    print(num)


# Consider this code:
# def get_numbers():
#     for number in range(1, 6):
#         yield number
# numbers = get_numbers()
# for number in numbers:
#     print(number)
# print("Again!")
# for number in numbers:
#     print(number)
# The developer expected the numbers to print twice, but instead they print once, and the second loop produces nothing. Explain why this happened, what "generator exhaustion" means, and how to fix the code if the developer needs to iterate over the values again.

# Ans => The second loop did'nt work cus the generator already finished yielding its values(generator exhaustion). To get the second loop working again, we reset by rewriting `numbers = get_numbers()` before the second loop.



# 🥋 Skill Check

# ## Question 1
# What is a generator?
# A generator is in itself an iterator but it doesn't return all it's values at once but yield's it on demand.
# ---

# ## Question 2
# What keyword is used to create a generator function?
# yield
# ---

# ## Question 3
# What is the biggest behavioral difference between return and yield?
# return terminates a function when executed. yield pauses the function until the next call or all generator values have been consumed.
# ---

# ## Question 4
# Why can we use next() with a generator?
# Because a generator is still an iterator meaning the __next__() function is available to it.
# ---

# ## Question 5
# What does Lazy evaluation mean?
# Lazy evaluation is all about yielding,processing or returning data/result on demand rather than all at once.
# ---

# ## Question 6
# What happens when a generator is exhausted?
# The generator can't produce any more values as it has finished consuming its values
# ---

# ## Question 7
# What is the difference between:
# [number * 2 for number in range(5)]
# and
# (number * 2 for number in range(5))?
# The first is a list comprehension while the second is a generator expression.
# ---

# ## Question 8
# When might a generator be a better choice than a list?
# When dealing usually with large amounts of data and results aren't expected to be processed and returned at once for all but yielded on demand. 
# ---

# # 🧠 Explain It Like a Sensei
# Explain this without drowning in technical jargon:
# FUNCTION
#    ▼
# yield
#    ├── Produce a value
#    └── Pause ⏸️
#           ▼
#        next()
#           ▼
#        Resume
#           ▼
#        yield
#           ▼
#        Pause again ⏸️
# A function yields or gives up a value. Then pauses until it's required to give the next value. This goes on until there's nothing left to yield.

print()
# ⚔️ Mini Challenge — Academy Training Stream
# Create a generator function called fit_players that takes a list of player dictionaries and a minimum fitness value. It should yield only those players whose fitness is greater than or equal to the minimum. For example, iterating over fit_players(players, 90) and printing each player's name should produce Salah and Saka.
players = [
    {
        "name": "Salah",
        "fitness": 92,
        "position": "RW"
    },
    {
        "name": "Rice",
        "fitness": 88,
        "position": "CM"
    },
    {
        "name": "Saka",
        "fitness": 95,
        "position": "RW"
    },
    {
        "name": "Palmer",
        "fitness": 76,
        "position": "AM"
    }
]
def fit_players(players, minimum_fitness):
    for player in players:
        if player['fitness']>=minimum_fitness:
            yield player
for player in fit_players(players, 90):
    print(player["name"])


## 🔥 Upgrade
# Now create another generator called player_names that takes a sequence of players and yields only the name of each player. Chain these generators together: first pass the original players list to fit_players to get only fit players, then pass that result to player_names to get just their names. For example, you should be able to do fit = fit_players(players, 90), then names = player_names(fit), and finally iterate over names to print each fit player's name.
def player_names(players):
    for player in players:
        yield player['name']
fit = fit_players(players, 90)

names = player_names(fit)

for name in names:
    print(name)