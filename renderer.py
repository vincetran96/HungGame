import pygame
from glob import glob

class SpriteRenderer:
    def __init__(self, image):
        self.flipped = False
        self.image = image
        self.width = self.image.get_width()
        self.height = self.image.get_height()

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
        self.staterender = StateRender(path, state_mngr)
        self.width = self.staterender.width
        self.height = self.staterender.height

    # DRAWING TASKS ARE ASSIGNED TO StateRender
    def draw(self, screen, position):
        self.staterender.draw_state(screen, position)


class StateRender:
    def __init__(self, path, state_mngr):
        self.path = path
        self.render_state_mngr = state_mngr

        self.image_dict = {}
        for state in self.render_state_mngr.states:
            paths = sorted(glob(self.path + state + "*.png"))
            self.image_dict[state] = [ pygame.image.load(path) for path in paths ]

        self.width = self.image_dict["normal"][0].get_width()
        self.height = self.image_dict["normal"][0].get_height()
        self.flipped = False
        self.image_index = 0
        self.counter = 0
        self.last_state = None


    # FUNCTION FOR DRAWING A PARTICULAR STATE
    def draw_state(self, screen, position):
        current_state = self.render_state_mngr.state
        frames = self.image_dict[current_state]

        if self.last_state != current_state:
            self.image_index = 0

        image = frames[self.image_index]
        egami = pygame.transform.flip(image, True, False)

        if self.flipped == False:
            screen.blit(image, (position.x, position.y))
        else:
            screen.blit(egami, (position.x , position.y))

        max_frames = len(frames) - 1
        self.counter += 1
        # SLOW IT DOWN 10 TIMES
        if self.counter == 9:
            self.counter = 0
            self.image_index = (self.image_index + 1) % (max_frames + 1)

        self.last_state = current_state

