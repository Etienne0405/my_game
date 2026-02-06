from utils.typewriter import typewriter

import systems.health as health_system
from systems.inventory import inventory_check
from systems.time_system import get_current_time

from systems.candle_gasoline import try_initiate_cangas

from puzzles.enddoor_puzzle import end_door
from puzzles.clock_puzzle import clock
from puzzles.desk_puzzle import desk

import os
import pygame
from utils.resource_path import resource_path

pygame.mixer.init()
lopen_path = resource_path(os.path.join("music", "overall", "lopen.wav"))


def before_enddoor():
    typewriter("As you walk to the south-east side of the room you stumble upon a golden door. " \
    "Sadly it's locked.\n" \
    "Before the door lies a white carpet. " \
    "The carpet feels and smells very dirty with the strong smelling liquid on it.\n" \
    "A little further you see a clock hanging on the wall.\n")

    current_time = get_current_time().strftime("%H:%M")
    typewriter(f"\nThe clock reads {current_time}.\n")

    while True:

        menu = (
            "What will you do?\n\n"
            "1 - Check your leg, see if it's okay.\n"
            "2 - Check inventory.\n"
            "3 - Try to open the golden door.\n"
            "4 - Walk towards the clock.\n"
            "5 - Walk towards the desk.\n"
            "6 - Go back.\n"
            "> \n"
        )

        user_selection = input(menu)

        if user_selection == "1":
            health_system.leg_health()
        elif user_selection == "2":
            inventory_check()

        elif user_selection == "3":
            try_initiate_cangas()
            sound = pygame.mixer.Sound(lopen_path)
            sound.play()
            end_door() # in puzzles

        elif user_selection == "4":
            try_initiate_cangas()
            sound = pygame.mixer.Sound(lopen_path)
            sound.play()
            clock() # In puzzles
        elif user_selection == "5":
            try_initiate_cangas()
            sound = pygame.mixer.Sound(lopen_path)
            sound.play()
            desk()

        elif user_selection == "6":
            try_initiate_cangas()
            sound = pygame.mixer.Sound(lopen_path)
            sound.play()
            break

        else:
            typewriter("\nError, try to type the number associated with the option!\n")
