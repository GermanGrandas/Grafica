import pygame


ANCHO = 680
ALTO = 400

class Jugador(pygame.sprite.Sprite):
    def __init__(self,imagmatriz):
        pygame.sprite.Sprite.__init__(self)
        self.imagmatriz = imagmatriz
        self.accion = 1
        self.con = 0
        self.dir = 0
        self.stop = False
        self.varx = 2
        self.vary = 0
        self.velocidad = 2
        self.image = self.imagmatriz[self.accion][self.con]
        self.rect = self.image.get_rect()
        self.rect.y = 200
        self.lsriv = None
        self.saltar = False

    def salto(self,distance = 10):
        if not self.saltar:
            self.vary = -distance

    def gravedad(self):
        if self.vary == 0:
            self.vary = 1
        else:
            self.vary += 0.3

        piso = ALTO-200#self.rect.height
        if self.rect.y >= piso and self.vary >= 0:
            self.vary =0
            self.rect.y = piso
            self.saltar = False

    def update(self):
        self.gravedad()
        #Caminar
        if self.accion == 1:
            self.image = self.imagmatriz[self.accion][self.con]
            if self.con <5 and not self.stop:
                self.con += 1
            else:
                self.con = 0
            if not self.saltar:
                if self.dir == 0:
                    self.stop = True
                if self.dir == 1:
                    self.rect.x += self.varx
                    self.stop=False
                if self.dir == 3:
                    self.rect.x -= self.varx
                    self.stop=False
        #Patada
        if self.accion == 2:
            self.image = self.imagmatriz[self.accion][self.con]
            if self.con <5:
                self.con += 1
            else:
                self.con = 0
            #analizar colision

            for e in self.lsriv:
                posgp = [self.rect.x+self.rect.width,self.rect.y]
                if e.rect.collidepoint(posgp):
                    e.rect.x +=self.varx
        #Salto
        if self.accion == 5:
            self.image = self.imagmatriz[self.accion][self.con]
            if self.dir == 0:
                self.stop = True
            if self.dir == 1:
                self.rect.x += self.varx
                self.stop=False
            if self.dir == 3:
                self.rect.x -= self.varx
                self.stop=False
            if self.con <4:
                self.con += 1
            else:
                self.con = 0
        #fist
        if self.accion == 0:
            self.image = self.imagmatriz[self.accion][self.con]
            if self.con <3:
                self.con += 1
            else:
                self.con = 0
            for e in self.lsriv:
                posgp = [self.rect.x+(self.rect.width-13),self.rect.y]
                if e.rect.collidepoint(posgp):
                    e.rect.x +=self.varx
        self.rect.y += self.vary

class Dummy(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([35,80])
        self.image.fill([255,255,255])
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.vida = 100

def cargarImgPlayer(image,al_re,an_re):
    m= []
    for fila in range(6):
        lista = []
        for i in range(8):
            cuadro = image.subsurface(0+i*an_re,0+fila*al_re,an_re,al_re)
            lista.append(cuadro)
        m.append(lista)
    return m

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])

    imagen = pygame.image.load('Cody.png').convert_alpha()

    m = cargarImgPlayer(imagen,100,100)
    player = Jugador(m)

    todos = pygame.sprite.Group()
    rivales = pygame.sprite.Group()
    todos.add(player)

    ob = Dummy([150,200])
    rivales.add(ob)
    player.lsriv = rivales
    todos.add(ob)

    fin  = False
    pause = False
    reloj = pygame.time.Clock()
    while not fin:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fin = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    player.dir = 1
                if evento.key == pygame.K_LEFT:
                    player.dir = 3
                if evento.key == pygame.K_SPACE:
                    player.accion = 2
                    player.salto(5)
                    player.saltar = True
                if evento.key == pygame.K_q:
                    player.accion = 5
                    player.salto()
                    player.saltar = True
                if evento.key == pygame.K_e:
                    player.accion = 0
                if evento.key == pygame.K_p:
                    if pause == False:
                        pause = True
                    else:
                        pause = False
            if evento.type == pygame.KEYUP:
                player.dir = 0
                player.accion = 1

        if not pause:
            pantalla.fill([0,0,0])
            todos.update()
            todos.draw(pantalla)
            pygame.display.flip()
            reloj.tick(15)
