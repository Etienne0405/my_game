# Global inventory
from utils.typewriter import typewriter
import pygame
import os

inventory = []

def inventory_check():
    # Initialize audio (safe to call multiple times)
    pygame.mixer.init()
    sound_path = os.path.join("music", "overall", "inventory_check.mp3")
    sound = pygame.mixer.Sound(sound_path)
    sound.play()   # play once

    if inventory:
        typewriter(f"Inventory: {', '.join(inventory)}")
    else:
        typewriter("Your inventory is empty.\n")

