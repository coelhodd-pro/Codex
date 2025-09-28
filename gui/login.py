from . import menu

def login_screen():
    try:
        user_input = input("Login[y | n]: ")
    except ValueError:
        print("Provide a valid option(y: yes | n: no)")

    if user_input.lower() == "y":
        menu.menu_screen()
    else:
        return False
