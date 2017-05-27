import pygame
from point import *
from renderer import *
from gamemanager import *
from physics import *
from constraints import *
from boxcollider import *

class Edible:
    def __init__(self):
        self.active = True
        self.position = Point()
        self.renderer = loadSpriteRenderer("resources/edible.png")
        self.box_collider = BoxCollider(self.position, self.renderer.width, self.renderer.height)
        self.constraints = None
        self.direction_x = 0
        self.direction_y = 5

    def run(self):
        self.position.add_up(self.direction_x, self.direction_y)
        target = physics.check_contact(self.box_collider)
        if target is not None and type(target) is Player:
            self.active = False
