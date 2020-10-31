from CasaInteligente.components.alarma import Alarma
from CasaInteligente.components.foco import Foco
from CasaInteligente.components.persiana import Persiana
from CasaInteligente.components.tira_led import TiraLED
from gpiozero import LightSensor

def main():
    foco = Foco(2,"foco")
    foco.set_light_sensor(LightSensor(21))
    foco.use_light_sensor()


if __name__ == "__main__":
    main()