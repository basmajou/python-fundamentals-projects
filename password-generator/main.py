import random  # To generating random characters.

# Define character sets for password generation
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "1234567890"
symbols = "-+=!@#$%^&*"
generated_password = ""

print("Password Generator..\n")

try:
    # Get user input for three numbers and convert them to integers
    letters_needed = int(input("\tHow many letters do you want in your password? "))
    numbers_needed = int(input("\tHow many numbers do you want in your password? "))
    symbols_needed = int(input("\tHow many symbols do you want in your password? "))
except ValueError:
    # Handle the case where the user input is not a valid integer
    print("\n\tThere was an error!")
    quit()


# Generate the password by iteratively adding random characters
while letters_needed > 0:
    generated_password += random.choice(letters)
    letters_needed -= 1
while numbers_needed > 0:
    generated_password += random.choice(nums)
    numbers_needed -= 1
while symbols_needed > 0:
    generated_password += random.choice(symbols)
    symbols_needed -= 1

# Shuffle the generated password for better randomness
password_list = list(generated_password)
random.shuffle(password_list)

# Reconstruct the password from the shuffled list
generated_password = ""
for letter in password_list:
    generated_password += letter

print(f"\n\tYour password is: {generated_password}")