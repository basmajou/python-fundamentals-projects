try:
    # Attempt to convert user input for score to float
    score = float(input("Enter score: "))
    if score < 0.0 or score > 1.0:
        # Raise a ValueError if the score is invalid
        raise ValueError
except ValueError:
    # Handle the case where the input is not a valid float or is out of range
    print("Bad score")
    quit()  # Exit the program

# Determine the letter grade based on the score
if (score >= 0.9):
    print("A")
elif (score >= 0.8):
    print("B")
elif (score >= 0.7):
    print("C")
elif (score >= 0.6):
    print("D")
elif (score < 0.6):
    print("F")