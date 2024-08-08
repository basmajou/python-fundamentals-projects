import random  # To generating random numbers

# Initialize the flag to control the loop
roll_dice = 'Y'

while roll_dice.upper() == 'Y':
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print("Dice1:", dice1)
    print("Dice2:", dice2)
    roll_dice = input("Roll the dice again? (Y/N) ")
    print()