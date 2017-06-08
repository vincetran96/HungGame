import inspect
from point import *
from renderer import *
from sfx_mixer import *
from inputmanager import *
import settings
from object_state import ObjectState
from things_from_sky import *
from health_bar import *
from trap import *
from settings import *


class Player:
    def __init__(self):
        self.position = Point()
        self.vel = Point()
        self.acc = Point()
        self.state_mngr = ObjectState("player")
        self.renderer = InfiniAnimation("resources/player/", self.state_mngr)
        self.sfx_mixer = SFXMixer("resources/player/", self.state_mngr)
        self.constraints = None
        self.active = True
        self.position.x = 200
        self.position.y = GROUND_y - self.renderer.height
        self.box_collider = BoxCollider(self.position, self.renderer.width, 50)
        self.eat_counter = settings.Counter(52)      # ABOUT 2-frames DELAY, SO FROM 29 TO 52......
        self.roll_counter = settings.Counter(100)
        self.move_disabled = False
        self.score = 0
        self.missed_edibles = 0

    def run(self):
        self.check()
        self.move()
        self.eat()
        self.key_cleared ()
        self.flip()

    def check(self):
        something = physics.check_contact(self.box_collider)
        if something is not None and NonEdible in inspect.getmro(type(something)):
            something.active = False
            self.score -= 10

        if something is not None and Edible in inspect.getmro(type(something)):
            self.state_mngr.state = "eat"
            self.sfx_mixer.mix_now("eat")
            something.active = False
            self.score += 100

        if something is not None and type(something) is Trap and not self.move_disabled:
            self.move_disabled = True
            self.state_mngr.state = "trap"
            self.sfx_mixer.mix_now("trap")
            self.move_counter = settings.Counter(240)
            something.begin_root = True

    def flip(self):
        if input_manager.right_pressed:
            self.renderer.staterender.flipped = False
        if input_manager.left_pressed:
            self.renderer.staterender.flipped = True

    def eat(self):
        if self.state_mngr.state == "eat":
            self.eat_counter.countdown ()
            # IN key_cleared CONDITION, TETE CAN ONLY SPEND 3 IMAGE-FRAMES FOR EATING (HE CANNOT EAT FOREVER!),
            # SO THE ANIMATION MUST STOP
            # THERE ARE 3 EATING FRAMES, BUT EACH EATING FRAMES TAKES 10 GAME FRAMES TO BE RENDERED (SEE
            # staterender MODULE)
            if self.eat_counter.countdown ():
                self.eat_counter.reset ()
                self.state_mngr.state = "normal"

    def move(self):
        if not self.move_disabled:
            self.rightleft()
            self.roll()
        self.release_move()

        if self.constraints is not None:
            self.constraints.make(self.position)

    # PART OF MOVE
    def rightleft(self):
        if input_manager.right_pressed:
            self.state_mngr.state = "move"
            if input_manager.space_pressed:
                self.position.add_up(1, 0)
            else:
                self.acc.x = PLAYER_ACC
                self.acc.add_up(self.vel.x * PLAYER_FRICTION,
                                self.vel.y * PLAYER_FRICTION)
                self.vel.add_up(self.acc.x, self.acc.y)
                self.position.add_up(self.vel.x + 0.5 * self.acc.x,
                                     self.vel.y + 0.5 * self.acc.y)
            if not input_manager.right_pressed:
                self.state_mngr.state = "normal"

        elif input_manager.left_pressed:
            self.state_mngr.state = "move"
            if input_manager.space_pressed:
                self.position.add_up(-1, 0)
            else:
                self.acc.x = -PLAYER_ACC
                self.acc.add_up(self.vel.x * PLAYER_FRICTION,
                                self.vel.y * PLAYER_FRICTION)
                self.vel.add_up(self.acc.x, self.acc.y)
                self.position.add_up(self.vel.x + 0.5 * self.acc.x,
                                     self.vel.y + 0.5 * self.acc.y)
            if not input_manager.left_pressed:
                self.state_mngr.state = "normal"

    # PART OF MOVE
    def roll(self):
        if input_manager.space_pressed:
            self.roll_counter.countdown()
            # THIS WILL BE REMOVED LATER AS RESIZED IMAGE IS AVAILABLE
            # THIS WILL BE ADDED LATER AS RESIZED IMAGE IS AVAILABLE
            # self.box_collider.position.y = 530
            if self.roll_counter.countdown():
                self.state_mngr.state = "roll"
            else:
                self.state_mngr.state = "preroll"
                if input_manager.space_play:
                    self.sfx_mixer.mix_now("preroll")
                    input_manager.space_play = False
        if not input_manager.space_pressed:
            self.roll_counter.reset()

    # PART OF MOVE
    def key_cleared(self):
        if input_manager.all_key_cleared:
            if self.state_mngr.state not in ["trap", "eat"]:
                self.state_mngr.state = self.state_mngr.states[0]

    # PART OF MOVE
    def release_move(self):
        if self.move_disabled:
            self.state_mngr.state = "trap"

            self.move_counter.countdown()
            if self.move_counter.countdown():
                self.move_disabled = False
                self.state_mngr.state = "normal"