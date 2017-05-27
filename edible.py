import pygame
from point import *
from renderer import *
from gamemanager import *
from physics import *
from constraints import *

class Edible:
	def __init__(self):
		self.active = True
		self.position = Point()
		self.renderer = loadSpriteRenderer("resources...")
		self.box_collider = BoxCollider(self.position, self.renderer.width, self.renderer.height)
		self.constraints = None

	def run(self):
		self.position.add_up(0, 10)
		target = physics.check_contact(self.box_collider)
		if target is not None and type(target) is Player:
			self.active = False