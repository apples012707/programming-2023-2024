# AOC Day 1
# Author: Amelia Tang
# Nov 30 2023

# There is one elf carrying the most calories
# How many does that one have?

# Create a list that holds all the calories of the elves
# Elves

# Create a lis to hold all calories of elves
elves = []

# Open the file
with open("https://adventofcode.com/2022/day/1/input") as f:
    # Calories of the current elf
    current_cals = 0
    
    for line in f:
        # If there is something in the line
        if line.strip():
            current_cals += int(line.strip())
        else:
            # Dump current_cals into elves list
            elves.append(current_cals)


print(elves)

# Find the biggest calories in the list
biggest_cals = 0
for elf in elves:
    if elf > biggest 


    elves = []       # empty list
# Open the file
with open("./aoc2022day1.txt") as f:
    # Calories of the current elf
    current_cals = 0       # Assuming elf does not carry anything
    for line in f:          # interating over every line in the file
        # If there is something in the line (other than a number)
        if line.strip():
            current_cals += int(line.strip())     # string -> integer
        else:
            # dump current_cals into elves list
            elves.append(current_cals)
            # reset current_cals for next elves
            current_cals = 0
print (elves)
# Set variables for each top elves
elf_one = 0
elf_two = 0
elf_three = 0
# find the biggest calories in the list
biggest_cals = 0
for elf in elves:
    if elf > biggest_cals:
        biggest_cals = elf

print(elves)
print(max(elves))

# get the top three and sum them
print(sum(sorted(elves)[-3:]))