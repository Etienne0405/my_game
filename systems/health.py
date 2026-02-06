import sys
from utils.typewriter import typewriter
from utils.resource_path import resource_path
import time
import pygame
import os

# Global variables
leg_okay = False
health = 100  # start with 100
max_health = 100

def check_death():
    if health <= 0:
        pygame.mixer.init()
        sound_path = resource_path(os.path.join("music", "health", "death.mp3"))
        sound = pygame.mixer.Sound(sound_path)
        sound.play()   # play once    

        typewriter("The pain is no longer tolerable, you feel pain in each and every part of your body.")
        time.sleep(1)
        typewriter("You fall down on your knees, a tear falls down your face. Now that you have given up, you feel a certain pressure lifting off of your body.")
        time.sleep(1)
        typewriter("Now I can rest, you say.")
        time.sleep(1)
        sys.exit("Game Over!")

def leg_health():
    if leg_okay:
        typewriter("Your leg still hurts, but you are able to soldier through.\n")
    else:
        typewriter("""You touch your leg and you feel that it's warm and wet from the blood.
It seems you got stabbed by something. Walking is doable, but jumping or climbing feels impossible.\n""")
        
    # Check current leg health and show a message.
    pygame.mixer.init()
    sound_path = resource_path(os.path.join("music", "health", "check_leg.mp3"))
    sound = pygame.mixer.Sound(sound_path)
    sound.play()   # play once

def fix_leg():
    # Function to fix your leg in the game
    global leg_okay
    leg_okay = True

    pygame.mixer.init()

    # Load ghost voice
    sound_path = resource_path(os.path.join("music", "health", "fix_leg.mp3"))
    sound = pygame.mixer.Sound(sound_path)
    sound.play()   # play once

    typewriter("""You feel much better and moving goes relatively smoothly.
You feel as though you are now able to jump and climb.\n""")
