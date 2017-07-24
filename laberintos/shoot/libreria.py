from pygame import *
from math import *


ANCHO = 1080
ALTO =600

Origen = [int(ANCHO/2),int(ALTO/2)]
#Colores

red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]
white =[255,255,255]
black = [0,0,0]



class Bala(sprite.Sprite):
    class Recta():

        def __init__(self,origen,posf):
            self._posi= origen
            self.posf = posf
            self._pendiente = (self.posf[1]-self._posi[1])/(self.posf[0]-self._posi[0])
            self._b = self.posf[1]-(self.posf[0]*self._pendiente)
            self.y = int(self.posf[0]*self._pendiente + self._b)

        def Position(self):
            if self.posf[0] > self._posi[0]:
                if self.posf[0] >= 0:
                    self.y = int(self.posf[0]*self._pendiente + self._b)
                    self.posf[0] -=1
            else:
                self.posf[0] = self._posi[0]
            return [self.posf[0],self.y]

    def __init__(self,archivo):
        sprite.Sprite.__init__(self)
        self.image = image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.count = 0
        self.recta = self.Recta([0,400],[1000,0])

    def update(self):
        #if self.rect.y <= ALTO-self.rect.height:
        pos = self.recta.Position()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.count+=1
