from pygame import *
#import ConfigParser
import configparser


ANCHO = 600
ALTO = 500

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
        self.muros = None
        self.vida =100

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

        l_col = sprite.spritecollide(self,self.muros,False)
        for block in l_col:
            self.vida -=1
            if self.dir == 2:
                self.con =0
                self.rect.right = block.rect.left
            if self.dir == 1:
                self.con =0
                self.rect.left =  block.rect.right
            if self.dir == 0:
                self.con =0
                self.rect.bottom = block.rect.top
            if self.dir == 3:
                self.con =0
                self.rect.top = block.rect.bottom

    def setDir(self,x):
        self.dir = x


class Muro(sprite.Sprite):
    def __init__(self,obj_img,pos):
        sprite.Sprite.__init__(self)
        self.image = obj_img
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

class Nivel(sprite.Sprite):
    def __init__(self,ar_mapa,al_re,an_re):
        sprite.Sprite.__init__(self)
        self.mapa = self.retMapa(ar_mapa)
        self.fondo = self.traerFondo(self.ar_fondo,an_re,al_re)


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

    def retMapa(self,archivo):
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

        info_muros = []
        nf=0
        for fila in plano:
            nc=0
            for e in fila:
                lista = d[e]
                if lista[1]==1:
                    pos = [nc,nf]
                    info = [pos,lista[0]]
                    info_muros.append(info)
                nc+=1
            nf+=1
        return info_muros



def cargarImgPlayer(image,al_re,an_re):
    m= []
    for fila in range(4):
        lista = []
        for i in range(4):
            cuadro = image.subsurface(0+i*an_re,0+fila*al_re,an_re,al_re)
            lista.append(cuadro)
        m.append(lista)
    return m

if __name__ == '__main__':
    init()
    pantalla = display.set_mode([ANCHO, ALTO])
    display.set_caption("animacion")


    player1 = image.load('Kgerman.png').convert_alpha()


    al_re1 = 48
    an_re1 = 32

    m = cargarImgPlayer(player1,al_re1,an_re1)



    player = Jugador(m,[50,100])

    todos = sprite.Group()


    muros = sprite.Group()
    mapa = Nivel('mapa.map',32,32)

    for lista in mapa.mapa:
        pos_obj = lista[0]
        pos_img = lista[1]
        x = pos_img[0]
        y = pos_img[1]
        img_m = mapa.fondo[x][y]
        xp = pos_obj[0]*32
        yp = pos_obj[1]*32
        pos = [xp,yp]
        m = Muro(img_m,pos)
        muros.add(m)
        todos.add(m)

    player.muros = muros

    todos.add(player)

    fondo = image.load('fondo.jpg')

    fuente = font.SysFont("comicsansms",25)



    fin = False
    reloj = time.Clock()
    finjuego = False

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

        if finjuego:
            pantalla.fill([0,0,0])
            texto = fuente.render('Fin de juego',True,[255,255,255])
            pantalla.blit(texto,[300,200])
            display.flip()
        else:
            pantalla.fill([0,0,0])
            vida = str(player.vida)
            if player.vida <=0:
                finjuego = True
            texto = fuente.render('vida: '+vida,True,[255,255,255])
            pantalla.blit(fondo,[0,0])
            pantalla.blit(texto,[20,460])
            todos.update()
            todos.draw(pantalla)
            display.flip()
            reloj.tick(30)
