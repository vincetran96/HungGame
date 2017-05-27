class Physics:
    def __init__(self):
        self.game_objects = []

    def add(self, game_object):
        self.game_objects.append(game_object)

    def check_contact(self, box_collider):
        for game_object in self.game_objects:
            if game_object.active: #Chỉ check những object active
                box_collider1 = box_collider
                box_collider2 = game_object.box_collider
                if box_collider1.check_collide(box_collider2):
                    return game_object

    def wall_bouncing(self, fruit):
        if fruit.position.x == 0 or fruit.position.x == 400:
            fruit.direction_x = fruit.direction_x * (-1)



physics = Physics()