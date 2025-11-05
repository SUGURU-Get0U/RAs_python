import time
from functions import Show_Cat 

is_string = False

if __name__ == "__main__":
  # Welcome message!
  print("Welcome to Rock Paper Scissors")

  time.sleep(2)

  print("loading game .....")
  time.sleep(3)

  # first lets start by getting the user input to start the game!
  while is_string == False: # While loop to check if the value is a string!
    try:
      start_game = input("Do you wish to start the game? [y]/[n]")
      is_string = True # ends the loop
    except ValueError: # if value is not a string, then gets the input again
      print("por favor digite [y] ou [n]!")
      start_game = input("Do you wish to start the game? [y]/[n]")

  if start_game == "y":
    print("Iniciando o Jogo... 🚀")
    time.sleep(1)
    print("Select the game mode:")
    Show_Cat()


