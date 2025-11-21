import pygame

pygame.init()

ecran = pygame.display.set_mode((300, 200))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False