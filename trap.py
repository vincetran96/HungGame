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

class Trap:
    def __init__(self):
        self.active = True
        self.position = Point()
        self.vel = Point()
        self.acc = Point()
        self.position.x = random.randrange(50, 750)
        self.state_mngr = ObjectState ("trap")
        self.renderer = loadSpriteRenderer("resources/trap/normal.png", flip_path="resources/trap/flip_normal.png")
        self.sfx_mixer = None
        self.constraints = None
        self.vel.x = random.choice ((-2, 0, 2))
        self.vel.y = 3
        self.ground_hit = 0
        self.box_collider = BoxCollider(self.position.add(105, 72), 120, 37)
        self.root_counter = Counter(240)
        self.begin_root = False
        physics.add_traps(self)
        game_manager.add(self)

    def run(self):
        if self.active:
            self.vel.add_up(0, self.acc.y)
            self.position.add_up(self.vel.x, self.vel.y + 0.5 * self.acc.y)
            self.flip()
        if self.begin_root:
            self.root_counter.countdown()
            if self.root_counter.counter == 189:
                self.vel.y, self.vel.x = 0, 0
            if self.root_counter.countdown():
                self.active = False
        self.flip ()

    def flip(self):
        if self.vel.x < 0:
            self.renderer.flipped = True
        if self.vel.x > 0:
            self.renderer.flipped = False
