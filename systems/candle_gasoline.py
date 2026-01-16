from utils.typewriter import typewriter
import systems.health as health_system
from systems.inventory import inventory

import pygame
import os
import random
import time

pygame.mixer.init()

tripping_sound_path = os.path.join("music", "overall", "tripping.mp3")

def try_initiate_cangas():
    if health_system.leg_okay:
        cangas_chance = 35
    else:
        cangas_chance = 20

    if random.randint(1, cangas_chance) == 1:
        initiate_cangas()

def initiate_cangas():
    typewriter("\nOh no! You trip over some stuff on the ground!")
    sound = pygame.mixer.Sound(tripping_sound_path)
    sound.play()   # play once

    if "candle" in inventory:
        typewriter("Your candle falls on the ground. To your horror, you realize the strong smelling liquid has been gasoline.")
        time.sleep(1)
        flames_path = os.path.join("music", "overall", "fire.mp3")
        sound = pygame.mixer.Sound(flames_path)
        sound.play()   # play once
        typewriter("The room gets filled with flames. You caught fire.")
        health_system.health -= 100
        health_system.check_death()
    else:
        time.sleep(1)
        if "wooden_plank" not in inventory:
            typewriter("Luckily you catch yourself, and you don't get hurt.")
            typewriter("\nHey there was a wooden plank sticking out of the ground.\n")
            inventory.append("wooden_plank")
            typewriter("You pick it up, it might be useful later.\n")
        else:
            typewriter("Luckily you catch yourself, and you don't get hurt.")

