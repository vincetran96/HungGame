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