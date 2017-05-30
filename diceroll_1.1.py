import random

name = input("What is your name?" + "\n")
print ("Hello, " + name + ". I am about to roll a six sided dice.")

letterednums = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6}

def setbet():
    bet = input("What do you think the number will be?" + "\n")
    bet = bet.lower()

    if bet in letterednums:
        bet = letterednums[bet]

    try:
        bet = int(bet)
    except ValueError:
        print (
        "You MUST have mistyped. It's okay. We all make mistakes, " + name + ". Please enter a number between 1 and 6.")
        return setbet()

    if bet < 1 or bet > 6:
        print ("I said six sided!")
        return setbet()
    return bet

def roll():
    answer = random.randrange(1, 7)
    print ("The dice rolls, and it's..." + str(answer) + "!")
    return int(answer)

def game(tries, score):
    tries += 1
    if setbet() == roll():
        print ("Woah, " + name + "! Are you psychic or something?")
        score += 1
        print ("Score: " + str(score) + "/" + str(tries))
    else:
        print ("Better luck next time, " + name + ".")
        print ("Score: " + str(score) + "/" + str(tries))

    def replaycheckfunc():
        replaycheck = input("Play again? Yes or no?" + "\n")

        if replaycheck.lower() in ["yes", "y"]:
            game(tries, score)
        elif replaycheck.lower() in ["no", "n"]:
            print ("Goodbye, " + name + "!")
            quit()
        else:
            print ("My robo-brain did not compute that as a yes or no. ")
            replaycheckfunc()

    replaycheckfunc()

game(0, 0)
