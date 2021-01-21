from CasaInteligente.components.foco import Foco
from CasaInteligente.components.persiana import Persiana
from gpiozero import LightSensor

from threading import Thread
from time import sleep

def set_foco():
    foco = Foco(2,"foco")
    foco.set_light_sensor(LightSensor(21))
    foco.use_light_sensor(debug=True)

def set_persiana():
    persiana = Persiana(19,26,name="persiana")
    persiana.open()

def main():
    foco = Foco(2,"foco")
    foco.set_light_sensor(LightSensor(21))
    foco.turn_on_sensor()
    sleep(3)
    foco.turn_off_sensor()
    #Thread(target=set_persiana).start()
    #Thread(target=set_foco).start()

if __name__ == "__main__":
    main()