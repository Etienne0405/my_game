# ----------------------------
# THE CLOCK
# ----------------------------

from utils.typewriter import typewriter
import systems.health as health_system
from systems.inventory import inventory
from systems.time_system import change_time
from systems.ghost_encounter import try_spawn_ghost
from systems.candle_gasoline import try_initiate_cangas

import pygame
import os

pygame.mixer.init()
lopen_path = os.path.join("music", "overall", "lopen.wav")

def clock():
    typewriter("You walk towards the clock, it is an old pendulum clock and you hear the ticking now that you are closer.\n")

    while True:
        menu = (
            "What will you do?\n\n"
            "1 - Check your leg, see if it's okay.\n"
            "2 - Check inventory\n"
            "3 - Change the time.\n"
            "4 - Go back.\n"
            "> \n"
        )

        user_selection = input(menu)

        if user_selection == "1":
            health_system.leg_health()
        elif user_selection == "2":
            if inventory:
                typewriter(f"Inventory: {', '.join(inventory)}")
            else:
                typewriter("Your inventory is empty")
        elif user_selection == "3":
            try_spawn_ghost()
            try_initiate_cangas()
            change_time()
        elif user_selection == "4":
            try_spawn_ghost()
            try_initiate_cangas()
            sound = pygame.mixer.Sound(lopen_path)
            sound.play()
            break
        else:
            typewriter("Error, try to type the number associated with the option!\n")
