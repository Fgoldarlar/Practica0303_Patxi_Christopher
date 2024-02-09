import pygame #Libreria que pertenece a Python


pygame.init() # Inicialización de Pygam
ventana = pygame.display.set_mode((1000 ,800)) #Inicia una ventana o pantalla para vizualitar, x (1000), y (800)
pygame.display.set_caption("ejercicio 2") #Establece el título de la ventana actual

# Crea el objeto pelota
ball = pygame.image.load("hamburguesa (1).png")

# Obtengo el rectángulo del objeto anterior
ballrect = ball.get_rect()

# Inicializo los valores con los que se van a mover la pelota
speed = [4,4]

# Pongo la pelota en el origen de coordenadas
ballrect.move_ip(0,0)

# Inicialización de la superficie de dibujo
jugando = True
while jugando:#Bucle while para ver todos los eventos de nuestro video juego
    # Comprobamos los eventos
    #Comprobamos si se ha pulsado el botón de cierre de la ventana
    for event in pygame.event.get(): #Eventos
        if event.type == pygame.QUIT:  #Si se cumple está condición(x de la ventana,parte superior derecha) termina
            jugando = False 

    # Muevo la pelota
    ballrect = ballrect.move(speed)

    # Compruebo si la pelota llega a los límites laterales de la ventana 
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]

    # Compruebo si la pelota llega a los límites frontales de la ventana 
    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speed[1] = -speed[1]

    # Se pinta la ventana con un color
    # Esto borra los posibles elementos que teníamos anteriormente
    ventana.fill((252, 243, 207))

    # Dibujo la pelota
    ventana.blit(ball, ballrect)
    pygame.display.flip() #Actualiza la pantalla para mostrar los cambios realizados
    pygame.time.Clock().tick(60) #Velocidad de fotogramas a 60 por segundo

pygame.quit()  #Desinializa todos los módulos de pygame

