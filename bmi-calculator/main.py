try:
    # Attempt to convert user input for height and weight to float
    height = float(input("Enter your height in m: "))
    weight = float(input("Enter your weight in kg: "))
except ValueError:
    # If conversion fails, print an error message
    print("There was an error!")
else:
    # If conversion is successful, calculate BMI
    BMI = round(weight / height ** 2, 2)

    # Determine and print BMI category based on calculated value
    if BMI < 18.5:
        print(f"Your bmi is {BMI} , you are underweight.")
    elif BMI < 25:
        print(f"Your bmi is {BMI} , you weight is normal.")
    elif BMI < 30:
        print(f"Your bmi is {BMI} , you are overweight.")
    else:
        print(f"Your bmi is {BMI} , you are obese.")