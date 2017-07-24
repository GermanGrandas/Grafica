from pygame import *
from math import *
import random


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


N =50




if __name__ == '__main__':

    init()
    pantalla = display.set_mode([ANCHO,ALTO])
    display.set_caption("ejemplo")
    fin = False

    mouse.set_visible(False)
    puntos = [0]*N
    reloj = time.Clock()

    pantalla.fill(black)

    for w in range(N):
        puntos[w] = random.randint(0,ANCHO)
    display.flip()


    x=0
    var_y=0
    while not fin:
        for evento in event.get():
            if evento.type == QUIT:
                fin = True
        draw.circle(pantalla,darkturquoise,[puntos[x],var_y],5)
        display.flip()
        var_y+=30

        if var_y >= ALTO: var_y=0 ;x+=1
        if x == 50: x =0
        reloj.tick(120)
