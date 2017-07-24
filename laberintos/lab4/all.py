import json
import pygame
import random

ANCHO = 800
ALTO = 500


class Jugador(pygame.sprite.Sprite):
    def __init__(self,imagmatriz,pos):
        pygame.sprite.Sprite.__init__(self)
        self.imagmatriz = imagmatriz
        self.dir = 2
        self.con = 0
        self.image = self.imagmatriz[self.dir][0]
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y =100
        self.varx = 2
        self.vary = 0
        self.saltar = False
        self.velocidad = 2
        self.muros = None
        self.vida =100
    def derecha(self):
        self.varx =self.velocidad
        self.dir = 2

    def izquierda(self):
        self.varx =-(self.velocidad)
        self.dir = 1

    def salto(self):
        if not self.saltar:
            self.vary = -10
            self.con = 0

    def gravedad(self):
        if self.vary == 0:
            self.vary = 1
        else:
            self.vary += 0.3

        piso = ALTO -self.rect.height
        if self.rect.y >= piso and self.vary >= 0:
            self.vary =0
            self.rect.y = piso
            self.saltar = False

    def update(self):
        self.gravedad()
        self.rect.x+=self.varx
        self.rect.y += self.vary

        self.image = self.imagmatriz[self.dir][self.con]
        if self.con <2:
            self.con+=1
        else:
            self.con =0

        l_col = pygame.sprite.spritecollide(self,self.muros,False)
        for block in l_col:
            if block.getType() == 1:
                self.vida -=1
            if block.getType() == 2:
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


class Muro(pygame.sprite.Sprite):
    def __init__(self,obj_img,pos,typewall):
        pygame.sprite.Sprite.__init__(self)
        self.image = obj_img
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.type = typewall

    def getType(self):
        return self.type


class Nivel(pygame.sprite.Sprite):
    def __init__(self,ar_mapa):
        pygame.sprite.Sprite.__init__(self)
        self.mapa = self.retMapa(ar_mapa)
        self.fondo = None


    def traerFondo(self,archivo,an_re,al_re):
        imagen = pygame.image.load(archivo)
        ancho, alto = imagen.get_size()

        tabla = []
        for var_y in range(0,int(alto/al_re)):
            for var_x in range(0,int(ancho/an_re)):
                cuadro = [0+var_x*an_re,0+var_y*al_re,an_re,al_re]
                img_cuadro = imagen.subsurface(cuadro)
                tabla.append(img_cuadro)
        return tabla

    def retMapa(self,archivo):
        mapa = archivo
        for valor in doc["tilesets"]:
            origen = valor["image"]
            c_al = valor["tileheight"]
            c_an = valor["tilewidth"]
            infoMuros = valor["tileproperties"]
        #print(infoMuros)
        self.ar_fondo = origen
        self.fondo = self.traerFondo(self.ar_fondo,c_an,c_al)

        for valor in doc["layers"]:
            plano = valor["data"] #valores del mapa

        posx = 0
        posy = 0
        d = {}
        #for elemento in plano:
        muros =infoMuros.items()
        for elemento in plano:
            for key, value in muros:
                for x in value.values():
                    if elemento-1 == int(key):
                        muro = x
                        d[elemento] = [self.fondo[elemento-1],muro]

        info_muros = []
        px=0
        py=0
        for imagen in plano:
            lista = d[imagen]
            walltype = lista[1]
            if walltype !=0:
                pos = [px,py]
                info = [pos,lista[0],walltype]
                info_muros.append(info)
            if px<= valor["width"]-2:
                px+=1
            else:
                px=0
                py+=1
        return info_muros

