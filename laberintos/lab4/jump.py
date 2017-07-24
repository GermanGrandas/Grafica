from pygame import *

ANCHO = 680
ALTO = 400

class Jugador(sprite.Sprite):
    def __init__(self,imagmatriz,pos):
        sprite.Sprite.__init__(self)
        self.imagmatriz = imagmatriz
        self.con = 0
        self.dir = 2
        self.image = self.imagmatriz[self.dir][0]
        self.rect = self.image.get_rect()
        self.varx = 2
        self.vary = 0
        self.saltar = False
        self.velocidad = 2



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

    def setDir(self,x):
        self.dir = x

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
    init()
    pantalla = display.set_mode([ANCHO, ALTO])
    display.set_caption("animacion")


    player = image.load('imagenes/me.png').convert_alpha()

    al_re1 = 48
    an_re1 = 32

    m = cargarImgPlayer(player,al_re1,an_re1)
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
                    player.derecha()
                if evento.key == K_LEFT:
                    player.izquierda()
                if evento.key == K_SPACE:
                     player.salto()
                     player.saltar =True


        pantalla.fill([0,0,0])
        todos.update()
        todos.draw(pantalla)
        display.flip()
        reloj.tick(30)
