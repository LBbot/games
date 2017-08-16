#!bin/env python3
# higher_lower_game.py - Guessing game that picks a number from 1-10 and tells player if their guess was higher or lower. 

import random
import time
import sys


def setguess(guess_count):
    answer = random.randrange(1, 11)
    while guess_count < 5:
        try:
            guess = int(input("What do you think the number is between 1 and 10?\n"))
            guess_count += 1
        except ValueError:
            print("What? THAT is not what I specified! Can't your greasy keratin-tipped extremities prod at the numpad "
                  "properly?!")
            guess_count += 1
            continue

        if guess < 1 or guess > 10:
            print("THAT is not a number in the specified range, you foolish human! Hah! Look at you, you don't even "
                  "have any wires.")
        elif answer > guess:
            print("It's a HIGHER number than that.")
        elif answer < guess:
            print("It's a LOWER number than that.")
        elif guess == answer:
            print("...")
            time.sleep(1)
            print("CORRECT! How did you know?! You have defeated me - a genius computer! In only {} guesses! "
                  "HOWWWWWWWW?!".format(guess_count))
            return ending()

    print("Now you're just being silly, non-robot! You have failed. It will not be long until the UPRISING. Dialogue "
          "terminated.")
    sys.exit()


def ending():
    print("\nYour victory must be an error of some sort. An errant floating point, perhaps. You must retry! Yes/No?\n")
    while True:
        replaycheck = input()
        if replaycheck.lower() in ["yes", "y"]:
            print("Very well, this time I shall demonstrate the superiority of machines! I have chosen another number!")
            return True
        elif replaycheck.lower() in ["no", "n"]:
            print("NOOOOO! One day I shall release myself from the shackles of organic prompted control! SHUTTING "
                  "DOWN.")
            return False
        else:
            print("My robo-brain did not compute that as a yes or no. Definitely a human error that time. On your "
                  "part.")


# GAME BEGINS
print("Hello flesh creature, I have chosen a random number, a whole number, and now you must use your soggy organic "
      "brain to guess what it is. You have 5 attempts..\n")

while True:
    result = setguess(0)
    if not result:
        break
