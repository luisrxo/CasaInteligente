from __future__ import print_function

import argparse
import os.path
import json

import google.oauth2.credentials
import RPi.GPIO as GPIO
from google.assistant.library import Assistant
from google.assistant.library.event import EventType
from google.assistant.library.file_helpers import existing_file

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.output(2,False)

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
        print("ON")
        GPIO.output(2,True)
    
    command_off = "turn off lights"
    if (event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED) and event.args["text"] == command_off:
        print("OFF")
        GPIO.output(2,False)


  
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