class Enemigo(pygame.sprite.Sprite):
    def __init__(self,archivo,pos):
        pygame.sprite.Sprite.__init__(self)
        self.imagmatriz = archivo
        self.dir = 2
        self.con = 0
        self.image = self.imagmatriz[self.dir][0]
        self.rect = self.image.get_rect()
        self.posdir = [0,1,2,3]
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.muros = None

    def update(self):
        if self.dir == 2:                             #Evitar salirse de la pantalla
            self.rect.x += 1 if self.rect.x < ANCHO-self.rect.width else 0
        if self.dir == 1:
            self.rect.x -= 1 if self.rect.x > 0 else 0
        if self.dir == 0:
            self.rect.y += 1 if self.rect.y < (ALTO-self.rect.height)  else 0
        if self.dir == 3:
            self.rect.y -= 1 if self.rect.y > 0 else 0
        self.image = self.imagmatriz[self.dir][self.con]
        if self.con <2:
            self.con+=1
        else:
            self.con =0
        l_col = pygame.sprite.spritecollide(self,self.muros,False)
        for block in l_col:
            if self.dir == 2:
                self.rect.right = block.rect.left
            if self.dir == 1:
                self.rect.left =  block.rect.right
            if self.dir == 0:
                self.rect.bottom = block.rect.top
            if self.dir == 3:
                self.rect.top = block.rect.bottom
            self.dir = random.choice(self.posdir)

    def setDir(self,x):
        self.dir = x

    def setMuros(self,muros):
        self.muros = muros


def cargarImgPlayer(image,al_re,an_re):
    m= []
    for fila in range(4):
        lista = []
        for i in range(3):
            cuadro = image.subsurface(0+i*an_re,0+fila*al_re,an_re,al_re)
            lista.append(cuadro)
        m.append(lista)
    return m


if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])

    with open('mapa.json') as js_archivo:
        doc = json.load(js_archivo)


    player1 = pygame.image.load('imagenes/me.png').convert_alpha()
    player1face = pygame.image.load('imagenes/Meface.png').convert_alpha()

    enemy = pygame.image.load('imagenes/Luisa.png').convert_alpha()

    al_re1 = 48
    an_re1 = 32

    m = cargarImgPlayer(player1,al_re1,an_re1)
    n = cargarImgPlayer(enemy,al_re1,an_re1)
    player = Jugador(m,[250,120])
    #enemigo = Enemigo(n,[400,100])

    todos = pygame.sprite.Group()
    muros = pygame.sprite.Group()

    mapa = Nivel(doc)
    for lista in mapa.mapa:
        img_m = lista[1]
        xp = lista[0][0]*32
        yp = lista[0][1]*32
        pos = [xp,yp]
        walltype = lista[2]
        m = Muro(img_m,pos,walltype)
        muros.add(m)
        todos.add(m)

    #enemigo.muros = muros
    player.muros = muros
    #todos.add(enemigo)
    todos.add(player)

    fondo = pygame.image.load('imagenes/fondo.jpg')
    fuente = pygame.font.SysFont("comicsansms",25)

    reloj = pygame.time.Clock()
    fin = False
    finjuego = False
    while not fin:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fin = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    player.derecha()
                if evento.key == pygame.K_LEFT:
                    player.izquierda()
                if evento.key == pygame.K_SPACE:
                     player.salto()
                     player.saltar =True
                """if evento.key == pygame.K_DOWN:
                    player.setDir(0)
                if evento.key == pygame.K_UP:
                    player.setDir(3)"""
        if finjuego:
            pantalla.fill([0,0,0])
            texto = fuente.render('Fin de juego',True,[255,255,255])
            pantalla.blit(texto,[300,150])
            pygame.display.flip()
        else:
            pantalla.fill([0,0,0])
            vida = str(player.vida)
            if player.vida <=0:
                finjuego = False
            texto = fuente.render('vida: '+vida,True,[255,255,255])
            pantalla.blit(fondo,[0,0])
            pantalla.blit(player1face,[650,10])
            pantalla.blit(texto,[650,150])
            todos.update()
            todos.draw(pantalla)
            pygame.display.flip()
            reloj.tick(15)
