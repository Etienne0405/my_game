import sys
from utils.typewriter import typewriter
from systems.ghost_encounter import ghost_encounter
from systems.candle_gasoline import try_initiate_cangas
import systems.game_state as gs

def end_door():
    if gs.rooms_unlocked.get("enddoor_room", False):
        try_initiate_cangas()
        end_game()
    else:
        typewriter(
            "You shake the lock and try to force it to open.\n"
            "It seems nothing works, perhaps you need to explore more first.\n"
        )
        # Failed attempt to open the door -> spawn ghost
        ghost_encounter()

def end_game():
    typewriter("A magic key appears in the lock. You hear a loud noise of the door moving.\n"
    "You notice the door being very thick. It seems more like a vault.\n"
    "You enter the room.\n"
    "It surprises you that you are on a beautiful field, full of flowers and green long grass.\n"
    "Funny, how you have found das Glück, the luck der Wanderer could not find.\n"
    "You WIN!!")

    sys.exit()
