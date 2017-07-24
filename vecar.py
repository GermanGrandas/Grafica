from pygame import *
from math import *


ANCHO = 1000
ALTO =600

Origen = [int(ANCHO/2),int(ALTO/2)]
#Colores

red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]
white =[255,255,255]
black = [0,0,0]
gold = [255,215,0]
darkturquoise = [0,206,209]

class Cartesiano:

    def __init__(self,win,centro = Origen):
        self.c= centro
        self.win = win
        self.Ejes()
        #self.EjeH()

    def Ejes(self):
        draw.line(self.win,blue,[self.c[0],0],[self.c[0],ALTO])
        draw.line(self.win,blue,[0,self.c[1]],[ANCHO,self.c[1]])

    def EjeH(self):
        draw.line(self.win,blue,[0,self.c[1]],[ANCHO,self.c[1]])

    def Tras(self,p):
        xp = self.c[0]+p[0]
        yp = self.c[1]-p[1]
        return [xp,yp]

    def Punto(self,p):
        draw.circle(self.win,red,self.Tras(p),5)

    def Linea(self,p1,p2,color = gold):
        draw.line(self.win,color,self.Tras(p1),self.Tras(p2))

    def Poli(self,l):
        nl = []
        for e in l:
            nl.append(self.Tras(e))
        draw.polygon(self.win,red,nl,1)

    def Evento(self,ev,a):
        if ev.key == K_a:
            print('a')
    def Fill(self):
        self.win.fill(white)

    def changeC(self,p):
        self.c = self.Tras(p)

class Vector():

    def __init__(self,p):
        self.pos = p
        self.origen = [0,0]
        self.mag = sqrt(self.pos[0]**2 + self.pos[1]**2)
        self.ang =0

    def vecUni(self):
        v = []
        for x in self.pos:
            r = x / self.mag
            v.append(r)
        return v

    def changeOrigen(self,o):
        self.origen = o

    def posOfang(self,a):
        a = radians(a)
        x = int(self.mag * cos(a))
        y = int(self.mag * sin(a))
        self.pos = [x,y]

    def proEscalar(self,K =1):
        w = []
        for x in self.pos:
            w.append(x*K)
        return w

    def getPos(self):
        return self.pos

    def changePos(self,p):
        self.pos = p


    def sumaVec(self,v):
        pos = v.getPos()
        v = Vector([0,0])
        v.changePos([self.pos[0] + pos[0],self.pos[1] + pos[1]])
        return v
