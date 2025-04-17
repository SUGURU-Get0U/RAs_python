
import random
import subprocess
import time



game_modes = ["VsCop", "CopVsCop", "1v1"]

def tie():
    print("O jogo terminou em empate!")

def win(champion= "bug"):
    print(champion + " venceu!")

def lost(winner="bot 2", loser="bot 1"):
    print(winner, " you lost :(", loser, " won!")

def clear_terminal():
    time.sleep(3)
    subprocess.run('cls', shell=True, check=True)

def start_game():
    for items in zip([1,2,3], game_modes, strict=True):
        print(items[0], "-", items[1])

    ps_call = input("Select the game mode: ")

def exitt():
    saida = input("Voce deseja recomecar o jogo? [s/n]: ")
    if saida == "s":
        start_game()
    else:
        print("obrigado por jogar")

# Comecar o jogo
start = input("Voce deseja comecar o jogo? [s/n] ")

if start == "s":
    start = True

else:
    start = False


#  saber o modo de jogo

while not start:
    start = input("Voce deseja comecar o jogo? [s/n]")



# Lista de opcoes jogáveis
calls = ["pedra", "papel", "tesoura"]

# 1 V 1
    # 2 inputs p1 e p2
    # analisar se os inputs sao validos
    # ver quem ganhou


# vs cop
    # 1 ‘input’ + jogada do computador
while ps_call == game_modes[0] or 0:
    Solop1 = input("")
    # verificao de inputs
    # ver quem ganhou
# cop vs cop
while ps_call == game_modes[1] or "2":
    b1 = random.choice(calls)
    b2 = random.choice(calls)
    print(f"A escolha do bot 1 foi: {b1}\n")
    print(f"A escolha do bot 2 foi: {b2}\n")
    # ver quem ganhou
    # empate
    if b1 == b2:
        tie()
        exitt()

    # vitoria do b1
    elif b1 == calls[0] and b2 == calls[2] \
            or b1 == calls[1] and b2 == calls[0] \
            or b1 == calls[2] and b2 == calls[1]:
        win("bot 1")
        exitt()

    # vitoria do b2
    else:
        lost()
        exitt()
    # sair do loop while







#
