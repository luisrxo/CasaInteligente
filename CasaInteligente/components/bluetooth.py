from bluedot import BlueDot
from signal import pause


class Bluetooth(object):

    def __init__(self, name, objetoControlado=None, metodoArriba=None, metodoAbajo=None, metodoDerecha=None, metodoIzquierda=None):
        self.name = name
        self.objetoControlado = objetoControlado
        self.metodoArriba = metodoArriba
        self.metodoAbajo = metodoAbajo
        self.metodoDerecha = metodoDerecha
        self.metodoIzquierda = metodoIzquierda

        bd = BlueDot()

        bd.when_pressed = self.dpad

        pause()
    
    def dpad(self, pos):
        if pos.top:
            self.metodoArriba(self.objetoControlado)
        elif pos.bottom:
            self.metodoAbajo(self.objetoControlado)
        elif pos.right:
            self.metodoDerecha(self.objetoControlado)
        elif pos.left:
            self.metodoIzquierda(self.objetoControlado)
