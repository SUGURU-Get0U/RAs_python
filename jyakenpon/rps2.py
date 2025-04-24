
import random
import time




# Lista de opcoes jogáveis
calls = ["1", "2", "3", "pedra","papel", "tesoura"]


# Funcao do Menu do jogo
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
    elif b1 == calls[3] and b2 == calls[5] \
            or b1 == calls[4] and b2 == calls[3] \
            or b1 == calls[5] and b2 == calls[4]:
        return print("O player 2 venceu")
    # vitoria do b2
    else:
        return print("O player 1 perdeu")


def end_game(mode,run):
    if run == 5:
        return

# Comecar o jogo



turn = 1

# Modo de jogo Player vs Cop
while choice == "1":
    print(f"Rodada {turn}")
    print("pedra [1] ","papel [2]", "tesoura [3]")
    p1_num = input("Faca sua escolha: ")
    if p1_num == '1' or 1:
        p1 = calls[3]
    elif p1_num == '2' or 2:
        p1 = calls[4]
    elif p1_num == '3' or 3:
        p1 = calls[5]
    else:
        print("Input do jogador invalido. \nPor favor escolha entre Pedra,papel ou tesoura")
        continue
    cop1 = random.choice(calls[3:])

    print(f"A escolha do jogador foi: {p1}\n")  # Mostra a escolha do player
    print(f"A escolha do computador foi: {cop1}\n")
    verifica(p1,cop1)
    turn += 1 # Passa para proxima rodada
    if turn == 5:  # Ao final de 5 rodadas
        res = input("quer recomeçar em outro modo?? [s/n]: ")
        if res.lower() == 's' or 'sim':
            game_menu()
        else:
            turn = 1
    else:
        continue
# Modo de Jogo Cop vs Cop
while choice == "2":
        print(f"Rodada {turn}") # Mostra a rodada atual
        bot1 = random.choice(calls) # Jogada do bot1
        bot2 = random.choice(calls) # Jogada do bot2
        print(f"A escolha do bot 1 foi: {bot1}") # Mostra a escolha do bot1
        print(f"A escolha do bot 2 foi: {bot2}\n") # Mostra a escolha do bot2
        verifica(bot1,bot2) # Chama a funcao para ver quem ganhou
        time.sleep(5)
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
    print("pedra [1] ", "papel [2]", "tesoura [3]")
    p1_call = input("Jogador 1 faca sua escolha: ")
    if p1_call == '1' or 1:
        p1 = calls[3]
    elif p1_call == '2' or 2:
        p1 = calls[4]
    elif p1_call == '3' or 3:
        p1 = calls[5]
    p2_call = input("Jogador 2 faca sua escolha: ")
    if p2_call == '1' or 1:
        p1 = calls[3]
    elif p2_call == '2' or 2:
        p1 = calls[4]
    elif p2_call == '3' or 3:
        p1 = calls[5]
    while p1_call not in calls or p2_call not in calls:  # Nao tem como saber quem teve o input invalido
        print("Input invalido")
        p1_call = input("Jogador 1 faca sua escolha: ")
        p2_call = input("Jogador 2 faca sua escolha: ")
    print(f"A escolha do jogador 1 foi: {p1_call}\n")  # Mostra a escolha do player
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
"a "
#

