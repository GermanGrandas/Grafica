import pygame



ANCHO = 600
ALTO = 400
rojo = (255,0,0)






if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])

    fondo = pygame.image.load('fondo.jpg')
    an_img , al_img = fondo.get_size()



    xf =0
    fin = False
    reloj = pygame.time.Clock()

    while not fin:
        pos = pygame.mouse.get_pos()
        for evento in pygame.event.get():
            if evento.type== pygame.QUIT:
                fin = True

        if pos[0] >= 590:
            xf -=2
            lim =-(an_img-ANCHO)
            if xf < lim:
                xf = lim
        elif pos[0] <= 10:
            xf +=2
            if xf >0:
                xf =0

        pantalla.blit(fondo,[xf,-520])
        reloj.tick(60)
        pygame.display.flip()
