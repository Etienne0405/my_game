import pygame
import os

pygame.mixer.init()

current_track = None

def play_music(track, loop=True):
    global current_track

    if current_track == track:
        return  # already playing this

    pygame.mixer.music.stop()

    path = os.path.join("music", track)
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(-1 if loop else 0)

    current_track = track


def stop_music():
    pygame.mixer.music.stop()
    global current_track
    current_track = None