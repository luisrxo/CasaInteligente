import pygame
from threading import Thread

def play_sound():
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

class Bocina(object):
    def __init__(self, path, name):
        self.name = name
        self.path = path
        pygame.mixer.init()
        pygame.mixer.music.load(path)

    def on(self):
        Thread(target=play_sound).start()

    def off(self):
        pygame.mixer.music.stop()