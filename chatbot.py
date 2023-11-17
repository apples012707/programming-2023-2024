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

# Ask the user what their favourite food is
print (f"that is a very interesting name {user_name}!")
fave_food = input ("what is your favourite food?")

# If they answer pasta, respond with something related
if fave_food == "pasta":
    print("🍝")
    print("I think I love pasta, too!")
elif fave_food == "burgers" or fave_food == "Burgers":
    print("🍔")
    print("Mmmmmm. Burgers!")
elif fave_food == "sushi" or fave_food == "Sushi":
    print("🍣")
    print("Delicious!")
else:
    # Respond with something that is NOT TOO repetitive
    # Create a list of appropriate responses
    list_of_fave_food_responses = [
        "Mmmmmm. That sounds delicious.",
        f"Yes, {fave_food} is one of my favourites, too!",
        "Cool.",
        "Interesting, I've never tried that before."
    ]

    # Choose one reponse randomly from the list
    random_response = random.choice(list_of_fave_food_responses)

    # Print out the chosen response
    print(random_response)


