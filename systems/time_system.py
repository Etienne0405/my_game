from datetime import datetime
from utils.typewriter import typewriter
from rooms.storage_room import unlock_room  # this works because storage_room.py defines unlock_room

import time

# Time stuff

time_set_at = datetime.now()
base_game_time = datetime.now()
time_frozen = False
midnight_triggered = False

def get_current_time():
    if time_frozen:
        return base_game_time

    elapsed = datetime.now() - time_set_at
    return base_game_time + elapsed

def change_time():
    global base_game_time, time_set_at, midnight_triggered, time_frozen

    typewriter("You move closer to the clock and adjust the hands.\n")
    new_time = input("Set the time (HH:MM): \n").strip()

    try:
        t = datetime.strptime(new_time, "%H:%M")
        now = datetime.now()

        base_game_time = now.replace(
            hour=t.hour,
            minute=t.minute,
            second=0,
            microsecond=0
        )
        time_set_at = now

        # If set to midnight → freeze time
        if t.hour == 0 and t.minute == 0:
            time_frozen = True
        else:
            time_frozen = False  # unfreeze when set to another time

        typewriter(f"You set the clock to {base_game_time.strftime('%H:%M')}.\n")

        # Trigger ONLY when set
        if t.hour == 0 and t.minute == 0 and not midnight_triggered:
            midnight_triggered = True
            trigger_midnight_event()

    except ValueError:
        typewriter("That doesn't seem to be a valid time.")

def trigger_midnight_event():
    typewriter("You hear very distorted creepy sounds, the clock is no longer moving and you feel the ground trembling below you. ")
    time.sleep(1)
    typewriter("Suddenly you hear a clicking noise.")
    time.sleep(2)
    typewriter("It seems you triggered something..\n")

    unlock_room("storage_room")
