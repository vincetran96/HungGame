from point import *
from renderer import *
from sfx_mixer import *
from inputmanager import *
import levels
from object_state import ObjectState
from nonedible import *
from edible import *
from health_bar import *
from trap import *


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
        self.box_collider = BoxCollider(self.position, 90, 10)
        self.eat_counter = levels.Counter(120)                                  # ABOUT 2-frames DELAY, SO FROM 69 TO 120
        self.roll_counter = levels.Counter(100)
        self.move_disabled = False
        #physics.add(self) # NO NEED TO ADD self

    def run(self):
        self.check()
        self.move()

    def check(self):
        something = physics.check_contact(self.box_collider)
        if something is not None and type(something) is NonEdible:
            something.active = False
            health_bar.hp -= 50
            print("Your HP is {}".format(health_bar.hp))
        if something is not None and type(something) is Edible:
            # self.eat_counter += 1
            # OLD WAY OF MAKING EAT ANIMATION
            self.state_mngr.state = "eat"
            self.sfx_mixer.mix_now()
            something.active = False
        if something is not None and type(something) is Trap:
            self.move_disabled = True
            self.sfx_mixer.mix_now ()
            self.move_counter = levels.Counter(240)

    def move(self):
        if not self.move_disabled:
            self.rightleft()
            self.roll()
        self.eat()
        self.key_cleared()
        self.release_move()

        if self.constraints is not None:
            self.constraints.make(self.position)

    # PART OF MOVE
    def rightleft(self):
        if input_manager.right_pressed:
            self.renderer.staterender.flipped = False
            self.state_mngr.state = "move"
            if input_manager.space_pressed:
                self.position.add_up(1, 0)
            else:
                self.position.add_up(5, 0)
            if not input_manager.right_pressed:
                self.state_mngr.state = "normal"

        elif input_manager.left_pressed:
            self.renderer.staterender.flipped = True
            self.state_mngr.state = "move"
            if input_manager.space_pressed:
                self.position.add_up(-1, 0)
            else:
                self.position.add_up(-5, 0)
            if not input_manager.left_pressed:
                self.state_mngr.state = "normal"

    # PART OF MOVE
    def roll(self):
        if input_manager.space_pressed:
            self.roll_counter.countdown()
            self.position.y = 530                       # THIS WILL BE REMOVED LATER AS RESIZED IMAGE IS AVAILABLE
            # self.box_collider.position.y = 530        # THIS WILL BE ADDED LATER AS RESIZED IMAGE IS AVAILABLE
            if self.roll_counter.countdown():
                self.state_mngr.state = "roll"
            else:
                self.state_mngr.state = "preroll"
                if input_manager.space_play:
                    self.sfx_mixer.mix_now()
                    input_manager.space_play = False
        if not input_manager.space_pressed:
            self.roll_counter.reset()
            self.position.y = 500

    # PART OF MOVE
    def eat(self):
        if self.state_mngr.state == "eat":
            self.eat_counter.countdown()
        # OLD WAY OF MAKING EAT ANIMATION
        # print (self.eat_counter)
        # IN key_cleared CONDITION, TETE CAN ONLY SPEND 5 OR 6 FRAMES FOR EATING (HE CANNOT EAT FOREVER!),
        # SO THE ANIMATION MUST STOP
        # WHY 69 HERE? THERE ARE 7 EATING FRAMES, BUT EACH EATING FRAMES TAKES 10 GAME FRAMES TO BE RENDERED (SEE
        # staterender MODULE)
            if self.eat_counter.countdown():
                self.eat_counter.reset()
                self.state_mngr.state = "normal"

        # if self.eat_counter > 0:
        #     self.state_mngr.state = "eat"
        #     if self.eat_counter == 69:
        #         self.eat_counter = 0
        #         self.state_mngr.state = "normal"

    # PART OF MOVE
    def key_cleared(self):
        if input_manager.all_key_cleared:
            if self.state_mngr.state != "eat":
                self.renderer.staterender.state = "normal"
                self.state_mngr.state = self.state_mngr.states[0]
                self.position.y = 500

    # PART OF MOVE
    def release_move(self):
        if self.move_disabled:
            self.state_mngr.state = "trap"
            self.position.y = 550

            if input_manager.left_pressed:
                self.renderer.staterender.flipped = True
            if input_manager.right_pressed:
                self.renderer.staterender.flipped = False

            self.move_counter.countdown()
            if self.move_counter.countdown():
                self.move_disabled = False
                self.state_mngr.state = "normal"