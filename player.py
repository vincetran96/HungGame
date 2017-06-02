from point import *
from renderer import *
from sfx_mixer import *
from inputmanager import *
from object_state import ObjectState
from nonedible import *
from edible import *
from health_bar import *



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
        self.eat_counter = 0
        physics.add(self)


    def run(self):
        self.move()
        self.check_eat()


    def check_eat(self):
        something = physics.check_contact(self.box_collider)
        if something is not None and type(something) is NonEdible:
            something.active = False
            health_bar.hp -= 50
            print ("Your HP is {}".format(health_bar.hp))
        if something is not None and type(something) is Edible:
            # self.eat_counter += 1
            # OLD WAY OF MAKING EAT ANIMATION
            something.active = False
            self.state_mngr.state = "eat"
            #self.eat()


    def move(self):
        self.rightleft()

        self.roll()

        self.eat()

        self.key_cleared()

        if self.constraints is not None:
            self.constraints.make(self.position)

    # PART OF MOVE
    def rightleft(self):
        if input_manager.right_pressed:
            if input_manager.space_pressed:
                self.position.add_up(15, 0)
            else:
                self.position.add_up(5, 0)
            self.renderer.staterender.flipped = False
            self.state_mngr.state = "move"
            if input_manager.right_pressed == False:
                self.state_mngr.state = "normal"

        elif input_manager.left_pressed:
            if input_manager.space_pressed:
                self.position.add_up(-15, 0)
            else:
                self.position.add_up(-5, 0)
            self.renderer.staterender.flipped = True
            self.state_mngr.state = "move"
            if input_manager.left_pressed == False:
                self.state_mngr.state = "normal"

    # PART OF MOVE
    def roll(self):
        if input_manager.space_pressed:
            self.position.y = 530                   # THIS WILL BE REMOVED LATER AS RESIZED IMAGE IS AVAILABLE
            self.state_mngr.state = "roll"
            #self.box_collider.position.y = 530     # THIS WILL BE ADDED LATER AS RESIZED IMAGE IS AVAILABLE
        if not input_manager.space_pressed:
            self.position.y = 500

    # PART OF MOVE
    def eat(self):
        # IN key_cleared CONDITION, TETE CAN ONLY SPEND 5 OR 6 FRAMES FOR EATING (HE CANNOT EAT FOREVER!), SO THE ANIMATION MUST STOP

        # OLD WAY OF MAKING EAT ANIMATION
        if self.state_mngr.state == "eat":
            self.eat_counter += 1
            #print (self.eat_counter)
            if self.eat_counter == 69:
                self.eat_counter = 0
                self.state_mngr.state = "normal"

        # if self.eat_counter > 0:
        #     self.state_mngr.state = "eat"
        #     if self.eat_counter == 70:
        #         self.eat_counter = 0
        #         self.state_mngr.state = "normal"

    # PART OF MOVE
    def key_cleared(self):
        if input_manager.all_key_cleared:
            if self.state_mngr.state != "eat":
                self.renderer.staterender.state = "normal"
                self.state_mngr.state = self.state_mngr.states[0]
                self.position.y = 500