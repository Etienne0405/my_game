from utils.typewriter import typewriter

import systems.health as health_system
from systems.inventory import inventory_check, inventory
import systems.game_state as gs
from systems.candle_gasoline import try_initiate_cangas
from systems.chess import play_chess

from puzzles.painting_puzzle import painting

from rooms.painting_room import enter_painting_room

import time
import random
import os
import pygame
from utils.resource_path import resource_path

pygame.mixer.init()
lopen_path = resource_path(os.path.join("music", "overall", "lopen.wav"))


def candle():            
    typewriter("""You feel sick and tired, but you still try to walk towards the candles.
You try to ignore the pain in your leg. Slowly you make your way towards the candles and you feel a certain fear upon you.\n""")
    time.sleep(1)
    typewriter("""You feel the warmth of the candles as you stand next to them.
Now that you are closer, you see that the table contains more than just candles.\n""")

    while True:
        # Dynamically change menu option 5 based on whether the painting room is unlocked
        painting_option_text = (
            "Enter painting room" if gs.rooms_unlocked["painting_room"] else "Check the painting"
        )


        menu = (
            "What will you do?\n\n"
            "1 - Check your leg, see if it's okay.\n"
            "2 - Check inventory.\n"
            "3 - Check the table.\n"
            "4 - Pick up one of the candles.\n"
            f"5 - {painting_option_text}.\n"
            "6 - Go back.\n"
            "> "
        )

        user_selection = input(menu).strip().upper()

        if user_selection == "H":
            if "flashlight" not in inventory:
                inventory.append("flashlight")
                typewriter("\nYou found the hidden flashlight! You can use it now.\n")
            else:
                typewriter("\nYou already have a flashlight.\n")
            continue

        if user_selection == "1":
            health_system.leg_health()
        elif user_selection == "2":
            inventory_check()

        elif user_selection == "3":
            typewriter("""\nOn the table before you lays a deck of cards, a chessboard, a box with a button, and a frame with a picture of a nice couple.
Looking at the couple, you feel a certain jealousy. They are smiling......\n""")
            time.sleep(1)
            typewriter("Whilst you are not.\n")
            option_menu_candletable()

        elif user_selection == "4":
            if "candle" not in inventory:
                inventory.append("candle")
                typewriter("You picked up a candle! You can now use it.\n")
            else:
                typewriter("It seems you already have a candle..\n")

        elif user_selection == "5":
            if gs.rooms_unlocked["painting_room"] and health_system.leg_okay and not gs.rooms_unlocked["hidden_room"]:
                enter_painting_room()
            elif gs.rooms_unlocked["painting_room"] and not health_system.leg_okay and not gs.rooms_unlocked["hidden_room"]:
                typewriter("Your leg is too hurt to climb into the space behind the painting.\n")
            elif gs.rooms_unlocked["painting_room"] and gs.rooms_unlocked["hidden_room"]:
                typewriter("You don't dare go in the oven again..\n")
            elif "candle" in inventory or "flashlight" in inventory:
                typewriter("With your light, you can see the details of the painting.\n")
                try_initiate_cangas()
                painting()
            else:
                typewriter("It's too dark to see the painting clearly, maybe check on it another time.\n")

        elif user_selection == "6":
            try_initiate_cangas()
            sound = pygame.mixer.Sound(lopen_path)
            sound.play()
            break

        else:
            typewriter("\nError, try to type the number associated with the option!\n")

def option_menu_candletable():
    while True:
        menu = (
            "What will you do?\n\n"
            "1 - Draw a card.\n"
            "2 - Press the button on the box.\n"
            "3 - Inspect the photo.\n"
            "4 - Play the chessboard.\n"
            "5 - Go back.\n"
            "> \n"
        )

        user_selection = input(menu)

        if user_selection == "1":
            draw_path = resource_path(os.path.join("music", "draw_card", "draw_card.mp3"))
            draw = pygame.mixer.Sound(draw_path)
            draw.play()
            draw_card()
        elif user_selection == "2":
            button_path = resource_path(os.path.join("music", "draw_card", "button.mp3"))
            button_sound = pygame.mixer.Sound(button_path)
            button_sound.play()
            button_box()
        elif user_selection == "3":
            typewriter("\nThe woman in the photo suddenly begins talking to you.\n")
            time.sleep(1)
            pygame.mixer.music.set_volume(0.3)

            sound_path = resource_path(os.path.join("music", "voices", "photoghost.wav"))

            if os.path.exists(sound_path):

                ghost_sound = pygame.mixer.Sound(sound_path)
                channel = ghost_sound.play()

                while channel.get_busy():
                    time.sleep(0.1)

            else:
                print("photoghost.wav not found!")
            pygame.mixer.music.set_volume(1.0)

            # Small delay so the sound starts before the text
            time.sleep(0.5) 
            typewriter('"BOO! Did I scare you? Hahaha!"\n')
            typewriter('"Don\'t be scared, ghosts come in all shapes and sizes. Like me and the lion!"\n')
            time.sleep(1)
            typewriter('"Have you noticed the lion always says something different when you visit him?"\n')
            time.sleep(1)
            typewriter('"Well, goodbye dear, my husband is getting jealous."')
            if "potion" not in inventory:
                typewriter("\n\nHey there is something strapped to the back!\n")
                time.sleep(1)
                typewriter("You picked up a potion.\n")
                inventory.append("potion")
            else:
                typewriter("Nope nothing here..\n")
        elif user_selection == "4":
            play_chess()
        elif user_selection == "5":
            try_initiate_cangas()
            sound = pygame.mixer.Sound(lopen_path)
            sound.play()
            break
        else:
            typewriter("\nError, try to type the number associated with the option!\n")

