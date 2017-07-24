import pygame



ANCHO = 640
ALTO = 480
rojo = (255,0,0)


if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])

    fondo = pygame.image.load('fondo.jpg')

    x =0
    fin = False
    reloj = pygame.time.Clock()
    while not fin:
        for evento in pygame.event.get():
            if evento.type== pygame.QUIT:
                fin = True
        pantalla.blit(fondo,[x,-720])
        pygame.display.flip()
        reloj.tick(60)
        x-=2
