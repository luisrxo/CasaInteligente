import pygame
from threading import Thread
from youtube_dl import YoutubeDL
from youtubesearchpython import VideosSearch
import sys
import os
import time
import wave

def play_sound():
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

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
        #pygame.mixer.init()
        #pygame.mixer.music.load(path)

    def on(self):
        """
        Crea un Thread para reproducir el archivo
        """        
        Thread(target=play_sound).start()

    def off(self):
        """
        Detiene la reproducción
        """        
        pygame.mixer.music.stop()

    def search(self, query):
        videosSearch = VideosSearch(query, limit=1)
        result = videosSearch.result()
        url = result["result"][0]["link"]
        name = result["result"][0]["title"]
        return url, name

    def download_video(self, url):
        audio_downloder = YoutubeDL({'format':'bestaudio', 'outtmpl': 'download.webm'})
        audio_downloder.download([url])
        return

    def video_to_mp3(self, file_name):
        """ Transforms video file into a MP3 file """
        try:
            file, extension = os.path.splitext(file_name)
            os.remove("{file}{ext}".format(file=file,ext=".wav"))
            # Convert video into .wav file
            inst = 'ffmpeg -i {file}{ext} {file}.wav'.format(file=file, ext=extension)
            os.system(inst)
            # Convert .wav into final .mp3 file
            #os.system('lame {file}.wav {file}.mp3'.format(file=file))
            #os.remove('{}.wav'.format(file))  # Deletes the .wav file
            print('"{}" successfully converted into WAV!'.format(file_name))
        except OSError as err:
            print(err.reason)
            return


    def play(self,query):
        url, video_name = self.search(query)
        name = "download"
        if os.path.exists("download.webm"):
            os.remove("download.webm")
        self.download_video(url)
        self.video_to_mp3(name + ".webm")
        file_wav = wave.open(name+".wav")
        frequency = file_wav.getframerate()
        pygame.mixer.init(frequency=frequency)
        pygame.mixer.music.load(name+".wav")
        self.on()
        return video_name
