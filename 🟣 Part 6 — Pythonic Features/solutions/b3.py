# Create three functions: show_players, show_teams, and show_stats. Then create another function called run_command that takes a function as an argument and calls it. Use it like run_command(show_players), run_command(show_teams), and run_command(show_stats). Additionally, create a dictionary called commands that maps string keys to these functions, with keys like "players", "teams", and "stats". Then try calling a function from the dictionary using commands["players"]().
def show_players():
    players=['Salah', 'Rice', 'Eze']
    print('PLAYERS LIST')
    for index, player in enumerate(players):
        print(f'{index+1}. {player}')
def show_teams():
    teams=['ARS','LIV','CRY']
    print('TEAMS LIST')
    for index, team in enumerate(teams):
        print(f'{index+1}. {team}')
def show_stats():
    team_stats=[
        {'team': 'ARS', 'stat': '3W 2D 0L'},
        {'team': 'LIV', 'stat': '4W 0D 1L'},
        {'team': 'CRY', 'stat': '2W 2D 1L'}
    ]
    print('TEAM STATS')
    for stat in team_stats:
        print(f'{stat["team"]} ------ {stat["stat"]}')
def run_command(command):
    command()
run_command(show_players)
run_command(show_teams)
run_command(show_stats)

commands =  {
    "players": show_players,
    "teams": show_teams,
    "stats": show_stats
}
commands['players']()
commands['stats']()
commands['teams']()

print()
def training_decorator(function):
    def wrapper():
        print('🏃 Training session starting...')
        function()
        print('💪 Training session complete!')
    return wrapper
def train_player():
    print('Player is training.')
train=training_decorator(train_player)
train()


print()
def logger_(function):
    print('Running function...')
    function()
    print('Function finished.')
@logger_
def save_player():
    print('Player saved.')


print()
# 🐛 Debugging Lab — Where Did My Function Go?
# Look at this:
# ```python
# def decorator(function):
#     def wrapper():
#         print("Before")
#         function()
#         print("After")
#     return wrapper
# def greet():
#     print("Hello!")
# greet = decorator(greet)
# greet()
# ```
# A beginner says:
# > "Wait... `greet` was a function. Then we replaced it. Did we delete the original?! 😭"
# ## Your Mission
# Explain what is happening.
# Use this map:
# ```text
# Original greet
#       ▼
# Passed into decorator
#       ▼
# wrapper remembers original function
#       ▼
# wrapper returned
#       ▼
# greet now points to wrapper
# ```
# Is the original function actually lost immediately?
# What allows `wrapper()` to still call it?
# Ans > Nope we didin't delete the original. From the top to bottom, we initialized the greet function, then passed it into the decorator function as an argument, the wrapper function in decorator nests/remembers the original function. The wrapper object gets returned and is referenced by the variable greet. Now running greet() runs the wrapper and our initial greet function.

print()
def announcer(function):
    def wrapper(*args, **kwargs):
        print('📢 Player announcement!')
        function(*args, **kwargs)
        print('📢 End of announcement.')
    return wrapper
@announcer
def introduce_player(name, position):
     print(f"{name} plays as a {position}.")
introduce_player('Saka', 'RW')


print()
def tracker(function):
    def wrapper(*args, **kwargs):
        print('Calculating...')
        return function(*args, **kwargs)
    return wrapper
@tracker
def calculate_score(goals, assists):
    return goals * 4 + assists * 3
calculate_score(2,3)



print()
# 🐛 Debugging Lab — The Missing Return
# What's wrong here?
# ```python
# def logger(function):
#     def wrapper(*args, **kwargs):
#         print("Running...")
#         function(*args, **kwargs)
#     return wrapper
# @logger
# def multiply(a, b):
#     return a * b
# result = multiply(5, 4)
# print(result)
# ```
# The developer expected:
# ```text
# Running...
# 20
# ```
# But the result isn't `20`.
# ## Your Mission
# 1. Explain why.
# 2. Fix the decorator.
# 3. Explain why decorators must sometimes return the original function's result.
# Ans > The multiply function after running returns a value in wrapper but it isn't used at all, so it's pretty much swallowed up silently.
# FIX
def logger(function):
    def wrapper(*args, **kwargs):
        print("Running...")
        return function(*args, **kwargs)
    return wrapper
@logger
def multiply(a, b):
    return a * b
result = multiply(5, 4)
print(result)
# Now returning the original function passes the return value of the original function to wrapper which is returned by logger(). Hence, the reason why decorators must return the original function's result is so that it doesn't get swallowed up by the wrapper.


def announce(function):
    def wrapper():
        print('▶ Starting...')
        function()
        print('⏹ Finished.')
    return wrapper
@announce
def train():
    print("Training players.")
@announce
def rest():
    print("Players are resting.")
train()
rest()


print()
# ⚔️ Mini Challenge — Football Academy Access Control
# Create a decorator function called require_admin that takes a function as an argument. Inside the decorator, define a wrapper function that first prints "🔐 Checking permissions...", then calls the original function, and finally prints "✅ Action completed." Return the wrapper function. Then use the decorator with the @require_admin syntax on a function called add_player that takes a name and prints a message like "Salah added to the academy." When you call add_player("Salah"), the output should be the permission check message, the player addition message, and the completion message in that order.
def require_admin(function):
    def wrapper(*args, **kwargs):
        print('🔐 Checking permissions...')
        function(*args, **kwargs)
        print('✅ Action completed.')
    return wrapper    
@require_admin
def add_player(name):
    print(f"{name} added to the academy.")
