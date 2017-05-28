import pygame
from point import *
from  renderer import *
from inputmanager import *

class Player:
    def __init__(self):
        self.position = Point()
        self.renderer = InfiniAnimation("resources/player/")
        self.constraints = None
        self.active = True
        self.position.x = 200
        self.position.y = 500

    def run(self):
        self.move()

    def move(self):
        if input_manager.right_pressed:
            self.position.add_up(5, 0)
            self.renderer.flipped = False
            self.renderer.staterender.state = "move"
        elif input_manager.left_pressed:
            self.position.add_up(-5, 0)
            self.renderer.flipped = True
            self.renderer.staterender.state = "move"
        # elif input_manager.down_pressed:
        #     self.position.add_up(0, 5)
        #     self.renderer.staterender.state = "move"
        # elif input_manager.up_pressed:
        #     self.position.add_up(0, -5)
        #     self.renderer.staterender.state = "move"
        else:
            self.renderer.staterender.state = "normal"

        if self.constraints is not None:
            self.constraints.make(self.position)