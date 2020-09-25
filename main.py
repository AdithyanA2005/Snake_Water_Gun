# In this game the player will play with the computer the'Computer'
# and the user is 'Player'


# Importing Modules needed for the game
import random


# First the turn is for the computer and we will print
print("Computer Turn: Snake(s) Water(w) or Gun(g)")

# We use the 'Random' module to make the computer choose
# "'s' or 'w' or 'g'"  randomly
RandomNumber = random.randint(1, 3)

print(RandomNumber)
# Player = input("Players's Turn: Snake(s) Water(w) or Gun(g)")
