try:
    # Handling potential error when read the input
    celsius = input("Enter Temperature in Celsius: ")
    celsius = float(celsius)
except ValueError:
    # If conversion fails, print an error message
    print("There was an error!")
else:
    # If conversion is successful, calculate Fahrenheit.
    fahrenheit = celsius * 9/5 + 32
    print(f"{celsius} Celsius = {fahrenheit} Fahrenheit")