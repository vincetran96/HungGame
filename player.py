import inspect
from point import *
from renderer import *
from sfx_mixer import *
from inputmanager import *
import settings
from object_state import ObjectState
from nonedible import *
from edible import *
from health_bar import *
from trap import *
from settings import *


class Player:
    def __init__(self):
        self.position = Point()
        self.state_mngr = ObjectState("player")
        self.renderer = InfiniAnimation("resources/player/", self.state_mngr)
        self.sfx_mixer = SFXMixer("resources/player/", self.state_mngr)
        self.constraints = None
        self.active = True
        self.position.x = 200
        self.position.y = GROUND_y - self.renderer.height
        self.box_collider = BoxCollider(self.position, self.renderer.width, 10)
        self.eat_counter = settings.Counter(120)      # ABOUT 2-frames DELAY, SO FROM 69 TO 120,......,
        self.roll_counter = settings.Counter(100)
        self.move_disabled = False
        self.score = 0
        self.missed_edibles = 0
        #physics.add(self) # NO NEED TO ADD self

    def run(self):
        self.check()
        self.move()

    def check(self):
        something = physics.check_contact(self.box_collider)
        if something is not None and NonEdible in inspect.getmro(type(something)):
            print ("EATEN")
            something.active = False
            self.score -= 10
            print("Your Score is {}".format(self.score))

        if something is not None and Edible in inspect.getmro(type(something)):
            # self.eat_counter += 1
            # OLD WAY OF MAKING EAT ANIMATION
            self.state_mngr.state = "eat"
            self.sfx_mixer.mix_now()
            something.active = False
            self.score += 10
            
        # if something is not None and type(something) is Trap:
        #     print ("TRAPPED!")
        #     self.move_disabled = True
        #     self.move_counter = 0

            self.sfx_mixer.mix_now()
            something.active = False
        if something is not None and type(something) is Trap and not self.move_disabled:
            print("TRAP!")
            self.move_disabled = True
            self.sfx_mixer.mix_now("trap")
            self.move_counter = settings.Counter(240)



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
            self.position.y = GROUND_y - self.renderer.height
            # THIS WILL BE REMOVED LATER AS RESIZED IMAGE IS AVAILABLE
            # THIS WILL BE ADDED LATER AS RESIZED IMAGE IS AVAILABLE
            # self.box_collider.position.y = 530
            if self.roll_counter.countdown():
                self.state_mngr.state = "roll"
            else:
                self.state_mngr.state = "preroll"
                if input_manager.space_play:
                    self.sfx_mixer.mix_now()
                    input_manager.space_play = False
        if not input_manager.space_pressed:
            self.roll_counter.reset()
            self.position.y = GROUND_y - self.renderer.height

    # PART OF MOVE
    def eat(self):
        if self.state_mngr.state == "eat":
            self.eat_counter.countdown()
        # IN key_cleared CONDITION, TETE CAN ONLY SPEND 5 OR 6 FRAMES FOR EATING (HE CANNOT EAT FOREVER!),
        # SO THE ANIMATION MUST STOP
        # WHY 69 HERE? THERE ARE 7 EATING FRAMES, BUT EACH EATING FRAMES TAKES 10 GAME FRAMES TO BE RENDERED (SEE
        # staterender MODULE)
            if self.eat_counter.countdown():
                self.eat_counter.reset()
                self.state_mngr.state = "normal"

    # PART OF MOVE
    def key_cleared(self):
        if input_manager.all_key_cleared:
            if self.state_mngr.state != "eat":
                self.renderer.staterender.state = "normal"
                self.state_mngr.state = self.state_mngr.states[0]
                self.position.y = GROUND_y - self.renderer.height

    # PART OF MOVE
    def release_move(self):
        if self.move_disabled:
            self.state_mngr.state = "trap"
            self.position.y = GROUND_y - self.renderer.height

            if input_manager.left_pressed:
                self.renderer.staterender.flipped = True
            if input_manager.right_pressed:
                self.renderer.staterender.flipped = False

            self.move_counter.countdown()
            if self.move_counter.countdown():
                self.move_disabled = False
                self.state_mngr.state = "normal"
