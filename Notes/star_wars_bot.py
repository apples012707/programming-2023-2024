# Star Wars Bot
# Author: Amelia Tang
# Date: 16th Oct, 2023

import time 

print ("Hello there! 🫨")
time.sleep(1)
print ("I will decide if u can join the Dark Side or the Light side.👻")
time.sleep(1)

fav_colour = input ("Is red your favourite colour? 🤡")
if fav_colour.lower().strip(",. ?!") == "yes" : 
    print ("Dark side it is... 😈")
else : 
    cape = input ("Do u like capes?🦸‍♀️")
    if cape.lower().strip(",. ?!") == "yes": 
        print ("Dark side it is... 😈")
    else : 
        print ("You are on the light side!🤩")









