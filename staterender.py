from glob import glob
import pygame


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