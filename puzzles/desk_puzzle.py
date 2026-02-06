from utils.typewriter import typewriter

import systems.health as health_system
from systems.inventory import inventory_check, inventory
from systems.ghost_encounter import ghost_encounter
import systems.music as music

import time
import os
import pygame
from utils.resource_path import resource_path


pygame.mixer.init()
lopen_path = resource_path(os.path.join("music", "overall", "lopen.wav"))
extra_menu_option = False

def desk():
    typewriter("You approach the desk and notice it's covered in dust and old newspapers.\n")
    typewriter("Below the desk, you find a chest.")
    typewriter("Next to the desk, on a separate table there is a gramophone with a record on it.\n")
    typewriter("As you sift through the newspapers, you find an article about mysterious disappearances in the house.\n")
    typewriter("One headline catches your eye: 'Mysterious disappearances in abandoned house. Authorities baffled as more people go missing without a trace.'\n")
    typewriter("You flip through the newspaper and see a small article about a man who was once killed in the house. Since then the place has been haunted.\n")

    while True:
        menu = (
            "What will you do?\n\n"
            "1 - Check your leg, see if it's okay.\n"
            "2 - Check inventory.\n"
            "3 - Play the record.\n"
            "4 - Open chest.\n"
        )
        
        # When extra_menu_option is true add a new option here to look at files in drawer
        if extra_menu_option:
            menu += "5 - Look at files.\n"
            menu += "6 - Go back.\n"
        else:
            menu += "5 - Go back.\n"
        
        menu += "> \n"

        user_selection = input(menu)

        if user_selection == "1":
            health_system.leg_health()
        elif user_selection == "2":
            inventory_check()
        elif user_selection == "3":
            typewriter("You carefully place the needle on the record. The gramophone crackles to life, filling the room with eerie music.\n")
            play_gramophone()
        elif user_selection == "4":
            open_chest()
        elif user_selection == "5":
            if extra_menu_option:
                view_files()
            else:
                sound = pygame.mixer.Sound(lopen_path)
                sound.play()
                break
        elif user_selection == "6":
            if extra_menu_option:
                sound = pygame.mixer.Sound(lopen_path)
                sound.play()
                break
        else:
            typewriter("Error, try to type the number associated with the option!\n")



def play_gramophone():

    # Stop current music properly
    music.stop_music()

    # Play gramophone via music system
    music.play_music("music/music/gramaphone.wav")

    typewriter("The gramophone crackles to life...\n")
    typewriter("Type 'stop' to turn it off.\n")

    while True:
        cmd = input("> ").lower().strip()

        if cmd == "stop":
            global extra_menu_option

            # Stop gramophone properly
            music.stop_music()

            typewriter("The gramophone slowly winds down.\n")

            # Resume theme
            music.play_music("music/music/theme_song.wav")
            time.sleep(2)
    
            typewriter("You see some files in a drawer under the gramophone..\n")
            extra_menu_option = True
            break

def open_chest():
    typewriter("You open the chest to find there are 3 compartments.")
    typewriter("Someone wrote some information on each compartment:")
    print(r"""
+---------+    +---------+    +---------+
|         |    |         |    |  3%^^*  |
|  WD-40  |    | letter  |    |   -+=-  |
|         |    |         |    |  z-0pr  |
+---------+    +---------+    +---------+

""")
    typewriter("It seems the third one is unreadable.")

    compartment_opened = False  # Track if the player opened a compartment

    while True:

        menu = (
            "What will you do?\n\n"
            "1 - Open the one with WD-40.\n"
            '2 - Open the one that says "letter".\n'
            "3 - Open the unreadable one.\n"
            "4 - Go back.\n"
            "> \n"
        )

        user_selection = input(menu)

        if user_selection in ["1", "2", "3"]:
            if compartment_opened:
                typewriter("Huh, the compartments are locked now..")
                continue  # skip the rest of the loop
            else:
                compartment_opened = True  # mark that a compartment has been opened

        if user_selection == "1":
            if "wd-40" not in inventory:
                typewriter("Hey there actually was a bottle of WD-40 here!")
                inventory.append("wd-40")
            else:
                typewriter("Hey you shouldn't be able to look twice!")
        elif user_selection == "2":
            typewriter("Inside the compartment is a small folded letter.")
            time.sleep(1)
            typewriter('It reads: "For all non german speakers. There, where the wanderer is not, is happiness!"')
        elif user_selection == "3":
            typewriter("You open the unreadable compartment.")
            ghost_encounter()
        elif user_selection == "4":
            break
        else:
            typewriter("Error, type the number associated with the option!")


def view_files():
    """Displays the mysterious medical files found under the gramophone"""
    from systems.files_data import files_data
    
    files = files_data["Look at the files"]
    typewriter("Very odd files lay here, information about people's medical history.\n")
    
    while True:
        print("\n" + "=" * 80)
        print("\nMedical Files Directory:\n")
        print(f"{'#':<3} {'Name':<25} {'Age':<6} {'Disease':<30}")
        print("-" * 80)
        
        for i, person in enumerate(files["people"], 1):
            print(f"{i:<3} {person['name']:<25} {person['age']:<6} {person['disease']:<30}")
        
        print("-" * 80)
        print(f"{len(files['people']) + 1} - Go back")
        print()
        
        choice = input("Select a file to view details (or go back): > ").strip()
        
        try:
            choice_num = int(choice)
            
            if choice_num == len(files["people"]) + 1:
                break
            elif 1 <= choice_num <= len(files["people"]):
                person = files["people"][choice_num - 1]
                
                print("\n" + "=" * 80)
                typewriter(f"Medical File - {person['name']}\n")
                print("=" * 80)
                print(f"Name:           {person['name']}")
                print(f"Age:            {person['age']}")
                print(f"Height:         {person['height']}")
                print(f"Weight:         {person['weight']}")
                print(f"Diagnosed:      {person['disease']}")
                print(f"Health Notes:   {person['health_info']}")
                print("=" * 80)
                print()
                
                input("Press Enter to return to file list...")
            else:
                typewriter("Invalid selection. Please try again.\n")
        except ValueError:
            typewriter("Invalid input. Please enter a number.\n")