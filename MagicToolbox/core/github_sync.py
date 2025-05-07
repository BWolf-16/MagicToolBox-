import requests
import json
import os

MANIFEST_PATH = os.path.join(os.path.dirname(__file__), '..', 'apps', 'manifest.json')

# You can point this to your raw GitHub file
GITHUB_MANIFEST_URL = "https://raw.githubusercontent.com/BWolf-16/MagicToolBox-/main/MagicToolbox/apps/manifest.json"

def fetch_remote_manifest():
    try:
        response = requests.get(GITHUB_MANIFEST_URL, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"[GitHub Sync] Failed to fetch manifest: {e}")
        return None

def update_local_manifest(remote_data):
    try:
        with open(MANIFEST_PATH, "w") as f:
            json.dump(remote_data, f, indent=4)
        return True
    except Exception as e:
        print(f"[GitHub Sync] Failed to save manifest: {e}")
        return False

def sync_manifest():
    remote = fetch_remote_manifest()
    if remote:
        return update_local_manifest(remote)
    return False
