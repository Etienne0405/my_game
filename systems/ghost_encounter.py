from utils.typewriter import typewriter
import systems.health as health_system
from systems.inventory import inventory
import systems.music as music
from utils.resource_path import resource_path
import systems.game_state as gs

import random
import time
import pygame
import os

low_health_sound = None
low_health_playing = False



def try_spawn_ghost():
    # Disabled automatic/random ghost spawns. Use explicit calls to
    # `ghost_encounter()` from puzzles when the player fails a puzzle.
    return False


def ghost_encounter():
    global low_health_sound, low_health_playing

    music.play_music("music/music/battle_music.wav")

    ghost_hp = 5
    pygame.mixer.init()

    low_health_path = resource_path(os.path.join("music", "health", "health_low.mp3"))
    low_health_sound = pygame.mixer.Sound(low_health_path)
    low_health_playing = False

    pygame.mixer.Sound(resource_path(os.path.join("music", "ghost_encounter", "ghost_entry.wav"))).play()
    time.sleep(0.5)

    typewriter("\nThe air grows cold...\n")
    time.sleep(1)
    typewriter("A ghost emerges from the darkness.\n\n")

    while ghost_hp > 0:
        attack_type = random.choice(["scare", "attack", "charge"])

        if attack_type == "scare":
            pygame.mixer.Sound(resource_path(os.path.join("music", "ghost_encounter", "scare.mp3"))).play()
            typewriter("The ghost tries to scare you with haunting sounds.\n")
        elif attack_type == "attack":
            pygame.mixer.Sound(resource_path(os.path.join("music", "ghost_encounter", "fast_attack.wav"))).play()
            typewriter("The ghost raises its arm for a quick attack!\n")
        else:
            pygame.mixer.Sound(resource_path(os.path.join("music", "ghost_encounter", "charge-attack.wav"))).play()
            typewriter("The ghost gathers energy... it is charging!\n")

        time.sleep(1)

        menu = "What will you do?\n\n1 - Attack\n2 - Dodge\n3 - Block\n"
        if "potion" in inventory:
            menu += "4 - Use potion\n"

        choice = input(menu + "> ")
        ghost_hp = resolve_combat_choice(choice, attack_type, ghost_hp)
        health_system.check_death()

    if low_health_playing:
        low_health_sound.stop()
        low_health_playing = False

    pygame.mixer.Sound(resource_path(os.path.join("music", "ghost_encounter", "ghost_death.mp3"))).play()
    typewriter("\nThe ghost screams and dissolves into mist...\n")
    typewriter("You are alone again.\n\n")

    music.play_music("music/music/theme_song.wav")


def choose_weapon():
    weapons = ["fists"]

    if "wooden_plank" in inventory:
        weapons.append("wooden plank")

    if "pistol" in inventory and "ammo" in inventory:
        weapons.append("pistol")

    # If there are no alternatives, default to fists without prompting
    if len(weapons) == 1:
        return "fists"

    typewriter("\nChoose your weapon:\n")
    for i, w in enumerate(weapons, 1):
        typewriter(f"{i} - {w}\n")

    try:
        return weapons[int(input("> ")) - 1]
    except:
        return "fists"


def get_weapon_stats(weapon):
    if weapon == "pistol":
        base = (0.8, 2.5)
    if weapon == "wooden_plank":
        base = (0.95, 1.5)
    if weapon == "fists":
        base = (0.7, 1.0)

    # Scale damage by difficulty multiplier from game state
    try:
        mult = gs.DIFFICULTY_MULTIPLIERS.get(gs.difficulty, 1.0)
    except Exception:
        mult = 1.0

    hit_chance, damage = base
    return hit_chance, damage * mult


def play_weapon_sound(weapon):
    sounds = {
        "fists": "fists.wav",
        "pistol": "pistol.mp3",
        "wooden plank": "wooden_plank_attack.mp3"
    }

    if weapon in sounds:
        pygame.mixer.Sound(resource_path(os.path.join("music", "ghost_encounter", sounds[weapon]))).play()


def resolve_combat_choice(choice, attack_type, ghost_hp):
    global low_health_playing

    if choice == "1":
        weapon = choose_weapon()
        hit_chance, damage = get_weapon_stats(weapon)

        if random.random() < hit_chance:
            play_weapon_sound(weapon)
            pygame.mixer.Sound(resource_path(os.path.join("music", "ghost_encounter", "ghost_hurt.mp3"))).play()
            typewriter(f"Your {weapon} hits the ghost!\n")
            ghost_hp -= damage
        else:
            pygame.mixer.Sound(resource_path(os.path.join("music", "ghost_encounter", "damaged_player.mp3"))).play()
            typewriter("You miss and the ghost hits you!\n")
            health_system.health -= 15

    elif choice == "2":
        dodge_chance = 1.0 - (0.5 if not health_system.leg_okay else 0)

        if random.random() < dodge_chance:
            pygame.mixer.Sound(resource_path(os.path.join("music", "ghost_encounter", "dodge.mp3"))).play()
            typewriter("You dodge successfully!\n")

            if attack_type == "charge":
                pygame.mixer.Sound(resource_path(os.path.join("music", "ghost_encounter", "fists.wav"))).play()
                pygame.mixer.Sound(resource_path(os.path.join("music", "ghost_encounter", "ghost_hurt.mp3"))).play()
                typewriter("You counterattack while the ghost is off balance!\n")
                ghost_hp -= 1
        else:
            typewriter("You fail to dodge!\n")
            pygame.mixer.Sound(resource_path(os.path.join("music", "ghost_encounter", "damaged_player.mp3"))).play()
            health_system.health -= 15

    elif choice == "3":
        if attack_type == "attack":
            pygame.mixer.Sound(resource_path(os.path.join("music", "ghost_encounter", "block.mp3"))).play()
            pygame.mixer.Sound(resource_path(os.path.join("music", "ghost_encounter", "ghost_hurt.mp3"))).play()
            typewriter("You block the attack and hurt the ghost!\n")
            ghost_hp -= 1
        else:
            typewriter("The attack breaks through your block!\n")
            pygame.mixer.Sound(resource_path(os.path.join("music", "ghost_encounter", "damaged_player.mp3"))).play()
            health_system.health -= 10

    elif choice == "4" and "potion" in inventory:
        pygame.mixer.Sound(resource_path(os.path.join("music", "ghost_encounter", "potion.mp3"))).play()
        inventory.remove("potion")
        health_system.health = min(health_system.health + 50, health_system.max_health)
        typewriter("You healed 50 HP.\n")

    else:
        typewriter("You freeze up!\n")
        health_system.health -= 5

    # ---------- LOW HEALTH LOOP ----------
    if health_system.health > 0 and health_system.health <= 20:
        if not low_health_playing:
            low_health_sound.play(loops=-1)
            low_health_playing = True
    else:
        if low_health_playing:
            low_health_sound.stop()
            low_health_playing = False

    typewriter(
        f"Your health: {health_system.health}/{health_system.max_health} | "
        f"Ghost HP: {max(ghost_hp, 0)}\n"
    )

    return ghost_hp
