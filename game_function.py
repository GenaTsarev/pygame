import pygame
# окно игры
gameDisplay = pygame.display.set_mode((display_width, display_height))  # размер
pygame.display.set_caption("Разбей мою тачку!!!")  # название игры

# функция отрисовка препятствий
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])