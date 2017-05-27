from point import *
from pygame import Rect

class BoxCollider:
    def __init__(self, position, width, height):
        self.position = position
        self.width = width
        self.height = height


    def print(self):
        print(self.position.x, self.position.y, self.width, self.height)

    def check_collide(self, other):
        # self.print()
        # other.print()

        rect1 = Rect(self.position.x - self.width / 2,
                     self.position.y - self.height / 2,
                     self.width,
                     self.height)

        rect2 = Rect(other.position.x - other.width / 2,
                     other.position.y - other.height / 2,
                     other.width,
                     other.height)

        return rect1.colliderect(rect2)
