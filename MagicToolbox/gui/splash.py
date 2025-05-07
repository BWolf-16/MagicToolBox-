import customtkinter as ctk
import threading
import time

def run_splash(callback=None):
    splash = ctk.CTk()
    splash.title("Summoning Magic Toolbox...")
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

    label = ctk.CTkLabel(splash, text=banner, font=("Consolas", 14), justify="left")
    label.pack(pady=30)

    def close_after_delay():
        time.sleep(2.5)  # show splash for 2.5 seconds
        splash.destroy()
        if callback:
            callback()

    threading.Thread(target=close_after_delay).start()
    splash.mainloop()
