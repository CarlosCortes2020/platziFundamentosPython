import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ejemplo Pygame")

# Definir colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Posición inicial del círculo
x, y = 400, 300
radius = 30
speed = 5

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtener teclas presionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Rellenar la pantalla con blanco
    screen.fill(WHITE)
    
    # Dibujar el círculo azul
    pygame.draw.circle(screen, BLUE, (x, y), radius)
    
    # Actualizar la pantalla
    pygame.display.flip()
    
    # Controlar la velocidad del bucle
    pygame.time.Clock().tick(30)

# Cerrar Pygame
pygame.quit()
sys.exit()
