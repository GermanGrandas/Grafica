import pygame
import json


ANCHO = 800
ALTO = 640
rojo = (255,0,0)
negro = (0,0,0)


class Muro(pygame.sprite.Sprite):
    def __init__(self,obj_img,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = obj_img
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


def recortar(archivo, anc, alc):
    linea=[]
    imagen=pygame.image.load(archivo).convert_alpha()
    i_ancho, i_alto=imagen.get_size()
    #print i_ancho, ' ',i_alto
    for y in range(0,i_alto/alc):
        for x in range(0,i_ancho/anc):
            cuadro=(x*anc, y*alc, anc, alc)
            linea.append(imagen.subsurface(cuadro))
    return linea


def Separar(l,ancho):
    con = 0
    m = []
    fila = []
    for e in l:
        fila.append(e)
        con +=1
        if con == ancho:
            m.append(fila)
            fila = []
            con=0
    return m


if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])


    fondo = pygame.image.load('fondo.png')
    an_img , al_img = fondo.get_size()


    with open('mapa.json') as js_ar:
        base=json.load(js_ar)

    for valor in base['tilesets']:
        nom_arc= valor['image']
        c_al = valor["tileheight"]
        c_an = valor["tilewidth"]


    for valor in base['layers']:
        if valor['name'] == "plataforma":
            mapa = valor['data']
            an = valor['width']

    lm=recortar(nom_arc,c_an,c_al)
    lsep = Separar(mapa,an)


    todos = pygame.sprite.Group()

    x = 0
    y = 0
    for fila in lsep:
        for e in fila:
            if e!= 0:
                pos = [x,y]
                img_ob = lm[e-1]
                b = Muro(img_ob,pos)
                todos.add(b)
            x+=c_an
        y+=c_al
        x=0

    


    fin = False
    reloj = pygame.time.Clock()
    xf = 0
    while not fin:
        pos = pygame.mouse.get_pos()
        for evento in pygame.event.get():
            if evento.type== pygame.QUIT:
                fin = True

        if pos[0] >= 590:
            xf -=1
            lim =-(an_img-ANCHO)
            if xf < lim:
                xf = lim
        elif pos[0] <= 10:
            xf +=1
            if xf >0:
                xf =0



        pantalla.blit(fondo,[xf,0])
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
