import tkinter as tk

class MenuWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Codex - Main Menu")
        self.master.geometry("400x300")
        self.master.configure(bg="#101820")

        tk.Label(
            master,
            text="Main Menu",
            font=("Helvetica", 18, "bold"),
            fg="#FEE718",
            bg="#101820"
        ).pack(pady=40)

        tk.Button(
            master,
            text="Exit",
            font=("Helvetica", 12),
            bg="#FEE718",
            fg="#101820",
            command=self.master.destroy
        ).pack(pady=10)
