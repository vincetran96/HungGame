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
    def __init__(self, path, state_mngr):
        self.staterender = staterender.StateRender(path, state_mngr)
        self.width = self.staterender.width
        self.height = self.staterender.height

    # DRAWING TASKS ARE ASSIGNED TO StateRender
    def draw(self, screen, position):
        self.staterender.draw_state(screen, position)
