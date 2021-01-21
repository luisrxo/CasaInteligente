# CasaInteligente

Es un modulo de python para tener una "casa inteligente" por medio de una raspberry pi y diferentes elementos que nos permitirán desarrollar un proyecto de domótica a la medida.

## Instalación

Instalar los requerimientos mediante 

```bash
pip3 install -r requirements.txt
```

## Caso de Uso
Este repositorio tiene un ejemplo de como se utilizaría una Raspberry Pi 4, para controlar un dormitorio.

## Integraciones
Se incluyen diferentes integraciones con servicios online y bluetooth entre ellos están:

* [Google Assistant](https://assistant.google.com/intl/es_es/)
* [Telegram](https://telegram.org/)
* Bluetooth a través de la aplicación [bluedot](https://play.google.com/store/apps/details?id=com.stuffaboutcode.bluedot&hl=es_PE)

## Uso
En el ejecutable main.py se incluyen todas las funcionalidades para ser ejecutadas a la vez y ser controlada por voz, por chat o por una app desde bluetooth.

```bash
sudo python3 main.py
```
## Ejemplos
En este repositorio se cuenta con algunos ejemplos usando diferentes servicios e integraciones.

* [GoogleAssistant](https://github.com/miguel17546mals/CasaInteligente/blob/main/google_assistant_demo.py)
* [Telegram](https://github.com/miguel17546mals/CasaInteligente/blob/main/casa_inteligente_telegram.py)
* [Bluetooth](https://github.com/miguel17546mals/CasaInteligente/blob/main/control_casa_inteligente.py)


## Uso para crear tu propio proyecto

```python
from CasaInteligente.services.telegram_api import Telegram
from CasaInteligente.components.alarma import Alarma
from CasaInteligente.components.foco import Foco
from CasaInteligente.components.persiana import Persiana
from CasaInteligente.components.tira_led import TiraLED

alarma_obj = Alarma(0,"alarma")
persiana_obj = Persiana(1,"persiana")
foco_obj = Foco(2,"foco")
tira_led_obj = TiraLED(3,"tira_led") 

foco.obj.on()
```

## Contribuciones
Pull requests son bienvenidas. Para cambios mayores, por favor, abre primero un issue para discutir que se quiere cambiar.

Por favor, asegurarse de actualizar los tests.

## Licencia
[GNU V3](https://choosealicense.com/licenses/agpl-3.0/)