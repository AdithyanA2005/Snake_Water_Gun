# SNAKE WATER GUN
# In this game the player will play with the computer'Computer'
# and the user 'Player'




# Importing Modules needed for the game
import random


# Function's needed for the program
def playRule(Computer, Player):

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




# START
# First the turn is for the computer and we will print
print("\nComputer Turn: Snake(s) Water(w) or Gun(g)")


# We use the 'Random' module to make the computer choose "'s' or 'w' or 'g'"  randomly
# the 'randit' provide number from first number to the last number
RandomNumber = random.randint(1, 3)
if RandomNumber == 1:  # If random number is 1 the computer choose for 'Snake'
    Computer = 's'

elif RandomNumber == 2:  # If random number is 2 the computer choose for 'Water'
    Computer = 'w'

elif RandomNumber == 3:  # If random number is 3 the computer choose for 'Gun'
    Computer = 'g'

# After the computer have choosed we will tell the user that the comuter had choosed
print(f"Computer Choosed")

# After the computer it is the players turn to put the input
Player = input("\nYour Turn: Snake(s) Water(w) or Gun(g)")


# We are calling the function we created earlier in 'result'
result = playRule(Computer, Player)  

# We will also show the selection of the Computer and the Player to the user
print(f"\nComputer Choosed: {Computer}")
print(f"You Choosed: {Player}\n")


# Now we are creating other if case to declare who had winned the game 

# if The user and the computer are in tie('None')
if result == None:
    print("The game was a tie match")

# If the player scored the point('True')
elif result:
    print("You Win")

else:
    print('You loose')
