# CLASS FOR MANAGING state, WHICH WILL BE USED FOR
# IMAGE AND SOUND FX RENDERING


class ObjectState:
    def __init__(self, object_str):
        if object_str == "player":
            self.states = ["normal", "trap", "eat", "preroll", "hitted",
                           "roll", "move"]
        elif object_str == "edible" or object_str == "non_edible":
            self.states = ["move", "normal"]
        elif object_str == "trap":
            self.states = ["normal"]
        elif object_str == "lion":
            self.states = ["normal", "attack", "retreat", "hit"]

        # DEFAULT BEGINNING STATE
        self.state = self.states[0]