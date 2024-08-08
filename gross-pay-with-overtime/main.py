def gross_pay(w_hours, p_rate):
    """
      Calculates the gross pay based on worked hours and pay rate.

      Args:
          w_hours (float): Total number of hours worked.
          p_rate (float): Hourly pay rate.

      Returns:
          float: The calculated gross pay.
    """
    if w_hours > 40:
        over_time = w_hours - 40
        return (p_rate * 40) + (p_rate * over_time * 1.5)
    else:
        return w_hours * p_rate


try:
    # Get user input for hours and rate, and convert them to float values
    hours = float(input("Enter Hours: "))
    if hours > 60:
        print("Working hours cannot be more 60 weekly!")
        quit()  # Exit the program
    rate = float(input("Enter Rate: "))
except ValueError:
    # If conversion fails, print an error message
    print("Error, please enter numeric input")
    quit()  # Exit the program
else:
    # Calculate the gross pay
    pay = gross_pay(hours, rate)
    print("Pay:", round(pay, 2))
