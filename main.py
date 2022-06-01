import pygame
import sys
from pygame.color import THECOLORS


pygame.init()

pygame.display.set_caption('myNewGame')

#создание экрана
screen = pygame.display.set_mode((1200, 800))
#загрузка картинки из папки
image = pygame.image.load('bin/01.png')
# размер картинки
image = pygame.transform.scale(image, (250, 250))
#агрузка фона
bg = pygame.image.load('bin/2.png')
# размер фона
bg = pygame.transform.scale(bg, (1200, 800))
#координаты
screen.blit(bg, (0, 0))
screen.blit(image, (250, 250))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        pygame.display.flip()