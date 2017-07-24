from pygame import *

ANCHO = 680
ALTO = 400

black = [0,0,0]

class Jugador(sprite.Sprite):

    def __init__(self,archivo):
        sprite.Sprite.__init__(self)
        self.image = archivo
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
    def setDir(self,x):
        self.dir = x

    def setImage(self,x):
        self.image = x


if __name__ == '__main__':
    init()
    pantalla = display.set_mode([ANCHO, ALTO])
    display.set_caption("prueba")

    todos = sprite.Group()

    imagen = image.load('1.png').convert_alpha()
    ancho, alto = imagen.get_size()

    an_re = 32
    al_re = 50

    fila = []

    for var_y in range(0,4):
        cuadro = [0,0+var_y*al_re,an_re,al_re]
        img_cuadro = imagen.subsurface(cuadro)
        fila.append(img_cuadro)


    jg = Jugador(fila[0])
    todos.add(jg)
    display.flip()

    fin = False
    reloj = time.Clock()
    while not fin:
        for evento in event.get():
            if evento.type== QUIT:
                fin = True
            if evento.type == KEYDOWN:
                if evento.key == K_RIGHT:
                    jg.setDir(1)
                    jg.setImage(fila[2])
                if evento.key == K_LEFT:
                    jg.setDir(2)
                    jg.setImage(fila[1])
                if evento.key == K_DOWN:
                    jg.setDir(3)
                    jg.setImage(fila[0])
                if evento.key == K_UP:
                    jg.setDir(4)
                    jg.setImage(fila[3])
                if evento.key == K_SPACE:
                    jg.setDir(0)
        pantalla.fill(black)
        todos.update()
        todos.draw(pantalla)
        display.flip()
        reloj.tick(60)
