from pygame import *
from math import *
import random


ANCHO = 1080
ALTO =600


#Colores

red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]
yellow = [255,255,0]
white =[255,255,255]
black = [0,0,0]
aqua = [0,255,255]
crimson = (220,20,60)
turquoise = (64,224,208)

#color = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

class Bloque(sprite.Sprite):
    def __init__(self,archivo_img):#color,ancho,alto):
        sprite.Sprite.__init__(self)
        #self.image = Surface([ancho,alto])
        #self.image.fill(color)
        self.image = image.load(archivo_img).convert_alpha()
        self.rect = self.image.get_rect()

class Enemigo(sprite.Sprite):
    def __init__(self,archivo_img):#color,ancho,alto):
        sprite.Sprite.__init__(self)
        self.image = image.load(archivo_img).convert_alpha()
        self.rect = self.image.get_rect()
        self.vel = 2
        self.dir = False

    def update(self):
        if self.rect.x <= 0:
            self.dir = True
            self.rect.y+=self.vel
        elif self.rect.x >=(ANCHO - self.rect.width):
            self.dir = False
            self.vel+=1
            self.rect.y+=self.vel

        self.rect.x+= self.vel if self.dir else -self.vel


if __name__ == '__main__':
    init()
    pantalla = display.set_mode([ANCHO, ALTO])
    display.set_caption("Sprite")
    pantalla.fill(white)

    mouse.set_visible(False)

    enemigos = sprite.Group()
    todos = sprite.Group()

    #jugador = Bloque(crimson,50,50)
    jugador = Bloque('i.png')
    todos.add(jugador)

    for i in range(10):

        #b = Bloque(turquoise,20,20)
        b = Enemigo('en1.png')
        c = Enemigo('en2.png')
        b.rect.x = random.randint(10,ANCHO)
        b.rect.y = 50
        c.rect.x = random.randint(10,ANCHO)
        c.rect.y = 200


        enemigos.add(b)
        todos.add(b)
        enemigos.add(c)
        todos.add(c)




    fin = False
    puntos = 0
    reloj = time.Clock()
    while not fin:
        pos = mouse.get_pos()
        for evento in event.get():
            if evento.type== QUIT:
                fin = True

        jugador.rect.x = pos[0]
        jugador.rect.y = pos[1]
        #lista de tocados
        ls_t = sprite.spritecollide(jugador,enemigos,True)

        for elemento in ls_t:
            puntos+=1
            #print puntos

        pantalla.fill(black)
        todos.update()
        todos.draw(pantalla)
        display.flip()
        reloj.tick(60)
