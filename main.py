import pygame
import random

pygame.init()
pygame.display.set_mode((800, 600), pygame.RESIZABLE | pygame.DOUBLEBUF | pygame.HWSURFACE)
pygame.display.set_caption("Asteroid Game")
pygame.display.set_icon(pygame.image.load("icon.bmp"))

clock = pygame.time.Clock()
FPS = 60

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
    clock.tick(FPS)

