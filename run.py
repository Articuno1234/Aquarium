import sys
import os
import random
import time
fish = False
IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"
INTERACTIVE_MODE = not len(sys.argv) > 1  # CLI flags = non-interactive

def wait():
    if INTERACTIVE_MODE:
        input("Press enter to continue.")
        
def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")
        
def user_choice():
    return input("> ").lower().strip()
  
  
def menu():
  clear_screen()
  print("-=-=-=-=-=-=-=-=-=-=-=-=-\n"
        "        Aquarium         \n"
        "       {}                \n"
        "-=-=-=-=-=-=-=-=-=-=-=-=-\n".format(random.choice(moto)))
  print("1. Start")
  print("2. Credits")
  print("0. Exit")
  choice = user_choice()
  if choice == "1":
    game()
  if choice == "2":
    credits()
  if choice == "0":
    print("Exiting with code 0")
    time.sleep(2)
    sys.exit(1)
def credits():
  print("Project Leaders\n"
        "DRAGONBLOOD830\n"
        "Developers\n"
        "Articuno1234\n")
  wait()
  game()
def game():
  print("==============================================\n"
        "                                              \n"
        "                                              \n"
        "                                              \n"
        "                                              \n"
        "                                              \n"
        "                                              \n"
        "                                              \n"
        "                                              \n"
        "==============================================\n"
        "  Shop  |  Menu  |                            \n"
        "==============================================\n")
  choice = user_choice()
  if choice == "shop":
    shop()
  if choice == "menu":
    menu()
def shop():
  print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"
        "Shop\n"
        "\n"
        "\n"
        "Fish\n"
        "$Free")
  choice = user_choice()
  if choice == "fish":
    fish = True
    print("Would you like to buy fish (i know you would anyway :))")
    wait()
