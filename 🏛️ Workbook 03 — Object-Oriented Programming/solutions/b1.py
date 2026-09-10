# 🏃 Practice
## Think Before You Code
# For each item below, answer:

# Would it make sense as an object?
# Why?

# A football player
'''
Definitely an object would be the best way to model a football player, cus it'll has attributes(i.e data like name, age, position, goals and so on) and behaviour(methods or functions like score, tackle, assign xp points to level up attributes and so on)
'''

# A football academy
'''
I kinda thought it'll be say an 'all encompassing' dictionary or list, but I think it can work quite well as an object too. Um data like academy name could be a string, location(tuple), squad(s) - could be a list of dicts or dict with name and squad list, where in either cases more than one squad is availabe - etc. As for it behaviour, well there could be methods to update or clear the entire squad, change the name of the academy, train a player in the academy and so on. (i'm getting wild here...). So yeah, if we had many academies, they'll have different attributes and if we wanted wanted to deal with em separately from the same base or control center and skip repititions, OOP is the way to go.
'''

# A shopping cart
'''
My take, I think a list of dicts will just about suffice here. We rarely have different carts for a single user. However, say we want to have say cart id, track the number of items per cart or even have only specific item categories in a cart, an object will do... yet again, I'm all over the place.
'''

# A weather report
'''
A weather report could simple be a dict... right? But if its reports from multiple places, an object will be better cus more attributes can easily be added and methods like update or refresh, or get previous report could be called...
'''

# A bank account
'''
Could be a dict or an object. Well, as an object, it could have attributes like id, number, amount, history and so on. It could also have its own operation like set interest rate... out of ideas...
'''

# A random multiplication table
'''
Aboslutely not an object!!! Ahem...
'''


## Design Exercise
# Imagine creating a Car. What data should it have? What actions should it perform? Don't write code. Just list ideas.
'''
Attributes => color, manufacture date, brand, engine capacity, pump capacity etc
Methods => accelerate, refuel, brake etc
'''

# Now do the same for Book
'''
Attributes => name, author, pages, publish date etc
Methods => ... a book should be flipping it own pages or reading itself right??... hmmm
'''

# And finally Football Player
'''
Attributes => name, age, postion etc
Methods => shoot, tackle, pass etc
'''