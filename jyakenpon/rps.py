
import random
from tkinter import *

# Variaveis para o jogo
calls = ["pedra", "papel", "tesoura"]

turn = 1
# UI (user interface)
# Cria uma janela
tela = Tk()
tela.geometry("200x200")
tela.title("Pedra Papel e Tesoura")
Game_title = Label(tela, text="Pedra Papel e Tesoura")
Game_title.grid(column=0, row=0)

game_mode = Label(tela, text= "")
# Cria a resposta ao botão play, o texto será alterado pela funcao game_menu

def start_game():
    global turn, game_mode
    turn = 1
    # Modo de jogo Player vs Cop
    if game_mode["text"] == "1":

        while game_mode["text"] == "1":
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
            verifica(p1, cop1)
            turn += 1  # Passa para proxima rodada
            if turn == 5:  # Ao final de 5 rodadas
                res = input("quer recomeçar em outro modo?? [s/n]: ")
                if res.lower() == ['s','sim']:
                    game_menu()

                else:
                    turn = 1
            else:
                continue
    elif game_mode["text"] == "2":
    # Modo de Jogo Cop vs Cop
        while game_mode["text"]== "2":
            print(f"Rodada {turn}")  # Mostra a rodada atual
            b1 = random.choice(calls)  # Jogada do bot1
            b2 = random.choice(calls)  # Jogada do bot2
            print(f"A escolha do bot 1 foi: {b1}\n")  # Mostra a escolha do bot1
            print(f"A escolha do bot 2 foi: {b2}\n")  # Mostra a escolha do bot2
            verifica(b1, b2)  # Chama a funcao para ver quem ganhou
            turn += 1  # Passa para proxima rodada
            if turn == 5:  # Ao final de 5 rodadas
                res = input("quer recomeçar em outro modo?? [s/n]: ")
                if res.lower() == ["s","sim"]:
                    game_menu()

                else:
                    turn = 1
            else:
                continue
    else:
    # Modo de jogo Player vs Player
        while game_mode['text'] == "3":
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
                if res.lower() == ["s","sim"]:
                    game_menu()

                else:
                    turn = 1
            else:
                continue
def select_mode(mode):
    global modo_jogo
    modo_de_jogo = mode
    game_mode.config(text= f"O modo de jogo selecionado foi: {mode}")
    # seleciona o modo de jogo
    start_game() #comeca o jogo
    #tira os botoes de modo de jogo depois da selecao
    for widget in tela.winfo_children():
        if isinstance(widget, Button) and widget != Play_button:
            widget.destroy()
    # "Para cada elemento dentro da tela,
    # se esse elemento for um botão e não for o botão 'Play', então destrua esse elemento."

# Funcao cria botoes para cada modo de jogo
def game_menu():
    menu_options = {
        "1": "Versus Computador",
        "2": "Computador vs Computador",
        "3": "Player vs Player"
    }
    linha = 2
    for key, value in menu_options.items():
        button = Button(tela, text=value, command=lambda m=key: select_mode(m))
        button.grid(column=0, row=linha,padx=10,pady=10)
        linha += 1
    Play_button.grid_forget() # Remove o "Play apos o clique"

# Cria um botão que executa a funcao game_menu ao ser clicado
Play_button = Button(tela, text="Play", command=game_menu)
Play_button.grid(column=0, row=2)
Play_button.place(relx=0.5,rely=0.5,anchor=CENTER)



# Deixa a janela rodando para sempre ate alguém fechar
tela.mainloop()



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






        # sair do loop while

#

