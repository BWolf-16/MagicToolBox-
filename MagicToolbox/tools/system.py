import platform
import psutil
import os
import subprocess
import shutil

def get_system_info():
    return {
        "OS": platform.system(),
        "Version": platform.version(),
        "Release": platform.release(),
        "Machine": platform.machine(),
        "CPU": platform.processor(),
        "RAM (GB)": round(psutil.virtual_memory().total / (1024 ** 3), 2),
        "Uptime (min)": round(psutil.boot_time() / 60, 2)
    }

def restart_computer():
    if platform.system() == "Windows":
        subprocess.run(["shutdown", "/r", "/t", "0"])
    elif platform.system() == "Linux":
        subprocess.run(["sudo", "reboot"])

def shutdown_computer():
    if platform.system() == "Windows":
        subprocess.run(["shutdown", "/s", "/t", "0"])
    elif platform.system() == "Linux":
        subprocess.run(["sudo", "shutdown", "now"])

def clean_temp_files():
    if platform.system() == "Windows":
        temp_dir = os.getenv("TEMP")
        if temp_dir and os.path.exists(temp_dir):
            for root, dirs, files in os.walk(temp_dir):
                for name in files:
                    try:
                        os.remove(os.path.join(root, name))
                    except Exception:
                        pass
    elif platform.system() == "Linux":
        subprocess.run(["rm", "-rf", "/tmp/*"])

def debloat():
    if platform.system() == "Windows":
        apps_to_remove = [
            "Microsoft.XboxGameOverlay", "Microsoft.Xbox.TCUI",
            "Microsoft.People", "Microsoft.SkypeApp",
            "Microsoft.ZuneMusic", "Microsoft.ZuneVideo"
        ]
        for app in apps_to_remove:
            subprocess.run(["powershell", "-Command", f"Get-AppxPackage *{app}* | Remove-AppxPackage"])
