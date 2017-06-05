import statesfxmixer


class SFXMixer:
    def __init__(self, path, state_mngr):
        self.statemixer = statesfxmixer.StateSFXMixer(path, state_mngr)

    def mix(self):
        self.statemixer.mix_state()

    def mix_now(self, state_string):
        self.statemixer.mix_now(state_string)