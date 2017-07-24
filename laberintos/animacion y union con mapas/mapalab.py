from pygame import *
#import ConfigParser
import configparser

#en python 3.5 from backports import configparser

ANCHO = 680
ALTO = 400

def traerFondo(archivo,an_re,al_re):
    imagen = image.load(archivo)
    ancho, alto = imagen.get_size()

    tabla = []
    for var_x in range(0,int(ancho/an_re)):
        fila = []
        for var_y in range(0,int(alto/al_re)):
            cuadro = [0+var_x*an_re,0+var_y*al_re,an_re,al_re]
            img_cuadro = imagen.subsurface(cuadro)
            fila.append(img_cuadro)
        tabla.append(fila)
    return tabla



if __name__ == '__main__':
    init()
    pantalla = display.set_mode([ANCHO, ALTO])
    display.set_caption("laberinto")

    archivo = 'mapa.map'
    #mapa = ConfigParser.ConfigParser()
    mapa = configparser.ConfigParser()
    mapa.read(archivo)

    #print mapa.get('nivel1','origen')

    plano = mapa.get('nivel1','mapa').split('\n')
    #print plano
    tabla = traerFondo('fondo.png',32,32)
    posx = 0
    posy = 0
    d = {}
    for sec in mapa.sections():
        if len(sec) == 1:
            #print sec, mapa.get(sec,'nombre'), mapa.get(sec,'ux'), mapa.get(sec,'uy')
            x = int(mapa.get(sec,'ux'))
            y = int(mapa.get(sec,'uy'))
            d[sec] = [x,y]
            #pantalla.blit(tabla[x][y],[posx,posy])

    #print d['.']
    #print plano[0]

    var_y = 0
    for y in plano:
        var_x =0
        for e in y:
            pos = d[e]
            x = pos[0]
            y = pos[1]
            lin_x = 0+var_x*32
            lin_y = 0+var_y*32
            pantalla.blit(tabla[x][y],[lin_x,lin_y])
            var_x+=1
        var_y+=1


    display.flip()

    fin = False
    while not fin:
        # Captura de eventos

        for evento in event.get():
            if evento.type== QUIT:
                fin = True
