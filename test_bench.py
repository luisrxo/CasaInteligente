from CasaInteligente.components.alarma import Alarma
from CasaInteligente.components.foco import Foco
from CasaInteligente.components.persiana import Persiana
from CasaInteligente.components.tira_led import TiraLED
from gpiozero import LightSensor

from threading import Thread


def set_foco():
    foco = Foco(2,"foco")
    foco.set_light_sensor(LightSensor(21))
    foco.use_light_sensor(debug=True)

def set_persiana():
    persiana = Persiana(19,26,name="persiana")
    persiana.open()

def main():
    set_persiana()
    set_foco()

if __name__ == "__main__":
    main()