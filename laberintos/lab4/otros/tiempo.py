import pygame

ANCHO = 640
ALTO = 460

blanco = [255,255,255]
negro = [0,0,0]
rojo = [255,0,0]




if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])

    fr_cont = 0
    tasa = 60
    t_ini = 20
    fuente = pygame.font.Font(None,50)
    col = blanco

    reloj = pygame.time.Clock()
    fin = False
    while not fin:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fin = True

        total_seg = fr_cont//tasa
        minutos = total_seg // 60
        segundos = total_seg%60
        pantalla.fill(negro)
        txt_tiempo = 'tiempo: {0:02}:{1:02}'.format(minutos,segundos)
        texto = fuente.render(txt_tiempo,True,blanco)
        pantalla.blit(texto,[100,100])

        total_seg = t_ini -(fr_cont//tasa)
        if total_seg < 0:
            total_seg = 0
        if total_seg < 5:
            col = rojo
        minutos = total_seg // 60
        segundos = total_seg%60
        txt_tiempo = 'tiempo: {0:02}:{1:02}'.format(minutos,segundos)
        texto1 = fuente.render(txt_tiempo,True,col)
        pantalla.blit(texto1,[100,300])

        pygame.display.flip()
        reloj.tick(tasa)
        fr_cont+=1
