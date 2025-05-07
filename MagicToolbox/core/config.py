import json
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'config.json')

# Default config
default_config = {
    "auto_update": {},         # per-app toggles
    "theme": "dark",           # future use
    "magic_mode": True,        # controls splash screen
    "auto_sync_manifest": True  # enable GitHub manifest pull on startup
}

def load_config():
    if not os.path.exists(CONFIG_PATH):
        save_config(default_config)
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=4)

# --- Convenience functions ---

def get_auto_update(app_name):
    config = load_config()
    return config.get("auto_update", {}).get(app_name, False)

def set_auto_update(app_name, enabled):
    config = load_config()
    config.setdefault("auto_update", {})[app_name] = enabled
    save_config(config)

def toggle_magic_mode():
    config = load_config()
    config["magic_mode"] = not config.get("magic_mode", True)
    save_config(config)

def set_auto_sync(enabled: bool):
    config = load_config()
    config["auto_sync_manifest"] = enabled
    save_config(config)
