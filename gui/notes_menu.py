from utils.clear_terminal import clear
from storage.notes_db import *

def notes_menu(context):
    clear()
    print(f"{context.capitalize()} Menu")
    print("=" * len(f"{context.capitalize()} Menu"))

    while True: 
        print("""
            Controls:
            [1] - Show notes on database
            [2] - Show specific note
            [3] - Write new note
            [4] - Edit an exising note
            [5] - Go back to Main Menu
        """)
        
        user_input = input(">>> ")
                
        if user_input == "1":
            show(context)
        elif user_input == "2":
            read(context)
        elif user_input == "3":
            write(context)
        elif user_input == "4":
            edit(context)
        elif user_input == "5":
            break
        else:
            print("Invalid option. Try again.")

