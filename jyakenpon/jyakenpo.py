import random
import time

# Lista de opcoes jogáveis (apenas as opções principais)
options = ["pedra", "papel", "tesoura"] # Tirei os números da lista deixando apenas as opcoes principais

def agradecimento(): # Funcao que printa no final do jogo o agradecimento
    print(" OBRIGADO POR JOGAR! \n"
          "     feito por:\n"
          "     Daniel Jose\n"
          "     Daniel Langner\n"
          "     Eduardo de Oliveira\n"
          "     Isabelle Duarte\n "
          "         <3 ")

def mostrar_placar(pontplayer1, nome_jogador1, pontplayer2, nome_jogador2): # Funcao que mostra o placar
    # pega como atributos a Quantidade de pontos e o nome dos players (sejao eles bots ou pessoas)
    print(f"\nPlacar: {nome_jogador1} {pontplayer1} x {pontplayer2} {nome_jogador2}\n")

def game_menu():
    menu_options = ["1", "2", "3"]
    print("(1) VsCop \n(2) CopVsCop \n(3) 1v1")
    while True: # Cria um loop que valida a escolha do player
        choice = input("Selecione o modo de jogo: ")
        if choice in menu_options:
            return choice
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

def verifica(b1, b2):
    if b1 == b2:
        print("Empate!")
        return 0
    elif (b1 == "pedra" and b2 == "tesoura") or \
         (b1 == "papel" and b2 == "pedra") or \
         (b1 == "tesoura" and b2 == "papel"):
        print("Jogador 1 venceu!")
        return 1
    else:
        print("Jogador 2 venceu!")
        return 2

def vs_cop_game():
    pont_player = 0
    pont_coop = 0
    nome_jogador = "Jogador"
    nome_cop = "Computador"
    turn = 1
    while True:
        print(f"\nRodada {turn}")
        print("pedra [1] ", "papel [2]", "tesoura [3]")
        p1_choice_str = input("Faça sua escolha: ")
        if p1_choice_str == '1':
            p1 = "pedra"
        elif p1_choice_str == '2':
            p1 = "papel"
        elif p1_choice_str == '3':
            p1 = "tesoura"
        elif p1_choice_str.lower() == 'q':
            mostrar_placar(pont_player, nome_jogador, pont_coop, nome_cop)
            return None
        else:
            print("Input do jogador inválido. Por favor, escolha entre 1, 2 ou 3 ou 'q' para sair.")
            continue

        cop1 = random.choice(options)

        print(f"A escolha do jogador foi: {p1}")
        print(f"A escolha do computador foi: {cop1}\n")
        resultado = verifica(p1, cop1)
        if resultado == 1:
            pont_player += 1
        elif resultado == 2:
            pont_coop += 1

        mostrar_placar(pont_player, nome_jogador, pont_coop, nome_cop)

        turn += 1
        if turn > 5:
            res = input("Quer recomeçar em outro modo? [s/n]: ")
            if res.lower() in ['s', 'sim']:
                return game_menu()
            else:
                mostrar_placar(pont_player, nome_jogador, pont_coop, nome_cop)
                return None

def cop_vs_cop_game():
    pont_bot1 = 0
    pont_bot2 = 0
    nome_bot1 = "Bot 1"
    nome_bot2 = "Bot 2"
    turn = 1
    while True:
        print(f"\nRodada {turn}")
        bot1 = random.choice(options)
        bot2 = random.choice(options)
        print(f"A escolha do {nome_bot1} foi: {bot1}")
        print(f"A escolha do {nome_bot2} foi: {bot2}\n")
        resultado = verifica(bot1, bot2)
        if resultado == 1:
            pont_bot1 += 1
        elif resultado == 2:
            pont_bot2 += 1

        mostrar_placar(pont_bot1, nome_bot1, pont_bot2, nome_bot2)
        time.sleep(2)

        turn += 1
        if turn > 5:
            res = input("Quer recomeçar em outro modo? [s/n]: ")
            if res.lower() in ['s', 'sim']:
                return game_menu()
            else:
                mostrar_placar(pont_bot1, nome_bot1, pont_bot2, nome_bot2)
                return None

def player_vs_player_game():
    pont_p1 = 0
    pont_p2 = 0
    nome_jogador1 = "Jogador 1"
    nome_jogador2 = "Jogador 2"
    turn = 1
    while True:
        print(f"\nRodada {turn}")
        print("pedra [1] ", "papel [2]", "tesoura [3]")

        while True:
            p1_choice = input(f"{nome_jogador1}, faça sua escolha: ")
            if p1_choice == '1':
                p1 = "pedra"
                break
            elif p1_choice == '2':
                p1 = "papel"
                break
            elif p1_choice == '3':
                p1 = "tesoura"
                break
            elif p1_choice.lower() == 'q':
                mostrar_placar(pont_p1, nome_jogador1, pont_p2, nome_jogador2)
                return None
            else:
                print(f"{nome_jogador1}, escolha inválida. Use 1, 2 ou 3 ou 'q' para sair.")

        while True:
            p2_choice_str = input(f"{nome_jogador2}, faça sua escolha: ")
            if p2_choice_str == '1':
                p2 = "pedra"
                break
            elif p2_choice_str == '2':
                p2 = "papel"
                break
            elif p2_choice_str == '3':
                p2 = "tesoura"
                break
            elif p2_choice_str.lower() == 'q':
                mostrar_placar(pont_p1, nome_jogador1, pont_p2, nome_jogador2)
                return None
            else:
                print(f"{nome_jogador2}, escolha inválida. Use 1, 2 ou 3 ou 'q' para sair.")

        print(f"A escolha do {nome_jogador1} foi: {p1}")
        print(f"A escolha do {nome_jogador2} foi: {p2}\n")
        resultado = verifica(p1, p2)
        if resultado == 1:
            pont_p1 += 1
        elif resultado == 2:
            pont_p2 += 1

        mostrar_placar(pont_p1, nome_jogador1, pont_p2, nome_jogador2)

        turn += 1
        if turn > 5:
            res = input("Quer recomeçar em outro modo? [s/n]: ")
            if res.lower() in ['s', 'sim']:
                return game_menu()
            else:
                mostrar_placar(pont_p1, nome_jogador1, pont_p2, nome_jogador2)
                return None

# Começar o jogo
while True:
    game_choice = game_menu()
    if game_choice == "1":
        next_action = vs_cop_game()
    elif game_choice == "2":
        next_action = cop_vs_cop_game()
    elif game_choice == "3":
        next_action = player_vs_player_game()

    if next_action is None:
        break

agradecimento()