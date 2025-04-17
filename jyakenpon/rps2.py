
import random
import subprocess
import time

game_modes = ["VsCop", "CopVsCop", "1v1"]
# Lista de opcoes jogáveis
calls = ["pedra", "papel", "tesoura"]

def game_menu():
    menu_options = ["1","2","3","VsCop","CopVsCop","1v1"]
    print("(1) VsCop \n(2) CopVsCop \n(3) 1v1")
    x = 0
    while x not in menu_options:
          x = input("Select the game mode: ")
    return x

def verifica(b1,b2):
    if b1 == b2:
        return print("empatou")
    # vitoria do b1
    elif b1 == calls[0] and b2 == calls[2] \
            or b1 == calls[1] and b2 == calls[0] \
            or b1 == calls[2] and b2 == calls[1]:
        return print("bot1")
    # vitoria do b2
    else:
        return print("bot2")


def end_game(mode,run):
    if run == 5:
        return


# Comecar o jogo

start = input("Voce deseja comecar o jogo? [s/n] ")
if start == "s":
  choice = game_menu()
else:
  exit()

turn = 1
while choice == "2":
        print(f"Rodada {turn}")
        b1 = random.choice(calls)
        b2 = random.choice(calls)
        print(f"A escolha do bot 1 foi: {b1}\n")
        print(f"A escolha do bot 2 foi: {b2}\n")
        verifica(b1,b2)
        turn += 1
        if turn == 5:
            res = input("quer recomecar em outro mode?? s/n")
            if res == 's':
                game_menu()
            else:
                turn = 1
        else:
            continue



        # sair do loop while

#
