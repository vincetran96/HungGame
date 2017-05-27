import pygame

class SpriteRenderer:
	def __init__(self, image):
		self.image = image
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.flipped = False

	def draw(self, screen, position):
		image_flipped = pygame.transform.flip(self.image, True, False)
		width = self.image.get_width()
		height = self.image.get_height()
		if self.flipped == False:
			screen.blit(self.image, (position.x - width / 2, position.y - height / 2))
		else:
			screen.blit(image_flipped, (position.x - width / 2, position.y - height / 2))


class Animation:
    def __init__(self, image_list):
        self.images = image_list
        self.width = self.images[0].get_width()
        self.height = self.images[0].get_height()
        self.image_index = 0
        self.has_ended = False
        self.counter = 0
        self.flipped = False

    # def draw(self, screen, position):
    # 	if self.flipped:
    # 		self.draw_flipped
    # 	elif self.flipped == False:
    # 		self.draw_normal

    # def draw_flipped(self, screen, position):
    # 	image = self.images[self.image_index]
    # 	image2 = pygame.transform.flip(image, True, False)

    def draw(self, screen, position):
        image = self.images[self.image_index]
        image_flipped = pygame.transform.flip(image, True, False)
        if self.flipped == False:
        	screen.blit(image, (position.x - self.width / 2, position.y - self.height / 2))
        else:
        	screen.blit(image_flipped, (position.x - self.width / 2, position.y - self.height / 2))

        max_frames = len(self.images) - 1
        self.counter += 1
        if self.counter == 10:
            self.counter = 0
            self.image_index = (self.image_index +1) % len(self.images)
            # if self.image_index == max_frames:
            #     self.has_ended = True


def loadSpriteRenderer(path):
    return SpriteRenderer(pygame.image.load(path))

def loadAnimation(paths):
    return Animation( [pygame.image.load(path) for path in paths] )
