import pygame
from point import *
from renderer import *
from gamemanager import *
from physics import *
from constraints import *
from boxcollider import *
import random

class NonEdible:
    def __init__(self):
        self.active = True
        self.position = Point()
        self.renderer = InfiniAnimation("resources/non_edible/")
        self.renderer.staterender.state = "move"
        self.box_collider = BoxCollider(self.position, self.renderer.width, self.renderer.height)
        self.constraints = None
        self.direction_x = random.choice((-5,0,5))
        self.direction_y = 5

    def run(self):
        self.position.add_up(self.direction_x, self.direction_y)
        
        if self.position.y >= 600:
            self.active = False
        
        self.renderer.flipped = (self.direction_x < 0)

        target = physics.check_contact(self.box_collider)
        if target is not None and type(target) is Player:
            self.active = False
