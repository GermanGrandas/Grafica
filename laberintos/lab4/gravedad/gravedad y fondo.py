import pygame



ANCHO = 600
ALTO = 400
rojo = (255,0,0)


class Jugador(pygame.sprite.Sprite):
    def __init__(self,alto,ancho,infoimg):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([ancho,alto])
        self.image.fill(rojo)
        self.rect = self.image.get_rect()
        self.varx = 2
        self.vary = 0
        self.saltar = False
        self.velocidad = 2
        self.xf =0
        self.img = infoimg

    def derecha(self):
        self.varx =self.velocidad

    def izquierda(self):
        self.varx =-(self.velocidad)


    def salto(self):
        if not self.saltar:
            self.vary = -10

    def gravedad(self):
        if self.vary == 0:
            self.vary = 1
        else:
            self.vary += 0.3

        piso = ALTO-self.rect.height
        if self.rect.y >= piso and self.vary >= 0:
            self.vary =0
            self.rect.y = piso
            self.saltar = False


    def update(self):
        self.gravedad()

        if self.rect.x >= 560 and self.varx>0:
            self.rect.x = 560
            self.xf -=2
            lim =-(self.img[0]-ANCHO)
            if self.xf < lim:
                self.xf = lim
        elif self.rect.x <= 60 and self.varx<0:
            self.rect.x = 60
            self.xf +=2
            if self.xf >0:
                self.xf =0
        else:
            self.rect.x+=self.varx

        self.rect.y += self.vary



if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])

    fondo = pygame.image.load('fondo.jpg')
    an_img , al_img = fondo.get_size()

    todos = pygame.sprite.Group()
    jp = Jugador(50,30,[an_img,al_img])
    todos.add(jp)

    xf =0
    fin = False
    reloj = pygame.time.Clock()
    while not fin:
        for evento in pygame.event.get():
            if evento.type== pygame.QUIT:
                fin = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    jp.derecha()
                if evento.key == pygame.K_LEFT:
                    jp.izquierda()
                if evento.key == pygame.K_SPACE:
                    jp.salto()
                    jp.saltar =True


        pantalla.blit(fondo,[jp.xf,-520])
        todos.update()
        todos.draw(pantalla)
        reloj.tick(60)
        pygame.display.flip()
