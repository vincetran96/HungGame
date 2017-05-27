class Constraints:
    def __init__(self, min_x, max_x, min_y, max_y):
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y

    def clamp(self, value, min_value, max_value):
        value = min(value, max_value)
        value = max(value, min_value)
        return value

    def make(self, position):
        position.x = self.clamp(position.x, self.min_x, self.max_x)
        position.y = self.clamp(position.y, self.min_y, self.max_y)
