from CasaInteligente.components.bocina import Bocina
import time
from threading import Thread

def set_bocina():
    bocina = Bocina("./Song.mp3", "Bocina1")
    bocina.on()
    time.sleep(1)

def main():
    Thread(target=set_bocina).start()

if __name__ == "__main__":
    main()

