#!bin/env python3
# turn_based_battle.py - A Pokemon/JRPG style turn-based battle in the Python console. 

import random, sys

class Combatant:
    def __init__(self):
        self.hp = 100

player1 = Combatant()
enemy1 = Combatant()

def basic_hp_effect():
    return random.randrange(18, 26)

def wider_hp_effect():
    return random.randrange(10, 35)


def battle_start():
    coin_flip = random.randrange(1, 3)
    if coin_flip == 1:
        print("First strike!")
        player_turn()
    if coin_flip == 2:
        print("The enemy surprises you!")
        enemy_turn()


def player_turn():
    if player1.hp <= 0:
        print("You died! \nGAME OVERRRRR")
        sys.exit()
    print("Player HP: {}/100".format(player1.hp))
    print("Enemy HP: {}/100\n".format(enemy1.hp))
    move_input = input("Your turn. Select a move by inputting a number: \n"
                       "1. Super Boring Attack (deals 18-25 damage)\n"
                       "2. Unpredictable Strike (deals 10-35 damage)\n"
                       "3. Heal Thyself (restores 18-25 HP)\n"
                       "4. Skip turn. (take no action)\n")
    if move_input == "1":
        move1("player1")
        enemy_turn()
    elif move_input == "2":
        move2("player1")
    elif move_input == "3":
        move3("player1")
    elif move_input == "4":
        return enemy_turn()
    else:
        print("That's not a move!")
        return player_turn()
    return enemy_turn()


def enemy_turn():
    if enemy1.hp <= 0:
        print("Enemy defeated! \nVictory achieved! \n(note to self: write code that plays the Final Fantasy fanfare here.)")
        sys.exit()
    print("Player HP: {}/100".format(player1.hp))
    print("Enemy HP: {}/100\n".format(enemy1.hp))
    print("Enemy turn!")
    enemy_move = random.randrange(1, 101)
    if enemy_move < 40:
        move1("enemy1")
    elif 40 <= enemy_move <= 80:
        move2("enemy1")
    elif enemy_move > 80:
        move3("enemy1")
    return player_turn()


def move1(user):
    print("BANG!\n")
    if user == "player1":
        temp = basic_hp_effect()
        print(temp)
        enemy1.hp -= temp
        #enemy1.hp -= basic_hp_effect()
    if user == "enemy1":
        player1.hp -= basic_hp_effect()

def move2(user):
    print("CRACK?!\n")
    if user == "player1":
        enemy1.hp -= wider_hp_effect()
    if user == "enemy1":
        player1.hp -= wider_hp_effect()

def move3(user):
    print("TINKLY TINKLING\n")
    if user == "enemy1":
        enemy1.hp += basic_hp_effect()
        if enemy1.hp > 100:
            enemy1.hp = 100
        print(("Enemy HP: {}/100\n".format(enemy1.hp)))
    if user == "player1":
        player1.hp += basic_hp_effect()
        if player1.hp > 100:
            player1.hp = 100
        print("Player HP: {}/100\n".format(player1.hp))


battle_start()
