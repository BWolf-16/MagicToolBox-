import requests
import json
import os

MANIFEST_PATH = os.path.join(os.path.dirname(__file__), '..', 'apps', 'manifest.json')

# You can point this to your raw GitHub file
GITHUB_MANIFEST_URL = "https://raw.githubusercontent.com/BWolf-16/MagicToolBox-/main/MagicToolbox/apps/manifest.json"

def fetch_remote_manifest():
    try:
        response = requests.get(GITHUB_MANIFEST_URL, timeout=10)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx, 5xx)

        # Debug: Check the response status code and content
        print(f"[GitHub Sync] Response Status: {response.status_code}")  # Check the response status code
        print(f"[GitHub Sync] Response Content: {response.text[:500]}")  # Print out first 500 characters of response
        
        return response.json()  # Try to parse JSON if the response is good
    except Exception as e:
        print(f"[GitHub Sync] Failed to fetch manifest: {e}")
        return None

def update_local_manifest(remote_data):
    try:
        with open(MANIFEST_PATH, "w") as f:
            json.dump(remote_data, f, indent=4)
        print("[GitHub Sync] Manifest updated locally.")
        return True
    except Exception as e:
        print(f"[GitHub Sync] Failed to save manifest: {e}")
        return False

def sync_manifest():
    print("[GitHub Sync] Syncing manifest from GitHub...")
    remote = fetch_remote_manifest()
    if remote:
        if update_local_manifest(remote):
            print("[GitHub Sync] Manifest sync completed successfully!")
        else:
            print("[GitHub Sync] Failed to update local manifest.")
    else:
        print("[GitHub Sync] No manifest to sync.")
