import pygame


class StateSFXMixer:
    def __init__(self, path, state_mngr):
        self.path = path
        self.mixer_state_mngr = state_mngr

        self.sfx_dict = {}
        for state in self.mixer_state_mngr.states[1:]:
            # ASSUMING THERE IS ONLY 1 SOUND FOR EACH STATE
            path = self.path + "sounds/" + state + ".wav"
            #paths = sorted(glob(self.path + "sounds/" + state + ".wav"))
            self.sfx_dict[state] =  pygame.mixer.Sound(path)

        self.counter = 0

    def mix_state(self):
        self.counter += 1
        if self.counter == 5:
            self.counter = 0
            current_state = self.mixer_state_mngr.state
            try:
                sound = self.sfx_dict[current_state]
                pygame.mixer.Sound.play(sound)
            except Exception:
                pass
