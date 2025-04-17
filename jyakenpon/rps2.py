
import random

import requests

# Pega todos os codigos da biblioteca
from tkinter import *


# Lista de opcoes jogáveis
calls = ["pedra", "papel", "tesoura"]

# UI (user interface)
tela = Tk()  # Cria um janela
tela.title("minecraft 2")
Game_title = Label(tela, text="Pedra Papel e Tesoura")
    # Cria um texto inicial na tela.
    # Precisa de 2 atributos (A janela que será exibida, um texto)

# Funcao do Menu do jogo
def game_menu():
    menu_options = ["1","2","3","VsCop","CopVsCop","1v1"]
    print("(1) VsCop \n(2) CopVsCop \n(3) 1v1")
    x = 0
    while x not in menu_options:
        x = input("Select the game mode: ")
    return x




Game_title.grid(column=0, row=0)
# Exibe o texto usando os atributos (coluna, linha)
# como se fosse no Excel

Play_button = Button(tela, text="Play", command=game_menu())
# Cria um botão que executa funcao game_menu

Play_button.grid(column=0, row=2)
# Posiciona o Botao recém criado

game_mode = Label(tela, text= "")
# Cria a resposta ao botão play, o texto será alterado pela funcao game_menu

tela.mainloop()  # Deixa a janela rodando para sempre ate alguém fechar

choice =game_menu()




# Funcao da condicao de vitoria
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



turn = 1

# Modo de jogo Player vs Cop
while choice == "1":
    print(f"Rodada {turn}")
    p1 = input("Faca sua escolha: ")
    cop1 = random.choice(calls)
    if p1 not in calls:
        print("Input do jogador invalido. \nPor favor escolha entre Pedra,papel ou tesoura")
        p1 = input("Faca sua escolha: ")
    else:
        continue
    print(f"A escolha do jogador foi: {p1}\n")  # Mostra a escolha do player
    print(f"A escolha do computador foi: {cop1}\n")
    verifica(p1,cop1)
    turn += 1 # Passa para proxima rodada
    if turn == 5:  # Ao final de 5 rodadas
        res = input("quer recomeçar em outro modo?? [s/n]: ")
        if res == 's' or 'sim':
            game_menu()
        else:
            turn = 1
    else:
        continue
# Modo de Jogo Cop vs Cop
while choice == "2":
        print(f"Rodada {turn}") # Mostra a rodada atual
        b1 = random.choice(calls) # Jogada do bot1
        b2 = random.choice(calls) # Jogada do bot2
        print(f"A escolha do bot 1 foi: {b1}\n") # Mostra a escolha do bot1
        print(f"A escolha do bot 2 foi: {b2}\n") # Mostra a escolha do bot2
        verifica(b1,b2) # Chama a funcao para ver quem ganhou
        turn += 1 # Passa para proxima rodada
        if turn == 5: # Ao final de 5 rodadas
            res = input("quer recomeçar em outro modo?? [s/n]: ")
            if res == 's' or 'sim':
                game_menu()
            else:
                turn = 1
        else:
            continue

        # Modo de jogo Player vs Player
# Modo de Jogo Player vs Player
while choice == "3":
    print(f"Rodada {turn}")
    p1_call = input("Jogador 1 faca sua escolha: ")
    p2_call = input("Jogador 2 faca sua escolha: ")
    while p1_call not in calls or p2_call not in calls:  # Nao tem como saber quem teve o input invalido
        print("Input invalido")
        p1_call = input("Jogador 1 faca sua escolha: ")
        p2_call = input("Jogador 2 faca sua escolha: ")
    print(f"A escolha do jogador 1foi: {p1_call}\n")  # Mostra a escolha do player
    print(f"A escolha do jogador 2 foi: {p2_call}\n")
    verifica(p1_call, p2_call)
    turn += 1  # Passa para proxima rodada
    if turn == 5:  # Ao final de 5 rodadas
        res = input("quer recomeçar em outro modo?? [s/n]: ")
        if res == 's' or 'sim':
            game_menu()
        else:
            turn = 1
    else:
        continue


        # sair do loop while

#

