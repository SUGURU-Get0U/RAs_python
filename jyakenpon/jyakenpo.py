# Jokenpon
import random
import os
from random import randrange
from time import sleep


def endgame():
    print('el juego termino')
    sleep(3)
    os.system('cls')
def victory():
    print(Player1, " chose ", playerop, "computer chose ", BotOp)
    print('you won <3')

def lost():
    print(Player1, " chose ", playerop, "computer chose ", BotOp)
    print('COP won :(')

def bot1(botwon):
    print(botwon + "won")


print("Welcome!")

Player1 = input('Type in your username: ')
modes = ['vs COP', 'vs human', 'bot vs bot']
PlayableOptions = ['rock', 'paper', 'scissors']

for mode in zip([1,2,3], modes, strict=True):
    print(mode[0], ' - ', mode[1])

typemode = input('Select the mode: ')

print('lets start the game')

while typemode == 'vs COP':

    for item in zip([1,2,3], PlayableOptions, strict= True):
        print(item[0], ' - ', item[1])

    playerop = input("Choose an option: ")


    BotOp = random.choice(PlayableOptions)


    if playerop == BotOp:
        print("Both chose the same option, its a draw")

    elif playerop == "rock" and BotOp == "paper" \
            or playerop == "paper" and BotOp == "scissors" \
            or playerop == "scissors" and BotOp == "rock":
        lost()

    else:
        victory()

    endgame()


while typemode == 'bot vs bot':
    BotOp2 = random.choice(PlayableOptions)
    BotOp = random.choice(PlayableOptions)

    if BotOp == BotOp2:
        print(Player1, 'and the computer chose the same option')
        print('draw!')

    elif BotOp2 == "rock" and BotOp == "paper" \
            or BotOp2 == "paper" and BotOp == "scissors" \
            or BotOp2 == "scissors" and BotOp == "rock":
        bot1(botwon= 'bot 1')

    elif BotOp == "rock" and BotOp2 == "paper" \
            or BotOp == "paper" and BotOp2 == "scissors" \
            or BotOp == "scissors" and BotOp2 == "rock":
        bot1(botwon= 'bot 2')







