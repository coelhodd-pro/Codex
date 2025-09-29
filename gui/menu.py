from . import codex
from . import journal
from utils.clear_terminal import clear

def menu_screen():
    clear()
    print("Main Menu")
    print(f"{"=" * len("Main Menu")}")

    while True:
        user_input = input("Which functionality do you wish to access[Codex or Journal (type 'Quit' to quit)]? ")
        
        if user_input.lower() == "quit":
            print("Logging you out...")
            break

        if user_input.lower() == "codex":
            codex.codex_screen()
        elif user_input.lower() == "journal":
            journal.journal_screen()
        else:
            print("Invalid Option. Try again. [Codex | Journal | Quit]")
