from utils.typewriter import typewriter
from rooms.storage_room import unlock_room
import time
from systems.inventory import inventory_check, inventory
import systems.game_state as gs
from systems.ghost_encounter import ghost_encounter

# ONLY POSSIBLE WITH THE CANDLE
def painting():
    if gs.rooms_unlocked["painting_room"]:
        typewriter("The painting has already moved, revealing the hidden room.\n")
        return

    typewriter("""The look on the mans face, makes it seem as if the man is chasing something.
He has beautiful hair waving in the wind, he wears an elegant brown suit and nice leather shoes.\n""")
    time.sleep(1)
    typewriter("""On the other side of the painting is a gorgeous field of long green grass.
The paint in that section seems warmer in colour and you get a happy feeling from it.
It seems as though the man is chasing that feeling.\n""")
    time.sleep(1)
    typewriter("Above the painting, someone wrote something in german.\n")
    time.sleep(1)
    typewriter("""[Ich wandle still, bin wenig froh,
Und immer fragt der Seufzer, wo?
Im Geisterhauch tönt's mir zurück,
"Dort, wo du nicht bist, dort is das Glück."]\n""")
    typewriter("You notice warmth coming from the painting, you feel weird.\n")
    typewriter("Beneath the painting, on the wall, are scratch marks.\n")
    typewriter("You also notice a certain space meant for something to write on.\n")

    if "pencil" in inventory:
        typewriter("Luckily you have a pencil.\n")
        puzzle_painting_answer = input("What will you write down?\n")

        if puzzle_painting_answer.replace(" ", "").lower() == "derwanderer":
            typewriter("The painting moves out of the way!\n")
            unlock_room("painting_room")
        else:
            typewriter("Nothing happens. The painting remains in place.\n")
            # Failed puzzle attempt — trigger a ghost encounter
            ghost_encounter()
    else:
        typewriter("Too bad you don't have anything to write with.\n")
