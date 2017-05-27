class GameManager:
    def __init__(self):
        self.game_objects = []

    def add(self, game_object):
        self.game_objects.append(game_object)

    def run(self):
        for game_object in self.game_objects:
            if game_object.active:
                game_object.run()

    def draw(self, screen):
        for game_object in self.game_objects:
            if game_object.active:
                renderer = game_object.renderer
                position = game_object.position
                renderer.draw(screen, position)

game_manager = GameManager()