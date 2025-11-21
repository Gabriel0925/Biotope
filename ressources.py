import pygame

pygame.init()

ecran = pygame.display.set_mode((300, 200))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False