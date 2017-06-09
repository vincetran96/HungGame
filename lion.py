import pygame
from point import *
from renderer import *
from gamemanager import *
from physics import *
from constraints import *
from boxcollider import *
import random
from object_state import ObjectState
from settings import *
from player import *


class Lion:
    def __init__(self):
        self.active = True
        self.position = Point ()
        self.state_mngr = ObjectState ("lion")
        self.renderer = InfiniAnimation ("resources/lion/", self.state_mngr)
        self.position.y = GROUND_y - self.renderer.height
        self.sfx_mixer = SFXMixer("resources/lion/", self.state_mngr)
        self.constraints = None
        self.box_collider = BoxCollider (self.position, self.renderer.width, self.renderer.height)
        self.atk_counter = settings.Counter(240)
        self.atk_time = 260
        physics.add(self)
        game_manager.add(self)

    def run(self):
        self.atk_counter.countdown()
        if self.atk_counter.countdown():
            self.attack()
            self.retreat()
            self.atk_time -= 1
            if self.atk_time < 0:                               # FINISH ATTACKING
                self.state_mngr.state = "normal"
                self.atk_time = 260
                self.atk_counter.reset()

    # PART OF RUN
    def attack(self):
        if self.atk_time in range(130, 260):
            self.state_mngr.state = "attack"
            self.position.add_up(2, 0)

    def retreat(self):
        if self.atk_time in range(0, 130):
            self.state_mngr.state = "retreat"
            self.position.add_up(-2, 0)
