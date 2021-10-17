import pygame
import sys
from random import randint
 
screen = pygame.display.set_mode((600, 725))
screen.fill((100, 150, 200))
# размеры шлем 600 725
def new_helmet():
    helmet_surf = pygame.image.load(
        '1.jpeg').convert()
    helmet_surf.set_colorkey(
        (0, 0, 0))
    helmet_rect = helmet_surf.get_rect(
        center=(0, 0))
    # уменьшаем в h_size раза
    h_size = randint(4, 15)
    x = randint(100, 400)
    y = randint(50, 250)
    scale = pygame.transform.scale(
        helmet_surf, (helmet_surf.get_width() // h_size,
                   helmet_surf.get_height() // h_size))
    scale_rect = scale.get_rect(
       center=(x, y))  #координаты положения правого угла прямоугольник на экране
    x1 = scale_rect[0]
    y1 = scale_rect[1]
    r1 = h_size



     
    screen.blit(scale, scale_rect)

    pygame.display.update(helmet_rect)
new_helmet()
new_helmet()
'''
helmet_surf = pygame.image.load(
        'helmet.png').convert()
helmet_surf.set_colorkey(
        (0, 0, 0))
helmet_rect = helmet_surf.get_rect(
        center=(0, 0))
    # уменьшаем в h_size раза
h_size = randint(4, 15)
x = randint(100, 400)
y = randint(50, 250)
scale = pygame.transform.scale(
        helmet_surf, (helmet_surf.get_width() // 1,
                   helmet_surf.get_height() // 1))
scale_rect = scale.get_rect(
       center=(300, 375))  #координаты положения центра прямоугольника на экране
     
screen.blit(scale, scale_rect)

pygame.display.update(helmet_rect)
'''
# ждем 1 секунду перед изменением
pygame.time.wait(1000)
 
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
    pygame.time.delay(20)
 