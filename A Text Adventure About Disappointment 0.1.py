def keyreset():
    global keyget
    keyget = 0

def white_room():
    print("You are in a nearly featureless white room, reminiscent of an extremely clean hospital, or the Star Wars \n"
          "prequels.\n"
          "To the west is a blue door, to the north is a green door, to the east is a red door.\n")
    direction = input("Choose a direction:\n")
    if direction == "west":
        blue_room()
    if direction == "north":
        green_room()
    if direction == "east":
        red_room_check()
    if direction == "south":
        print("There is only a featureless white wall on this side. You cannot go further, and do not think to question "
              "\nhow you entered.")
        white_room()
    else:
        print("I don't recognise that as a direction. Please try again.")
        white_room()

def blue_room():
    print("The blue door opens into a room with walls covered by posters of Sonic The Hedgehog. In the center is a bed "
          "\nwith Sonic The Hedgehog sheets, Sonic The Hedgehog pillowcases and a Sonic The Hedgehog duvet cover. A few "
          "\nSonic The Hedgehog plush toys are scattered across it. It is an adult-sized bed. You feel slightly embarassed.")
    direction = input("Choose a direction:\n")
    if direction == "east":
        white_room()
    else:
        print("There's nowhere to go.")
        blue_room()

def green_room():
    print("The green door opens into a black void inexplicably with solid footing, and bordered by walls of green lightning, "
          "\ncrackling bolts arcing down like pillars into the void. It reminds you of special effects from the early "
          "\n2000s, or Dragon Age 3, and you wonder why green lightning always appears so cheap and tacky in art design.")
    global keyget
    if keyget == 0:
        print("In the center of the room hovers a Red Key, bobbing up and down suspended by some mysterious force.")
        direction = input("Choose a direction or 'take key':\n")
        if direction == "south":
            white_room()
        if direction == "take key":
            print("You trepidatiously reach out and pluck the Red Key from the void, cringing as though the green lightning "
                  "\nwill close in on you. It doesn't. You look down at the key in your hand and leave, mildly disappointed.")
            keyget = 1
            white_room()
        else:
            print("There's nowhere to go.")
            green_room()

    elif keyget > 0:
        direction = input("Choose a direction:\n")
        if direction == "south":
            white_room()
        else:
            print("There's nowhere to go.")
            green_room()

def red_room_check():
    global keyget
    if keyget == 0:
        print("The door to the red room does not open, despite your attempts. There is, however, a keyhole. This fills "
              "\nyou with DETERMINATION.")
        white_room()
    if keyget == 1:
        print("You unlocked the red door with the Red Key, and entered.")
        keyget = 2
        red_room()
    if keyget == 2:
        red_room()

def red_room():
    print("The red door opens to a room stained entirely red with blood! Or, possibly, given the fruity tang in your "
          "\nnostrils, wine or cranberry juice. Anyway, there's a big lever with a sign saying 'DISAPPOINTMENT: Pull this "
          "\nto blow up the Reapers and end the game once and for all. Until the Extended Cut.")
    direction = input("Choose a direction or 'pull lever':\n")
    if direction == "west":
        white_room()
    if direction == "pull lever":
        print("Goodbye, cruel world.")
        quit()
    else:
        print("There's nowhere to go.")
        red_room()

keyreset()
white_room()
