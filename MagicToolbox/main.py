from gui.splash import run_splash
from gui.main_ui import run_ui, show_apps
from core.config import load_config
from core.github_sync import sync_manifest

if __name__ == '__main__':
    config = load_config()

    # Optional: auto-fetch updated manifest from GitHub on startup
    if config.get("auto_sync_manifest", True):
        print("[Magic Toolbox] Syncing manifest from GitHub...")
        sync_manifest()

    # Show demon splash if enabled
    if config.get("magic_mode", True):
        run_splash(callback=run_ui)
    else:
        run_ui()

    # After sync, call show_apps to refresh the app list
    app_frame = run_ui()  # Get the frame after UI is loaded
    show_apps(app_frame)  # Pass the main frame to show_apps
