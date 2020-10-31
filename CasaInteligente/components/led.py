from gpiozero import PWMLED
from time import sleep
from math import ceil

class LED(object):
    def __init__(self,pin_gpio, name="GPIO"):
        self.GPIO = PWMLED(pin_gpio)
        self.name = name if name != "GPIO" else "GPIO " + str(pin_gpio)
        self.set_blink = False
        self.sensors = []

    def on(self):
        self.GPIO.on()
    
    def set_value(self,pwm_value):
        self.GPIO.value = pwm_value
    
    def off(self):
        self.GPIO.off()
    
    def blink(self,time_blink,inter_blink):
        alarma_n = ceil(time_blink/(2 * inter_blink))
        for k in range(alarma_n):
            if not self.set_blink:
                break
            self.GPIO.on()
            sleep(inter_blink)
            self.GPIO.off()
            sleep(inter_blink)
    
    def on_time(self,time_on):
        self.GPIO.on()
        sleep(time_on)
        self.GPIO.off()


    def set_light_sensor(self,sensor):
        self.light_sensor = sensor
        self.light_sensor_enable = False
        self.sensors.append(sensor)
    
    def use_light_sensor(self, turn_on_when_dark = True, use_pwm=False):
        self.light_sensor_enable = True
        while self.light_sensor_enable:
            if not use_pwm:
                if turn_on_when_dark:
                    self.light_sensor.when_dark = self.GPIO.on()
                    self.light_sensor.when_light = self.GPIO.off()
                else:
                    self.light_sensor.when_dark = self.GPIO.off()
                    self.light_sensor.when_light = self.GPIO.on() 
            else:
                self.GPIO.source = self.light_sensor