add_player('Salah')

# Upgrade:
# Now imagine you have a variable called current_user that is a dictionary containing a name and a role, such as "Coach Alex" with the role "admin". Modify the require_admin decorator so that it checks whether the user's role is equal to "admin". If the role is "admin", allow the decorated function to run normally. If the role is not "admin", print a message that says "❌ Access denied." and do not execute the function.
current_user = {
    "name": "Coach Alex",
    "role": "admin"
}
def require_admin(function):
    def wrapper(*args, **kwargs):
        print('🔐 Checking permissions...')
        if current_user['role'] == 'admin':
            function(*args, **kwargs)
            print('✅ Action completed.')
        else:
            print('❌ Access denied.')
    return wrapper
@require_admin
def add_player(name):
    print(f"{name} added to the academy.")
add_player('Salah')

# 🔥 Hard Challenge — Universal Action Decorator
# Create a decorator called academy_action that does the following: before running the original function, it prints "▶ Starting academy action..."; then it runs the original function; and after that, it prints "🏁 Academy action complete!". The decorator must work with functions that have no arguments, functions that take positional arguments, and functions that take keyword arguments. It must also preserve any return value from the original function. Test it with a function like train that prints a message, a function like register_player that takes name and position and returns a registration message, and a function like update_fitness that takes name and an optional fitness keyword argument and returns a fitness update message.
def academy_action(function):
    def wrapper(*args, **kwargs):
        print('▶ Starting academy action...')
        result = function(*args, **kwargs)
        print('🏁 Academy action complete!')
        return result
    return wrapper

@academy_action
def train():
    print("Players are training.")
train()

@academy_action
def register_player(name, position):
    return f"{name} registered as {position}"
register_player('Val', 'CDM')

@academy_action
def update_fitness(name, fitness=100):
    return f"{name}'s fitness is now {fitness}"
update_fitness('Val', fitness=83)


# 🐛 Debugging Lab — Argument Explosion
# Look at this decorator:
# ```python
# def logger(function):
#     def wrapper():
#         print("Running...")
#         return function()
#     return wrapper
# ```
# Then:
# ```python
# @logger
# def greet(name):
#     print(f"Hello, {name}")
# ```
# Calling:
# ```python
# greet("Valerian")
# ```
# causes a problem.
# ## Your Mission
# 1. Why does this fail?
# 2. What does `wrapper()` currently accept?
# 3. How can `*args` fix positional arguments?
# 4. Why might we also use `**kwargs`?
# Rewrite the decorator correctly.

# Ans => The wrapper makes no provisions for recieving arguments and passing em to the original function in it. So the function recieves an argument when it expects none at all. Using **args makes just that provision and allows for some flexibility cus wrapper can now recieve arguments and pass em to the original function. Thesame applies to **kwargs but while *args are positional and recieve arguments as tuples, **kwargs use key-value pairing.

def logger(function):
    def wrapper(*args, **kwargs):
        print("Running...")
        return function(*args, **kwargs)
    return wrapper
@logger
def greet(name):
    print(f"Hello, {name}")
greet("Valerian")

# 🧪 Comprehension Check
# Complete this sentence:
# > A decorator is a function that takes another function and gives it extra features.

# Then:
# > The wrapper is responsible for calling the original function and passing arguments to it.

# Then:
# > `*args` and `**kwargs` are useful because it allows for flexibility and provides room for the wrapper to pass expected arguments to the the function it calls.

# Then:
# > We return `result` when we want to preserve the value of the original function.


# 🥋 Skill Check
# ## Question 1
# Why are functions able to be passed into other functions in Python?
# Ans=> Because they are objects
# ---

# ## Question 2
# What makes a function a higher-order function?
# Ans =>  When it can recieve another function as arguments and/or return another function as a value
# ---

# ## Question 3
# Explain this:
# ```python
# new_function = decorator(original_function)
# ```
# Ans => The decorator function takes the original_function as an argument, then a wrapper function in the decorator calls the original_function after adding whatever extra features needs adding and haven passed the necessary arguments to the original_function which it then returns if need be. In the end the wrapper function gets returned and the value can be referenced by new_function. 
# ---

# ## Question 4
# What does this syntax:
# ```python
# @decorator
# ```
# conceptually do?
# Ans => It runs the decorator function passing the subsequent function below it as an arguement to decorator
# ---

# ## Question 5
# Why do decorators often use:
# ```python
# *args
# ```
# and:
# ```python
# **kwargs
# ```
# ?
# Ans > Flexibility and allows arguments to be recieved and passed to the original function
# ---

# ## Question 6
# Why might a decorator need:
# ```python
# return result
# ```
# ?
# Ans => When it wants its values to be preserved
# ---

# ## Question 7
# What problem does:
# ```python
# @wraps(function)
# ```
# help with?
# Ans => It helps keep information and metadata about the original function intact(eg original function name, docstrings etc)
# ---

# ## Question 8
# Give two real-world uses for decorators.
# Ans > loggers, caching
# ---

# # 🧠 Explain It Like You're Teaching Someone
# Explain decorators using this idea:
# ```text
# 🎁 ORIGINAL FUNCTION
#       ↓
# 📦 WRAPPER
#       ↓
# Extra behavior
#       +
# Original behavior
# ```
# Your explanation should answer:
# > "Why not just put the extra code inside every function?"
# Ans => The original function is recieved by a decorator function which provides a wrapper function thats adds the extra features to the original function. This is a lot more reuseable, less-repititive and flexible than putting extra code inside evry function.