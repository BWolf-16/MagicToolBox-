import os
import hashlib
import requests
from tools import apps
from core.config import get_auto_update

DOWNLOAD_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'downloads')

def get_remote_hash(url):
    try:
        response = requests.get(url, stream=True, timeout=10)
        hasher = hashlib.md5()
        for chunk in response.iter_content(8192):
            hasher.update(chunk)
        return hasher.hexdigest()
    except Exception as e:
        print(f"Error hashing remote file: {e}")
        return None

def get_local_hash(filepath):
    try:
        hasher = hashlib.md5()
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception:
        return None

def check_for_updates(app_list):
    updates = []
    for app in app_list:
        if not get_auto_update(app["name"]):
            continue

        filename = app["url"].split("/")[-1]
        local_path = os.path.join(DOWNLOAD_DIR, filename)
        if not os.path.exists(local_path):
            updates.append(app)
            continue

        remote_hash = get_remote_hash(app["url"])
        local_hash = get_local_hash(local_path)

        if remote_hash and local_hash and remote_hash != local_hash:
            updates.append(app)

    return updates

def update_apps(update_list):
    for app in update_list:
        print(f"Updating {app['name']}...")
        apps.install_app(app)
