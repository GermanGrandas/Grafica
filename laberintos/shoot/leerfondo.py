from pygame import *


#en python 3.5 from backports import configparser

ANCHO = 680
ALTO = 400


if __name__ == '__main__':
    init()
    pantalla = display.set_mode([ANCHO, ALTO])
    display.set_caption("laberinto")

    imagen = image.load('imagenes/fondo.png')
    ancho, alto = imagen.get_size()
    print ancho,alto

    an_re = 32 38
    al_re = 32 57
    tabla = []
    for var_x in range(0,(ancho/an_re)):
        fila = []
        for var_y in range(0,(alto/al_re)):
            cuadro = [0+var_x*an_re,0+var_y*al_re,an_re,al_re]
            img_cuadro = imagen.subsurface(cuadro)
            fila.append(img_cuadro)
        tabla.append(fila)

    pantalla.blit(tabla[0][5],[200,200])
    display.flip()

    fin = False
    while not fin:
        # Captura de eventos

        for evento in event.get():
            if evento.type== QUIT:
                fin = True
