# Importación de clases Bocina y Bluetooth
from CasaInteligente.components.bocinaU import Bocina
from CasaInteligente.components.bluetooth import Bluetooth
# Importación de clase time
import time
# Importación de clase Thread
from threading import Thread

# Función set_bocina
# Crea un objeto bocina, indicando la ruta de una canción
def set_bocina():
    bocina = Bocina("./Song.mp3", "Bocina1")
    return bocina

# Función reproduce_bocina
# Reproduce las canciones del objeto bocina proporcionado
def reproduce_bocina(speaker):
    speaker.on()

# Función detiene_bocina
# Detiene la reproducción de la canción del objeto bocina proporcionado
def detiene_bocina(speaker):
    speaker.off()
    
# Función sube_vol
# Incrementa el volumen de la bocina proporcionada
def sube_vol(speaker):
    volumen = speaker.get_volume()
    if volumen <= 0.8:
        volumen += 0.2
        speaker.set_volume(volumen)

# Función baja_vol
# Decrementa el volumen de la bocina proporcionada
def baja_vol(speaker):
    volumen = speaker.get_volume()
    if volumen >= 0.2:
        volumen -= 0.2
        speaker.set_volume(volumen)

# Función set_bluetooth
# Crea un objeto Bluetooth
# Proporciona el objeto a controlar, así como los métodos para cada uno de las partes del BlueDot (arriba, abajo, derecha, izquierda)
def set_bluetooth(nombre, objeto, metArr, metAb, metDer, metIzq):
    bluetooth = Bluetooth(nombre, objeto, metArr, metAb, metDer, metIzq)

# Función main
# Manda a llamar a la creación de la bocina, así como la ejecución de la interfaz bluetooth
def main():
    speaker = set_bocina()
    Thread(target=set_bluetooth, args=("Bluetooth1", speaker, sube_vol, baja_vol, reproduce_bocina, detiene_bocina)).start()

# Ejecución
if __name__ == "__main__":
    main()

