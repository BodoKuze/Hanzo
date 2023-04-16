import pygame
import os
pygame.init()


class Background_Music:

    def __init__(self,track:int) -> None:
        self.track = [(fr"{os.getcwd()}\sfx\Track_A.wav"),
                      (fr"{os.getcwd()}\sfx\Track_B.wav"),
                      (fr"{os.getcwd()}\sfx\Track_C.wav"),
                      ][track]


    def play(self):
        
        pygame.mixer.music.load(self.track)
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(0.5)

    def stop(self):
        pygame.mixer.music.stop()

class Sound_Effect:

    def __init__(self,effect:str) -> None:
        self.sfx = pygame.mixer.Sound(fr"{os.getcwd()}\sfx\{effect}.wav")
        
    def play(self):
        self.sfx.play()