import pygame
from point import *
from renderer import *

class Background:
    def __init__(self):
        self.image = pygame.image.load("resources/background.png")
        self.position = Point()
        self.renderer = SpriteRenderer(pygame.image.load("resources/background.png"))


    def run(self):
        pass