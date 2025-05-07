import tkinter as tk
import customtkinter as ctk

def run_ui():
    app = ctk.CTk()
    app.title("Magic Toolbox")
    app.geometry("800x600")
    label = ctk.CTkLabel(app, text="Welcome to Magic Toolbox, Master 🐾")
    label.pack(pady=20)
    app.mainloop()
