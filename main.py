import pygame
import sys
import time
import random
from colors import black, white, red, green, bright_red, bright_green

from Player import carImg, car_wigth

# стартует в файле модуль пайгейм
pygame.init()

# размер окна
display_width = 800  # параметр высота
display_height = 600  # параметр ширина

# окно игры
gameDisplay = pygame.display.set_mode((display_width, display_height))  # размер
pygame.display.set_caption("Разбей мою тачку!!!")  # название игры



# модуль для времени, чтобы мониторить кадры в секунду
clock = pygame.time.Clock()




# функция отрисовка препятствий
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


# отрисовка авто
def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 100)
        TextSurf, TextRect = text_objects("Don't crash my car", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!", 150, 450, 100, 50, green, bright_green, game_loop)

        pygame.display.update()
        clock.tick(15)


# счетчик
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render('Проехал: '+str(count), True, black)
    gameDisplay.blit(text, (0, 0))


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

    # базовое значение для dodged
    dodged = 0

    x_change = 0  # позиция
    car_speed = 0  # скорость
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.quit()
                quit()

            # блок для обработки нажатия на клавиши
            if event.type == pygame.KEYDOWN:
                # если нажале на  esc , то окно закрывается
                if event.key == pygame.K_ESCAPE:
                    carshed = True
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

        #работаем с  things
        things(thing_startx, thing_starty, thing_wigth, thing_height, black)
        thing_starty += thing_speed # увеличивает скорость
        # создаем машину
        car(x, y)
        things_dodged(dodged)

        # задаем граници при которых машина врезается ->конец
        if x > display_width - car_wigth or x < 0:
            gameExit = True
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 1
            #thing_width += (dodged * 1.2)

        if y < thing_starty + thing_height:
            print('y crossover')
            if x > thing_startx and x < thing_startx + thing_wigth or x + car_wigth > thing_startx and x + car_wigth < thing_startx + thing_wigth:
                print('x crossover')
                crash()

        # проверяем на обнавления дисплея(кадров)
        pygame.display.update()
        # кадры в сек. 60
        clock.tick(60)


game_intro()
game_loop()
pygame.quit()
quit()
