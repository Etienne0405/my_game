from utils.typewriter import typewriter

import systems.health as health_system
from systems.inventory import inventory_check, inventory

import pygame
import os

pygame.mixer.init()
lopen_path = os.path.join("music", "overall", "lopen.wav")

def desk():
    typewriter("You approach the desk and notice it's covered in dust and old newspapers.\n")
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
            "4 - Go back.\n"
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

  