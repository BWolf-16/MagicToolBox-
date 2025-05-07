import subprocess
import shutil
import os

ADB_PATH = shutil.which("adb") or "adb"  # fallback if in PATH

def is_adb_installed():
    try:
        result = subprocess.run([ADB_PATH, "version"], capture_output=True, text=True)
        return "Android Debug Bridge" in result.stdout
    except Exception:
        return False

def list_devices():
    try:
        result = subprocess.run([ADB_PATH, "devices"], capture_output=True, text=True)
        lines = result.stdout.strip().splitlines()[1:]  # Skip header
        return [line.split()[0] for line in lines if "device" in line]
    except Exception:
        return []

def install_apk(apk_path):
    try:
        result = subprocess.run([ADB_PATH, "install", "-r", apk_path], capture_output=True, text=True)
        return "Success" in result.stdout
    except Exception as e:
        print(f"Failed to install APK: {e}")
        return False

def get_device_info(device_id=None):
    args = [ADB_PATH]
    if device_id:
        args += ["-s", device_id]
    args += ["shell", "getprop"]
    try:
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error: {e}"
