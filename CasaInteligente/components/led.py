from gpiozero import PWMLED
from time import sleep
from math import ceil
from threading import Thread

light_sensor_enable = False


def use_sensor(GPIO,led,light_sensor,use_pwm,on_range):
    while light_sensor_enable:
        if not use_pwm:
            if on_range[0]<= light_sensor.value and light_sensor.value <= on_range[1]:
                led.on()
            else:
                led.off()
        else:
            GPIO.source = light_sensor
    return


class LED(object):
    def __init__(self,pin_gpio, name="GPIO"):
        """
        Constructor del objeto LED

        Args:
            pin_gpio (int): pin GPIO donde va a estar conectado el dispositivo.
            name (str, optional): Nombre con el que se mostrará el dispositivo en los diferentes servicios implementados. Defaults to "GPIO".
        """        
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
        """
        Se queda prendido un cierto tiempo determinado por time on

        Args:
            time_on (float): Tiempo que estara prendido el LED.
        """        
        self.GPIO.on()
        sleep(time_on)
        self.GPIO.off()


    def set_light_sensor(self,sensor):
        """
        Establece el dispositivo para sensar.

        Args:
            sensor (LightSensor): Sensor con el que se trabajara
        """
        global light_sensor_enable   
        self.light_sensor = sensor
        light_sensor_enable = False
        self.sensors.append(sensor)
    
    def use_light_sensor_exp(self, use_pwm=False, on_range=(0.5,1), debug=False):
        """
        Utiliza el sensor de forma indeterminada con los valores que se le hayan asignado.

        Args:
            use_pwm (bool, optional): Si se requiere que el valor del LED dependa completamente del sensor de luz. Defaults to False.
            on_range (tuple, optional): Rango en el que estara encendido el LED. Defaults to (0.5,1).
        """    
        global light_sensor_enable   
        light_sensor_enable = True
        Thread(target=use_sensor,args=(self.GPIO,self,self.light_sensor,use_pwm,on_range)).start()
        return

    def turn_off_sensor(self):
        global light_sensor_enable   
        light_sensor_enable = False
        return

    def turn_on_sensor(self):
        global light_sensor_enable   
        light_sensor_enable = True
        self.use_light_sensor_exp()
        return

    def use_light_sensor(self, use_pwm=False, on_range=(0.5,1), debug=False):
        """
        Utiliza el sensor de forma indeterminada con los valores que se le hayan asignado.

        Args:
            use_pwm (bool, optional): Si se requiere que el valor del LED dependa completamente del sensor de luz. Defaults to False.
            on_range (tuple, optional): Rango en el que estara encendido el LED. Defaults to (0.5,1).
        """        
        self.light_sensor_enable = True
        while self.light_sensor_enable:
            if debug:
                print(self.light_sensor.value)
            if not use_pwm:
                if on_range[0]<= self.light_sensor.value and self.light_sensor.value <= on_range[1]:
                    self.on()
                else:
                    self.off()
            else:
                self.GPIO.source = self.light_sensor



