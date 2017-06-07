import pygame
import inspect
from point import *
from renderer import *
from gamemanager import *
from physics import *
from constraints import *
from boxcollider import *
from player import *
import random
from object_state import ObjectState
from settings import *


# class Edible:
#     def __init__(self):
#         self.active = True
#         self.position = Point()
#         self.vel = Point()
#         self.acc = Point()
#         self.state_mngr = ObjectState("edible")
#         self.sfx_mixer = None
#         self.constraints = None
#         self.ground_hit = 0
#         self.position.x = random.randrange(50, WIDTH - 50)
#         self.vel.x = random.choice((-5, 0, 5))
#         self.vel.y = 5
#         self.acc.y = 0.01
#         physics.add_fruits(self)
#         game_manager.add(self)
#
#     def run(self):
#         if self.active:
#             self.vel.add_up(0, self.acc.y)
#             self.position.add_up(self.vel.x, self.vel.y + 0.5 * self.acc.y)
#             # if self.position.y >= 600:
#             #     self.active = False
#             self.flip()
#
#     # PART OF RUN
#     def flip(self):
#         if self.vel.x < 0:
#             self.renderer.staterender.flipped = True
#         if self.vel.x > 0:
#             self.renderer.staterender.flipped = False
#
# class Fly(Edible):
#     def __init__(self):
#         Edible.__init__(self)
#         self.renderer = InfiniAnimation("resources/fly/", self.state_mngr)
#         self.box_collider = BoxCollider(self.position, self.renderer.width, self.renderer.height)


# class Ant(Edible):
#     def __init__(self):
#         Edible.__init__(self)
#         self.renderer = InfiniAnimation("resources/ant/", self.state_mngr)
#         self.position.x = random.choice ((0, WIDTH))
#         self.position.y = GROUND_y - self.renderer.height
#         self.sfx_mixer = None
#         self.direction_x = ((self.position.x - WIDTH / 2) / abs(self.position.x - WIDTH / 2)) * -5
#         self.direction_y = 0
#         self.box_collider = BoxCollider (self.position, 2*self.renderer.width, 2*self.renderer.height)
#         physics.add_fruits (self)
#         game_manager.add (self)
#
#     def run(self):
#         if self.active:
#             self.position.add_up(self.direction_x, self.direction_y)
#             if self.position.y >= 600:
#                 self.active = False
#             self.flip()