from gpiozero import MotionSensor

class SensorPIR(object):

    def __init__(self, pin_gpio, name="GPIO", time_sense=1):
        self.name = name if name != "GPIO" else "GPIO " + str(pin_gpio)
        self.GPIO = MotionSensor(pin_gpio)
        self.time_sense = time_sense
    
    def is_move(self):
        return self.GPIO.motion_detected
    