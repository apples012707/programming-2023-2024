# Semester Evaluator 
# Author: Amelia
# Nov 9 2023

# Greet and ask for the number of courses
num_courses = int(input("How many courses are you taking this semester? "))

total_rating = 0
num_course = 0

# Ask for the rating for each course
for i in range(1, num_courses + 1):
    course_rating = float(input(f"How would you rate course {i} out of 5? "))
    total_rating += course_rating
    num_course += 1

# Calculate the average rating
if num_course > 0:
    average_rating = total_rating / num_course
    print(f"Your average rating for {num_course} courses is: {average_rating:.2f}")
else:
    print("No valid courses rated. Unable to calculate average.")

# Give a comment based on the average
if average_rating < 1 or average_rating == 1:
    print("Ouch.")
elif average_rating > 3:
    print("Glad to hear that.")
else:
    print("Not a bad semester.")