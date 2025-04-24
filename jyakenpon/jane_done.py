
import random
import time
from enum import *

Options = {
    "Pedra": 1,
    "Papel": 2,
    "Tesoura": 3
}


for chave, valor in Options.items():
    print(f"{chave} -> {valor}")


# Lista de opcoes jogáveis



# Função do Menu do jogo
def game_menu():
    menu_options = ["1","2","3","VsCop","CopVsCop","1v1"]
    print("(1) VsCop \n(2) CopVsCop \n(3) 1v1")
    x = 0
    while x not in menu_options:
        x = input("Select the game mode: ")
    return x



choice =game_menu()




# Funcao da condicao de vitoria
def verifica(b1,b2):
    if b1 == b2:
        return print("empatou")
    # vitoria do b1
    elif b1 == Options.value([1]) and b2 == Options[3].value() \
            or b1 == Options[2].value() and b2 == Options[1].value()\
            or b1 == Options[3].value and b2 == Options[2].value():
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
    for key,value  in Options.items():
        print(f"{key} -> {value}")
    p1 = int(input("Faca sua escolha: "))
    cop1 =  random.randint(1, 3)
    if p1 not in Options.values():
        print("Input do jogador invalido. \nPor favor escolha entre Pedra ,papel ou tesoura")
        p1 = int(input("Faca sua escolha: "))
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
        bot1 = random.randint(1, 3)
        bot2 = random.randint(1, 3)
        print(f"A escolha do bot 1 foi: {bot1}") # Mostra a escolha do bot1
        print(f"A escolha do bot 2 foi: {bot2}\n") # Mostra a escolha do bot2
        verifica(bot1,bot2) # Chama a funcao para ver quem ganhou
        time.sleep(5)
        turn += 1 # Passa para proxima rodada
        if turn == 5: # Ao final de 5 rodadas
            res = input("quer recomeçar em outro modo?? [s/n]: ")
            if res.lower() == 's' or 'sim':
                game_menu()
            else:
                turn = 1
        else:
            continue

        # Modo de jogo Player vs Player
# Modo de Jogo Player vs Player
while choice == "3":
    print(f"Rodada {turn}")
    print(list(Options))
    p1_call = input("Jogador 1 faca sua escolha: ")
    p2_call = input("Jogador 2 faca sua escolha: ")
    while p1_call not in Options.values() or p2_call not in Options.values():  # Nao tem como saber quem teve o input invalido
        print("Input invalido")
        p1_call = input("Jogador 1 faca sua escolha: ")
        p2_call = input("Jogador 2 faca sua escolha: ")
    print(f"A escolha do jogador 1foi: {p1_call}\n")  # Mostra a escolha do player
    print(f"A escolha do jogador 2 foi: {p2_call}\n")
    verifica(p1_call, p2_call)
    turn += 1  # Passa para proxima rodada
    if turn == 5:  # Ao final de 5 rodadas
        res = input("quer recomeçar em outro modo?? [s/n]: ")
        if res.lower() == 's' or 'sim':
            game_menu()
        else:
            turn = 1
    else:
        continue


        # sair do loop while