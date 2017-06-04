import pygame
class LevelManager:
    def __init__(self):
        self.active = True

level_manager = LevelManager()

class Counter:
    def __init__(self, n_frames):
        self.time = n_frames
        self.counter = self.time
    def countdown(self):
        self.counter -= 1
        if self.counter < 0:
            return True
    def reset(self):
        self.counter = self.time




# game options/settings
TITLE = "Hứng game"
WIDTH = 800
HEIGHT = 600
FPS = 60
FONT_NAME = 'arial'
GROUND_y = 530

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)

def draw_text( screen, text, size, color, x, y): #For score and player's status
    font_name = pygame.font.match_font(FONT_NAME)
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)