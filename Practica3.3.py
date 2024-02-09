import pygame #Libreria que pertenece a Python


pygame.init()   #Inicia todo lo importado de los modulos de pygame
ventana = pygame.display.set_mode((1000,800))   #Inicia una ventana o pantalla para vizualitar, x (1000), y (800)
pygame.display.set_caption("Hamburgueso")   #Establece el título de la ventana actual


ball = pygame.image.load("hamburguesa (1).png") #Cargar una imganen desde un archivo y en () el nombre de la imagen o archivo formato png
ballrect = ball.get_rect()  #La imagen cargada será en forma rectangular
speed = [4,4]           #Velocidad en el eje x(4), y(4)
ballrect.move_ip(0,0)   #Posición de la imagen cargada en el punto 0,0 'parte superior izquierda'




bate = pygame.image.load("barra (1).png")  # Carga una imagen nueva desde un archivo,  y en () el nombre de la imagen o archivo formato png
baterect = bate.get_rect() #La imagen cargada será en forma rectangular


# Pongo el bate en la parte inferior de la pantalla
baterect.move_ip(500,700)  #posición de nuestra 2da imagen, en este caso depende de nuestra venta, 1000,800
                           #para tenerlo en la posición correcta




jugando = True
while jugando: #Bucle while para ver todos los eventos de nuestro video juego
    for event in pygame.event.get():    #Eventos
        if event.type == pygame.QUIT:  #Si se cumple está condición(x de la ventana,parte superior derecha) termina
            jugando = False


    # Compruebo si se ha pulsado alguna tecla
    keys = pygame.key.get_pressed()     #Obtiene el estado de todos los botones del teclado    
    if keys[pygame.K_LEFT]:         #.K_LEFT = Consigue el identificador del codigo desde el nombre descriptivo, flecha izquierda
        baterect = baterect.move(-5,0)          #Velocidad y dirección (-) de la barra hacia la izquierda
    if keys[pygame.K_RIGHT]:        #.K_RIGHT = Consigue el identificador del codigo desde el nombre descriptivo, flecha derecha
        baterect = baterect.move(5,0)           #Velocidad y dirección (+) de la barra hacia la derecha


    # Compruebo si hay colisión
    if baterect.colliderect(ballrect): #Verifica la detección de colisiones entre baterect y ballrect
        speed[1] = -speed[1] #Consigue un número de lista de 2 índices, y de está manera debota la imagen1 con la imagen2.
    ballrect = ballrect.move(speed) #Actualiza la posición del objeto ballrect
    if ballrect.left < 0 or ballrect.right > ventana.get_width(): #Verifica si el objeto ha alcanzado los limites laterales de la ventana


        speed[0] = -speed[0]    #La imagen 1 rebota con los laterales de la ventana
    if ballrect.top < 0 or ballrect.bottom > ventana.get_height(): #Verifica si el objeto ha alcanzado los frontales y traseros de la ventana


        speed[1] = -speed[1]    #La imagen 1 rebota con la parte baja y superior de la ventana
    ventana.fill((133, 193, 233))   #Colores del sistema RGB, Rojo, verde, azul
    ventana.blit(ball, ballrect)    #Pone el objeto en la ventana del juego en una posición especifica


    # Dibujo el bate
    ventana.blit(bate, baterect) #Pone  el objeto en la ventada de juego en una posición específica
    pygame.display.flip()   #Actualiza la superficia de la pantalla que vizualisamos
    pygame.time.Clock().tick(60)    #Crea un objeto para ayudar a la pista del tiempo,en milisegundos,y actualiza el reloj.


pygame.quit()       #Desinializa todos los módulos de pygame