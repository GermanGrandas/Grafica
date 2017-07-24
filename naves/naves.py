from pygame import *
import random

ANCHO = 960
ALTO = 540


class Jugador(sprite.Sprite):

    def __init__(self,archivo):
        sprite.Sprite.__init__(self)
        self.image = image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = ALTO - self.rect.height
        self.dir = True

    def setDir(self,x):
        self.dir = x

    def getPos(self):
        m = int(self.rect.width/2) -2
        return [self.rect.x+m,self.rect.y]

    def update(self):
        #moverse derecha
        if self.dir:
            self.rect.x+=2
            if self.rect.x >= ANCHO-self.rect.width:
                self.rect.x = ANCHO-self.rect.width
        #moverse izquierda
        if not self.dir:
            self.rect.x-=2
            if self.rect.x <= 0:
                self.rect.x = 0




class Enemigo(sprite.Sprite):
    def __init__(self,archivo_img,vel = 1):#color,ancho,alto):
        sprite.Sprite.__init__(self)
        self.image = image.load(archivo_img).convert_alpha()
        self.rect = self.image.get_rect()
        self.vel = vel
        self.dir = True
        self.contador = 0#random.randint(100,400)

    def update(self):
        if self.rect.x <= 0:
            self.dir = True
            #self.rect.y+=self.vel
        elif self.rect.x >=(ANCHO-self.rect.width):
            self.dir = False
            self.vel+=1
        """if self.vel > 10:
            self.rect.y+=self.vel"""
        self.contador+=1
        self.rect.x+= self.vel if self.dir else -self.vel

    def getPos(self):
        m = int(self.rect.width/2) -2
        return [self.rect.x+m,self.rect.y]

    def getCont(self):
        return self.contador
    def resetCont(self):
        self.contador = 0

class Bala(sprite.Sprite):
    def __init__(self,archivo,pos,who):
        sprite.Sprite.__init__(self)
        self.image = image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.who = who

    def update(self):
        #if self.rect.y <= ALTO-self.rect.height:
        if self.who:
            self.rect.y-=2
        else:
            self.rect.y+=2


if __name__ == '__main__':
    init()
    pantalla = display.set_mode([ANCHO, ALTO])
    display.set_caption("naves")



    todos = sprite.Group()
    enemigos = sprite.Group()
    b_ene = sprite.Group()
    b_jug = sprite.Group()

    #variables: inicializacion
    fondo = image.load('imagenes/fondo.jpg')
    jp = Jugador('imagenes/i.png')
    soundshot =mixer.Sound('sonidos/jpshot.wav')
    todos.add(jp)


    for i in range(10):

        #b = Bloque(turquoise,20,20)
        b = Enemigo('imagenes/en1.png')
        c = Enemigo('imagenes/en2.png')
        b.rect.x = random.randint(10,ANCHO)
        b.rect.y = 50
        c.rect.x = random.randint(10,ANCHO)
        c.rect.y = 200

        enemigos.add(b)
        todos.add(b)
        enemigos.add(c)
        todos.add(c)


    fin = False
    reloj = time.Clock()
    while not fin:
        # Captura de eventos

        for evento in event.get():
            if evento.type== QUIT:
                fin = True

            if evento.type == KEYDOWN:
                if evento.key == K_RIGHT:
                    jp.setDir(True)
                if evento.key == K_LEFT:
                    jp.setDir(False)
                if evento.key == K_SPACE:
                    bala = Bala('imagenes/shot1.png',jp.getPos(),True)
                    soundshot.play()
                    b_jug.add(bala)
                    todos.add(bala)


        #ciclo del juego
        for x in enemigos:
            if x.getCont() == random.randint(100,600):
                balaE = Bala('imagenes/shot3.png',x.getPos(),False)
                b_ene.add(balaE)
                todos.add(balaE)
                x.resetCont()

        for bala in b_jug:
            ls = sprite.spritecollide(bala,enemigos,True)
            for e in ls:
                b_jug.remove(bala)
                todos.remove(bala)
        pantalla.blit(fondo,[0,0])
        todos.update()
        todos.draw(pantalla)
        display.flip()
        reloj.tick(60)
