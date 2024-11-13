import pygame
from settings import click_sound_path, water_flow_sound_path

def play_click_sound():
    pygame.mixer.Sound(click_sound_path).play()

def play_water_flow_sound():
    pygame.mixer.Sound(water_flow_sound_path).play()
