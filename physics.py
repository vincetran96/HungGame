class Physics:
    def __init__(self):
        self.game_objects = []
        self.fruits = []

    def add(self, game_object):
        self.game_objects.append(game_object)

    def add_fruits(self, game_object):
        self.fruits.append(game_object)

    def check_contact(self, box_collider):
        for game_object in self.game_objects:
            if game_object.active == True:
                box_collider1 = box_collider
                box_collider2 = game_object.box_collider
                if box_collider1.check_collide(box_collider2):
                    return game_object

    def check_hit_wall(self):
        for fruit in self.fruits:
            if fruit.position.x <= 0 or fruit.position.x >= 400:
                #print ("VA CHAM")
                fruit.direction_x = fruit.direction_x * -1
            if fruit.direction_x <= 0:
                fruit.renderer.flipped = True

   def check_hit_ground(self):
        for fruit in self.fruits:
            if fruit.position.x <= 0 or fruit.position.x >= 400:
                #print ("VA CHAM")
                fruit.direction_x = fruit.direction_x * -1
            if fruit.direction_x <= 0:
                fruit.renderer.flipped = True
physics = Physics()