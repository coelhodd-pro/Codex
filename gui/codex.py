from utils.clear_terminal import clear
from storage.codex_db import *

def codex_screen():
    clear()
    print("Codex Menu")
    print(f"{"=" * len("Codex Menu")}")

    while True: 
        print("""
            Controls:
            [1] - Show notes on database
            [2] - Show specific note
            [3] - Write new note
            [4] - Edit an exising note
            [5] - Go back to Main Menu
        """)
        
        try:
            user_input = input(">>> ")
        except ValueError:
            print("Invalid option. Try again.")
            continue
        
        if user_input == "1":
            show()
        elif user_input == "2":
            read()
        elif user_input == "3":
            write()
        elif user_input == "4":
            edit()
        elif user_input == "5":
            break
        else:
            print("Invalid option. Try again.")

