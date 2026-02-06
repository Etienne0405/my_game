from utils.typewriter import typewriter

import systems.health as health_system
from systems.inventory import inventory_check, inventory
from systems.candle_gasoline import try_initiate_cangas
import systems.game_state as gs

from rooms.hidden_room import hidden_room

import time
import pygame
import os
from utils.resource_path import resource_path

pygame.mixer.init()
lopen_path = resource_path(os.path.join("music", "overall", "lopen.wav"))

def hallway():

    # Check if hidden room is unlocked
    hidden_unlocked = gs.rooms_unlocked.get("hidden_room", False)

    # Intro text
    if hidden_unlocked:
        typewriter(
            "Intrigued by the bright lights, you walk towards the hallway.\n"
            "As you step inside, you notice something is different.\n"
            "Where once there was only a blank wall, a passage has appeared.\n"
        )
    else:
        typewriter("Intrigued by the bright lights, you walk towards the hallway.")
        time.sleep(1)
        typewriter(
            'As you step inside it, you notice that it leads to an empty wall with the word "backwards" scratched into it.'
        )
        typewriter(
            "Although the end doesn't seem too interesting, there are several interesting drawings on the walls of the hallway."
        )

    while True:

        # Base menu
        menu = (
            "What will you do?\n\n"
            "1 - Check your leg, see if it's okay.\n"
            "2 - Check inventory.\n"
            "3 - Check out drawing #1.\n"
            "4 - Check out drawing #2.\n"
            "5 - Check out drawing #3.\n"
            "6 - Check out drawing #4.\n"
        )

        # Add hidden room option if unlocked
        if hidden_unlocked:
            menu += "7 - Enter the hidden room.\n"
            menu += "8 - Go back.\n"
        else:
            menu += "7 - Go back.\n"

        menu += "> \n"


        user_selection = input(menu)

        if user_selection == "1":
            health_system.leg_health()
        elif user_selection == "2":
            inventory_check()
        elif user_selection == "6":

            print(r"""\

                 /| |\
                ( \./ )
                 \ : /
                 ) : (
                /  :  \
                |_d=p_|
""")
        elif user_selection == "5":
            print(r"""\

            .~~~~`\~~\
            ;       ~~ \
            |           ;
        ,----at--,______|---.
        /          \-----`    \
        `.__________`-_______-'
""")
        elif user_selection == "4":
            print(r"""\
    .--.              .--.
   : (\ ". _.b=n.._ ." /) :
    '.    `        `    .'
     /'   _        _   `\
    /     0}      {0     \
   |       /      \       |
   |     /'        `\     |
    \   | .  .==.  . |   /
     '._ \.' \__/ './ _.'
     /  ``'._-''-_.'``  \
""")
        elif user_selection == "3":
            print(r"""\
    /\           /\           /\
   //\\         //\\         //\\
   \\//         \\//         \\//
    ><           ><           ><
 .._||_..      ._||..       ._||..
 :/  !! :     |     \:     :/    :;
 |:  :| |     |  ::  |     |  :: ;|
 |:  :; |     |  :;  |     |  :: :|
 |;   : |     | : :  |     |  :: :|
 |      |     |      |     |     ,|
 |_._.__|     |__.__.|     |._._._|
|        |   |        |   |        |
|        |   |        |   |        |
 \_.. ._/     \_. .._/     \_.. ._/
  |    |       |    |       |    |
  |    |       |    |       |    |
  |    \._____./    \._____./    |
  \                              /
    `-.______.  . ..   ._______.-'
              \  ..   /
               |     |
               |     |
               |     |
               |     |
               |     |
               |... .|
          ____/.. . ..\____
     _. -'                  '-._
    /___________________________\
""")

        # Hidden room
        elif hidden_unlocked and user_selection == "7":
            typewriter("You step through the narrow opening, leaving the hallway behind...\n")
            hidden_room()
            break


        # Go back (with hidden room)
        elif hidden_unlocked and user_selection == "8":
            try_initiate_cangas()
            sound = pygame.mixer.Sound(lopen_path)
            sound.play()
            break


        # Go back (normal)
        elif not hidden_unlocked and user_selection == "7":
            try_initiate_cangas()
            sound = pygame.mixer.Sound(lopen_path)
            sound.play()
            break


        else:
            typewriter("\nError, try to type the number associated with the option!\n")








