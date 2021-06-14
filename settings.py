import pygame


class FrameClock:
    def __init__(self, **kwargs):
        self.frames = kwargs.get("n_frames", 0)
        self.counter = self.frames
        self.stopwatch = 0

    def countdown(self):
        self.counter -= 1
        if self.counter < 0:
            return True

    def countup(self):
        self.timer += 1

    def reset(self):
        self.counter = self.frames
        self.timer = 0


class LevelManager:
    def __init__(self):
        self.active = True
        self.has_lion = False
        self.lion_left = 0
        self.bird_spawn = 0
        self.fly_spawn = 0
        self.fruit_spawn = 0
        self.trap_spawn = 0

    def generate_obs(self):
        pass

level_manager = LevelManager()


# game options/settings
TITLE = "Pangolin Survival Game"
WIDTH = 800
HEIGHT = 600
FPS = 60
FONT_NAME = 'arial'
GROUND_y = 530
LOSING_SCORE = -20000

# Player properties
PLAYER_ACC = 1.0
PLAYER_FRICTION = -0.12
GRAVITY = 10
PLAYER_JUMP = 20

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


def draw_text( screen, text, size, color, x, y): #For score and player's status
    font_name = pygame.font.match_font(FONT_NAME)
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)


def check_lose(player):
    if player.missed_edibles >= 10:
        print ("NOOB")