print("Welcome to the Trip Cost Calculator.")
try:
    # Get user input for trip details and convert to appropriate data types
    number_days = int(input("\n\tHow many days will you stay? "))
    hotel_price = float(input("\n\tHow much does hotel cost per night? $"))
    flight_cost = float(input("\n\tHow much does flight cost? $"))
    car_rent = float(input("\n\tIf you need rental car please enter the price (otherwise enter zero). $"))
    other_expenses = float(input("\n\tEnter other possible expenses $"))
except ValueError:
    # If conversion fails, print an error message
    print("\nThere was an error!")
else:
    # Calculate the total trip cost based on user input
    total_cost = number_days * hotel_price + flight_cost + car_rent * number_days + other_expenses
    print(f"\n\tTotal Cost: ${total_cost}")