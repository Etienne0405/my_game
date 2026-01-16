from utils.typewriter import typewriter

import systems.health as health_system
from systems.inventory import inventory_check, inventory
from systems.ghost_encounter import ghost_encounter

import time
import pygame
import os

pygame.mixer.init()
lopen_path = os.path.join("music", "overall", "lopen.wav")

def desk():
    typewriter("You approach the desk and notice it's covered in dust and old newspapers.\n")
    typewriter("Below the desk, you find a chest.")
    typewriter("Next to the newspapers, there is a gramophone with a record on it.\n")
    typewriter("As you sift through the newspapers, you find an article about mysterious disappearances in the house.\n")
    typewriter("One headline catches your eye: 'Mysterious disappearances in abandoned house. Authorities baffled as more people go missing without a trace.'\n")
    typewriter("You flip through the newspaper and see a small article about a man who was once killed in the house. Since then the place has been haunted.\n")

    while True:

        menu = (
            "What will you do?\n\n"
            "1 - Check your leg, see if it's okay.\n"
            "2 - Check inventory.\n"
            "3 - Play the record.\n"
            "4 - Open chest.\n"
            "5 - Go back.\n"
            "> \n"
        )

        user_selection = input(menu)

        if user_selection == "1":
            health_system.leg_health()
        elif user_selection == "2":
            inventory_check()
        elif user_selection == "3":
            typewriter("You carefully place the needle on the record. The gramophone crackles to life, filling the room with eerie music.\n")
            play_gramophone()
        elif user_selection == "4":
            open_chest()
        elif user_selection == "5":
            sound = pygame.mixer.Sound(lopen_path)
            sound.play()
            break
        else:
            typewriter("Error, try to type the number associated with the option!\n")



def play_gramophone():
    # Initialize pygame mixer
    pygame.mixer.init()

    # Path to audio file
    sound_path = os.path.join("music", "gramaphone.wav")

    # Check if file exists
    if not os.path.exists(sound_path):
        typewriter("The gramophone crackles... but there is no record inside.\n")
        return

    # Load and play
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play(-1)   # -1 means loop forever

    typewriter("The gramophone crackles to life...\n")
    typewriter("A distorted melody fills the room.\n")
    typewriter("Type 'stop' to turn it off.\n")

    # Wait for user to stop
    while True:
        cmd = input("> ").lower().strip()
        if cmd == "stop":
            pygame.mixer.music.stop()
            typewriter("The gramophone slowly winds down.\n")
            break

def open_chest():
    typewriter("You open the chest to find there are 3 compartments.")
    typewriter("Someone wrote some information on each compartment:")
    print(r"""
+---------+    +---------+    +---------+
|         |    |         |    |  3%^^*  |
|  WD-40  |    | letter  |    |   -+=-  |
|         |    |         |    |  z-0pr  |
+---------+    +---------+    +---------+

""")
    typewriter("It seems the third one is unreadable.")

compartment_opened = False  # Track if the player opened a compartment

while True:

    menu = (
        "What will you do?\n\n"
        "1 - Open the one with WD-40.\n"
        '2 - Open the one that says "letter".\n'
        "3 - Open the unreadable one.\n"
        "4 - Go back.\n"
        "> \n"
    )

    user_selection = input(menu)

    if user_selection in ["1", "2", "3"]:
        if compartment_opened:
            typewriter("Huh, the compartments are locked now..")
            continue  # skip the rest of the loop
        else:
            compartment_opened = True  # mark that a compartment has been opened

    if user_selection == "1":
        if "wd-40" not in inventory:
            typewriter("Hey there actually was a bottle of WD-40 here!")
            inventory.append("wd-40")
        else:
            typewriter("Hey you shouldn't be able to look twice!")
    elif user_selection == "2":
        typewriter("Inside the compartment is a small folded letter.")
        time.sleep(1)
        typewriter('It reads: "For all non german speakers. There, where the wanderer is not, is happiness!"')
    elif user_selection == "3":
        typewriter("You open the unreadable compartment.")
        ghost_encounter()
    elif user_selection == "4":
        break
    else:
        typewriter("Error, type the number associated with the option!")




  