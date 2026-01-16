# ----------------------------
# THE END DOOR
# ----------------------------

import sys
from utils.typewriter import typewriter
from systems.ghost_encounter import try_spawn_ghost
from systems.candle_gasoline import try_initiate_cangas
from systems.inventory import inventory

def end_door():
    if "key" in inventory: # I will maybe change later
        try_spawn_ghost()
        try_initiate_cangas()
        end_game()
    else:
        typewriter("You shake the lock and try to force it to open.\n"
        "It seems nothing works, I guess you really do need a key.")

def end_game():
    typewriter("You slide the key into the lock."
    "You have a feeling it could be right."
    "When you turn the key, you hear a loud noise of the door moving"
    "You notice the door being very thick. It seems more like a vault.\n"
    "You enter the room."
    "It surprises you that you are on a beautiful field, full of flowers and green long grass."
    "Funny, how you have found das Glück, the luck der Wanderer could not find."
    "You WIN!!")

    sys.exit()
