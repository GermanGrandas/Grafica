from pygame import *

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



if __name__ == '__main__':
    init()
    pantalla = display.set_mode([ANCHO, ALTO])
    display.set_caption("animacion")


    imagen = image.load('p.png').convert_alpha()


    al_re = 48
    an_re = 32
    m = []
    for fila in range(4):
        lista = []
        for i in range(4):
            cuadro = imagen.subsurface(0+i*an_re,0+fila*al_re,an_re,al_re)
            lista.append(cuadro)
        m.append(lista)

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
