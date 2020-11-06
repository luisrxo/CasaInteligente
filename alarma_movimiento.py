from CasaInteligente.components.buzzer import Buzzer
from CasaInteligente.components.sensor_pir import SensorPIR
from CasaInteligente.components.alarma_movimiento import AlarmaMov
from CasaInteligente.services.telegram_api import Telegram
from threading import Thread
import telebot

API_TOKEN = "1088193438:AAFffJIzdeGBWtSZhzDCeoYTlkDK2O_Naq4"
bot_enc = telebot.TeleBot(API_TOKEN)

buzzer = Buzzer(26,name="Buzzer")
sensor = SensorPIR(21,name="Sensor Movimiento")
bot_alarma= Telegram("Encendido", bot_enc)
alarma = AlarmaMov([buzzer,bot_alarma],sensor,name="Alarma_Mov")

bot_alarma.set_on_message("Se ha Detectado movimiento")

bot_alarma.set_elements([alarma])
bot_alarma.add_action_message("\on","\nEnciende el/los dispositivos seleccionados","\n\on alarma,foco")
bot_alarma.add_action_message("\off","\nApaga el/los dispositivos seleccionados","\n\off alarma,foco")
bot_alarma.add_action_message("\show","\nMuestra los dispositivos que se encuentran activados","\show")

@bot_enc.message_handler(commands=['on'])
def command_ledon(message):
    bot_alarma.set_chat(message.chat.id)
    response = bot_alarma.command_on(message)
    print("Se encendio")
    bot_enc.reply_to(message, response)
    
@bot_enc.message_handler(commands=['off'])
def command_ledoff(message):
    response = bot_alarma.command_off(message)
    bot_enc.reply_to(message, response)

@bot_enc.message_handler(commands=['help','start'])
def send_welcome(message):
    response = bot_alarma.command_start_help()
    bot_enc.reply_to(message, response)

@bot_enc.message_handler(commands=['show'])
def command_show(message):
    response = bot_alarma.command_show(message)
    bot_enc.reply_to(message, response)

bot_enc.polling()