from utils.typewriter import typewriter

import systems.game_state as gs
import systems.health as health_system
from systems.inventory import inventory_check
from systems.ghost_encounter import try_spawn_ghost
from systems.candle_gasoline import try_initiate_cangas

import time
import pygame
import os

# --- MIDNIGHT acrostic variations for the lion dialogue ---
MIDNIGHT_DIALOGUE = [
    # M
    '"Mischief, if only just a little, is all what was needed for him to fall into the deep depths. Was he fated to remain there in solitude, carrying an emptiness that no echo could answer?"',
    # I
    '"In the moment he committed his crime, he recognized the fall into the depths. Was he fated to remain there in solitude, carrying an emptiness that no echo could answer?"',
    # D
    '"Darkness filled his life, when he fell into the depths, was he fated to remain there in solitude, carrying an emptiness that no echo could answer?"',
    # N
    '"Now, he is forever trapped in the depths. The moment he fell was the last moment he recognized joy. Is he fated to remain there in solitude, carrying an emptiness that no echo can answer?"',
    # I
    '"Inside the depths he fell, where no one could here him, was he fated to remain there in solitude, carrying an emptiness that no echo could answer?"',
    # G
    '"Grimly he looked. The boundary he surpassed let him fall into the depths. Was he fated to remain there in solitude, carrying an emptiness that no echo could answer?"',
    # H
    '"Haunting sounds he heared in the depths, when he fell. Was he fated to remain there in solitude, carrying an emptiness that no echo could answer?"',
    # T
    '"Trembling grounds below his feet, deep inside the depths where he fell. Was he fated to remain there in solitude, carrying an emptiness that no echo could answer?"'
]

pygame.mixer.init()
lopen_path = os.path.join("music", "overall", "lopen.wav")

def lionstatue(gs):  # pass in the global state object
    # Display entrance line
    typewriter("As you walk to the south-west side of the room, you come before a large lion head.")
    time.sleep(1)

    # Determine which MIDNIGHT line to display
    visit_count = gs.room_visits
    dialogue_line = MIDNIGHT_DIALOGUE[visit_count % len(MIDNIGHT_DIALOGUE)]

    # Room interaction loop
    while True:
        menu = (
            "What will you do?\n\n"
            "1 - Check your leg, see if it's okay.\n"
            "2 - Check inventory.\n"
            "3 - Interact with the lion.\n"
            "4 - Go back.\n"
            "> \n"
        )

        user_selection = input(menu)

        if user_selection == "1":
            health_system.leg_health()
        elif user_selection == "2":
            inventory_check()
        elif user_selection == "3":
            typewriter("The lion moves its mouth slowly, and speaks to you in a vague low voice.")
            time.sleep(1)
            typewriter(dialogue_line)
            time.sleep(1)
            typewriter('"Or would he one day find the light, drawn by courage or by chance, and in that company turn his silent world into one rich with colour and life?"')
            time.sleep(1)
            typewriter("The lion closes its mouth.")
            # Increment visit counter
            gs.room_visits += 1
        elif user_selection == "4":
            try_spawn_ghost()
            try_initiate_cangas()
            sound = pygame.mixer.Sound(lopen_path)
            sound.play()
            break
        else:
            typewriter("\nError, try to type the number associated with the option!\n")