def draw_card():
    # Random number from 1 to 100
    roll = random.randint(1, 100)

    # Determine card based on percentages
    if 1 <= roll <= 30:
        typewriter("You drew the Laughing Clown! You heal 20 HP.\n")
        clown_path = resource_path(os.path.join("music", "draw_card", "clown.mp3"))
        clown_sound = pygame.mixer.Sound(clown_path)
        clown_sound.play()
        health_system.health += 20

    elif 31 <= roll <= 60:
        typewriter("You drew the Demon! You lose 10 HP.\n")
        demon_path = resource_path(os.path.join("music", "draw_card", "demon.mp3"))
        demon_sound = pygame.mixer.Sound(demon_path)
        demon_sound.play()
        health_system.health -= 10

    elif 61 <= roll <= 75:
        earthquake_path = resource_path(os.path.join("music", "draw_card", "earthquake.mp3"))
        earthquake_sound = pygame.mixer.Sound(earthquake_path)
        earthquake_sound.play()
        if random.choice([True, False]):
            typewriter("""You drew The Earthquake! You feel the earth trembling and shaking.
Looking up you see something falling towards you, it hits you directly in your face.
Unfortunately, it was a ceiling tile.\n""")
            time.sleep(1)
            typewriter("You lose 20 HP.")
            health_system.health -= 20
        else:
            typewriter("""You drew The Earthquake! You feel the earth trembling and shaking.
Looking up you see something falling towards you, it hits you directly in your face.
Fortunately, it was just some some dust
The shaking actually felt kinda nice. You feel as if the quake messaged your every muscle.\n""")
            time.sleep(1)
            typewriter("You heal 20 hp.")
            health_system.health += 20


    elif 76 <= roll <= 90:
        from systems.music import stop_music, play_music
        stop_music()
        musicbox_path = resource_path(os.path.join("music", "draw_card", "music_box.wav"))
        musicbox_sound = pygame.mixer.Sound(musicbox_path)
        channel = musicbox_sound.play()
        typewriter("You drew the Music Box! Music starts playing...\n")
        
        # Wait for music box to finish playing
        while channel.get_busy():
            time.sleep(0.1)
        
        # Resume theme song
        play_music("music/music/theme_song.wav")

    elif 91 <= roll <= 95:
        hades_path = resource_path(os.path.join("music", "draw_card", "hades.mp3"))
        hades_sound = pygame.mixer.Sound(hades_path)
        hades_sound.play()
        typewriter("You drew Hades! You lose all HP!\n")
        health_system.health = 0

    elif 96 <= roll <= 100:
        god_path = resource_path(os.path.join("music", "draw_card", "god.mp3"))
        god_sound = pygame.mixer.Sound(god_path)
        god_sound.play()
        typewriter("You drew God! You are fully healed!\n")
        health_system.health = health_system.max_health

    # Clamp health between 0 and max
    health_system.health = min(max(health_system.health, 0), health_system.max_health)

    typewriter(f"Your current health: {health_system.health}/{health_system.max_health}\n")
    health_system.check_death()


def button_box():
    button_box_path = resource_path(os.path.join("music", "draw_card", "button.mp3"))
    button_box_sound = pygame.mixer.Sound(button_box_path)
    button_box_sound.play()
    typewriter("You try pressing the button on the box.\n")
    typewriter("It seems stuck..")

    if "wd-40" in inventory:
        typewriter("You apply some wd-40 to the button and try pressing it again.")
        if "ammo" not in inventory:
            inventory.append("ammo")
            typewriter("Pistol ammo rolled out of the box! Without a gun it seems useless.\n")
        else:
            typewriter("You waited for the box to do something, but it seems it doesn't work twice..\n")
