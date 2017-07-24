
from vecar import *



def cartesiano(p):
    np = [p[0]+Origen[0],Origen[1]-p[1]]
    return np


if __name__ == '__main__':

    init()
    pantalla = display.set_mode([ANCHO,ALTO])
    display.set_caption("ejemplo")
    fin = False


    pantalla.fill(black)

    plano = Cartesiano(pantalla)
    #plano2 = Cartesiano(pantalla,[100,550])

    reloj = time.Clock()

    vec = Vector([100,50])
    vec2 = Vector([100,10])
    vec3 = Vector([100,200])

    var_x=0

    """v1 = Vector([50,50])
    v2 = Vector([20,30])
    v3 = Vector([10,40])

    v12 = v1.sumaVec(v2)
    v23 = v12.sumaVec(v3)

    plano.Linea(v1.origen,v1.pos,white)
    plano.Linea(v12.origen,v12.pos,red)
    #v23.posOfang(90)
    #plano.Linea(v23.origen,v23.pos)"""

    plano.Linea(vec.origen,vec.pos)
    plano.changeC(vec.pos)


    #dibujar_plano()
    """plano2.Linea(vec.origen,vec.pos)
    plano2.changeC(vec.pos)
    vec2.posOfang(30)
    plano2.Linea(vec2.origen,vec2.pos,red)
    plano2.changeC(vec2.pos)
    vec3.posOfang(45)
    plano2.Linea(vec3.origen,vec3.pos,white)"""


    while not fin:
        for evento in event.get():
            if evento.type == QUIT:
                fin = True


        vec2.posOfang(var_x)
        plano.Linea(vec2.origen,vec2.pos,darkturquoise)
        vec2.posOfang(var_x-1)
        plano.Linea(vec2.origen,vec2.pos,black)

        display.flip()

        var_x+=1

        reloj.tick(60)
