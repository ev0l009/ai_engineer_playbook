
## Hard
# Create `academy.txt`
# Contents
# ```text
# James
# David
# Samuel
# Musa
# ```
# Read the file. Store each name in a list. Print the list.

players=[]
file=open('academy.txt', 'r')
lines=file.readlines()
for line in lines:
  player = line.strip()
  players.append(player)
file.close()
print(players)
## my output
# ['James', 'David', 'Samuel', 'Musa']