import pygame
import random

pygame.init()
pygame.display.set_caption("Asteroid Game")
screen = pygame.display.set_mode((800, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    screen.fill("#e63946")
    x = random.randint(10, 790)
    y = random.randint(10, 590)
    r = random.randint(2, 100)

    pygame.draw.circle(screen, ("#1d3557"), (x, y), r)
    pygame.display.flip()
