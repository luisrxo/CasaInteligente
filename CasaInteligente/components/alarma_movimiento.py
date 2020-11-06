from CasaInteligente.components.led import LED

class AlarmaMov(object):
    def __init__(self, out_devices, input_device, name="AlarmaMov"):
        self.out_devices = out_devices
        self.in_device = input_device
        self.name = name
        self.active = False

    def use(self):
        while self.active:
            if self.in_device.is_move():
                if type(self.out_device) != type(list()):
                    self.out_devices = [self.out_devices]
                for device in self.out_devices:
                    device.on()

    def on(self):
        self.use()

    def off(self):
        self.active = False
