# 🧰 Magic Toolbox

**Magic Toolbox** is a modern, modular desktop tool built with Python and CustomTkinter.  
It brings together system tools, Android utilities, app management, and auto-updating capabilities — all wrapped in a demon-cat-themed GUI. 🐾

---

## ✨ Features

- 🧠 **App Manager**
  - One-click install/update of common software
  - `wget`-based downloads with silent installers
  - Per-app auto-update toggle
  - "Update All" feature

- 📱 **Android Toolkit**
  - ADB device detection
  - APK installer
  - Emulator setup ready (LDPlayer, BlueStacks)

- 🖥️ **System Tools**
  - System info display
  - Restart / shutdown / temp cleanup
  - Bloatware remover (Windows)

- 💻 **Developer Zone**
  - Git log viewer
  - Project build runner
  - VSCode launcher

- 🐾 **Demon-Themed Splash Screen**
  - Optional ASCII intro with "magic mode"
  - Dark mode UI with tabbed layout

---

## 🛠️ Requirements

- Python 3.10+
- `customtkinter`, `psutil`, `requests`, `Pillow`

```bash
pip install customtkinter psutil requests pillow
