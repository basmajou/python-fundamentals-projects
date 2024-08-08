print("Welcome to Love Calculator .>_<.")

# Get the names of the two people from the user
name1 = input("\nEnter your name: ")
name2 = input("Enter your lover name: ")

# Combine the names and convert them to lowercase for case-insensitive counting
combined_name = name1.lower() + name2.lower()

true_char = combined_name.count('t') + combined_name.count('r') + combined_name.count('u') + combined_name.count('e')

love_char = combined_name.count('l') + combined_name.count('o') + combined_name.count('v') + combined_name.count('e')

love_score = true_char * 10 + love_char


# Determine the love compatibility based on the calculated score
if love_score < 10 or love_score > 85:
    print(f"\nYour love score is: {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 70:
    print(f"\nYour love score is: {love_score}, you are alright together.")
else:
    print(f"\nYour love score is: {love_score}.")
'''
#also can use:
import random
love_score = random.randint(1,100)
'''