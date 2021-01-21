from CasaInteligente.services.telegram_api import Telegram
from CasaInteligente.components.foco import Foco
from CasaInteligente.components.persiana import Persiana
from CasaInteligente.components.tira_led import TiraLED
from CasaInteligente.components.bocina import Bocina
from gpiozero import LightSensor
import telebot
"""
Este es un ejemplo para controlar diferentes dispositivos con un bot de telegram con los siguientes comandos
/on dispositivo,dispositivo,... 
o
/on dispositivo

Ejemplo
/on foco

Y asi con off
"""

# Para todos los Dispositivos que heredan de LED que aqui son todos en el constructor se le pasa el pin GPIO y el nombre
persiana_obj = Persiana(5, 6, name="persiana", open_direction_backward=True, time_open=5)
foco_obj = Foco(2,"foco")
foco_obj.set_light_sensor(LightSensor(21))
#foco_obj.use_light_sensor(debug=True)
tira_led_obj = TiraLED(3,"tira_led") 
bocina_obj = Bocina("","bocina")
dispositivos = [bocina_obj, persiana_obj, foco_obj, tira_led_obj]

API_TOKEN = "1088193438:AAFffJIzdeGBWtSZhzDCeoYTlkDK2O_Naq4"
bot_enc = telebot.TeleBot(API_TOKEN)
bot_encendido = Telegram("Casa Inteligente", bot_enc)
bot_encendido.set_elements(dispositivos)
bot_encendido.add_action_message("/on","\nEnciende el/los dispositivos seleccionados","\n/on alarma,foco")
bot_encendido.add_action_message("/off","\nApaga el/los dispositivos seleccionados","\n/off alarma,foco")
bot_encendido.add_action_message("/play","\nReproduce una cancion dada por el usuario","\n/play im so tired the beatles 2018")
bot_encendido.add_action_message("/setvalue","\nEstablece el valor PWM al seleccionado","\n/setvalue alarma 0.5")
bot_encendido.add_action_message("/show","\nMuestra los dispositivos que se encuentran activados","/show")

@bot_enc.message_handler(commands=['on'])
def command_ledon(message):
    response = bot_encendido.command_on(message)
    bot_enc.reply_to(message, response)
    
@bot_enc.message_handler(commands=['off'])
def command_ledoff(message):
    response = bot_encendido.command_off(message)
    bot_enc.reply_to(message, response)

@bot_enc.message_handler(commands=['play'])
def command_ledoff(message):
    response = bot_encendido.command_play(message)
    bot_enc.reply_to(message, response)

@bot_enc.message_handler(commands=['help','start'])
def send_welcome(message):
    response = bot_encendido.command_start_help()
    bot_enc.reply_to(message, response)

@bot_enc.message_handler(commands=['show'])
def command_show(message):
    response = bot_encendido.command_show(message)
    bot_enc.reply_to(message, response)

bot_enc.polling()
