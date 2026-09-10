class AcademyGate:
    def __enter__(self):
        print('🚪 Academy gate opened.')
        return self
    def __exit__(self, exc_type, exc, tb):
        print('🔒 Academy gate closed.')
with AcademyGate():
    print('Players entered the Academy')

print()
class PlayerSession:
    def __enter__(self):
        return 'Saka'
    def __exit__(self, exc_type, exc, tb):
        print('Player session closed.')
with PlayerSession() as player:
    print(f'"Current player": {player}')

print()
# 🐛 Debugging Lab — Where Did `session` Come From?
# Look at this:
# ```python
# class TrainingSession:
#     def __enter__(self):
#         return "Morning Session"
#     def __exit__(self, exc_type, exc_value, traceback):
#         print("Session ended")
# ```
# Then:
# ```python
# with TrainingSession() as session:
#     print(session)
# ```
# Output:
# ```text
# Morning Session
# Session ended
# ```
# ## Your Mission
# Explain:
# 1. Where did `session` get its value?
# 2. Which method returned it?
# 3. When did `__exit__()` run?
# Ans => Session's value is what __enter__() returned. __enter__ returned it. __exit__() runs automatically at the end of the with block's execution regardless expected execution or error.

print()
# 🧪 Practice — Error Detector
# Create:
# ```python
# class SafeTraining:
# ```
# Requirements:
# ### `__enter__()`
# Print:
# ```text
# 🏃 Training started.
# ```
# ### `__exit__()`
# If an exception happened:
# ```text
# ⚠️ Training encountered a problem.
# ```
# Then always print:
# ```text
# 🧹 Cleaning up training equipment.
# ```
# Use it with:
# ```python
# with SafeTraining():
#     print("Running drills...")
# ```
# Then try another version where something inside the block causes an error. Observe the flow.

class SafeTraining():
    def __enter__(self):
        print('🏃 Training started.')
        return self
    def __exit__(self, exc_type, exc, tb):
        if exc_type:
            print('⚠️ Training encountered a problem.')
            return True
        print('🧹 Cleaning up training equipment.')
with SafeTraining():
    print("Running drills...")
print()
with SafeTraining():
    print(undefined_value)

# Console
# 🏃 Training started.
# Running drills...
# 🧹 Cleaning up training equipment.

# 🏃 Training started.
# ⚠️ Training encountered a problem.
# 🧹 Cleaning up training equipment.
# Traceback (most recent call last):
#   File "/home/valerian/Desktop/py/pythonic_features/sol/b4.py", line 86, in <module>
#     print(undefined_value)
# NameError: name 'undefined_value' is not defined


print()
# ⚔️ Mini Challenge — Training Facility
# Create a context manager:
# ```python
# class TrainingFacility:
# ```
# When entering:
# ```text
# 🏟️ Training facility opened.
# ```
# Return the object itself.
# The class should have a method:
# ```python
# train(self, player):
# ```
# which prints:
# ```text
# [player] is training.
# ```
# When exiting:
# ```text
# 🏟️ Training facility closed.
# ```
# Use it like:
# ```python
# with TrainingFacility() as facility:
#     facility.train("Saka")
#     facility.train("Salah")
# ```
# Expected idea:
# ```text
# 🏟️ Training facility opened.
# Saka is training.
# Salah is training.
# 🏟️ Training facility closed.
# ```
class TrainingFacility:
    def __enter__(self):
        print('🏟️ Training facility opened.')
        return self
    def train(self,player):
        print(f'{player} is training.')
    def __exit__(self, exc_type, exc, tb):
        print('🏟️ Training facility closed.')
with TrainingFacility() as facility:
    facility.train("Saka")
    facility.train("Salah")


print()
from contextlib import contextmanager

@contextmanager
def academy_session():
    print('🎬 Academy session begins.')
    yield
    print('🏁 Academy session ends.')
with academy_session():
    print("Players are learning.")


# 🔥 Hard Challenge — Football Academy Resource Manager
# Create a class called AcademySession. When entering the session using a with statement, it should print "🚪 Academy session opened." and return self. The class should have an add_player method that takes a name and prints "[name] joined the session." It should also have a start_training method that takes a drill and prints "Training drill: [drill]." When leaving the session, it should print "🧹 Cleaning up academy resources." and then "🔒 Academy session closed." Use it in a with block to add players and start a training drill.

# For the upgrade, modify the __exit__ method so that it can detect whether an exception occurred inside the block. If an exception happens, it should report it in some way; if no exception occurs, it should continue normally. The flow should still handle cleanup and closing the session regardless of whether an error occurred.
class AcademySession:
    def __enter__(self):
        print('🚪 Academy session opened.')
        return self
    def add_player(self,name):
        print(f'{name} joined the session.')
    def start_training(self,drill):
        print(f'Training drill: {drill}')
    def __exit__(self, exc_type, exc, tb):
        if exc_type:
            print(f'Encountered some issues!{tb}')
        print('🧹 Cleaning up academy resources.')
        print('🔒 Academy session closed.')

with AcademySession() as academy:
    academy.add_player("Saka")
    academy.add_player("Salah")
    academy.start_training("Speed")

print()
with AcademySession() as academy:
    academy.add_player("Saka")
    academy.add_player("Salah")
    academy.cause_error()
    academy.start_training("Speed")

print()
# 🧠 Comprehension Check
# Complete these sentences.
# ### 1.
# > A context manager is useful when something needs setting up before use and cleaned up after use.

# ### 2.
# > The `with` statement helps ensure that the clean-up after executing code within it's scope/block happens.

# ### 3.
# > `__enter__()` runs when setting up.

# ### 4.
# > `__exit__()` runs when cleaning or closing.

# ### 5.
# > The value after `as` usually comes from what __enter__() returns.

# ### 6.
# > A decorator wraps around function and gives it extra functions.

# ### 7.
# > A context manager manages entry(setup, preparations), use(actual functionalities) and exit(cleaning up) regardless of exception or safety.


