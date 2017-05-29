import pygame
from point import *
from  renderer import *
from sfx_mixer import *
from inputmanager import *
from object_state import ObjectState
from staterender import StateRender

class Player:
    def __init__(self):
        self.position = Point()
        self.state_mngr = ObjectState("player")
        self.renderer = InfiniAnimation("resources/player/", self.state_mngr)
        self.sfx_mixer = SFXMixer("resources/player/", self.state_mngr)
        self.constraints = None
        self.active = True
        self.position.x = 200
        self.position.y = 500

    def run(self):
        self.move()

    def move(self):
        if input_manager.right_pressed:
            self.position.add_up(5, 0)
            self.renderer.staterender.flipped = False
            self.state_mngr.state = "move"
        elif input_manager.left_pressed:
            self.position.add_up(-5, 0)
            self.renderer.staterender.flipped = True
            self.state_mngr.state = "move"
        # elif input_manager.down_pressed:
        #     self.position.add_up(0, 5)
        #     self.renderer.staterender.state = "move"
        # elif input_manager.up_pressed:
        #     self.position.add_up(0, -5)
        #     self.renderer.staterender.state = "move"
        else:
            self.renderer.staterender.state = "normal"
            self.state_mngr.state = self.state_mngr.states[0]

        if self.constraints is not None:
            self.constraints.make(self.position)