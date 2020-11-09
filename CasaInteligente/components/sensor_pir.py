from gpiozero import MotionSensor

class SensorPIR(object):

    def __init__(self, pin_gpio, name="GPIO", time_sense=1):
        self.name = name if name != "GPIO" else "GPIO " + str(pin_gpio)
        self.GPIO = MotionSensor(pin_gpio)
        self.time_sense = time_sense
    
    def is_move(self):
        """
        Wrapper que sirve como método universal en este módulo/ biblioteca para detectar movimiento
        En este caso ya que usamos el MotionSensor de gpiozero solo se llama esa funcion
        En otro caso que necesitemos algo mas complejo solo lo agregamos.

        Returns:
            bool: Si hay movimiento o no
        """        
        return self.GPIO.motion_detected
