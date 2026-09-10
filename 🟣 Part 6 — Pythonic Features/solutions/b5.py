# 👹 BOSS FIGHT — The Pythonic Training Arena
# Your task is to build a small system for the Football Academy that manages training drills. This is not just another OOP project—you are to use the Pythonic features you have just learned, including custom iterators, generators, decorators, and context managers. Your system should involve training data that flows through a custom iterator, then through a generator, then through decorated actions, and finally through a managed training session using a context manager. Build the system step by step, applying each concept appropriately.

# Follow the arena map to build your system step by step. Start by entering the training session, then prepare actions using decorators, iterate through players using custom iterators, generate results using generators, record or report the outcomes, and finally clean up and close the session. Structure your code to move through each stage in order, applying the appropriate Pythonic features at each step.

# The goal is to build a coherent system for the Football Academy that combines classes, functions, lists, loops, OOP, iterators, generators, decorators, and context managers. The focus is not on making the program as complicated as possible, but on demonstrating that you can recognize when each Python feature is useful and combine them effectively into one working system.

# ROUND 1 - PLAYER ITERATOR
# Create a custom iterable class called PlayerSquad that accepts a list of player names. Your class should implement the iterator protocol by defining __iter__ and __next__ methods. It should keep track of the current position so that each time next is called, it returns the next player in the list. When there are no more players, it should raise StopIteration. Your class should work in a for loop and also with manual next calls. After implementing it, explain what causes Python to know when there are no more players.

class PlayerSquad:
    def __init__(self,players) -> None:
        self.players=players
        self.current_index=0
    def __iter__(self):
        return self
    def __next__(self):
        while self.current_index<len(self.players):
            current_player=self.players[self.current_index]
            self.current_index+=1
            return current_player
        raise StopIteration
squad = PlayerSquad(
    ["Saka", "Salah", "Musiala", "Yamal"]
)
for player in squad:
    print(player)

print()
## 💀 Mini Boss Upgrade
# Implement and explain what causes Python to know when there are no more players.
squad = PlayerSquad(["Saka", "Salah"])
iterator = iter(squad)
print(next(iterator))
print(next(iterator))
print(next(iterator))
# Ans => For an iterator, the __next__() method checks the conditions and raises a StopIteration exception when all items in the are consumed.

# 🥊 ROUND 2 — The Training Generator
# Create a generator function called training_drills that yields each drill from the drills list one at a time. Do not build and return a list—use the yield keyword to produce each drill lazily. The generator should pause after each yield and resume when the next value is requested. For example, iterating over training_drills with a for loop should produce Passing, Speed, Finishing, and Positioning in that order.
def training_drills():
    yield "Passing"
    yield "Speed"
    yield "Finishing"
    yield "Positioning"
for drill in training_drills():
    print(drill) 

# 🥊 ROUND 3 — Decorate the Training
# Create a decorator called announce_training that prints "🏟️ Training action starting..." before the decorated function runs, and "🏁 Training action complete." after it runs. The decorator should be flexible enough to work with functions that accept different numbers of arguments by using *args and **kwargs. Apply the decorator to a function called start_drill that takes a player and a drill, prints a message like "Saka is practicing Finishing." When you call start_drill("Saka", "Finishing"), the output should show the announcement, the drill message, and the completion message in that order.
def announce_training(function):
    def wrapper(*args,**kwargs):
        print('🏟️ Training action starting...')
        function(*args,**kwargs)
        print('🏁 Training action complete.')
    return wrapper
@announce_training
def start_drill(player, drill):
    print(f"{player} is practicing {drill}.")
start_drill('Saka', 'Finishing')

#Upgrade
def announce_training(function):
    def wrapper(*args,**kwargs):
        print('🏟️ Training action starting...')
        result=function(*args,**kwargs)
        print('🏁 Training action complete.')
        return result
    return wrapper

# 🥊 ROUND 4 — Enter the Training Arena
# Create a context manager class called TrainingArena. When entering the arena using a with statement, it should print "🚪 Training arena opened." and return self. When leaving, it should print "🧹 Cleaning training equipment." followed by "🔒 Training arena closed." Add a method called prepare that takes a drill and prints "Preparing drill: [drill]." This should allow you to use the arena in a with block, call prepare on the arena instance, and have the entry and exit messages appear as expected.
class TrainingArena:
    def __enter__(self):
        print('🚪 Training arena opened.')
        return self
    def prepare(self, drill):
        print(f"Preparing drill: {drill}")
    def __exit__(self, exc_type, exc, tb):
        print("🧹 Cleaning training equipment.") 
        print("🔒 Training arena closed.")
with TrainingArena():
    print("Players are ready.")
print()
with TrainingArena() as arena:
    arena.prepare("Passing")


# 👹 FINAL BOSS — Combine Everything
class PlayerSquad:
    def __init__(self,players) -> None:
        self.players=players
        self.current_index=0
    def __iter__(self):
        return self
    def __next__(self):
        while self.current_index<len(self.players):
            current_player=self.players[self.current_index]
            self.current_index+=1
            return current_player
        raise StopIteration
    
def training_drills():
    yield "Passing"
    yield "Speed"
    yield "Finishing"
    yield "Positioning"

def announce_training(function):
    def wrapper(*args,**kwargs):
        print('🏟️ Training action starting...')
        result=function(*args,**kwargs)
        print('🏁 Training action complete.')
        print()
        return result
    return wrapper
