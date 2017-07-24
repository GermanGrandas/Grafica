import pygame
import random


ANCHO = 600
ALTO = 400
rojo = (255,0,0)

class bloque(pygame.sprite.Sprite):
    def __init__(self,archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.vida = 100

class Arma(pygame.sprite.Sprite):
    def __init__(self,archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo)
        self.rect = self.image.get_rect()

    def setPos(self,pos):
        self.rect.x = pos[0]-(self.rect.width /2)
        self.rect.y = pos[1] - (self.rect.height / 2)



if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])

    todos = pygame.sprite.Group()

    cubos= pygame.sprite.Group()
    disparo = pygame.mixer.Sound("shoot.ogg")
    fondo = pygame.image.load('fondo.jpg')
    an_img , al_img = fondo.get_size()

    arma = Arma('t32.png')
    todos.add(arma)

    fuente = pygame.font.SysFont("comicsansms",25)
    pygame.mouse.set_visible(False)
    xf =0
    fin = False
    reloj = pygame.time.Clock()
    temp = 100
    count = 0
    victoria = False
    while not fin:
        pos = pygame.mouse.get_pos()
        for evento in pygame.event.get():
            if evento.type== pygame.QUIT:
                fin = True
            if evento.type == pygame.MOUSEBUTTONDOWN:
                disparo.play()
                for c in cubos:
                    if c.rect.collidepoint(pos):
                        count+=10
                        cubos.remove(c)
                        todos.remove(c)

        arma.setPos(pos)

        if pos[0] >= 590:
            xf -=2
            lim =-(an_img-ANCHO)
            moneda = random.randrange(100)
            if moneda >80:
                if temp<=0:
                    b = bloque('enemy.png')
                    b.rect.x = ANCHO+100
                    b.rect.y = ALTO-50 -b.rect.height
                    if len(todos) < 4:
                        todos.add(b)
                        cubos.add(b)
                    t=100
            if xf < lim:
                xf = lim
        elif pos[0] <= 10:
            xf +=2
            if xf >0:
                xf =0
        for e in todos:
            if pos[0] > 550:
                e.rect.x -=2
            if pos[0] < 50:
                e.rect.x +=2
        if count >= 210:
            pantalla.fill([0,0,0])
            texto = fuente.render('Fin de juego. Ganaste',True,[255,255,255])
            pantalla.blit(texto,[200,150])
            pygame.display.flip()
        else:
            pantalla.blit(fondo,[xf,-520])
            texto = fuente.render('Puntaje:'+ str(count),True,[255,255,255])
            pantalla.blit(texto,[300,150])
            todos.draw(pantalla)
            pygame.display.flip()
            reloj.tick(60)
            temp-=1
