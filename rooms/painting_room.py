from utils.typewriter import typewriter

from systems.inventory import inventory
import systems.health as health_system

from rooms.storage_room import unlock_room

import time

def enter_painting_room():
    all_correct = True

    typewriter("You climb into the tight space behind the painting.")
    time.sleep(1)
    typewriter("It is a very tight space and you are crawling. You feel heat coming from the end.\n")
    typewriter("Behind you the painting closes.\n")
    typewriter("As the heat rises, you begin to think maybe this was not such a good idea after all...\n")

    typewriter("Suddenly, you hear a voice echoing around you: 'Welcome, normally I bake my sourdough here, but i guess you will do.'\n")
    typewriter("If you can correctly answer my questions, I will let you go.\n")
    time.sleep(1)
    
    typewriter("'Which animal is on the wall of this room?'\n")
    answer1 = input("> ")

    if answer1.replace(" ", "").lower() == "lion":
        typewriter("'Correct! Now for the next question.'\n")
    else:
        all_correct = False
        typewriter("'Wrong! I guess for you to turn golden brown I need a little more heat..'\n")
        health_system.health -= 25
        typewriter("You lost 25 hp.\n")
        health_system.check_death()
        typewriter("'Let's continue.'\n")

    time.sleep(1)
    typewriter("'What lies on the desk?'\n")
    answer2 = input("> ")

    if answer2.replace(" ", "").lower() == "newspapers":
        typewriter("'Correct again! You are quite clever.'\n")
    else:
        all_correct = False
        typewriter("'Wrong! You seem to love saunas!'\n")
        health_system.health -= 25
        typewriter("You lost 25 hp.\n")
        health_system.check_death()
        typewriter("'Let's continue.'\n")

    time.sleep(1)
    typewriter("'Final question: From which material is the door made where a carpet lies?'\n")
    answer3 = input("> ")

    if answer3.replace(" ", "").lower() == "gold":
        typewriter("'Impressive! You may leave now, next time think twice before you wander through uncharted territories'\n")
        time.sleep(1)
        typewriter("You crawl back out from behind the painting, relieved to be out of the heat.\n")
    else:
        all_correct = False
        typewriter("'Wrong! I guess you will be my sourdough after all!'\n")
        health_system.health -= 25
        typewriter("You lost 25 hp.\n")
        health_system.check_death()
        time.sleep(1)
        typewriter("You crawl back out from behind the painting, feeling quite weak from the heat.\n")

    if all_correct:
        unlock_room("hallway")
        typewriter("You hear a faint noise.\n")

