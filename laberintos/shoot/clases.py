from pygame import *
from libreria import *



if __name__ == '__main__':
    init()
    pantalla = display.set_mode([ANCHO,ALTO])
    display.set_caption("ejemplo")
    fin = False

    pantalla.fill(black)
    #plano = Cartesiano([540,300],pantalla)
    #vector = Vector([100,15])

    #plano.Punto([10,20])
    #plano.EjeH()

    #plano.Punto(recta.Position())
    todos = sprite.Group()
    var_x = 0

    #plano.Poli([[-100,20],[26,30],[150,-100],[48,200]])
    pantalla.fill(black)

    reloj = time.Clock()
    while not fin:
        for evento in event.get():
            if evento.type == QUIT:
                fin = True
            if evento.type == KEYDOWN:
                if evento.key == K_SPACE:
                    bala = Bala('bullet.png')
                    todos.add(bala)
                    if bala.recta.posf[0] <= 0:
                        todos.remove(bala)

        pantalla.fill(black)

#        draw.circle(pantalla,red,recta.Position(var_x),5)
        todos.update()
        todos.draw(pantalla)
        display.flip()
        reloj.tick(120)
