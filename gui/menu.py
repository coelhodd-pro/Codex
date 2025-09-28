from . import codex
from . import journal

def menu_screen():
    while True:
        try:
            user_input = input("Which functionality do you wish to access[Codex or Journal (type 'Quit' to quit)]? ")
        except ValueError:
            print("Provide a valid option: Codex | Journal | ")
            continue

        if user_input.lower() == "quit":
            print("Logging you out...")
            break

        if user_input.lower() == "codex":
            codex.codex_screen()
        elif user_input.lower() == "journal":
            journal.journal_screen()
        else:
            print("Invalid Option. Try again.")
