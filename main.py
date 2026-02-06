# This final project is made by Etienne Schaap
# In this game you are stuck in a room in which you have to find items and solve puzzles to escape.
# The game is only played in the terminal.
import sys
import os
import traceback

# Set up error handling first
def handle_exception(exc_type, exc_value, exc_traceback):
    """Global exception handler to keep console open"""
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    
    print("\n" + "="*60)
    print("ERROR: An unhandled exception occurred!")
    print("="*60)
    print(f"\nError type: {exc_type.__name__}")
    print(f"Error message: {str(exc_value)}")
    print("\nFull traceback:")
    print("-"*60)
    traceback.print_exception(exc_type, exc_value, exc_traceback)
    print("="*60)
    input("\nPress Enter to exit...")
    sys.exit(1)

sys.excepthook = handle_exception

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

try:
    from rooms.main_room import main_room
    from utils.typewriter import typewriter
    import systems.game_state as gs
    import time
except Exception as e:
    print("\n" + "="*60)
    print("ERROR: Failed to import game modules!")
    print("="*60)
    print(f"\nError type: {type(e).__name__}")
    print(f"Error message: {str(e)}")
    print("\nFull traceback:")
    print("-"*60)
    traceback.print_exc()
    print("="*60)
    input("\nPress Enter to exit...")
    sys.exit(1)


def start_game():
    while True:
        typewriter("Welcome to my chat-based game. In this game you will have to solve puzzles to escape the room in which you are stuck. ")
        time.sleep(0.5)
        typewriter("This game works by typing the number associated with the option you want to select. ")
        time.sleep(0.5)
        typewriter("You start with 100 hp out of 100.")
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
                # Ask for difficulty
                while True:
                    diff = input(
                        "Choose difficulty (easy / medium / hard) [medium]: \n> "
                    ).strip().lower()
                    if diff == "":
                        diff = "medium"
                    if diff in ("easy", "medium", "hard"):
                        gs.difficulty = diff
                        typewriter(f"Difficulty set to {diff}. Starting game..\n")
                        break
                    else:
                        typewriter("Invalid difficulty, please type easy, medium or hard.")

                main_room()
            elif user_selection == "2":
                sys.exit("Bye!")
            else:
                typewriter("Error, try to type the number associated with the option!")

def main():
    try:
        start_game()
    except KeyboardInterrupt:
        print("\n\nGame interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print("\n" + "="*60)
        print("ERROR: An unhandled exception occurred during game execution!")
        print("="*60)
        print(f"\nError type: {type(e).__name__}")
        print(f"Error message: {str(e)}")
        print("\nFull traceback:")
        print("-"*60)
        traceback.print_exc()
        print("="*60)
        input("\nPress Enter to exit...")
        sys.exit(1)

if __name__ == "__main__":
    main()

