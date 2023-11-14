# Olympic scoring
# Author: Amelia
# 6 November 2023

# Greet the user
print("Hello! What is your favourite Olympic sport?")
print("Awesome, now imagine yourself as the judge and answer the following questions...")

# Create a list of questions to ask
questions = [
    "Was the athlete's timing precise and well-coordinated during their performance? 1 is imprecise and 5 is perfect",
    "How well were the athlete's technical skills, including body position, control, and coordination? 1 is poor, 5 is extremely well.",
    "What level of difficulty did the athlete demonstrate in their performance? 1 is easy and 5 is extremely difficult.",
    "How well did the athlete present respect to you and to the audience? 1 is none and 5 is very respectful.",
    "How was the athlete's mental performance? 1 is doubting oneself and 5 is confident"
]

total_score = 0

# For every question in that list
for question in questions:
    print(question)

    # Get the user's rating
    user_score = float(input().strip(",.?! "))

    # Add the rating to some total-rating
    total_score += user_score

# Do some maths on the results
# Use the average score to represent the final score
average_score = total_score / len(questions)

# Present the results
print(f"The average score for this athlete is: {average_score:.2f} / 5")



