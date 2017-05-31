import pygame
from point import *
from renderer import *
from gamemanager import *

class HealthBar:
    def __init__(self):
        self.active = True
        self.flipped = False
        self.position = Point()
        #self.renderer = loadSpriteRenderer("resources/player/health_bar.png")
        self.image = pygame.image.load("resources/player/health_bar.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.full_width = self.width
        self.full_hp = 1000
        self.hp = 1000

    def run(self):
        # CUT THE WIDTH OF THE BAR ACCORDING TO HEALTH
        k = self.hp / self.full_hp
        self.image = self.image.subsurface((0, 0, self.width * k, self.height))
        print (k)

    def draw(self, screen):
        screen.blit(self.image, (self.position.x, self.position.y))

health_bar = HealthBar()