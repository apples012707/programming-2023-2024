# Spotify Data Analyzer
# Author : Amelia
# 16th Jan 2024
# Open up the file
# ----  Look for all songs performed by Drake
#       Use linear search
# Create a list to store all Drake's song
# For every song in the raw file

import csv
# open up the file
with open("./spotify.csv") as f:
    # ---- Look for all song performed by Drake
    #      Use Linear search
    #      Create a csv reader object
    csv_reader = csv.DictReader(f)

    # Create a list to store all Drake's songs
    drake_songs = []

    # Create a counter for the current line number 
    line_num = 0

    # For every song in the .csv file
    for line in csv_reader:
        if "drake" in line["artist"].lower():
            # add

        # If this song if sung by Drake
        # add it to the Drake's song list
drake_songs = find_all_drake("Drake")

ed_sheeran_songs = find_all_songs("Edfor song in drake_songs:
            print(song)

# Print our all songs that have
# a danceability of >=0.6
            
