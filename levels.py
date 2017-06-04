class LevelManager:
    def __init__(self):
        self.active = True

level_manager = LevelManager()


class Counter:
    def __init__(self, n_frames):
        self.time = n_frames
        self.counter = self.time

    def countdown(self):
        self.counter -= 1
        if self.counter < 0:
            return True

    def reset(self):
        self.counter = self.time

