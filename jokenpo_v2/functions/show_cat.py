import time
from calculate_results import game_logic

# game modes
def PvP_Mode(player1, player2, score1=0, score2=0):
  print("Starting **PVP** mode...")
  time.sleep(1)

  player1 = input("Player 1, please type your USERNAME")
  player2 = input("Player 2, please type your USERNAME")

  print("Game Started!")
  time.sleep(0.5)
  player1_op = input(f" {player1} please make a choice: \n [0 - Rock] \n[1- Paper] \n [2- Scissors]")
  print("Fetching choice...")
  time.sleep(1)
  player2_op = input(f"Great now {player2} please make a choice: \n [0 - Rock] \n[1- Paper] \n [2- Scissors]")

  # call the function to calculate the result
  game_logic()


# 3 categories
def Show_Cat():
  text = "Game modes"
  print(f"{text:-20}") # Game modes will be followed by 20 - both on the right and left
  print(f"1- Player vs Player (pvp)")
  print(f"2- Player vs Computer (p vs Cop)")
  print(f"3- Computer vs Computer")


def Choose_Cat():
  Show_Cat()

  option = input("Please choose a category")

  if option == "1" or option == "pvp":
    PvP_Mode()
# Player vs Player

# Player vs Computer
# Computer vs Computer

