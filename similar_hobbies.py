# Hobbies similarity score
# Author: Amelia
# Date: 16th Nov 2023

print("User 1, please enter hobbies separated by spaces:")
user1_hobbies = input().lower().split()

print("User 2, please enter hobbies separated by spaces:")
user2_hobbies = input().lower().split()

# Calculate similarity score based on the number of common hobbies
similarity_score = 0

for hobby in user1_hobbies:
    if hobby in user2_hobbies:
        similarity_score += 1

# Display the result
print(f"The similarity score between the users is: {similarity_score}")