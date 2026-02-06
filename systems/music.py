import pygame
import os
from utils.resource_path import resource_path

pygame.mixer.init()

current_track = None

def play_music(track, loop=True):
    global current_track

    pygame.mixer.music.stop()

    # Handle both "music/track.wav" and "track.wav" formats
    if track.startswith("music/"):
        path = resource_path(track)
    else:
        path = resource_path(os.path.join("music", track))
    
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(-1 if loop else 0)

    current_track = track


def stop_music():
    pygame.mixer.music.stop()
    global current_track
    current_track = None