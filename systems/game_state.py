user_name = ""

rooms_unlocked = {
    "painting_room": False,
    "storage_room": False,
    "hidden_room": False,
    "enddoor_room": False,
}

room_visits = 0


red_shelf_unlocked = False
shelf_sequence = []
CORRECT_SEQUENCE = ["green", "blue", "red"]
ghost_event_triggered = False
ghost_clue = "banana"

# Difficulty settings: affects weapon damage multiplier
# Options: "easy", "medium", "hard"
difficulty = "medium"
DIFFICULTY_MULTIPLIERS = {
    "easy": 1.35,
    "medium": 1.0,
    "hard": 0.65,
}



