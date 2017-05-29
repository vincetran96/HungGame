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
            if fruit.position.x <= 0 or fruit.position.x >= 800:
                fruit.direction_x = fruit.direction_x * -1            

    def check_hit_ground(self):
        for fruit in self.fruits:
            if fruit.ground_hit == 0 and fruit.position.y >= 530 :
                fruit.direction_y = fruit.direction_y * -0.7
                fruit.direction_x = fruit.direction_x * 0.8
                fruit.ground_hit += 1

            if fruit.ground_hit == 1 and fruit.position.y <= 480:
                fruit.direction_y = fruit.direction_y * -0.7
                fruit.direction_x = fruit.direction_x * 0.8
                fruit.ground_hit += 1

            if fruit.ground_hit == 2 and fruit.position.y >= 530:
                fruit.direction_y = fruit.direction_y * -1
                fruit.direction_x = fruit.direction_x * 0.8
                fruit.ground_hit += 1

            if fruit.ground_hit == 3 and fruit.position.y <= 500:
                fruit.direction_y = fruit.direction_y * -1
                fruit.direction_x = fruit.direction_x * 0.8
                fruit.ground_hit += 1

            if fruit.ground_hit == 4 and fruit.position.y >= 530:
                fruit.direction_x = 0
                fruit.direction_y = 0

physics = Physics()