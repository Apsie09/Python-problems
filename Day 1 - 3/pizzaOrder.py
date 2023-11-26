small_Pizza = 15
medium_Pizza = 20
large_Pizza = 25

add_peperoni_small = 2
add_peperoni_mediumOrLarge = 3
add_cheese = 1

size_input = input()
pepperoni_input = input()
cheese_input = input()

bill = 0

if size_input == 'S':
    bill += small_Pizza
elif size_input == "M":
    bill += medium_Pizza
elif size_input == "L":
    bill += large_Pizza

if size_input == "S" and pepperoni_input == "Y":
    bill += add_peperoni_small
elif (size_input == "M" or size_input == "L") and (pepperoni_input == "Y"):
    bill += add_peperoni_mediumOrLarge

if (size_input == "M" or size_input == "L" or size_input == "S") and cheese_input == "Y":
    bill += add_cheese

print("Thank you for choosing Python Pizza Deliveries!")
print(f"Your final bill is: ${bill}.")