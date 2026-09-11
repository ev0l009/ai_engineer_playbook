## Challenge 1
# Easy
# Create a list called `players` with the values `["Salah", "Saka", "Palmer"]`. Then create an iterator from the list. Now use the `next()` function to retrieve the players and print them one at a time. Do not use a for loop.
players = ['Salah', 'Saka', 'Palmer']
iterator = iter(players)
print(next(iterator))
print(next(iterator))
print(next(iterator))
# OR
iterator = iter(players)
while True:
    try:
        player=next(iterator)
        print(player)
    except:
        break

print()
# Create a variable called `word` and assign it the string value `"Python"`. Then turn the string into an iterator. Now use the `next()` function repeatedly on that iterator to get each character one by one and produce the letters P, y, t, h, o, and n in sequence, without using a for loop. This allows you to manually experience how iteration works step by step.
word='python'
iterator=iter(word)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

print()
# Medium
# Create a list called `numbers` with the values `[10, 20, 30, 40, 50]`. Create an iterator from it. Then retrieve only the first three values using `next()`. Your program should produce 10, 20, and 30. Do not retrieve the remaining values. Then think about where the iterator is now.
numbers=[10,20,30,40,50]
iterator=iter(numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator))
# OR
count = 1
iterator=iter(numbers)
while count<=3:
    try:
        number=next(iterator)
        print(number)
        count+=1
    except:
        break
# The iterator is at 30

print()
# Create a list called `colors` with the values `["red", "green", "blue"]`. Create an iterator from it. Call `next()` on the iterator once, then call it again. Stop there. Answer this question: What value would the iterator return if you called `next()` one more time?
colors=['red','green','blue']
iterator=iter(colors)
print(next(iterator))
print(next(iterator))
# It'll be on or print `blue`

print()
# Hard
# Consider the following code where you have a list called numbers containing 1, 2, and 3, and you create an iterator from that list. You then call print(next(iterator)) four times in a row. Answer these questions: What are the first three outputs? What happens on the fourth call? Why does that happen? What exception is raised?
# 1.The first three outputs are 1,2 and 3. On the fourth call, the iterator has pretty much run out of values so it raises the StopIteration error.

print()
# Consider the following code. You have a list called numbers containing the values 10, 20, 30, and 40. You create an iterator from that list using the iter function and assign it to the variable iterator. You then call print(next(iterator)) twice. Now imagine that another piece of code receives the same iterator by assigning it to a new variable called other. Then you call print(next(other)). What gets printed on that final print statement, and why does that happen?
# 30 gets printed. We just stored the iterator with it's current state or value in 'other' or better still, other points to thesame address in memory as the iterator object. 

print()
# Mini challenge
# You are to recreate a for loop manually using the iterator protocol. Given a list called players containing the names "Salah", "Saka", and "Palmer", your goal is to use iter and next along with exception handling to print every player in the list. Conceptually, you are trying to reproduce the behavior of a for loop that prints each player, but without actually using the for keyword. Your program should eventually stop cleanly when there are no more players to retrieve. You may use iter, next, try, except, and print, but you may not use for or while. The challenge is to experience the iterator protocol directly.

players=['Salah', 'Saka', 'Palmer']
iterator=iter(players)

def print_player(val):
    try:
        print(next(val))
        print_player(val)
    except:
        return
print_player(iterator)





print()
# 🧪 Practice — Build Your Own Counter
# Create a class called Countdown. It should count down from 5 to 1, printing each number, and then stop. Your class must implement the __init__, __iter__, and __next__ methods. You should raise a StopIteration exception when the countdown finishes.
class Countdown:
    def __init__(self) -> None:
        self.current=5
        self.limit=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current>=self.limit:
            current=self.current
            self.current-=1
            return current
        raise StopIteration
for number in Countdown():
    print(number)

