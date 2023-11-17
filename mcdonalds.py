# McDoland's program
# Author : Amelia 
# Date : 6 Nov, 2023

# Ask if the user wants a burger
print("Would you like a burger for $5?")
burger_input = input().strip(",.?!")
if burger_input.lower() == "yes":
    burger_price = 5
else:
    burger_price = 0

# Ask if the user wants fries
print("Would you like fries for $3?")
fries_input = input().strip(",.?!")
if fries_input.lower() == "yes":
    fries_price = 3
else:
    fries_price = 0

# Calculate the output with 14% tax
total_price = (burger_price + fries_price) * 1.14
# Print the result
print(f"Awesome, your total order would be ${total_price:.2f}.")