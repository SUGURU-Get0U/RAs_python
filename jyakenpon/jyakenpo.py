# Jokenpon
import random
from random import randrange

print('Bien-venido ao jokenpo!')

Player1 = input('Type in your username: ')

PlayerOption = []
BotOption = []
Draw = PlayerOption == BotOption
PlayableOptions = ['rock', 'paper', 'scissors']

print('lets start the game')

for item in zip([1,2,3], PlayableOptions, strict= True):
    print(item[0], ' - ', item[1])

playerop = input("Choose an option: ")
PlayerOption.append(playerop)

BotOp = randrange(0,3)
BotOption.append(BotOp)

if PlayerOption == BotOption:
    print("Both chose the same option, its a draw")

