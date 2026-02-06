from utils.typewriter import typewriter
from systems.inventory import inventory_check
import systems.music as music
from utils.resource_path import resource_path

import time
import random
import curses
import pygame


def hidden_room():
    typewriter(
        "You enter through the hidden door. Before you lies a dimly lit room with a pedestal in the middle. On top of which sits an old arcade game."
    )
    time.sleep(1)
    typewriter("This room doesn't feel scary at all. As if there is no ghostly presence here.\n")

    while True:
        menu = (
            "What will you do?\n\n"
            "1 - Check inventory.\n"
            "2 - Play the arcade game.\n"
            "3 - Go back.\n"
            "> \n"
        )
        user_selection = input(menu)

        if user_selection == "1":
            inventory_check()
        elif user_selection == "2":
            curses.wrapper(hidden_room_runner)
        elif user_selection == "3":
            typewriter("You decide to leave the hidden room and return to the previous area.\n")
            break

# =========================
# CONFIG
# =========================
LANES = ["1", "2", "3"]
NUM_LANES = len(LANES)
HEIGHT = 15
BASE_FRAME_DELAY = 0.15
SCORE_PER_STEP = 1
LEVEL_UP_SCORE = 100
MIN_WAVE_SPACING = 3

MUSIC_LAYERS = [
    "music/music/base_arcade.wav",
    "music/music/layer1.wav",
    "music/music/layer2.wav",
    "music/music/layer3.wav",
    "music/music/layer4.wav",
    "music/music/layer5.wav",
]

# =========================
# MUSIC
# =========================
music_channels = []
current_layer = 0

def init_music():
    global music_channels, current_layer
    pygame.mixer.init()
    pygame.mixer.set_num_channels(len(MUSIC_LAYERS))
    music_channels.clear()
    for i, path in enumerate(MUSIC_LAYERS):
        sound = pygame.mixer.Sound(resource_path(path))
        channel = pygame.mixer.Channel(i)
        channel.set_volume(0.0)
        channel.play(sound, loops=-1)
        music_channels.append(channel)
    music_channels[0].set_volume(0.5)
    current_layer = 0

def update_music_layers(score):
    global current_layer
    target_layer = min(score // LEVEL_UP_SCORE, len(music_channels) - 1)
    while current_layer < target_layer:
        current_layer += 1
        music_channels[current_layer].set_volume(0.5)

def stop_music():
    try:
        pygame.mixer.stop()
        # Don't quit mixer here; let main game manage it
    except Exception:
        pass

# =========================
# WAVE GENERATOR
# =========================
def generate_wave(level):
    """Generate a wave pattern: 1–2 obstacles, non-adjacent lanes"""
    wave = [0] * NUM_LANES
    # only allow 2 obstacles from level 3+
    num_obstacles = 1 if level < 3 else random.choice([1, 2])
    choices = list(range(NUM_LANES))
    random.shuffle(choices)
    obstacles_placed = 0
    for lane in choices:
        # prevent adjacent lanes in same wave
        if lane > 0 and wave[lane - 1] == 1:
            continue
        if lane < NUM_LANES - 1 and wave[lane + 1] == 1:
            continue
        wave[lane] = 1
        obstacles_placed += 1
        if obstacles_placed == num_obstacles:
            break
    return wave

# =========================
# GAME LOOP
# =========================
def hidden_room_runner(stdscr):
    # Stop main music and start layered arcade music
    music.stop_music()
    init_music()

    # Curses setup
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    stdscr.nodelay(True)
    curses.resize_term(HEIGHT + 4, NUM_LANES * 4 + 10)
    stdscr.clear()

    # Show countdown before starting
    for countdown in [3, 2, 1]:
        stdscr.clear()
        stdscr.addstr(HEIGHT // 2, NUM_LANES * 2, str(countdown))
        stdscr.refresh()
        time.sleep(1)

    stdscr.clear()
    stdscr.refresh()

    # Game state
    obstacles = []  # list of [lane_index, y_position]
    score = 0
    level = 1
    frame_delay = BASE_FRAME_DELAY
    wave_spacing = MIN_WAVE_SPACING
    wave_counter = wave_spacing

    # Player
    player_lane = 1
    player_y = HEIGHT - 1

    try:
        while True:
            # ---- INPUT ----
            key = stdscr.getch()
            if key != -1:
                key_char = chr(key).upper()
                if key_char == "A" and player_lane > 0:
                    player_lane -= 1
                elif key_char == "D" and player_lane < NUM_LANES - 1:
                    player_lane += 1
                elif key_char == "Q":
                    break

            # ---- SPAWN WAVE ----
            if wave_counter >= wave_spacing:
                wave = generate_wave(level)
                for lane_index, val in enumerate(wave):
                    if val:
                        obstacles.append([lane_index, 0])
                wave_counter = 0
            else:
                wave_counter += 1

            # ---- MOVE OBSTACLES ----
            for ob in obstacles:
                ob[1] += 1
            obstacles = [ob for ob in obstacles if ob[1] < HEIGHT]

            # ---- COLLISION ----
            collision = any(ob[0] == player_lane and ob[1] == player_y for ob in obstacles)
            if collision:
                stdscr.clear()
                stdscr.addstr(6, 4, "GAME OVER")
                stdscr.addstr(7, 4, f"Score: {score}")
                stdscr.addstr(9, 2, "Press any key...")
                stdscr.nodelay(False)
                stdscr.getch()
                break

            # ---- SCORE & LEVEL ----
            score += SCORE_PER_STEP
            new_level = score // LEVEL_UP_SCORE + 1
            if new_level > level:
                level = new_level
                frame_delay = max(0.03, BASE_FRAME_DELAY * (0.9 ** (level - 1)))
                wave_spacing = max(1, MIN_WAVE_SPACING - (level // 2))

            update_music_layers(score)

            # ---- DRAW ----
            stdscr.clear()
            # lane headers
            for i, lane in enumerate(LANES):
                stdscr.addstr(0, i * 4 + 2, lane)
            # obstacles and empty lane dots
            for y in range(HEIGHT):
                for lane_index in range(NUM_LANES):
                    char = "."
                    for ob in obstacles:
                        if ob[0] == lane_index and ob[1] == y:
                            char = "#"
                            break
                    stdscr.addstr(y + 1, lane_index * 4 + 2, char)
            # player
            stdscr.addstr(player_y + 1, player_lane * 4 + 2, "A")
            # score/level
            stdscr.addstr(HEIGHT + 1, 0, "-" * (NUM_LANES * 4 + 3))
            stdscr.addstr(HEIGHT + 2, 0, f"Score: {score}  Level: {level}")

            stdscr.refresh()
            time.sleep(frame_delay)

    finally:
        stop_music()
        music.play_music("music/music/theme_song.wav")
        curses.nocbreak()
        curses.echo()
        curses.curs_set(1)