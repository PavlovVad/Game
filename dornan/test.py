import pygame
import sys
 
sc = pygame.display.set_mode((500, 300))
sc.fill((100, 150, 200))

h_size = 7

helmet_surf = pygame.image.load(
    'helmet.png').convert()
helmet_surf.set_colorkey(
    (0, 0, 10))
helmet_rect = helmet_surf.get_rect(
    center=(0, 0))
sc.blit(helmet_surf, helmet_rect)
pygame.display.update()
 
sc.fill((0, 0, 225))
# уменьшаем в h_size раза
scale = pygame.transform.scale(
    helmet_surf, (helmet_surf.get_width() // h_size,
               helmet_surf.get_height() // h_size))
 
scale_rect = scale.get_rect(
   center=(60, 60))  #координаты положения изображения на экране
 
sc.blit(scale, scale_rect)

pygame.display.update(helmet_rect)



# ждем 1 секунду перед изменением
pygame.time.wait(1000)
 
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
    pygame.time.delay(20)
 