import pygame
from point import *
from renderer import *

class Background:
    def __init__(self):
        self.position = Point()
        self.renderer = SpriteRenderer(pygame.image.load("resources/background.png"))
<<<<<<< HEAD

background = Background()
=======
        self.active = True
        self.position.x += self.renderer.width / 2
        self.position.y += self.renderer.height / 2

>>>>>>> 298b073e59de0a6bd304603d7b359065aa35d05e
    def run(self):
        pass