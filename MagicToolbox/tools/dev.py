import subprocess
import os

def run_git_log(path="."):
    try:
        result = subprocess.run(["git", "-C", path, "log", "--oneline"], capture_output=True, text=True)
        return result.stdout.strip().splitlines()
    except Exception as e:
        return [f"Error: {e}"]

def build_project(build_cmd="make", path="."):
    try:
        result = subprocess.run(build_cmd, cwd=path, shell=True, capture_output=True, text=True)
        return result.stdout.strip() + "\n" + result.stderr.strip()
    except Exception as e:
        return f"Build failed: {e}"

def open_in_vscode(path="."):
    try:
        subprocess.run(["code", path])
        return True
    except Exception as e:
        print(f"VSCode not found or failed to open: {e}")
        return False
