import json
import os
import subprocess

MANIFEST_PATH = os.path.join(os.path.dirname(__file__), '..', 'apps', 'manifest.json')
DOWNLOAD_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'downloads')
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# --- Loader functions ---

def load_apps_grouped():
    with open(MANIFEST_PATH, 'r') as f:
        data = json.load(f)
        return data.get("apps", {})

def load_apps_flat():
    grouped = load_apps_grouped()
    flat = []
    for group in grouped.values():
        flat.extend(group)
    return flat

# --- Installer logic ---

def download_app(app):
    url = app.get("url")
    filename = url.split("/")[-1].split("?")[0]  # remove query params
    filepath = os.path.join(DOWNLOAD_DIR, filename)

    try:
        print(f"[Download] {app['name']} from {url}")
        subprocess.run(["wget", "-O", filepath, url], check=True)
        return filepath
    except subprocess.CalledProcessError:
        print(f"[ERROR] Failed to download {app['name']}")
        return None

def install_app(app):
    filepath = download_app(app)
    if not filepath:
        return False

    install_args = app.get("install_args", "/S")

    try:
        print(f"[Install] Running installer for {app['name']}")
        subprocess.run([filepath] + install_args.split(), check=True)
        return True
    except subprocess.CalledProcessError:
        print(f"[ERROR] Failed to install {app['name']}")
        return False

# --- Basic detection (optional) ---

def is_installed(app):
    filename = app.get("url").split("/")[-1].split("?")[0]
    filepath = os.path.join(DOWNLOAD_DIR, filename)
    return os.path.exists(filepath)
