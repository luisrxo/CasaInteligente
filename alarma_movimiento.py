from CasaInteligente.components.bocina import Bocina
from CasaInteligente.components.sensor_pir import SensorPIR
from CasaInteligente.components.alarma_movimiento import AlarmaMov
from CasaInteligente.services.telegram_api import Telegram
import telebot

# Se crea el bot con el TOKEN
API_TOKEN = "1088193438:AAFffJIzdeGBWtSZhzDCeoYTlkDK2O_Naq4"
bot_enc = telebot.TeleBot(API_TOKEN)
# Se crean los dispositivos a usar, en este caso se tiene
# Bocina, se utiliza pygame para reproducir el sonido. 
bocina = Bocina("alarm_sound.mp3",name="Bocina")
# Se define el sensor que servirá como entrada a la alarma, en este caso es un PIR
sensor = SensorPIR(21,name="Sensor Movimiento")
# Se define el bot que contiene la lógica para encender y apagar dispositivos
bot_alarma= Telegram("Encendido", bot_enc)
# Se define el dispositivo principal que es la alarma de movimiento. 
# Se crea con una lista de dispositivos de salida buzzer,bot_alarma y 
# un dispositivo de entrada, este dispositivo si encuentra algún movimiento activará los dispositivos de salida
# Y finalmente el nombre del dispositivo para encontrarlo en telgram
alarma = AlarmaMov([bocina,bot_alarma],sensor,name="Alarma_Mov")
# Se establece el mensaje de salida de telegram, podemos incluir cualquier cosa.
bot_alarma.set_on_message("Se ha Detectado movimiento")
# Se establecen los dispositivos que seran visibles por el bot
bot_alarma.set_elements([alarma])
# Se añaden las acciones 
bot_alarma.add_action_message("\on","\nEnciende el/los dispositivos seleccionados","\n\on alarma_mov")
bot_alarma.add_action_message("\off","\nApaga el/los dispositivos seleccionados","\n\off alarma_mov")
bot_alarma.add_action_message("\show","\nMuestra los dispositivos que se encuentran activados","\show")

@bot_enc.message_handler(commands=['on'])
def command_ledon(message):
    # Cuando se activa, se guarda el chat id para asi mandar un mensaje cuando se active el sensor
    bot_alarma.set_chat(message.chat.id)
    response = bot_alarma.command_on(message)
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