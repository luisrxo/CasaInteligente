from CasaInteligente.services.telegram_api import Telegram
from CasaInteligente.components.alarma import Alarma
from CasaInteligente.components.foco import Foco
from CasaInteligente.components.persiana import Persiana
from CasaInteligente.components.tira_led import TiraLED
from CasaInteligente.components.led import LED
import telebot

"""
Este es un ejemplo para controlar diferentes dispositivos con un bot de telegram con los siguientes comandos
\setvalue dispositivo 0.5
El valor va desde 0 hasta 1
tambien incluye los comandos
/help que mostrara ayuda con los comandos disponibles y sus ejemplos.
/show muestra los dispositivos que con los que se puede interactuar.
"""
# Para todos los Dispositivos que heredan de LED que aqui son todos en el constructor se le pasa el pin GPIO y el nombre
alarma_obj = Alarma(0,"alarma")
# Se toma como un LED normal ya que actualmente se encuentra implementada la parte de la persiana como un MOTOR. 
persiana_obj = LED(1,"persiana")
foco_obj = Foco(2,"foco")
tira_led_obj = TiraLED(3,"tira_led") 
dispositivos = [alarma_obj, persiana_obj, foco_obj, tira_led_obj]

API_TOKEN = "1483085558:AAER06Yd9L4CRWb8IIA-gAJnF5uD0MbZ3sw"

bot_enc = telebot.TeleBot(API_TOKEN)

bot_encendido = Telegram("PWM", bot_enc)
bot_encendido.set_elements(dispositivos)
bot_encendido.add_action_message("\setvalue","\nEstablece el valor PWM al seleccionado","\n\setvalue alarma 0.5")
bot_encendido.add_action_message("\show","\nMuestra los dispositivos que se encuentran activados","\show")

@bot_enc.message_handler(commands=['help','start'])
def send_welcome(message):
    response = bot_encendido.command_start_help()
    bot_enc.reply_to(message, response)

@bot_enc.message_handler(commands=['show'])
def command_show(message):
    response = bot_encendido.command_show(message)
    bot_enc.reply_to(message, response)

@bot_enc.message_handler(commands=['setvalue'])
def command_show(message):
    response = bot_encendido.command_set_value(message)
    bot_enc.reply_to(message, response)

bot_enc.polling()
