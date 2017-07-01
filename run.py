try:
   import sys
   import os
   import random
   import time
   import subprocess
except ImportError:
        input("sys, os, random or time import was not found")
fish = False
moto = ["an awesome fish game", "Fishy wishy"]
mfish = ["<()", "()>", " "]
IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"
INTERACTIVE_MODE = not len(sys.argv) > 1  # CLI flags = non-interactive

def is_git_installed():
    try:
        subprocess.call(["git", "--version"], stdout=subprocess.DEVNULL,
                                              stdin =subprocess.DEVNULL,
                                              stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        return False
    else:
        return True



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
  if IS_WINDOWS:
      os.system("start d:\beep.mp3")
  else:
      os.system("start /beep.mp3")
  clear_screen()
  print("Verifying Git installation...")
  has_git = is_git_installed()
  is_git_installation = os.path.isdir(".git")
  if not is_git_installation:
      print("WARNING: Looks like this was not installed with git!\n"
            "Try install again! https://github.com/Articuno1234/Aquarium")
      sys.exit(1)
  if not has_git:
      print("GIT PATH was not found!")
      sys.exit(1)
  else:
      print("This has been installed with git and has git!")
      time.sleep(2)
      clear_screen()
  print("-=-=-=-=-=-=-=-=-=-=-=-=-\n"
        "  {}      Aquarium    {}     \n"
        "       {}                \n"
        "-=-=-=-=-=-=-=-=-=-=-=-=-\n".format(random.choice(mfish), random.choice(mfish), random.choice(moto)))
  print("1. Start")
  print("2. Credits")
  print("3. Changelog")
  print("0. Exit")
  choice = user_choice()
  if choice == "1":
    game()
  if choice == "2":
    credits()
  if choice == "3":
    changelog()
  if choice == "0":
    print("Exiting with code 0")
    time.sleep(2)
    clear_screen()
    sys.exit(1)
def changelog():
  clear_screen()
  print("-=-=-=-Changelog-=-=-=-\n"
        "+\n"
        "-\n")
  wait()
  menu()
def credits():
  clear_screen()
  print("Project Leader(s):\n"
        "DRAGONBLOOD830 (Matthew Lamb)\n"
        "\nDeveloper(s):\n"
        "Articuno1234 (None)\n")
  wait()
  menu()
def game():
  clear_screen()
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
  clear_screen()
  print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"
        "Shop                                | Back <----\n"
        "\n"
        "\n"
        "Fish\n"
        "$Free")
  choice = user_choice()
  if choice == "fish":
    fish = True
    print("Would you like to buy fish (i know you would anyway :))")
    wait()
    print("The item Fish was bought")
    wait()
    shop()
  if choice == "back":
    game()
menu = menu()
print(menu)
