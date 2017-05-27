import pygame
import staterender

class SpriteRenderer:
	def __init__(self, image):
		self.flipped = False
		self.image = image
		self.width = self.image.get_width()
		self.height = self.image.get_height()
        #self.flipped = False

	def draw(self, screen, position):
		egami = pygame.transform.flip(self.image, True, False)
		width = self.image.get_width()
		height = self.image.get_height()
		if self.flipped == False:
			screen.blit(self.image, (position.x - width / 2, position.y - height / 2))
		else:
			screen.blit(egami, (position.x - width / 2, position.y - height / 2))

def loadSpriteRenderer(path):
    return SpriteRenderer(pygame.image.load(path))


class InfiniAnimation:
    def __init__(self, path):
        self.staterender = staterender.StateRender(path)
        self.width = self.staterender.image_dict["normal"][0].get_width()
        self.height = self.staterender.image_dict["normal"][0].get_height()
        self.flipped = False
        self.image_index = 0
        self.has_ended = False
        self.counter = 0
        self.last_state = None
        

    # I CREATE current_state AND last_state TO SWITCH BETWEEN ANIMATIONS OF DIFFERENT STATES OF THE CHARACTER
    def draw(self, screen, position):
        current_state = self.staterender.state
        frames = self.staterender.image_dict[current_state]

        if self.last_state != current_state:
            self.image_index = 0

        image = frames[self.image_index]
        egami = pygame.transform.flip(image, True, False) 

        if self.flipped == False:
        	screen.blit(image, (position.x - self.width / 2, position.y - self.height / 2))
        else:
        	screen.blit(egami, (position.x - self.width / 2, position.y - self.height / 2))

        max_frames = len(frames) - 1
        self.counter += 1
        if self.counter == 10:
            self.counter = 0
            self.image_index = (self.image_index +1) % (max_frames + 1)        
            # if self.image_index == max_frames:
            #     self.has_ended = True
        self.last_state = current_state
