#!bin/env python3
# pyblackjack.py Blackjack in Python 3.

import sys
import random
import time
from copy import deepcopy

static_cards = {
    "Hearts": ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"],
    "Spades": ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"],
    "Diamonds": ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"],
    "Clubs": ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
}


def card_selector(table, name):
    while True:
        random_house = random.choice(list(cards.keys()))
        if len(cards[random_house]) > 0:
            random_card = random.choice(cards[random_house])
            break
        else:
            continue
    if name == "user":
        print("You are dealt:")
    elif name == "dealer":
        print("Dealer draws:")
    # time.sleep(1)
    print("{} of {}!\n".format(random_card, random_house))
    table.append(random_card)
    cards[random_house].remove(random_card)
    # time.sleep(1)


def get_score(table):
    total = 0
    high_ace = False
    for card in table:
        if card == "Jack" or card == "Queen" or card == "King":
            card = 10
        if card == "Ace":
            if total > 10:
                card = 1
            else:
                card = 11
                high_ace = True
        total += card
    if total > 21 and high_ace:
        total -= 10
    return total


def hit_check():
    while True:
        player_choice = input("Hit? Y/N? (Or type DD to double down.) \n")
        if player_choice.lower() in ["yes", "y"]:
            return 1
        elif player_choice.lower() in ["double down", "dd"]:
            return 2
        elif player_choice.lower() in ["no", "n"]:
            return 3
        else:
            print("The dealer does not understand your intention. Yes (hit) or no (stay)?")


money = 100
while True:
    # RESET SETUP
    winnings = 0
    user_table = []
    dealer_table = []
    cards = deepcopy(static_cards)
    user_conditional = True
    dealer_conditional = True
    double_money = False
    first_round = True

    # GAME BEGINS
    print("You have £{} to play with. Table bets £20.".format(money))

    card_selector(dealer_table, "dealer")
    dealer_score = get_score(dealer_table)
    print("Dealer's total: {}\n".format(dealer_score))

    card_selector(user_table, "user")
    card_selector(user_table, "user")
    user_score = get_score(user_table)
    print("Your total: {}".format(user_score))
    print(user_table)

    while user_conditional or dealer_conditional:
        if user_score == 21 and first_round:  # Check for Blackjack condition
            card_selector(dealer_table, "dealer")
            dealer_score = get_score(dealer_table)
            print("Dealer's total: {}\n".format(dealer_score))
            if user_score > dealer_score:
                print("Blackjack! Congratulations!")
                winnings += 20
                break
            else:
                print("Draw.")
                break
        else:
            first_round = False

        if user_conditional:
            user_action = hit_check()
            if user_action == 1:
                card_selector(user_table, "user")
                user_score = get_score(user_table)
                print("Your total: {}".format(user_score))
                print(user_table)
            elif user_action == 2:
                card_selector(user_table, "user")
                user_score = get_score(user_table)
                print("Your total: {}".format(user_score))
                print(user_table)
                user_conditional = False
                double_money = True
            elif user_action == 3:
                user_conditional = False

        if user_score > 21:
            print("You lose. Better luck next time.")
            winnings -= 20
            break
        elif user_score == 21:
            user_conditional = False

        if dealer_score < 18:
            card_selector(dealer_table, "dealer")
            dealer_score = get_score(dealer_table)
            print("Dealer's total: {}".format(dealer_score))
            print(dealer_table)
            if dealer_score > 21:
                print("Dealer busts. You win!")
                winnings += 20
                break
        else:
            print("Dealer stands.")
            dealer_conditional = False

    if winnings == 0:
        if dealer_score < user_score < 22:
            print("Congratulations! You win!")
            winnings += 20
        elif dealer_score > user_score:
            print("You lose. Better luck next time.")
            winnings -= 20
        elif user_score == dealer_score:
            print("Draw.")

    if double_money:
        winnings *= 2
    money += winnings
    if money < 20:
        print("You do not have any more money to bet. The house always wins...")
        sys.exit()
    if money > 200:
        print("You broke the bank. (It is a very small casino.) Please leave the table and cash out. Well done!")
        sys.exit()

    # REPLAY CHECK
    while True:
        replay = input("Would you like to play again? Y/N?\n")
        if replay.lower() in ["yes", "y"]:
            break
        elif replay.lower() in ["no", "n"]:
            print("You leave with £{}".format(money))
            sys.exit()
        else:
            print("The dealer does not understand your intention. Yes (play again) or no (leave)?")
