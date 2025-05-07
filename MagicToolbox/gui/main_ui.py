import customtkinter as ctk
from tkinter import ttk
from tools import apps, android, system, dev
from core import config as cfg
from core import updater

def run_ui():
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("Magic Toolbox 🐾")
    app.geometry("900x600")

    # Sidebar
    sidebar = ctk.CTkFrame(app, width=180)
    sidebar.pack(side="left", fill="y", padx=10, pady=10)

    main_frame = ctk.CTkFrame(app)
    main_frame.pack(side="left", expand=True, fill="both", padx=10, pady=10)

    title = ctk.CTkLabel(main_frame, text="Welcome to Magic Toolbox, Master 🖤", font=("Arial", 20))
    title.pack(pady=20)

    tabs = {
        "Apps": lambda: show_apps(main_frame),
        "Android": lambda: show_android(main_frame),
        "System": lambda: show_system(main_frame),
        "Dev": lambda: show_dev(main_frame),
    }

    for name, func in tabs.items():
        btn = ctk.CTkButton(sidebar, text=name, command=func)
        btn.pack(pady=10, fill="x")

    app.mainloop()

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def show_apps(frame):
    clear_frame(frame)
    manifest = apps.load_apps_grouped()
    ctk.CTkLabel(frame, text="App Manager", font=("Arial", 20)).pack(pady=10)

    def update_all():
        flat_apps = []
        for category_apps in manifest.values():
            flat_apps.extend(category_apps)
        outdated = updater.check_for_updates(flat_apps)
        updater.update_apps(outdated)

    ctk.CTkButton(frame, text="🔁 Update All", command=update_all).pack(pady=10)

    for category, app_list in manifest.items():
        category_label = ctk.CTkLabel(frame, text=f"📦 {category}", font=("Arial", 16, "bold"))
        category_label.pack(pady=(20, 5))

        for app_data in app_list:
            row = ctk.CTkFrame(frame)
            row.pack(fill="x", pady=4, padx=20)

            name = app_data.get("name", "Unknown")
            label = ctk.CTkLabel(row, text=name)
            label.pack(side="left", padx=5)

            install_btn = ctk.CTkButton(row, text="Install", width=80,
                                        command=lambda a=app_data: apps.install_app(a))
            install_btn.pack(side="right", padx=5)

            def toggle(val, app_name=name):
                cfg.set_auto_update(app_name, val)

            auto_update = cfg.get_auto_update(name)
            togglebox = ctk.CTkCheckBox(
                row,
                text="Auto-update",
                command=lambda name=name: toggle(togglebox.get() == 1, name)
            )
            togglebox.pack(side="right", padx=10)
            togglebox.select() if auto_update else togglebox.deselect()

def show_android(frame):
    clear_frame(frame)
    ctk.CTkLabel(frame, text="Android Tools", font=("Arial", 18)).pack(pady=10)

    if not android.is_adb_installed():
        ctk.CTkLabel(frame, text="ADB not found!").pack(pady=10)
        return

    devices = android.list_devices()
    ctk.CTkLabel(frame, text=f"Devices: {', '.join(devices) if devices else 'None'}").pack(pady=10)

def show_system(frame):
    clear_frame(frame)
    ctk.CTkLabel(frame, text="System Info", font=("Arial", 18)).pack(pady=10)

    info = system.get_system_info()
    for k, v in info.items():
        ctk.CTkLabel(frame, text=f"{k}: {v}").pack(anchor="w", padx=20)

def show_dev(frame):
    clear_frame(frame)
    ctk.CTkLabel(frame, text="Developer Zone", font=("Arial", 18)).pack(pady=10)

    logs = dev.run_git_log()
    box = ctk.CTkTextbox(frame, height=200, width=600)
    box.insert("0.0", "\n".join(logs))
    box.pack(pady=10)
