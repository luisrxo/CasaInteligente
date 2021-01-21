import pygame
from threading import Thread

def play_sound():
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

def stop_sound():
    pygame.mixer.music.stop()

"""
Esta clase es para utilizar el jack 3.5 mm para reproducir sonido
"""
class Bocina(object):
    def __init__(self, path, name):
        """
        Constructor del objeto

        Args:
            path (str): Path donde se encuentra el archivo de sonido que se va a reproducir en la alarma
            name (str): Nombre del dispositivo
        """        
        self.name = name
        self.path = path
        pygame.mixer.init()
        pygame.mixer.music.load(path)

    def on(self):
        """
        Crea un Thread para reproducir el archivo
        """        
        Thread(target=play_sound).start()

    def off(self):
        """
        Detiene la reproducción
        """        
        Thread(target=stop_sound).start()
        #pygame.mixer.music.stop()

    def get_volume(self):
        return pygame.mixer.music.get_volume()

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(volume)
