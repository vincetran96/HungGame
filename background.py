import pygame
from point import *
from renderer import *

class Background:
    def __init__(self):
        self.position = Point()
        self.renderer = loadSpriteRenderer("resources/background.png")
        self.sfx_mixer = None
        self.active = True

    def run(self):
        pass
    
background = Background()