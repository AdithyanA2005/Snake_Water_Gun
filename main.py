# SNAKE WATER GUN

# In this game the player will play with the computer'Computer'
# and the user 'Player'



# Importing Modules needed for the game
import random



# Function's needed for the program
def whoWin(Computer, Player):

    # 1) If the computer and the player choose same nothing will happen
    if Computer == Player:
        return None

    # 2) If the computer chooses 'Snake'
    elif Computer == 's':

        # and player choose 'Water', Computer got point
        if Player == 'w':
            return False

        # or Player choose 'Gun', Player got point
        elif Player == 'g':
            return True

    # 3) If computer chooses 'Water'
    elif Computer == 'w':

        # and player choose 'Gun', Computer got point
        if Player == 'g':
            return False

        # or player choose 'Snake', Player got point
        elif Player == 's':
            return True

    # 4) If compute chooses 'Gun'
    elif Computer == 'g':

        # and player choose 'Snake', Computer got point
        if Player == 's':
            return False

        # or player choose 'Water', Player got point
        elif Player == 'w':
            return True

            

# First the turn is for the computer and we will print
print("Computer Turn: Snake(s) Water(w) or Gun(g)")

# We use the 'Random' module to make the computer choose "'s' or 'w' or 'g'"  randomly
RandomNumber = random.randint(1, 3)
if RandomNumber == 1:  # If random number is 1 the computer choose for 'Snake'
    Computer = 's'

elif RandomNumber == 2:  # If random number is 2 the computer choose for 'Water'
    Computer = 'w'

elif RandomNumber == 3:  # If random number is 3 the computer choose for 'Gun'
    Computer = 'g'


print(RandomNumber)


# After the computer it is the players turn to put the input
Player = input("Your Turn: Snake(s) Water(w) or Gun(g)")


whoWin(Computer, Player)