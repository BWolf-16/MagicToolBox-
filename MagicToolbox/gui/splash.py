import customtkinter as ctk


def run_splash(callback=None):
    splash = ctk.CTk()
    splash.title("Magic Toolbox - Loading")
    splash.geometry("500x300")
    splash.resizable(False, False)

    # Demon-themed banner
    banner = """
       ／＞　 フ
      | 　_　_| Demon Cat Console
     ／` ミ＿xノ   Preparing your magic tools...
    /　　　　 |
   /　 ヽ　　 ﾉ   🐾
   │　　|　|　|
／￣|　　 |　|　|
(￣ヽ＿_ヽ_)__)
＼二)
    """

    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")

    label = ctk.CTkLabel(splash, text=banner, font=("Courier New", 16), justify="left")
    label.pack(expand=True, padx=20, pady=20)

    # Close splash after 2 seconds and call the callback (run_ui)
    def on_close():
        splash.destroy()
        if callback:
            callback()  # explicitly calling run_ui()

    # Set a timer for splash screen
    splash.after(2000, on_close)

    splash.mainloop()
