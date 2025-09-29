from . import menu

def login_screen():
    while True:
        user_input = input("Login[y | n]: ")
        
        if user_input.lower() == "y":
            menu.menu_screen()
        elif user_input.lower() == "n":
            break
        else:
            print("Provide a valid option: y(es) | n(o).")
