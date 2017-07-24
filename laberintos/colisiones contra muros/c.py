from pygame import *
import random



ANCHO = 800
ALTO = 600


class Jugador(sprite.Sprite):

    def __init__(self,archivo):
        sprite.Sprite.__init__(self)
        self.image = image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.dir = 0
        self.muros= None

    def update(self):
        if self.dir == 1:                             #Evitar salirse de la pantalla
            self.rect.x += 1 if self.rect.x < ANCHO-self.rect.width else 0
        if self.dir == 2:
            self.rect.x -= 1 if self.rect.x > 0 else 0
        if self.dir == 3:
            self.rect.y += 1 if self.rect.y < (ALTO-self.rect.height)  else 0
        if self.dir == 4:
            self.rect.y -= 1 if self.rect.y > 0 else 0

        l_col = sprite.spritecollide(self,self.muros,False)
        for block in l_col:
            if self.dir == 1:
                self.rect.right = block.rect.left
            if self.dir == 2:
                self.rect.left =  block.rect.right
            if self.dir == 3:
                self.rect.bottom = block.rect.top
            if self.dir == 4:
                self.rect.top = block.rect.bottom

    def setDir(self,x):
        self.dir = x

    def setMuros(self,muros):
        self.muros = muros

class Muro(sprite.Sprite):
    def __init__(self, archivo,pos):
        sprite.Sprite.__init__(self)
        self.image = image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

class Enemigo(sprite.Sprite):
    def __init__(self,archivo,pos):
        sprite.Sprite.__init__(self)
        self.image = image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.dir = 0
        self.posdir = [1,2,3,4]
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.muros = None

    def update(self):
        if self.dir == 1:                             #Evitar salirse de la pantalla
            self.rect.x += 1 if self.rect.x < ANCHO-self.rect.width else 0
        if self.dir == 2:
            self.rect.x -= 1 if self.rect.x > 0 else 0
        if self.dir == 3:
            self.rect.y += 1 if self.rect.y < (ALTO-self.rect.height)  else 0
        if self.dir == 4:
            self.rect.y -= 1 if self.rect.y > 0 else 0

        l_col = sprite.spritecollide(self,self.muros,False)
        for block in l_col:
            if self.dir == 1:
                self.rect.right = block.rect.left
            if self.dir == 2:
                self.rect.left =  block.rect.right
            if self.dir == 3:
                self.rect.bottom = block.rect.top
            if self.dir == 4:
                self.rect.top = block.rect.bottom
            self.dir = random.choice(self.posdir)

    def setDir(self,x):
        self.dir = x

    def setMuros(self,muros):
        self.muros = muros



if __name__ == '__main__':
    init()
    pantalla = display.set_mode([ANCHO, ALTO])
    display.set_caption("Sprite")
    fondo = image.load('fondo.jpg')


    todos = sprite.Group()
    muros = sprite.Group()
    enemigos = sprite.Group()


    x=400
    y = 50
    for i in range(5):
        n = Muro('wall1.png',[x,y+(i*64)])
        muros.add(n)
        todos.add(n)

    jp = Jugador('player.png')
    jp.setMuros(muros)
    todos.add(jp)

    en = Enemigo('pika.gif',[400,400])
    en.setMuros(muros)
    enemigos.add(en)
    todos.add(en)

    fin = False
    reloj = time.Clock()
    while not fin:
        for evento in event.get():
            if evento.type== QUIT:
                fin = True
            if evento.type == KEYDOWN:
                if evento.key == K_RIGHT:
                    jp.setDir(1)
                if evento.key == K_LEFT:
                    jp.setDir(2)
                if evento.key == K_DOWN:
                    jp.setDir(3)
                if evento.key == K_UP:
                    jp.setDir(4)
                if evento.key == K_SPACE:
                    jp.setDir(0)
        en.setDir(1)

        pantalla.blit(fondo,[0,0])
        todos.update()
        todos.draw(pantalla)
        display.flip()
