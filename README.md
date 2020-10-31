# CasaInteligente

Es un modulo de python para tener una "casa inteligente" por medio de una raspberry pi y diferentes elementos que nos permitirán desarrollar un proyecto de domótica a la medida.

## Installation

Instalar los requerimientos mediante 

```bash
pip3 install -r requirements.txt
```

## Usage

```python
from CasaInteligente.services.telegram_api import Telegram
from CasaInteligente.components import foco,persiana,alarma,tira_led

alarma_obj = alarma.Alarma(0,"alarma")
persiana_obj = persiana.Persiana(1,"persiana")
foco_obj = foco.Foco(2,"foco")
tira_led_obj = tira_led.TiraLED(3,"tira_led") 

foco.obj.on()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GNU V3](https://choosealicense.com/licenses/agpl-3.0/)