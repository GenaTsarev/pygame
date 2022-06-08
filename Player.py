import pygame
# игрок
carImg = pygame.image.load('images/car.png')  # картинка для игрока
carImg = pygame.transform.scale(carImg, (70, 140))  # задаем размеры картинки, если это нреобходимо
car_wigth = 70