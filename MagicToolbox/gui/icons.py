import os
from PIL import Image
import customtkinter as ctk

ICON_PATH = os.path.join(os.path.dirname(__file__), '..', 'assets', 'icons')

def load_icon(name, size=(24, 24)):
    path = os.path.join(ICON_PATH, name)
    if os.path.exists(path):
        return ctk.CTkImage(light_image=Image.open(path), size=size)
    else:
        print(f"Icon not found: {name}")
        return None

from gui.icons import load_icon
gear_icon = load_icon("gear.png")

