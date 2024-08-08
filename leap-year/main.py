def leap_year(year):
    """
      Determines if a given year is a leap year.

      Args:
          year (int): The year to check.

      Returns:
          str: "Leap year" or "Not leap year" depending on the result.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "Leap year."
            else:
                return "Not leap year."
        else:
            return "Leap year."
    else:
        return "Not leap year."


# EXECUTION

try:
    # Attempt to convert user input for year to int
    input_year = int(input("Enter year: "))
except ValueError:
    # If conversion fails, print an error message
    print("There was an error!")
else:
    print(leap_year(input_year))