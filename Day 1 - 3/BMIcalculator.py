import math
# 1st input: enter height in meters e.g: 1.65
height_input = input("Please enter height in meters: ")
# 2nd input: enter weight in kilograms e.g: 72
weight_input = input("Please enter weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


try:

    height = float(height_input)
    weight = float(weight_input)

    if(height < 0 or weight < 0):
        raise ValueError("Height and Weight must be positive")
    
    else:
        formatBMI = weight / math.pow(height,2)

        formatBMI = round(formatBMI,2)

        if(formatBMI < 18.5):
            print(f"Your formatBMI is {formatBMI}, you are underweight.")
        elif(formatBMI > 18.5 and formatBMI < 25):
            print(f"Your formatBMI is {formatBMI}, you have a normal weight.")
        elif(formatBMI >= 25 and formatBMI < 30):
            print(f"Your formatBMI is {formatBMI}, you are slightly overweight.")
        elif(formatBMI >= 30 and formatBMI < 35):
            print(f"Your formatBMI is {formatBMI}, you are obese.")
        elif(formatBMI >= 35):
            print(f"Your formatBMI is {formatBMI}, you are clinically obese.")




except ValueError as e:
    print(f"Error: {e}. Please enter valid numerical values for height and weight.")

