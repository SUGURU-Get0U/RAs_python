
import random
import subprocess
import time

from IPython.core.display_functions import display

game_modes = ["Vs Cop, \n Cop Vs Cop,\n 1 v 1"]

def tie():
    print("O jogo terminou em empate!")

def win(champion= "bug"):
    print(champion + " venceu!")

def lost(winner, loser):
    print(loser, " you lost :(",  winner, " won!")

def clear_terminal():
    time.sleep(3)
    subprocess.run('cls', shell=True, check=True)

def start_game():
    print(game_modes)


def cop_vs_cop():
    b1 = random.choice(calls)
    b2 = random.choice(calls)
    print(f"A escolha do bot 1 foi: {b1}\n")
    print(f"A escolha do bot 2 foi: {b2}")
    # ver quem ganhou
    # empate
    if b1 == b2:
        tie()

    # vitoria do b1
    elif b1 == calls[0] and b2 == calls[2] \
            or b1 == calls[1] and b2 == calls[0] \
            or b1 == calls[2] and b2 == calls[1]:
        win("bot 1")

    else:
        lost("bot 2", "bot 1")
    # limpar terminal
    clear_terminal()



# Comecar o jogo
start = input("Voce deseja comecar o jogo? [s/n] ")

if start == "s":
    start = True

else:
    start = False

#  saber o modo de jogo

while not start:
    start = input("Voce deseja comecar o jogo? [s/n]")

start_game()
ps_call = input("Select the game mode: ")

# Lista de opcoes jogáveis
calls = ["pedra", "papel", "tesoura"]

# 1 V 1
    # 2 inputs p1 e p2
    # analisar se os inputs sao validos
    # ver quem ganhou


# vs cop
    # 1 ‘input’ + jogada do computador
    # verificao de inputs
    # ver quem ganhou
# cop vs cop
while ps_call == game_modes[1]:
    cop_vs_cop()


#
