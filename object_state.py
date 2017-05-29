# CLASS FOR MANAGING GAME OBJECT'S state, WHICH WILL BE USED FOR
# IMAGE AND SOUND FX RENDERING

class ObjectState:
    def __init__(self, object_str):
        if object_str == "player":
            self.states = ["normal", "move", "eat"]
        elif object_str == "edible" or object_str == "non_edible":
            self.states = ["normal", "move"]
        elif object_str == "background":
            self.states = ["normal"]

        # DEFAULT BEGINNING STATE
        self.state = self.states[0]