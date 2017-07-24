import pygame


ANCHO = 640
ALTO = 480

class Jugador(pygame.sprite.Sprite):
    def __init__(self,imagmatriz,pos):
        pygame.sprite.Sprite.__init__(self)
        self.imagmatriz = imagmatriz
        self.dir = 2
        self.con = 0
        self.image = self.imagmatriz[self.dir][0]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.muros = None
        self.vida =100

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
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    pygame.display.set_caption("niveles")

    fuente = pygame.font.Font(None,32)
    texto = fuente.render('mensaje',True,[255,255,255])

    player1 = pygame.image.load('imagenes/me.png').convert_alpha()
    al_re1 = 48
    an_re1 = 32

    m = cargarImgPlayer(player1,al_re1,an_re1)
    player = Jugador(m,[100,100])

    todos = pygame.sprite.Group()
    todos.add(player)




    reloj = pygame.time.Clock()

    continuar = True
    pag = 1
    while continuar:
        for evento in pygame.event.get():
            if evento.type== pygame.QUIT:
                fin = True
                continuar = False
            if evento.type == pygame.KEYDOWN:
                pag+=1
                if pag >2:
                    continuar = False

            if pag == 1:
                texto = ("Habia una vez...")
                texto = fuente.render(texto,True,[255,255,255])
                pantalla.blit(texto,[200,200])
                pygame.display.flip()

            if pag == 2:
                txt = ("En una galaxia no muy lejana...")
                txt = fuente.render(txt,True,[255,255,255])
                pantalla.blit(txt,[200,50])
                img_info = pygame.image.load('imagenes/somewhere.jpg')
                img_info = pygame.transform.scale(img_info,[500,200])
                pantalla.blit(img_info,[50,80])
                pygame.display.flip()
            reloj.tick(60)

    #codigo del juego
    #nivel 1
    fondo = pygame.image.load('imagenes/fondo.jpg')

    victoria = False

    fin = False
    finjuego = False
    seguir = True
    while seguir and not fin:
        pos = pygame.mouse.get_pos()
        for evento in pygame.event.get():
            if evento.type== pygame.QUIT:
                fin = True
                seguir = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    player.setDir(2)
                if evento.key == pygame.K_LEFT:
                    player.setDir(1)
                if evento.key == pygame.K_DOWN:
                    player.setDir(0)
                if evento.key == pygame.K_UP:
                    player.setDir(3)
                if evento.key == pygame.K_q:
                    victoria = True
                if evento.key == pygame.K_SPACE:
                    victoria = False
                seguir = False

        txt = 'Informacion'
        pantalla.blit(fondo,[0,0])
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(20)

    if not victoria:
        seguir = True
        while seguir:
            for evento in pygame.event.get():
                if evento.type== pygame.QUIT:
                    fin = True
                    seguir = False
                if evento.type == pygame.KEYDOWN:
                    seguir = False

            pantalla.fill([0,0,0])
            txt = 'Fin de juego'
            texto = fuente.render(txt,True,[255,255,255])
            pantalla.blit(texto,[200,200])
            pygame.display.flip()
    else:
        seguir = True
        while seguir:
            for evento in pygame.event.get():
                if evento.type== pygame.QUIT:
                    fin = True
                    seguir = False
                if evento.type == pygame.KEYDOWN:
                    seguir = False

            pantalla.fill([0,0,0])
            txt = 'Nivel 2'
            texto = fuente.render(txt,True,[255,255,255])
            pantalla.blit(texto,[200,200])
            pygame.display.flip()

#Nivel 2
#cargo informacion mapa

if victoria:
    seguir = True
    victoria = False
    while seguir and not fin:
        for evento in pygame.event.get():
            if evento.type== pygame.QUIT:
                fin = True
                seguir = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_q:
                    victoria = True
                if evento.key == pygame.K_SPACE:
                    victoria = False
                seguir = False

        txt = 'Informacion'
        pantalla.blit(fondo,[0,0])
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(20)

if not victoria:
    seguir = True
    while seguir:
        for evento in pygame.event.get():
            if evento.type== pygame.QUIT:
                fin = True
                seguir = False
            if evento.type == pygame.KEYDOWN:
                seguir = False

        pantalla.fill([0,0,0])
        txt = 'Fin de juego'
        texto = fuente.render(txt,True,[255,255,255])
        pantalla.blit(texto,[200,200])
        pygame.display.flip()