@announce_training
def start_drill(player, drill):
    print(f"{player} is practicing {drill}.")

class TrainingArena:
    def __enter__(self):
        print('🚪 Training arena opened.')
        print('\n')
        return self
    def prepare(self, drill):
        print(f"Preparing drill: {drill}")
    def __exit__(self, exc_type, exc, tb):
        if exc:
            print(f'Encounter issues during session: {exc}')
        print()
        print("🧹 Cleaning training equipment.") 
        print("🔒 Training arena closed.")
players = [
    "Saka",
    "Salah"
]
squad=PlayerSquad(players)
with TrainingArena() as arena:
    for player in squad:
        for drill in training_drills():
            arena.prepare(drill)
            start_drill(player,drill)

print()
print()
print()

squad=PlayerSquad(players)
drills=training_drills()
with TrainingArena() as arena:
    for player in squad:
        for drill in drills:
            arena.prepare(drill)
            start_drill(player,drill)
# Ans => In the first one, every player gets to call the training_drill() generator. To demonstrate, the first player calls training_drill() which completely exhausts its contents and then the next player gets to call training_drill() again which resets the generator. This repeats for all players. Since generators recall their last yielded value, when they exhaust their contents, a fresh call resets em. For the second, drill gets called outside the loop and the first player exhausts the generator, when the next player calls the generator, there's nothing left, therefore only the first player recieves every drill.


# 🐛 DEBUGGING LAB — The Missing Players
# The boss has sabotaged your iterator. 😈
# Look at this:
# ```python
# class PlayerSquad:
#     def __init__(self, players):
#         self.players = players
#         self.index = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index >= len(self.players):
#             raise StopIteration
#         player = self.players[self.index]
#         return player
# ```
# Run this mentally:
# ```python
# for player in PlayerSquad(["Saka", "Salah"]):
#     print(player)
# ```
# Uh oh.
# What is wrong? Why could this lead to a problem where the iterator never moves forward? Fix it.
# Ans => self.index never updates and this will lead to an infinite loop.
# FIX
class PlayerSquad:
    def __init__(self, players):
        self.players = players
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.players):
            raise StopIteration
        player = self.players[self.index]
        self.index+=1
        return player
for player in PlayerSquad(["Saka", "Salah"]):
    print(player)


# 🐛 DEBUGGING LAB — The Broken Decorator
# The boss has also attacked your decorator.
# ```python
# def announce_training(func):
#     def wrapper(*args, **kwargs):
#         print("🏟️ Training action starting...")
#         func(*args, **kwargs)
#         print("🏁 Training action complete.")
#     return wrapper
# ```
# Then:
# ```python
# @announce_training
# def calculate_score(a, b):
#     return a + b
# ```
# What happens here?
# ```python
# score = calculate_score(10, 20)
# print(score)
# ```
# Why? Fix the decorator so the original function's result is preserved.
# Ans => The original calculate_score() function returns a value which isn't used in the wrapper() function, so it gets swallowed up. So the value of score is None.
# FIX:
def announce_training(func):
    def wrapper(*args, **kwargs):
        print("🏟️ Training action starting...")
        result = func(*args, **kwargs)
        print("🏁 Training action complete.")
        return result
    return wrapper
@announce_training
def calculate_score(a, b):
    return a + b
score = calculate_score(10, 20)
print(score)


# 🐛 DEBUGGING LAB — The Arena Doesn't Close
# Look at this:
# ```python
# class TrainingArena:
#     def __enter__(self):
#         print("🚪 Training arena opened.")
#         return self
# ```
# Then:
# ```python
# with TrainingArena() as arena:
#     print("Training...")
# ```
# What important part is missing?
# Add it.
# Then explain:
# > Why is `__exit__()` especially useful if an error happens inside the `with` block?
# Ans > The __exit__() method which is responsible for cleaning up behaviour, handling exceptions and ensuring a smooth flow regardless of safety-exceptions.
# FIX:
class TrainingArena:
    def __enter__(self):
        print("🚪 Training arena opened.")
        return self
    def __exit__(self, exc_type, exc, tb):
        if exc_type:
            print(f'Error: {exc_type}')
        print('Training arena closed.')
with TrainingArena() as arena:
    print("Training...")


# # 🧠 COMPREHENSION CHECK
# No code for these.
# Explain them in your own words.
## 1. Iterators 🔁
# What is the relationship between:
# ```python
# iter()
# ```
# and:
# ```python
# next()
# ```
# Ans=>They are both methods implementable by an iterator object.

## 2. Generators ⚡
# Why does:
# ```python
# yield
# ```
# behave differently from:
# ```python
# return
# ```
# ?
# Ans => 'return' returns a value and terminates a function but 'yield' yields a value and pauses the function until the function is called again and it yields the next value if any otherwise it raises an exception


## 3. Decorators 🎁
# What does this line actually do conceptually?
# ```python
# @announce_training
# ```
# Ans => It calls the decorator function that recieves a function argument. It passes this argument to an inner wrapper function that wraps extra behaviour/features around the original and returns the original function's value if it needs preserving, otherwise it just calls it.


## 4. Context Managers 🚪
# What is the relationship between:
# ```python
# with
# ```
# and:
# ```python
# __enter__()
# ```
# and:
# ```python
# __exit__()
# ```
# ?
# Ans => They are part of a context manager flow. When code is run within the with block, the __enter__() method handles setup and the __exit__() handles cleanup irrespective of safety or exceptions.