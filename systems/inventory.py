# Global inventory
from utils.typewriter import typewriter
from utils.resource_path import resource_path
import pygame
import os

inventory = []

def inventory_check():
    # Initialize audio (safe to call multiple times)
    pygame.mixer.init()
    sound_path = resource_path(os.path.join("music", "overall", "inventory_check.mp3"))
    sound = pygame.mixer.Sound(sound_path)
    sound.play()   # play once

    if inventory:
        typewriter(f"Inventory: {', '.join(inventory)}")
    else:
        typewriter("Your inventory is empty.\n")

