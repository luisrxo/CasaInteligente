from gpiozero import Motor
from time import sleep

class Persiana(object):
    
    def __init__(self,forward_pin_gpio, backward_pin_gpio, name="GPIO", open_direction_backward=True, time_open=5):
        self.motor = Motor(forward=forward_pin_gpio,backward=backward_pin_gpio)
        self.name = name if name != "GPIO" else "GPIO " + "{},{}".format(forward_pin_gpio,backward_pin_gpio)
        self.open_direction_backward = open_direction_backward
        self.time_open = time_open
    
    def open(self):
        if self.open_direction_backward:
            self.motor.backward()
        else:
            self.motor.forward()
        sleep(self.time_open)

    def close(self):
        if self.open_direction_backward:
            self.motor.forward() 
        else:
            self.motor.backward()
        sleep(self.time_open)

    def on(self):
        self.open()
    
    def off(self):
        self.close()
