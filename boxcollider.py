from point import *
from pygame import Rect


class BoxCollider:
    def __init__(self, position, width, height):
        self.position = position
        self.width = width
        self.height = height

    def Print(self):
        print(self.position.x, self.position.y, self.width, self.height)

    def check_collide(self, other):
        rect1 = Rect(self.position.x, self.position.y,
                     self.width, self.height)

        rect2 = Rect(other.position.x, other.position.y,
                     other.width, other.height)

        return rect1.colliderect(rect2)

