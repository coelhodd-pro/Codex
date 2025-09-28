from utils.clear_terminal import clear

def codex_screen():
    clear()
    print("Codex Menu")
    print(f"{"=" * len("Codex Menu")}")
    while True:
        print(f"Notes in database: {0}")

        try:
            user_input = input("Do you wish to write a new note[y | n]? ")
        except ValueError:
            print("Provide a valid response: y(yes) | n(no)")
            continue

        if user_input.lower() == "y":
            print("You just wrote a new note!")
        else:
            break
