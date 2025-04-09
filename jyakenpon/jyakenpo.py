# Jokenpon
import random
from random import randrange

def victory():
    print("YOU WON OMGA!")

def lost():
    print("O computador venceu")

print('Bien-venido ao jokenpo!')

Player1 = input('Type in your username: ')

PlayableOptions = ['rock', 'paper', 'scissors']

print('lets start the game')

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