from . import codex
from . import journal
from utils.clear_terminal import clear

def menu_screen():
    clear()
    print("Main Menu")
    print(f"{"=" * len("Main Menu")}")

    while True:
        print("Which functionality do you wish to access? | [1] Codex | [2] Journal | [3] Quit")
        user_input = input(">>> ")
        
        if user_input.lower() == "3":
            print("Logging you out...")
            break

        if user_input == "1":
            codex.codex_screen()
        elif user_input == "2":
            journal.journal_screen()
        else:
            print("Invalid Option. Try again. [Codex | Journal | Quit]")
