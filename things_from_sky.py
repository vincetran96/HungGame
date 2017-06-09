import pygame
import inspect
from point import *
from renderer import *
from gamemanager import *
from physics import *
from constraints import *
from boxcollider import *
import random
from object_state import ObjectState
from settings import *
# from player import Player


class Things_from_sky:
    def __init__(self):
        self.active = True
        self.position = Point()
        self.vel = Point()
        self.acc = Point()
        self.sfx_mixer = None
        self.constraints = None
        self.ground_hit = 0
        self.position.x = random.randrange(50, WIDTH - 50)
        self.vel.x = random.choice((-5, 0, 5))
        self.vel.y = 3
        self.acc.y = 0.01995
        physics.add_fruits(self)
        game_manager.add(self)

    def run(self):
        if self.active:
            self.vel.add_up(0, self.acc.y)
            self.position.add_up(self.vel.x, self.vel.y + 0.5 * self.acc.y)
            self.flip()


# EDIBLE
class Edible(Things_from_sky):
    def __init__(self):
        Things_from_sky.__init__(self)
        self.state_mngr = ObjectState("edible")

    def flip(self):
        if self.vel.x < 0:
            self.renderer.staterender.flipped = True
        if self.vel.x > 0:
            self.renderer.staterender.flipped = False


class Fly(Edible):
    def __init__(self):
        Edible.__init__(self)
        self.renderer = InfiniAnimation("resources/fly/", self.state_mngr)
        self.box_collider = BoxCollider(self.position, self.renderer.width+30, self.renderer.height+30)


# NON EDIBLE
class NonEdible(Things_from_sky):
    def __init__(self):
        Things_from_sky.__init__(self)
        self.state_mngr = ObjectState("non_edible")


class Fruit(NonEdible):
    def __init__(self):
        NonEdible.__init__(self)
        self.renderer = loadSpriteRenderer("resources/fruit/normal.png", flip_path="resources/fruit/flip_normal.png")
        self.box_collider = BoxCollider(self.position, self.renderer.width, self.renderer.height)
    def flip(self):
        if self.vel.x < 0:
            self.renderer.flipped = True
        if self.vel.x > 0:
            self.renderer.flipped = False


class Bird(NonEdible):
    def __init__(self):
        NonEdible.__init__ (self)
        self.renderer = InfiniAnimation ("resources/bird/", self.state_mngr)
        self.box_collider = BoxCollider(self.position, self.renderer.width, self.renderer.height)
    def flip(self):
        if self.vel.x < 0:
            self.renderer.staterender.flipped = True
        if self.vel.x > 0:
            self.renderer.staterender.flipped = False

class Things_from_sky:
    def __init__(self):
        self.active = True
        self.position = Point()
        self.vel = Point()
        self.acc = Point()
        self.sfx_mixer = None
        self.constraints = None
        self.ground_hit = 0
        self.position.x = random.randrange(50, WIDTH - 50)
        self.vel.x = random.choice((-5, 0, 5))
        self.vel.y = 3
        self.acc.y = 0.01995
        physics.add_fruits(self)
        game_manager.add(self)


# TRAP
