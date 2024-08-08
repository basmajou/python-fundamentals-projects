import random  # To generate random numbers for the coin flip.

# Generate a random number (0 or 1) to simulate a coin flip.
coin = random.randint(0, 1)

# Determine the outcome based on the random number.
if coin == 1:
    print("Heads")
else:
    print("Tails")