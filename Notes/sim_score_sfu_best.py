# SFU bEST - Similarity score
# Author: Amelia Tang
# Date November 9 2023



# Load data from a file
# "Read" it in a meanful
# Link our Sim Score algo to the data

# Open the file
with open("./data.csv") as f:
   f.readline()
   
f.readline ()


#Create a "profile" of likes
# (fave places in SFU)
profile = 
"Bubble World",
"Chef Huang",
"Guadalupe (MBC)",
"Steves's poke Bar"

with open ("./data.csv")as f:
   # Throw away the header
   header = f.readline()

   for line in f:
      #convert the string to a list
      curent_likes = line.split(",")

   #store the person's name
current_name = current_likes[1]


   # Initalize the current sim score
currrent_sim_score = 0

# Sim score algorithm
for item in profile:
   if item in cureent_likes:
      current_sim_score += 1

# Print the results from this line of data
print(f"{current_name }")