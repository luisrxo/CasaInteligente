from CasaInteligente.components.led import LED

class AlarmaMov(object):
    def __init__(self, out_devices, input_device, name="AlarmaMov"):
        self.out_devices = out_devices
        self.in_device = input_device
        self.name = name
        self.active = False

    def use(self):
        """
        Método para usar la alarma, en este caso se hace uso de un dispositivo de entrada cualquiera, preferentemente
        se usa un sensor y en este caso el sensor debe de tener un método llamado is_move.
        Si este método detectó algún movimiento entonces se encienden los dispositivos que se tengan de salida.
        Estos pueden ser desde alarmas, bocinas, leds, focos etc. Mientras tengan el método on()
        En este caso la salida está probada para que se encienda un LED y se mande un mensaje por telegram.
        """        
        self.active = True
        if type(self.out_devices) != type(list()):
            self.out_devices = [self.out_devices]
        while self.active:
            if self.in_device.is_move():
                for device in self.out_devices:
                    device.on()
            else:
                for device in self.out_devices:
                        device.off()
    def on(self):
        """
        Wrapper para usar el sensor
        """        
        self.use()

    def off(self):
        """
        Simplemente se desactiva la señal para que deje de estar en el ciclo
        """        
        self.active = False
