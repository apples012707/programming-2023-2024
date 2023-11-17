# Loop Practice
# Author: Amelia Tang
# Date: 10 October 2023

# Create a list of groceries
groceries = ["hot wheels", "lego", "ice cream", "video games"]


# Do something for each thing in the list
# Eg.   *item
#        ---
#       *item
#        ---

# Print it out in a pretty way

for item in groceries:
    print(f"*{item}")
    print("  ---")


# Create a pyramid like this using a for loop.# Problem:
# Createa new years eve countdown
# Requirements:
# * Start off at 10
# * Countdown every second and print the second taht it's at 
# * Instead of reaching zero it says "Happy New Year"
# * Example output

stars = ["*", "**", "***", "****", "*****"]

for items in stars:
    print(f"{items}")
    print("---")


# Problem:
# Createa new years eve countdown
# Requirements:
# * Start off at 10
# * Countdown every second and print the second taht it's at 
# * Instead of reaching zero it says "Happy New Year"
# * Example output

countdown = ["10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "HAPPY NEW YEAR!🥳"]
import time
for items in countdown:
    print(f"{items}")
    print("---")
    time.sleep(1)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Finished solution