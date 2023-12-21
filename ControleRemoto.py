from televisor import Televisor

class ControleRemoto:
    def __init__(self, tv):
        self.tv = tv

    def aumentaVolume(self):
        self.tv.aumentaVolume(10)

    def diminuiVolume(self):
        self.tv.diminuiVolume(10)

    def trocaDeCanal(self, canal):
        self.tv.trocaCanal(canal)

    def sintonizaCanal(self, canal):
        self.tv.sintonizaCanal(canal)