# This final project is made by Etienne Schaap
# In this game you are stuck in a room in which you have to find items and solve puzzles to escape.
# The game is only played in the terminal.
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

from rooms.main_room import main_room
from utils.typewriter import typewriter
import systems.game_state as gs
import sys
import time


def start_game():
    while True:
        typewriter("Welcome to my chat-based game. In this game you will have to solve puzzles to escape the room in which you are stuck. ")
        time.sleep(0.5)
        typewriter("This game works by typing the number associated with the option you want to select. ")
        time.sleep(0.5)
        typewriter("You start with 50 hp out of 100.")
        time.sleep(0.5)
        typewriter("You can press 'Enter' to fast forward the text.\n")

        while True:
            user_selection = input(
                """Do you want to start the game?
            1 - Yes!
            2 - No, thank you
            > """
            )

            if user_selection == "1":
                typewriter("Starting game..\n")
                main_room()
            elif user_selection == "2":
                sys.exit("Bye!")
            else:
                typewriter("Error, try to type the number associated with the option!")

def main():
    start_game()

if __name__ == "__main__":
    main()

