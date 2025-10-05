import tkinter as tk
from menu_window import MenuWindow

class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.titlte = "Codex - Login"
        self.master.geometry("400x250")
        self.master.configure(bg="#101820")

        self.title_label = tk.Label(
            master,
            text="Welcome to Codex",
            font=("Helvetica", 18, "bold"),
            fg="#FEE715",
            bg="#101820"
        )
        self.title_label.pack(pady=40)

        self.login_button = tk.Button(
            master,
            text="Login",
            font=("Helvetica", 14),
            bg="#FEE715",
            fg="#101820",
            width=12,
            height=1,
            command=self.login
        )
        self.login_button.pack(pady=20)

    def login(self):
        self.master.destroy()
        self.open_menu()

    def open_menu(self):
        new_root = tk.Tk()
        MenuWindow(new_root)
        new_root.mainloop()
