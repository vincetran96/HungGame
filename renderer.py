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
    def __init__(self, image):
        self.image = image
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, screen, position):
        screen.blit(self.image, (position.x - self.width / 2,
                                 position.y - self.height / 2))


class Animation:
    def __init__(self, image_list):
        self.images = image_list
        self.width = self.images[0].get_width()
        self.height = self.images[0].get_height()
        self.image_index = 0
        self.has_ended = False
        self.counter = 0

    def draw(self, screen, position):
        image = self.images[self.image_index]
        screen.blit(image, (position.x - self.width / 2,
                                 position.y - self.height / 2))
        self.counter += 1
        if self.counter == 5:
            self.counter = 0
            self.image_index = (self.image_index +1) % len(self.images)
            if self.image_index == len(self.images) - 1:
                self.has_ended = True


def loadSpriteRenderer(path):
    return SpriteRenderer(pygame.image.load(path))

def loadAnimation(paths):
    return Animation( [pygame.image.load(path) for path in paths])
