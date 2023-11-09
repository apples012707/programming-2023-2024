# Calculating Similarity Score
# Author: Ubial
# 9 November 2023

# Calculate similar scores between two people

# Create two lists that represent the movies that they like
ubials_fave_movies = [
    "the matrix"
    "avengers: infinity war",
    "inferal affairs",
    "rogue one",
    "the empires strikes back"
]

bens_fave_movies = [
    "thomas and friends, world big adventure",
    "paddington 2",
    "avengers: infinity war",
    "rogue one"
]

similarity_score = 0

# For every movie in the fist list
    # If that mobie is in the second list
        # Increase the similarity score by 1 if movies are the same
for movie in ubials_fave_movies:
    if movie in bens_fave_movies:
        similarity_score += 1

# Display the results
print(f"The similarity score betweem the users is:")
print(similarity_score)