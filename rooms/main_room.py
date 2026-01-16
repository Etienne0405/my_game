from utils.typewriter import typewriter

from rooms.storage_room import storage_door
from rooms.candle_room import candle
from rooms.lionhead_room import lionstatue
from rooms.enddoor_room import before_enddoor
from rooms.hallway_room import hallway

import systems.health as health_system
from systems.inventory import inventory_check, inventory
from systems.ghost_encounter import try_spawn_ghost
from systems.candle_gasoline import try_initiate_cangas
import systems.game_state as gs
import systems.music as music

import time
import pygame
import os

pygame.mixer.init()
lopen_path = os.path.join("music", "overall", "lopen.wav")

def main_room():
    music.play_music("music/theme_song.wav")
    typewriter("""You wake up, your eyes are still heavy, and you feel a sharp pain in your leg.
You find yourself on a hard cold floor soaked in a strong smelling liquid. It's almost completely dark.
In the distance you see a couple of dimly lit candles standing on an antique table, next to it, on the wall, is a painting of a man on a dark empty road.
Behind you, to the left, a hallway filled with light.
You can't see more details on the painting.\n""")
    time.sleep(1)
    typewriter("You also see a door to the left.\n")

    while True:
        menu = (
            "What will you do?\n\n"
            "1 - Check your leg, see if it's okay.\n"
            "2 - Check inventory.\n"
            "3 - Walk towards the candles.\n"
            "4 - Walk towards the door.\n"
            "5 - Walk towards the hallway.\n"
        )

        if "candle" in inventory or "flashlight" in inventory:
            menu += "6 - Explore the room to the south-west.\n"
            menu += "7 - Explore the room to the south-east.\n"

        menu += "> \n"

        user_selection = input(menu)

        if user_selection == "1":
            health_system.leg_health()
        elif user_selection == "2":
            inventory_check()
        elif user_selection == "3":  # move typewriter
            try_spawn_ghost()
            try_initiate_cangas()
            sound = pygame.mixer.Sound(lopen_path)
            sound.play()
            candle()
        elif user_selection == "4":
            typewriter("You walk towards the door.\n")
            try_spawn_ghost()
            try_initiate_cangas()
            sound = pygame.mixer.Sound(lopen_path)
            sound.play()
            storage_door()
        elif user_selection == "5":
            try_spawn_ghost()
            try_initiate_cangas()
            sound = pygame.mixer.Sound(lopen_path)
            sound.play()
            hallway()
        elif user_selection == "6" and ("candle" in inventory or "flashlight" in inventory):
            try_spawn_ghost()
            try_initiate_cangas()
            sound = pygame.mixer.Sound(lopen_path)
            sound.play()
            lionstatue(gs)
        elif user_selection == "7" and ("candle" in inventory or "flashlight" in inventory):
            try_spawn_ghost()
            try_initiate_cangas()
            sound = pygame.mixer.Sound(lopen_path)
            sound.play()
            before_enddoor()

        else:
            typewriter("\nError, try to type the number associated with the option!\n")
