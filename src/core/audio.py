import pygame
from src.core.settings import click_sound_path, water_flow_sound_path

def play_click_sound():
    """
    Plays the click sound effect. 
    Complexity: O(1) - Plays a sound with no iteration or recursion.
    """
    pygame.mixer.Sound(click_sound_path).play()

def play_water_flow_sound():
    """
    Plays the water flow sound effect.
    Complexity: O(1) - Plays a sound with no iteration or recursion.
    """
    pygame.mixer.Sound(water_flow_sound_path).play()
