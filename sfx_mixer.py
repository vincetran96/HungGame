import pygame
import statesfxmixer

class SFXMixer:
    def __init__(self, path, state_mngr):
        self.statemixer = statesfxmixer.StateSFXMixer(path, state_mngr)

    def add(self, sound):
        self.sounds.append(sound)

    def play_sounds(self):
        for sound in self.sounds:
            pygame.mixer.Sound.play(sound)

#sound_manager = SoundManager()
