from gui.splash import run_splash
from gui.main_ui import run_ui
from core.config import load_config
from core.github_sync import sync_manifest

if __name__ == '__main__':
    config = load_config()

    if config.get("auto_sync_manifest", True):
        print("[Magic Toolbox] Syncing manifest from GitHub...")
        sync_manifest()

    if config.get("magic_mode", True):
        run_splash(callback=run_ui)
    else:
        run_ui()
