import pygame
from glob import glob
from settings import *


class SpriteRenderer:
    def __init__(self, image, flip_image):
        self.flipped = False
        self.image = image
        self.flip_image = flip_image
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self, screen, position):
        if not self.flipped:
            screen.blit(self.image, (position.x, position.y))
        else:
            screen.blit(self.flip_image, (position.x, position.y))


def loadSpriteRenderer(path, **kwargs):
    if kwargs:
        return SpriteRenderer(pygame.image.load(path), pygame.image.load(kwargs.get("flip_path")))
    else:
        return SpriteRenderer(pygame.image.load(path), None)


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
            flip_paths = sorted((glob(self.path + "flip_" + state + "*.png")))
            self.image_dict[state]= dict(noflip = [ pygame.image.load(path) for path in paths ], \
                                         flip = [ pygame.image.load(path) for path in flip_paths ])

        self.width = self.image_dict["normal"]["noflip"][0].get_width()
        self.height = self.image_dict["normal"]["noflip"][0].get_height()
        self.flipped = False
        self.image_index = 0
        self.counter = FrameClock(n_frames=20)
        self.last_state = None

    # FUNCTION FOR DRAWING A PARTICULAR STATE
    def draw_state(self, screen, position):
        current_state = self.render_state_mngr.state

        if self.last_state != current_state:
            self.image_index = 0

        if not self.flipped:
            screen.blit(self.image_dict[current_state]["noflip"][self.image_index], (position.x, position.y))
        else:
            screen.blit(self.image_dict[current_state]["flip"][self.image_index], (position.x , position.y))

        max_frames = len(self.image_dict[current_state]["noflip"])

        # SLOW IT DOWN 10 game-frames, BUT THE countdown() method takes 2-frame delay (from 20 to 10)
        self.counter.countdown()
        if self.counter.countdown():
            self.counter.reset()
            self.image_index = (self.image_index + 1) % (max_frames)

        self.last_state = current_state


# frames = self.image_dict[current_state]
# image = frames[self.image_index]
# egami = pygame.transform.flip(image, True, False)

