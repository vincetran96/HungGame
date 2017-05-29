import pygame
from point import *
from renderer import *
from gamemanager import *
from physics import *
from constraints import *
from boxcollider import *
from player import *

class Edible:
    def __init__(self):
        self.active = True
        self.position = Point()
        self.renderer = loadSpriteRenderer("resources/edible.png")
        self.box_collider = BoxCollider(self.position, self.renderer.width, self.renderer.height)
        self.constraints = None
        self.direction_x = 0
        self.direction_y = 5
        self.box_collider = BoxCollider(self.position, 32, 32)
        self.ground_hit = 0

    def run(self):
        self.position.add_up(self.direction_x, self.direction_y)

        eaten_edible = physics.check_contact(self.box_collider)
        if eaten_edible is not None and type(eaten_edible) is Edible:
            self.active = False
            eaten_edible.active = False
            print("XXX")
