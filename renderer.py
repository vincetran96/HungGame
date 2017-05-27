import pygame

class SpriteRenderer:
	def __init__(self, image):
		self.image = image
		self.width = self.image.get_width()
		self.height = self.image.get_height()

	def draw(self, screen, position):
		width = self.image.get_width()
		height = self.image.get_height()
		screen.blit(self.image, (position.x - width / 2, position.y - height / 2))

def loadSpriteRenderer(path):
	return SpriteRenderer(pygame.image.load(path))