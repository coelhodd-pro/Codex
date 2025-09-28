from utils.clear_terminal import clear
from storage.journal_db import *

def journal_screen():
    clear()
    print("Journal Menu")
    print(f"{"=" * len("Journal Menu")}")

    while True:
        print("""
            Controls:
            [1] - Show notes on database
            [2] - Write new note
            [3] - Edit an exising note
            [4] - Go back to Main Menu
        """)
        
        try:
            user_input = input(">>> ")
        except ValueError:
            print("Invalid option. Try again.")
            continue
        
        if user_input == "1":
            read()
        elif user_input == "2":
            write()
        elif user_input == "3":
            edit()
        elif user_input == "4":
            break
        else:
            print("Invalid option. Try again.")

