def max_number(num1, num2, num3):
    """
      Finds the maximum of three numbers.

      Args:
          num1: The first number.
          num2: The second number.
          num3: The third number.

      Returns:
          The maximum of the three numbers.
    """
    if num1 > num2:
        if num1 > num3:
            return num1
        else:
            return num3
    elif num2 > num3:
        return num2
    else:
        return num3


try:
    # Get user input for three numbers and convert them to integers
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    c = int(input("Enter 3rd number: "))
except ValueError:
    # Handle the case where the user input is not a valid integer
    print("There was an error!")
else:
    # If the input is valid, find and print the maximum number7
    print("Max number is:", max_number(a, b, c))