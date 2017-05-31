from point import *
from renderer import *
from sfx_mixer import *
from inputmanager import *
from object_state import ObjectState
from nonedible import *


class Player:
    def __init__(self):
        self.position = Point()
        self.state_mngr = ObjectState("player")
        self.renderer = InfiniAnimation("resources/player/", self.state_mngr)
        # self.sfx_mixer = SFXMixer("resources/player/", self.state_mngr)
        self.constraints = None
        self.active = True
        self.position.x = 200
        self.position.y = 500
        self.box_collider = BoxCollider(self.position, 90, 10)
        self.eat_counter = 0

    def run(self):
        self.move()

        something = physics.check_contact(self.box_collider)
        if something is not None and type(something) is NonEdible:
            self.state_mngr.state = "eat"
            something.active = False

    def move(self):
        self.rightleft()

        self.roll()

        self.eat()

        self.key_cleared()

        if self.constraints is not None:
            self.constraints.make(self.position)

    def rightleft(self):
        if input_manager.right_pressed:
            if input_manager.space_pressed:
                self.position.add_up(15, 0)
            else:
                self.position.add_up(5, 0)
            self.renderer.staterender.flipped = False
            self.state_mngr.state = "move"

        elif input_manager.left_pressed:
            if input_manager.space_pressed:
                self.position.add_up(-15, 0)
            else:
                self.position.add_up(-5, 0)
            self.renderer.staterender.flipped = True
            self.state_mngr.state = "move"

    def roll(self):
        if input_manager.space_pressed:
            self.position.y = 550
            self.state_mngr.state = "roll"
            #print (self.box_collider.position.x, self.box_collider.position.y)
        if not input_manager.space_pressed:
            self.position.y = 500

    def eat(self):
        if self.state_mngr.state == "eat":
            self.eat_counter += 1
            print (self.eat_counter)
            if self.eat_counter == 49:
                self.eat_counter = 0
                self.state_mngr.state = "normal"

    def key_cleared(self):
        if input_manager.all_key_cleared and self.eat_counter == 0:
            self.renderer.staterender.state = "normal"
            self.state_mngr.state = self.state_mngr.states[0]
            self.position.y = 500

        # elif input_manager.down_pressed:
        #     self.position.add_up(0, 5)
        #     self.renderer.staterender.state = "move"
        # elif input_manager.up_pressed:
        #     self.position.add_up(0, -5)
        #     self.renderer.staterender.state = "move"