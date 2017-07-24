import json
import pygame
import random

ANCHO = 1080
ALTO = 680


class Jugador(pygame.sprite.Sprite):
    def __init__(self,imagmatriz,pos):
        pygame.sprite.Sprite.__init__(self)
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

class Bala(pygame.sprite.Sprite):
    class Recta(object):
        def __init__(self,origen,posf):
            self.origen= origen
            self.posf = posf
            self._pendiente = (self.posf[1]-self.origen[1])/(self.posf[0]-self.origen[0])
            self._b = self.posf[1]-(self.posf[0]*self._pendiente)
            self.y = 0

        def Position(self):
            if self.origen[0] < self.posf[0]:
                self.y = int(self.origen[0]*self._pendiente + self._b)
                self.origen[0] +=3
            #else:
                #self.origen[0] = 64
            return [self.origen[0],self.y]

    def __init__(self,archivo,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.count = 0
        self.recta = self.Recta(pos,[ANCHO,ALTO])

    def update(self):
        #if self.rect.y <= ALTO-self.rect.height:
        pos = self.recta.Position()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


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
            #if valor["name"] == "mapa1":
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
        self._posdir = [0,1,2,3]
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
            self.dir = random.choice(self._posdir)

    def setDir(self,x):
        self.dir = x

    def setMuros(self,muros):
        self.muros = muros

class Staticenemy(pygame.sprite.Sprite):
    def __init__(self,archivo,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = archivo
        self.rect = pos
        self.contador = 0
        self.shoot = False

    def update(self):
        if self.shoot:
            self.contador+=1

    def resetCont(self):
        self.contador = 0


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

    with open('mapa2.json') as js_archivo:
        doc = json.load(js_archivo)


    player1 = pygame.image.load('imagenes/me.png').convert_alpha()
    #player1face = pygame.image.load('imagenes/Meface.png').convert_alpha()

    enemy = pygame.image.load('imagenes/Luisa.png').convert_alpha()
    gargola = pygame.image.load('imagenes/gargola.png').convert_alpha()
    al_re1 = 48
    an_re1 = 32

    m = cargarImgPlayer(player1,al_re1,an_re1)
    n = cargarImgPlayer(enemy,al_re1,an_re1)

    player = Jugador(m,[50,100])
    enemigo = Enemigo(n,[400,100])
    gargola = Staticenemy(gargola,[32,32])

    enemigos = pygame.sprite.Group()
    b_ene = pygame.sprite.Group()

    todos = pygame.sprite.Group()
    muros = pygame.sprite.Group()

    enemigos.add(gargola)
    todos.add(gargola)

    mapa = Nivel(doc)
    for lista in mapa.mapa:
        img_m = lista[1]
        xp = lista[0][0]*32
        yp = lista[0][1]*32
        walltype = lista[2]
        pos = [xp,yp]
        m = Muro(img_m,pos,walltype)
        muros.add(m)
        todos.add(m)

    enemigo.muros = muros
    player.muros = muros
    #enemigos.add(enemigo)
    todos.add(enemigo)
    todos.add(player)

    fondo = pygame.image.load('imagenes/mapa2.png')
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
                    player.setDir(2)
                if evento.key == pygame.K_LEFT:
                    player.setDir(1)
                if evento.key == pygame.K_DOWN:
                    player.setDir(0)
                if evento.key == pygame.K_UP:
                    player.setDir(3)
                if evento.key == pygame.K_SPACE:
                    gargola.shoot = True
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

            for x in enemigos:
                if x.contador == 100:
                    balaE = Bala('imagenes/bullet.png',[64,70])
                    b_ene.add(balaE)
                    todos.add(balaE)
                    x.resetCont()


            #texto = fuente.render('vida: '+vida,True,[255,255,255])
            pantalla.blit(fondo,[0,0])
            #pantalla.blit(player1face,[650,10])
            #pantalla.blit(texto,[650,150])
            todos.update()
            todos.draw(pantalla)
            pygame.display.flip()
            reloj.tick(15)
