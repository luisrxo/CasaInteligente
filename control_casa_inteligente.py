from CasaInteligente.components.bocinaU import Bocina
from CasaInteligente.components.bluetooth import Bluetooth
import time
from threading import Thread

def set_bocina():
    bocina = Bocina("./Song.mp3", "Bocina1")
    return bocina

def reproduce_bocina(speaker):
    speaker.on()

def detiene_bocina(speaker):
    speaker.off()
    
def sube_vol(speaker):
    volumen = speaker.get_volume()
    if volumen <= 0.8:
        volumen += 0.2
        speaker.set_volume(volumen)

def baja_vol(speaker):
    volumen = speaker.get_volume()
    if volumen >= 0.2:
        volumen -= 0.2
        speaker.set_volume(volumen)

def set_bluetooth(nombre, objeto, metArr, metAb, metDer, metIzq):
    bluetooth = Bluetooth(nombre, objeto, metArr, metAb, metDer, metIzq)

def main():
    #Thread(target=set_bocina).start()
    speaker = set_bocina()
    Thread(target=set_bluetooth, args=("Bluetooth1", speaker, sube_vol, baja_vol, reproduce_bocina, detiene_bocina)).start()

if __name__ == "__main__":
    main()

