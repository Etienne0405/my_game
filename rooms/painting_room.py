from utils.typewriter import typewriter
from systems.inventory import inventory

import time

def enter_painting_room():
    typewriter("You climb into the tight space behind the painting.")
    time.sleep(1)

    if "key" not in inventory:
        typewriter("It is a very tight space but when you crawl to the end. You see a key!")
        inventory.append("key")
        typewriter("You pick up the key, it might be useful later.\n")
    else:
        typewriter("There is nothing else here.\n")
