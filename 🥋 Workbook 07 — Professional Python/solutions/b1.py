def get_age():
    try:
        age=int(input("Enter your age: "))
    except ValueError:
        print('⚠️ Please enter a valid age.')
    else:
        print(f'You are {age} years old.')

print()
def divide_nums():
    print('Starting program....')
    try:
        base = int(input('Enter a number: '))
    except ValueError:
        print('⚠️ Please enter valid numbers.')
    except ZeroDivisionError:
        print('⚠️ You cannot divide by zero.')
    else:
        print(f'The result is: {100/base}')
    finally:
        print('Cleaning up...\nExiting.')

# 🐛 DEBUGGING LAB — The Lazy Catch
# Here's some suspicious code:
# ```python
# try:
#     age = int(input("Age: "))
#     score = 100 / age
# except Exception:
#     print("Something went wrong.")
# ```
# Your mission:
### 1. Identify why this might be too broad.
### 2. Rewrite it using more specific exception handlers.
### 3. Explain which errors you're expecting.

# Ans => 1. They are many kinds of exceptions including ArithmeticError, ValueError, OSError and so on. Using just Exception doesn't narrow down to the errors expected.
print()
try:
    age = int(input("Age: "))
    score = 100 / age
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid entry.")

# ZeroDivisionError is one to expect should 0 be used
# Another error to except would be the ValueError should a string that can't be casted into an integer be used.

def set_player_age(age):
    try:
        age=int(age)
    except ValueError:
        raise ValueError('Age is invalid')
    if age<1:
        raise ValueError('Age cannot be less than 0')
    return age

try:
    age=set_player_age(-1)
    print(f'This player is {age} years old')
except ValueError as e:
    print(f'Could not set age: {e}')

# better design principle, the caller should handle what the error looks like. The function should focus only on raising/exceptions. Errors propagate backwards through the call stack. 

def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("Can't divide by zero")
    return a/b
def calculate():
    return divide(10,0)
try:
    result=calculate()
    print(f"Result: {result}")
except ZeroDivisionError as e:
    print(f"Err: {e}")


# 🥋 Practice 10 — Narrow the Scope
# Break the thinking apart.
# Ask:
# Which operation can raise ValueError?
# Which operation can raise ZeroDivisionError?
# Which operation might raise an I/O-related exception?
# Which failures should be allowed to propagate?
# You don't need to implement a database or email system.
# The objective is to reason about **where exception handling belongs**.
# try:
#     name = input("Name: ")
#     age = int(input("Age: "))
#     score = 100 / age
#     print(f"{name}: {score}")
#     save_to_database(name, score)
#     send_email(name)

# except Exception:
#     print("Something went wrong.")

...
try:
    name = input("Name: ")
    age = int(input("Age: "))
    score = 100 / age
except ValueError:
    raise ValueError("Invalid entry")
except ZeroDivisionError:
    raise ZeroDivisionError("Cannot divide by zero")
else:
    print(f"{name}: {score}")

try:
    save_to_database(name, score)
except OSError:
    raise OSError
else:
    try:
        send_email(name)
    except ConnectionError as e:
        print(f"Connection error: {e}")
...


# 🧪 Mini Challenge — Layered Failure
# Imagine:
# ```python
# def load_player_data():
#     ...
# ```
# Suppose the underlying file isn't found.
# Your job:
# 1. Catch the low-level exception.
# 2. Raise a more meaningful custom exception.
# 3. Chain the original exception.
# 4. Handle the custom exception at the calling level.
# Conceptually:
# ```text
# FileNotFoundError
#        ↓
# PlayerDataUnavailableError
#        ↓
# Application handles it

class PlayerDataUnavailableError(Exception):
    pass

def load_player_data():
    try:
        with open("error_file", 'r') as file:
            pass
    except FileNotFoundError:
        raise PlayerDataUnavailableError("Counldn't load players") from FileNotFoundError

try:
    players=load_player_data()
    print(players)
except PlayerDataUnavailableError as err:
    print(err)



