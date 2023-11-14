# World Traveller Bot
# Author : Amelia
# Date : 6th Nov, 2023
# Greet and ask for the user's name
user_name = input("What is your name?")
print (f"Hello {user_name}! It's nice to meet u.")
NUM_RESPONDENTS = 7
# Ask if the user has been to each of the continents
questions = [
    "Have u been to Asia?",
    "Have u been to Europe?",
    "Have u been to North America?",
    "Have u been to South America?",
    "Have u been to Australia?",
    "Have u been to Africa?",
    "Have u been to Antarctica?"
]
total_response = 0

for question in questions:
    print(question)
    user_response = input().strip(",.?! ").lower()  
    if user_response == "yes":
        total_response += 1  # Increment by 1 for "yes"


# Tell the user how many continents they've been to
print(f"I see, you've visited {total_response}/{NUM_RESPONDENTS} continents")