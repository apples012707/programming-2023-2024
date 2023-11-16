# Parental Bot
# Author : Amelia
# Date : 16 Nov 2023
# Create a list of questions
questions = [
  "Did u eat?",
  "Did u study?",
  "Did you do your laundry?",
  "Did u call ur grandma?"
]
total_point = 0
# Ask every question in that list
for question in questions:
    print(question)
    # Get the user's ans
    user_ans = input().strip(",.?! ").lower()
    # Point increases if they say yes
    if user_ans == "yes" :
        total_point += 1
   
if total_point == 0 :
    print ("I am coming over right now.")
elif total_point <= 2 :
    print ("Ok")
else:
    print ("Good!")
