# Chatbot
# Author: Amelia
# Date: 21 Swptember 2023


import random
import time

# Greet the user
# Pause in between lines of dialogue
print ("Hello there, I am called Mr. dumb-bot!")
time.sleep(2)
print ("I am here to talk to you!")
time.sleep(1.5)
# Get the user's name and store in a variable
user_name = input ("So... What is your name?")
time.sleep(2)

# Respond with the user's name
print (f"It's nice to meet you, {user_name}")

# Ask the user what their favourite food it
print (f"that is a very interesting name {user_name}!")
favourite_food = input ("what is your favourite food?")

# Respond with something that is NOT TOO repetitive
# Create a list of appropiate responses
list_of_favourite_food_responses = [
    f"That's so cool! But I personally hate {favourite_food}...",
    f"Wow, Ive never tried {favourite_food} before, you should share some to me one day!",
    "OMG really! Me too!",
    f"Interesting, I just ate {favourite_food} yesterday!"
]


# Choose one response randomly from the list
import random
random_response = random.choice(list_of_favourite_food_responses)
# print out the chosen response
print(random_response)