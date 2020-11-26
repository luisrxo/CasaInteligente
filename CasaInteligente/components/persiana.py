from gpiozero import Motor
from time import sleep

class Persiana(object):
    
    def __init__(self,forward_pin_gpio, backward_pin_gpio, name="GPIO", open_direction_backward=True, time_open=5):
        """
        Contructor de la clase persiana

        Args:
            forward_pin_gpio (int): Pin GPIO para el motor 1
            backward_pin_gpio (int): Pin GPIO para el motor 1
            name (str, optional): Nombre que tendrá el dispositivo. Defaults to "GPIO".
            open_direction_backward (bool, optional): Sirve para determinar hacia que dirección se abrirá la persiana. Defaults to True.
            time_open (int, optional): Tiempo que tarda en abrir la persiana, que será el mismo para abrir y cerrar. Defaults to 5.
        """        
        self.motor = Motor(forward=forward_pin_gpio,backward=backward_pin_gpio)
        self.name = name if name != "GPIO" else "GPIO " + "{},{}".format(forward_pin_gpio,backward_pin_gpio)
        self.open_direction_backward = open_direction_backward
        self.time_open = time_open
    
    def open(self):
        """
        Abre la persiana con el tiempo establecido
        """        
        if self.open_direction_backward:
            self.motor.backward()
        else:
            self.motor.forward()
        sleep(self.time_open)

    def close(self):
        """
        Cierra la persiana con el tiemp oestablecido.
        """        
        if self.open_direction_backward:
            self.motor.forward() 
        else:
            self.motor.backward()
        sleep(self.time_open)

    def on(self):
        """
        Wrapper para que cuando se llame el método on, se abra
        """        
        self.open()
    
    def off(self):
        """
        Wrapper para que cuando se llame el método off, se cierre
        """        
        self.close()
