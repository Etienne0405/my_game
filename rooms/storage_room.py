from utils.typewriter import typewriter
import systems.health as health_system
from systems.inventory import inventory_check, inventory
import systems.game_state as gs
from systems.ghost_encounter import try_spawn_ghost
from systems.candle_gasoline import try_initiate_cangas

import time
import os
import pygame

pygame.mixer.init()
lopen_path = os.path.join("music", "overall", "lopen.wav")

def unlock_room(room_name):
    gs.rooms_unlocked[room_name] = True
    typewriter(f"{room_name.replace('_',' ').title()} is now unlocked!\n")

def storage_door():
    typewriter("You walk towards the door.\n")
    while True:
        menu = (
            "What will you do?\n\n"
            "1 - Check your leg, see if it's okay.\n"
            "2 - Check inventory.\n"
            "3 - Try to open the door.\n"
            "4 - Go back.\n"
            "> "
        )

        user_selection = input(menu)

        if user_selection == "1":
            health_system.leg_health()

        elif user_selection == "2":
            inventory_check()

        elif user_selection == "3":
            if gs.rooms_unlocked.get("storage_room", False):
                typewriter("The door creaks open...")
                try_spawn_ghost()
                try_initiate_cangas()
                sound = pygame.mixer.Sound(lopen_path)
                sound.play()
                storage_room()
            else:
                typewriter("It seems the door is locked.\n")

        elif user_selection == "4":
            try_spawn_ghost()
            sound = pygame.mixer.Sound(lopen_path)
            sound.play()
            break

        else:
            typewriter("\nError, try to type the number associated with the option!\n")

def storage_room():
    typewriter("You step into the storage room. It's very small but there are a couple of shelves with items on them.\n")

    while True:
        menu = (
            "What will you do?\n\n"
            "1 - Check your leg, see if it's okay.\n"
            "2 - Check inventory.\n"
            "3 - Inspect shelves.\n"
            "4 - Go back.\n"
            "> "
        )

        user_selection = input(menu)

        if user_selection == "1":
            health_system.leg_health()

        elif user_selection == "2":
            inventory_check()

        elif user_selection == "3":
            if "candle" in inventory or "flashlight" in inventory:
                storage_items()
            else:
                typewriter("It's too dark to see anything.")

        elif user_selection == "4":
            try_spawn_ghost()
            try_initiate_cangas()
            sound = pygame.mixer.Sound(lopen_path)
            sound.play()
            break

        else:
            typewriter("Error, try to type the number associated with the option!\n")

def update_shelf_sequence(color):
    gs.shelf_sequence.append(color)

    # Keep only the last N entries
    if len(gs.shelf_sequence) > len(gs.CORRECT_SEQUENCE):
        gs.shelf_sequence.pop(0)

    # Check for success
    if (
        gs.shelf_sequence == gs.CORRECT_SEQUENCE
        and not gs.ghost_event_triggered
    ):
        gs.ghost_event_triggered = True
        friendly_ghost_event()


def friendly_ghost_event():
    time.sleep(3)
    typewriter("The air suddenly grows cold.\n")
    time.sleep(1)

    typewriter("The candles flicker violently.\n")
    time.sleep(1)

    typewriter("A ghost appears in front of you:\n\n")
    time.sleep(1)

    ghost_art = [
"      .-.                          ",
"    .'   `.                        ",
"    :g g   :                       ",
"    : o    `.                      ",
"   :         ``.                   ",
"  :             `.                 ",
" :  :         .   `.               ",
" :   :          ` . `.             ",
"  `.. :            `. ``;          ",
"     `:;             `:'           ",
"       :              `.           ",
"         `.              `.     .  ",
"           `'`'`'`---..,___`;.-'   ",
]

    for line in ghost_art:
        print(line)
        time.sleep(0.3)

    time.sleep(1)

    # Initialize audio (safe to call multiple times)
    pygame.mixer.init()

    # Load ghost voice
    sound_path = os.path.join("music", "voices", "friendly_ghost.wav")
    sound = pygame.mixer.Sound(sound_path)
    sound.play()   # play once


    typewriter(
        f'\nThe ghost whispers:\n'
        f'"Hello there, I am actually chill dude. I won\'t hurt you."\n'
        f'"The last thing I remember when I was alive is that a shelf fell on me. '
        f'What a fucking embarrassing death."\n\n'
        f'"Listen, I was also trying to escape this place in which you are now trapped."\n'
        f'"The host of this place is now giving me the privilege to help people here."\n\n'
        f'"I see your leg is pretty messed up. Let me help you."\n\n'
        f'"Oh yeah, by the way man. When someone is killed in this place, he or she turns into a ghost."\n'
        f'"They are haunted to attack the people trying to escape."\n'
        f'"Anyways.. Try to use the right move when you encounter a ghost."\n'
        f'"Bye man… avenge me."\n\n'
    )

    time.sleep(1)
    typewriter("And just like that, he vanishes.\n\n")
    time.sleep(1)
    health_system.fix_leg()


def storage_items():
    typewriter("There are three shelves")

    while True:
        menu = (
            "What will you do?\n\n"
            "1 - Inspect red shelf.\n"
            "2 - Inspect green shelf.\n"
            "3 - Inspect blue shelf.\n"
            "4 - Go back.\n"
            "> \n"
        )

        user_selection = input(menu)

        if user_selection == "1":
            if not gs.red_shelf_unlocked:
                typewriter('On the red shelf lies a glass box. You can see some writing equipment in there. Scratched on the side of the box are the words: "Colour" and "Carpet" ')

                password = input("What's the password? > ")

                if password.replace(" ", "").lower() == "white":
                    gs.red_shelf_unlocked = True
                    typewriter("You hear a soft click. The glass box unlocks.\n")

                    if "pencil" not in inventory:
                        inventory.append("pencil")
                        typewriter(
                            "You cracked the password! There are a lot of items, but your mother taught you to be humble.\n"
                            "You only pick up one pencil.\n"
                        )
                else:
                    typewriter(
                        "You shake the lock and try to force it to open."
                        "It seems nothing works, I guess you really do need the password."
                    )
            else:
                typewriter(
                    "The glass box on the red shelf stands open. "
                    "There is nothing else of interest here.\n"
                )

            update_shelf_sequence("red")

        elif user_selection == "2":
            typewriter("Oh no! The shelf fell over!")
            time.sleep(1)
            typewriter("You lost 20 hp.")

            health_system.health -= 20

            typewriter(f"Your current health: {health_system.health}/{health_system.max_health}\n")
            health_system.check_death()

            update_shelf_sequence("green")

        elif user_selection == "3":
            typewriter("Hmm, it seems this shelf is empty.")

            update_shelf_sequence("blue")

        elif user_selection == "4":
            break
        else:
            typewriter("\nError, try to type the number associated with the option!\n")


