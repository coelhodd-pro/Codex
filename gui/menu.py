def menu_screen():
    while True:
        try:
            user_input = input("Which functionality do you wish to access[Codex or Journal]? ")
        except ValueError:
            print("Provide a valid option: Codex | Journal")
            continue

        if user_input.lower() == "codex":
            codex_screen()
        elif user_input.lower() == "journal":
            journal_screen()
        else:
            print("Invalid Option. Try again.")
