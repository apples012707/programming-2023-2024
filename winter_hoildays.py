# Winter Holidays Review
# Author: Amelia
# 8 January 2024

# Requirements:
# - create a function called winter_holiday()
# - take one parameter
#   - string
# - return a summary of an event from your holidays

import random


def winter_holiday(good_or_bad: str) -> str:
    """Give a summary of our winter holidays 2023/04
    
    Params:
        good_or_bad - indicate what kind of event to summarize
        
        Returns:
            an event that happened during the holidays"""

  
    if good_or_bad.strip().lower() == "good":
        return random.choice(good_events)
    elif good_or_bad.strip().lower() == "bad":
        return random.choice(bad_events)
    else:
        return "Sorry, I only take good or bad events."


good_events = [
    "I got a lego set for Christmas",
    "I went Richmond Centre for Christmas shopping.",
    "I went to eat crepes in downtown",
    "I went go the ferry and visited Lonsdale Quay mall!",
    "I cooked food for myself"
]


bad_events = [
    "I didn't go skating this winter break",
    "I didn't do secret santa this year...",
    "There was no snow this year :()"
    ]


def main() -> None:
    print(winter_holiday("good"))

    print(winter_holiday("bad"))




if __name__ == "__main__":
    main()


