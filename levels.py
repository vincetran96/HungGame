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

class game:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.FPS = 60
        self.game_title = "Hung Game"

    def draw_text(self, screen, text, size, color, x, y): #For score and player's status
        font_name = pygame.font.match_font('arial')
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text_surface, text_rect)

game = game()