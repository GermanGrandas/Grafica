from pygame import *
#import configParser
import configparser


ANCHO = 680
ALTO = 400

class Jugador(sprite.Sprite):
    def __init__(self,imagmatriz,pos):
        sprite.Sprite.__init__(self)
        self.imagmatriz = imagmatriz
        self.dir = 2
        self.con = 0
        self.image = self.imagmatriz[self.dir][0]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        if self.dir == 2:
            self.rect.x += 2 if self.rect.x < ANCHO-self.rect.width else 0
        if self.dir == 1:
            self.rect.x -= 2 if self.rect.x > 0 else 0
        if self.dir == 0:
            self.rect.y += 2 if self.rect.y < (ALTO-self.rect.height)  else 0
        if self.dir == 3:
            self.rect.y -= 2 if self.rect.y > 0 else 0
        self.image = self.imagmatriz[self.dir][self.con]
        if self.con <3:
            self.con+=1
        else:
            self.con =0

    def setDir(self,x):
        self.dir = x

class Nivel(sprite.Sprite):
    def __init__(self,archivo,ar_mapa,al_re,an_re):
        sprite.Sprite.__init__(self)
        self.mapa = self.retMapa(ar_mapa)
        self.ar_fondo = archivo
        self.fondo = self.traerFondo(self.ar_fondo,an_re,al_re)
        self.plano = self.getPlano(ar_mapa)

    def traerFondo(self,archivo,an_re,al_re):
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

    def getPlano(self,archivo):
        mapa = configparser.ConfigParser()
        mapa.read(archivo)
        plano = mapa.get('nivel1','mapa').split('\n')
        return plano

    def retMapa(self,archivo):
        #mapa = ConfigParser.ConfigParser()
        mapa = configparser.ConfigParser()
        mapa.read(archivo)
        self.ar_fondo = mapa.get('nivel1','origen')
        plano = mapa.get('nivel1','mapa').split('\n')

        posx = 0
        posy = 0
        d = {}
        for sec in mapa.sections():
            if len(sec) == 1:
                x = int(mapa.get(sec,'ux'))
                y = int(mapa.get(sec,'uy'))
                muro = int(mapa.get(sec,'muro'))
                d[sec] = [[x,y],muro]
        for fila in plano:
            for e in fila:
                lista = d[e]
                if lista[1]==1:
                    pass
                    #m = Muro(imagen,pos)
                    #muros.add(m)
        return d
        #return m


def imagenJ(image,al_re,an_re):
    m = []
    for fila in range(4):
        lista = []
        for i in range(4):
            cuadro = imagenjugador.subsurface(0+i*an_re,0+fila*al_re,an_re,al_re)
            lista.append(cuadro)
        m.append(lista)
    return m

if __name__ == '__main__':
    init()
    pantalla = display.set_mode([ANCHO, ALTO])
    display.set_caption("animacion")


    imagenjugador = image.load('Kgerman.png').convert_alpha()
    al_re = 48
    an_re = 32
    m = imagenJ(imagenjugador,al_re,an_re)

    nvl = Nivel('fondo.png','mapa.map',32,32)


    player = Jugador(m,[100,100])
    todos = sprite.Group()

    todos.add(player)



    fin = False
    reloj = time.Clock()
    i=0
    while not fin:

        for evento in event.get():
            if evento.type== QUIT:
                fin = True

            if evento.type == KEYDOWN:
                if evento.key == K_RIGHT:
                    player.setDir(2)
                if evento.key == K_LEFT:
                    player.setDir(1)
                if evento.key == K_DOWN:
                    player.setDir(0)
                if evento.key == K_UP:
                    player.setDir(3)

        pantalla.fill([0,0,0])
        todos.update()
        todos.draw(pantalla)
        display.flip()
        reloj.tick(10)
