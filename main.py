import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1200, 800))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUTT:
            pygame.quit()
            sys.exit()