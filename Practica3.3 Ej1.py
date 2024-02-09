    import pygame #Libreria que pertenece a Python

    # Inicialización de Pygame
    pygame.init()

    # Inicialización de la superficie de dibujo
    ventana = pygame.display.set_mode((1000,800)) #Inicia una ventana o pantalla para vizualitar, x (1000), y (800)
    pygame.display.set_caption("Ejemplo 1") #Establece el título de la ventana actual

    # Bucle principal del juego
    jugando = True
    while jugando:#Bucle while para ver todos los eventos de nuestro video juego
        # Comprobamos los eventos
        #Comprobamos si se ha pulsado el botón de cierre de la ventana
        for event in pygame.event.get(): #Eventos
            if event.type == pygame.QUIT:  #Si se cumple está condición(x de la ventana,parte superior derecha) termina
                jugando = False

        # Se pinta la ventana con un color
        # Esto borra los posibles elementos que teníamos anteriormente
        ventana.fill((255, 255, 255))

        # Todos los elementos del juego se vuelven a dibujar
        pygame.display.flip()

        # Controlamos la frecuencia de refresco (FPS)
        pygame.time.Clock().tick(60)

    pygame.quit()   #Desinializa todos los módulos de pygame