from utils.typewriter import typewriter

import systems.health as health_system
from systems.inventory import inventory_check, inventory
from systems.candle_gasoline import try_initiate_cangas

import time
import os
import pygame
from utils.resource_path import resource_path

lopen_path = resource_path(os.path.join("music", "overall", "lopen.wav"))

def basement():
    typewriter("You carefully walk down the creaky stairs into the basement. The air is damp and musty.\n")
    time.sleep(1)
    typewriter("As you step further in, you see a room that is best described as someone's private study. In the center of the room, a couch is placed in front of a tv.\n")
    typewriter("The floor is riddled with old scrambled up pieces of paper. The walls are lined with old bookshelves filled with dusty tomes.\n")
    typewriter("On the side of the couch, there is a tv-remote. A note is taped on the remote that reads: 'Inglorious Basterds'.\n")
    time.sleep(1)

    while True:
        menu = (
            "What will you do?\n\n"
            "1 - Check inventory.\n"
            "2 - Check your leg, see if it's okay.\n"
            "3 - Turn on TV.\n"
            "4 - Check the bookshelves.\n"
            "5 - Go back upstairs.\n"
            "> \n"
        )
        user_selection = input(menu)

        if user_selection == "1":
            inventory_check()
        elif user_selection == "2":
            health_system.leg_health()
        elif user_selection == "3":
            tv()
        elif user_selection == "4":
            bookshelves()
        elif user_selection == "5":
            typewriter("You decide to leave the basement and head back upstairs.\n")
            try_initiate_cangas()
            sound = pygame.mixer.Sound(lopen_path)
            sound.play()
            break
        else:
            typewriter("\nError, try to type the number associated with the option!\n")


def tv():
    typewriter("You pick up the remote and press the power button. The TV flickers to life, displaying a static-filled screen.\n")
    time.sleep(1)
    typewriter("Suddenly, a distorted figure appears on the screen, speaking in a garbled voice.\n")
    time.sleep(1)
    typewriter("'Welcome to my basement' the figure says.'\n")
    time.sleep(1)
    typewriter("The riddle echoes through the room: 'I am a minor being, with major disease. My name is tricky for those with dyslexia. What am I?'\n")

    answer = input("Your answer: ").lower()

    if answer == "emmanuelle mimieux":
        typewriter("The TV screen flickers and then goes black. A hidden compartment opens in the wall, revealing a small key inside.\n")
        typewriter("You take the key and add it to your inventory.\n")
        inventory.append("small_key")
    else:
        typewriter("The figure on the screen shakes its head. 'Incorrect. Try again when you're ready.' The TV goes back to static.\n")

def bookshelves():
    typewriter("You walk over to the bookshelves and start browsing through the dusty old books.\n")
    time.sleep(1)
    typewriter("Most of the books are too old and fragile to read, but a couple of books are readable. They are titles as followed:\n")
    time.sleep(1)
    titles = [
        "Write to Survive",
        "TV distracts young children",
        "To the future",
        "Get Back to Life",
        "UV Light for Dummies",
    ]

    # Use ANSI escape codes to render the first word bold in terminals that support it
    BOLD = "\033[1m"
    RESET = "\033[0m"

    for t in titles:
        parts = t.split(" ", 1)
        first = parts[0]
        rest = (" " + parts[1]) if len(parts) > 1 else ""
        typewriter(f"- '{BOLD}{first}{RESET}{rest}'")
