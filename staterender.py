from glob import glob
import pygame

class StateRender:
	def __init__(self, path):
		#path = resources/player/
		self.path = path
		self.state = "normal"
		self.state_list = ["normal", "eat", "move"]
		image_dict = {}
		for state in self.state_list:
			try:
				paths = sorted(glob(self.path + state + "*.png"))
				image_dict[state] = [ pygame.image.load(path) for path in paths ]
			except Exception:
				pass
		self.image_dict = image_dict

a = StateRender("resources/player/")
print (a.image_dict["normal"])