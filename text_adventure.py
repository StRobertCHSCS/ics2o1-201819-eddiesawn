'''
Author: Edison Tse
Type: Text Based Adventure Game
'''

print("Malware Attack")
start = input(str("Type Start to start"))
event = 0

if start == "start" or "Start":
    print("You are a commanding officer in a squad of 7 people in the antivirus army.")
    print("You and your squad are tasked with the objective of securing a hostage being held at point Google Chrome.")
    print("However, the area is heavily guarded by the enemy virus army, who recently took the area")
    print("You and your squad set out.")

import random

while event <= 2:
    event_gen = random.randint(1, 2)
    event += 1

    if event_gen == 1:
        print("You see an enemy trojan on your way to the point, but they haven't seen you yet.")
        print("You decide to avoid the trojan for now as the others can catch it.")
        event = event + 1

    elif event_gen == 2:
        print("Your squad finds a pillbox, would you rather try to go past it \"a\" or call in an air strike \"b\"?")
        event2_choice = input(str("Type a or b"))

        if event2_choice == "a":
            print("You got spotted and the enemy shot you and you died. Good job.")

        elif event2_choice == "b":
            print("Oh look, you made the right choice. Good for you.")

        else:
            print("dude. it said a or b. you screwed up. restart this game.")






