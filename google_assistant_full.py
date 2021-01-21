from __future__ import print_function

import argparse
import os.path
import json
import google.oauth2.credentials

from google.assistant.library import Assistant
from google.assistant.library.event import EventType
from google.assistant.library.file_helpers import existing_file

from CasaInteligente.components.foco import Foco
from CasaInteligente.components.persiana import Persiana
from CasaInteligente.components.tira_led import TiraLED
from CasaInteligente.components.bocina import Bocina
from gpiozero import LightSensor

persiana_obj = Persiana(26, 19, name="persiana", open_direction_backward=True, time_open=5)
foco_obj = Foco(2,"foco")
foco_obj.set_light_sensor(LightSensor(21))
#foco_obj.use_light_sensor(debug=True)
tira_led_obj = TiraLED(3,"tira_led") 
bocina_obj = Bocina("","bocina")

def process_event(event):
    """Pretty prints events.
    Prints all events that occur with two spaces between each new
    conversation and a single space between turns of a conversation.
    Args:
        event(event.Event): The current event to process.
    """
    if event.type == EventType.ON_CONVERSATION_TURN_STARTED:
        print()
        #GPIO.output(2,True)

    print(event)

    if (event.type == EventType.ON_CONVERSATION_TURN_FINISHED and
            event.args and not event.args['with_follow_on_turn']):
        print()
        #GPIO.output(2,False)
    if (event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED):
        print(event.args["text"])
    """
    Para Hacer uso del reconocimiento de voz de google, lo que hacemos es ver cuando haya un evento del tipo
    ON_RECOGNIZING_SPEECH_FINISHED, esto traerá en los argumentos del evento, el texto que reconoció. 
    A partir de aqui podemos hacer nuestros propios comandos, por ejemplo 
    "turn on lights" encenderá un LED. 
    "turn off lights" apagará el mismo LED. 

    podemos definir cualquier comando y mediante este reconocimiento apagar o encender cosas dentro de nuestra raspberry

    """
    

    command_led = "turn on lights"
    if (event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED) and event.args["text"] == command_led:
        foco_obj.on()
    
    command_off = "turn off lights"
    if (event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED) and event.args["text"] == command_off:
        foco_obj.off()
    
    command_blid_open = "open the blinds"
    if (event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED) and event.args["text"] == command_blid_open:
        persiana_obj.open()

    command_blind_close = "close the blinds"
    if (event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED) and event.args["text"] == command_blind_close:
        persiana_obj.off()

    command_on_strip = "turn on strip"
    if (event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED) and event.args["text"] == command_on_strip:
        tira_led_obj.on()

    command_off_strip = "turn off strip"
    if (event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED) and event.args["text"] == command_off_strip:
        tira_led_obj.off()

    command_use_light_sensor = "use the light sensor"
    if (event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED) and event.args["text"] == command_use_light_sensor:
        tira_led_obj.turn_on_sensor()

    command_play = "play"
    if (event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED) and command_play in event.args["text"].lower():
        bocina_obj.play(event.args["text"].lower().replace(command_play,""))
    
    command_stop = "stop"
    if (event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED) and command_stop in event.args["text"].lower():
        bocina_obj.off()

def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--credentials', type=existing_file,
                        metavar='OAUTH2_CREDENTIALS_FILE',
                        default=os.path.join(
                            os.path.expanduser('/home/pi/.config'),
                            'google-oauthlib-tool',
                            'credentials.json'
                        ),
                        help='Path to store and read OAuth2 credentials')
    args = parser.parse_args()
    with open(args.credentials, 'r') as f:
        credentials = google.oauth2.credentials.Credentials(token=None,
                                                            **json.load(f))

    with Assistant(credentials) as assistant:
        for event in assistant.start():
            process_event(event)


if __name__ == '__main__':
    main()
