import pygame
import math

ANCHO = 680
ALTO = 400




class Bala(pygame.sprite.Sprite):
    def __init__(self,archivo,pos = [200,200]):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.destino = pos
        self.m = 1
        self.move = False

    def update(self):
        if self.move:
            if self.rect.x <= self.xf :
                self.rect.x +=self.x
                self.rect.y +=self.m
                """elif self.rect.x >= self.xf:
                self.rect.x -=self.x
                self.rect.y += self.m
                elif self.rect.y <= self.yf and self.rect.x == self.xf:
                #self.rect.x = self.x
                self.rect.y += self.m"""
            else:
                self.move = False


    def mover(self,info,posf):
        if info:
            self.xf = posf[0]
            self.yf = posf[1]
            self.x = self.rect.x
            self.y = self.rect.y
            if self.xf > self.rect.x:
                self.dx = self.xf-self.rect.x
                self.dy = self.yf-self.rect.y
            """if self.xf > self.rect.x and self.yf > self.rect.y:
                self.dx = self.xf-self.rect.x2
                self.dy = self.yf-self.rect.y"""
            """else:
                self.dx = self.rect.x-self.xf
                self.dy = self.rect.y-self.yf"""
            if self.dx != 0:
                pendiente = float(self.dy/self.dx)
                if pendiente >=0:
                    self.m =1
                else:
                    self.m =(-1)
                self.x = 1
            else:
                self.m = 1
                self.x = 0
            self.move = True


if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    pygame.display.set_caption("disparo")

    bala = Bala('bullet.png',[100,100])
    todos = pygame.sprite.Group()
    todos.add(bala)


    #pygame.mouse.set_visible(False)
    reloj = pygame.time.Clock()
    fin = False
    while not fin:
        pos = pygame.mouse.get_pos()
        for evento in pygame.event.get():
            if evento.type== pygame.QUIT:
                fin = True

            if evento.type == pygame.MOUSEBUTTONDOWN:
                #botones = pygame.mouse.get_pressed()           #botones = (boton_izq, scroll, boton_der)
                bala.mover(True,pos)

        pantalla.fill([0,0,0])
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(180)
