import pygame
from point import *
from renderer import *
from gamemanager import *
from physics import *
from constraints import *
from boxcollider import *
import random
from object_state import ObjectState
from player import Player
from health_bar import *

class NonEdible:
    def __init__(self):
        self.active = True
        self.position = Point()
        self.state_mngr = ObjectState("non_edible")
        self.state_mngr.state = "move"
        self.renderer = InfiniAnimation("resources/non_edible/", self.state_mngr)
        self.sfx_mixer = None
        self.box_collider = BoxCollider(self.position, self.renderer.width, self.renderer.height)
        self.constraints = None
        self.direction_x = random.choice((-5,0,5))
        self.direction_y = 5
        self.ground_hit = 0

    def run(self):
        self.position.add_up(self.direction_x, self.direction_y)
        
        if self.position.y >= 600:
            self.active = False

        if self.direction_x < 0:
            self.renderer.staterender.flipped = True
        if self.direction_x > 0:
            self.renderer.staterender.flipped = False

        target = physics.check_contact(self.box_collider)
        if target is not None and type(target) is Player:
            self.active = False
