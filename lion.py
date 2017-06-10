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
        self.position.x = -self.renderer.width
        self.sfx_mixer = SFXMixer("resources/lion/", self.state_mngr)
        self.constraints = None
        self.box_collider = BoxCollider (self.position.add(160, 20), self.renderer.width - 160, self.renderer.height - 20)
        self.atk_counter = settings.Counter(n_frames=240)
        physics.add(self)
        game_manager.add(self)
        level_manager.has_lion = True

    def run(self):
        self.atk_counter.countdown()
        if self.atk_counter.countdown():
            self.state_mngr.state = "attack"
            self.attack()
        self.disappear()

    # PART OF RUN
    def attack(self):
        step = random.choice((2,8,30))
        self.position.add_up(step, 0)
        self.box_collider.position.add_up(step, 0)

    # def retreat(self):
    #     if self.atk_time in range(0, 130):
    #         self.state_mngr.state = "retreat"
    #         self.position.add_up(-2, 0)

    def disappear(self):
        if self.position.x >= WIDTH + self.renderer.width:
            level_manager.lion_left = pygame.time.get_ticks()
            level_manager.has_lion = False
            self.active = False