print()
# 🟡 Medium — Even Numbers Iterator
# Create a class called EvenNumbers. It should produce the even numbers 2, 4, 6, 8, and 10 when given a limit of 10. For example, when you create an instance with EvenNumbers(10) and then iterate over it using a for loop, printing each number, the output should be 2, 4, 6, 8, and 10.
# Challenge: Make the limit configurable so that when you create an instance with EvenNumbers(6), iterating over it produces the even numbers 2, 4, and 6.
class EvenNumbers:
    def __init__(self,limit) -> None:
        self.limit=limit
        self.current=2
    def __iter__(self):
        return self
    def __next__(self):
        if self.limit>=self.current:
            current=self.current
            self.current+=2
            return current
        raise StopIteration
for num in EvenNumbers(10):
    print(num)

print()
# 🔴 Hard — Range Iterator
# Create a class called MyRange that works like a simplified version of Python's built-in range function. It should support creating an instance with a single argument, such as MyRange(5), and when iterated over, it should produce the numbers 0, 1, 2, 3, and 4. Your iterator must start at 0, stop before reaching the given limit, return one number at a time, and raise StopIteration at the correct moment.
class MyRange:
    def __init__(self,limit:int) -> None:
        self.limit=limit
        self.current=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current<self.limit:
            current=self.current
            self.current+=1
            return current
        raise StopIteration
for val in MyRange(5):
    print(val)

print()
# ⚔️ Mini Project — Player Iterator
# Create a class called PlayerIterator that iterates over a list of player dictionaries. It should store the collection, track the current position, implement the __iter__ method, and implement the __next__ method to return each player's dictionary one at a time. When there are no more players left, it should raise StopIteration. For example, given the player data containing Salah, Saka, Palmer, and Rice with their positions, iterating over a PlayerIterator instance should print each player's name in order, producing Salah, Saka, Palmer, and Rice.
player_list = [
    {"name": "Salah", "position": "RW"},
    {"name": "Saka", "position": "RW"},
    {"name": "Palmer", "position": "AM"},
    {"name": "Rice", "position": "CM"},
]

class PlayerIterator:
    def __init__(self,players: list[dict[str,str]]) -> None:
        self.players=players
        self.current_index=0
    def __iter__(self):
        return self
    def __next__(self):
        if len(self.players)>self.current_index:
            current_index=self.current_index
            self.current_index+=1
            return self.players[current_index]
        raise StopIteration

players=PlayerIterator(player_list)
for player in players:
    print(player['name'])


### Question 1  
# What is the difference between an iterable and an iterator?
# Ans => An iterable(dicts,tuples,strings,list) is something you can iterate over. An iterator does the iterating. An iterator is also iterable. An iterator is gotten from an iterable. An iterator knows its position as it iterates.

### Question 2  
# What does the `iter()` function do when called on a list like `players`?
# Ans => It creates an iterator object, that iterates over the `players`.

### Question 3  
# What does the `next()` function do when called on an iterator?
# Ans => It moves the iterator to the next item if any

### Question 4  
# What happens when an iterator has no more values to return?
# Ans => If next() is called on an iterator with no more values to return, it raises an error, StopIteration.

### Question 5  
# Why does a `for` loop work on a list like `players` even though you never explicitly call `iter()` or `next()` in your code?
# Ans => Python's for loop already implements the __iter__() and next() functions. An iterator object is created that handles the loop/iteration procedures. 

### Question 6  
# What are the two key methods involved in the iterator protocol in Python?
# iter() and next() 

### Question 7  
# Why does the `__next__()` method eventually raise a `StopIteration` exception?
# Ans => Because the iterator has run out of items

### Explain It Like a Sensei  
# Without using technical jargon, explain the flow from an iterable to values being produced one by one, and what happens when there are no more values.
# Ans => An iterable can be likened to a batch of say food items to be inspected. The conveyor(iterator) moves each item one by one with its belt until it runs through all the items afterwhich it stops(StopIteration).