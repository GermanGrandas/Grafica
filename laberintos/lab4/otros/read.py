import json
import pygame

ANCHO = 800
ALTO = 500

def traerFondo(archivo,an_re,al_re):
    imagen = pygame.image.load(archivo)
    ancho, alto = imagen.get_size()

    tabla = []
    for var_y in range(0,int(alto/al_re)):
        #fila = []
        for var_x in range(0,int(ancho/an_re)):
            cuadro = [0+var_x*an_re,0+var_y*al_re,an_re,al_re]
            img_cuadro = imagen.subsurface(cuadro)
            tabla.append(img_cuadro)
        #tabla.append(fila)
    return tabla

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])

    with open('mapa.json') as js_archivo:
        doc = json.load(js_archivo)


    print ('alto',doc["height"])
    print ('ancho',doc["width"])

    origen = ''
    c_an = ''
    c_al = ''

    for valor in doc["tilesets"]:
        origen = valor["image"]
        c_al = valor["tileheight"]
        c_an = valor["tilewidth"]
        infoMuros = valor["tileproperties"]

    print (origen,c_al,c_an,infoMuros)
    img_fondo = traerFondo(origen,c_an,c_al)


    for valor in doc["layers"]:
        iv=valor["data"]
        #print(iv)
    px=0
    py=0
    for x in iv:
        pantalla.blit(img_fondo[x-1],[0+(px*32),0+(py*32)])
        if px<= valor["width"]-2:
            px+=1
        else:
            px=0
            py+=1


    #pantalla.blit(img_fondo[0],[100,100])
    pygame.display.flip()


    reloj = pygame.time.Clock()
    fin = False
    while not fin:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fin = True
