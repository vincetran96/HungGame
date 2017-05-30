import pygame

class InputManager:
    def __init__(self):
        self.right_pressed = False
        self.left_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.space_pressed = False
        self.all_key_cleared = True                     # THIS PROPERTY CHECKS IF ALL KEYS ARE RELEASED


    def run(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.all_key_cleared = False
                if event.key == pygame.K_RIGHT:
                    self.right_pressed = True
                if event.key == pygame.K_LEFT:
                    self.left_pressed = True
                if event.key == pygame.K_SPACE:
                    self.space_pressed = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.right_pressed = False
                if event.key == pygame.K_LEFT:
                    self.left_pressed = False
                if event.key == pygame.K_SPACE:
                    self.space_pressed = False

        if not (self.space_pressed or self.left_pressed or self.right_pressed or self.up_pressed or self.down_pressed):
            self.all_key_cleared = True

input_manager = InputManager()