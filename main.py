import pygame
import sys
import time
import random

# стартует в файле модуль пайгейм
pygame.init()

# размер окна
display_width = 800  # параметр высота
display_height = 600  # параметр ширина

# окно игры
gameDisplay = pygame.display.set_mode((display_width, display_height))  # размер
pygame.display.set_caption("Разбей мою тачку!!!")  # название игры

# цвета
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# модуль для времени, чтобы мониторить кадры в секунду
clock = pygame.time.Clock()

# игрок
carImg = pygame.image.load('images/car.png')  # картинка для игрока
carImg = pygame.transform.scale(carImg, (70, 140))  # задаем размеры картинки, если это нреобходимо
car_wigth = 70


# функция отрисовка препятствий
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


# отрисовка авто
def car(x, y):
    gameDisplay.blit(carImg, (x, y))


# вывод текста
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


# вывод текста на экран
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def crash():
    message_display('!!!ТЫ МЁРТВ!!!')


# блок для запуска игры
def game_loop():
    # размещение авто в игре
    x = (display_width * 0.45)
    y = (display_height * 0.75)

    # параметры для появления things
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 5
    thing_wigth = 100
    thing_height = 100

    x_change = 0  # позиция
    car_speed = 0  # скорость
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.quit()
                sys.quit()

            # блок для обработки нажатия на клавиши
            if event.type == pygame.KEYDOWN:
                # если нажале на  esc , то окно закрывается
                if event.key == pygame.K_ESCAPE:
                    gameExit = True
                    pygame.quit()

                if event.key == pygame.K_LEFT:
                    x_change = -5

                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            # условия для движения
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        # смена позиции
        x += x_change
        # фон
        gameDisplay.fill(white)

        #
        things(thing_startx, thing_starty, thing_wigth, thing_height, black)
        thing_starty += thing_speed  # увеличивает скорость
        # создаем машину
        car(x, y)
        # задаем граници при которых машина врезается ->конец
        if x > display_width - car_wigth or x < 0:
            gameExit = True
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)

        # проверяем на обнавления дисплея(кадров)
        pygame.display.update()
        # кадры в сек. 60
        clock.tick(60)


game_loop()
pygame.quit()
quit()
