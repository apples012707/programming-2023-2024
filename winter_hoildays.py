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
    """Give a summary of our winter holidays 2023/24

    Params:
        good_or_bad - indicate what kind of event to summarize

    Returns:
        an event that happened during the holidays
        the event is selected randomly"""

    # Create a list of good and bad events
    good_events = [
        "I got a lego set for Christmas",
    "I went Richmond Centre for Christmas shopping.",
    "I went to eat crepes in downtown",
    "I went go the ferry and visited Lonsdale Quay mall!",
    "I cooked food for myself",
    ]
    bad_events = [
        "I didn't go skating this winter break",
    "I didn't do secret santa this year...",
    "There was no snow this year💩",
    ]

    if good_or_bad.strip().lower() == "good":
        return random.choice(good_events)
    elif good_or_bad.strip().lower() == "bad":
        return random.choice(bad_events)
    else:
        return "Sorry, I only take good or bad events."


def main() -> None:
    print(winter_holiday("good"))
    # "I got a lego set for Christmas."
    # "I went to Richmond Centre to walk around aimlessly."

    print(winter_holiday("bad"))
    # "I asked for a bidet for Christmas instead I got a rando amazon smart watch."
    # "I hoped to snowboard but got lots of rain on the mountains instead."

    print(winter_holiday("banana"))


if __name__ == "__main__":
    main()