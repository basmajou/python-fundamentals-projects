def temperature_status(a):
    """
        Determines the temperature status based on the given value.

        Args:
            a (float): The temperature value.

        Returns:
            str: The temperature category ("Hot", "Warm", or "Cold").
    """
    if a > 28:
        return "Hot"
    elif a > 18:
        return "Warm"
    else:
        return "Cold"


def check_for_float(input1):
    """
        Checks if the input is a valid float and converts it if possible.

        Args:
            input1 (str): The input to be checked.
    """
    try:
        input1 = float(input1)
    except ValueError:
        print("Error, You must enter a numeric input!")
        quit()


# Convert the input to a float
temperature = input("Enter temperature: ")
check_for_float(temperature)
temperature = float(temperature)
print("It's", temperature_status(temperature))