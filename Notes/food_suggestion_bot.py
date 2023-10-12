# Food Suggesting Bot
# Author: Amelia Tang
# Date; Oct. 6. 2023

# A bot that asks the user what their favourite food is 
# The bot identifies the type/cuisine of the food and offer a suggest fot a resturant
# Of the food and offer a suggestion for 
# A resturant

import random
import time 

# Introduce the bot to the user
# Ask the user what their favourite food is
print("Hello, I am here to suggesta resturant to you.")
time.sleep(1)
fave_food = input("To help me suggest a resturant, tell me what your favourite food is.")
time.sleep(1)



# If they answer with an Italian dish
# Suggest an Italian restaurant
#List all the Italian dishes
italian_food = ["pizza", "pasta", "canneloni", "tiramisu"]
chinese_food = ["dumplings", "noodles", "fried rice", "hotpot"]


if fave_food.lower().strip(",.?!") in italian_food:
    print("I think that you might like Italian food.🍝")
    time.sleep(1)
    print("I suggest Bella Roma Italian Ristorante Richmond.")
    time.sleep(1)
    print ("You can find addtess below:")
    print("8368 Alexandra Rd, Richmond")
    time.sleep(1)
    print("Have a great day!💩")

elif fave_food.lower().strip(",.?!") in chinese_food:
    print("I think that you might like chinese food.🥟")
    time.sleep(1)
    print("I suggest Little Lamb Hotpot")
    time.sleep(1)
    print ("You can find addtess below:")
    print("Little Lamb Hotpot, Richmond")
    time.sleep(1)
    print("Have a great day!💩")
else:
    print("I can't offer a suggesting for you.🥸")
    time.sleep(1)
    print ("thanks you using this service! 🫥")