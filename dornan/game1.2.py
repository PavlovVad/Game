import pygame
import sys
from pygame.draw import *
from random import randint
pygame.init()

FPS = 80
screen = pygame.display.set_mode((1200, 900))

A = [0, 0, 0, 0, 0, 0] #массив хранящий координаты шариков, их радиус, их скорости, цвет
B = [] #массив хранящий шарики
A1 = [0, 0, 0, 0, 0, 0] #массив хранящий координаты квадратов, их сторону, их скорости, цвет, расширение за один кадр
B1 = [] #массив хранящий квадраты

helmet_surf = pygame.image.load(
            'helmet.png').convert()
helmet_surf.set_colorkey(
            (0, 0, 0))
helmet_rect = helmet_surf.get_rect(
            center=(0, 0))

armor_surf = pygame.image.load(
            'armor.png').convert()
armor_surf.set_colorkey(
            (0, 0, 0))
armor_rect = armor_surf.get_rect(
            center=(0, 0))
maxTime = 15
number_helmets = [10, 15]
number_armors = [5, 8]

pygame.mixer.music.load("march1.ogg")
soundstart = pygame.mixer.Sound('start.ogg')
sound2 = pygame.mixer.Sound('idiot.ogg')
soundfail = pygame.mixer.Sound('fail.ogg')
soundsucess = pygame.mixer.Sound('Sucess.ogg')
background_serf = pygame.image.load(
            'background2.png').convert()
background_rect = background_serf.get_rect(
            center=(0, 0))
scale1 = pygame.transform.scale(
        background_serf, (int((background_serf.get_width() * 1.4) // 1),
                   int(background_serf.get_height() * 1.4)))
scale_rect = scale1.get_rect(
           center=(0, 0))
screen.blit(scale1, (-475, 0))  #координаты начального экрана

win_serf = pygame.image.load(
            'SUCCESS.png').convert()
scale_win_serf = pygame.transform.scale(
        win_serf, (int((win_serf.get_width() // 1.3)),
                   int(win_serf.get_height() // 1.3)))
fail_serf = pygame.image.load(
            'FAIL.png').convert()
scale_fail_serf = pygame.transform.scale(
        fail_serf, (int((fail_serf.get_width() // 1.3)),
                   int(fail_serf.get_height() // 1.3)))
#pygame.mixer.music.play()


'''
pygame.mixer.music.load('file_name.ogg')
pygame.mixer.music.play()
pygame.mixer.music.pause()
'''
WINPOINTS_helmet = 3
WINPOINTS_armor = 3 #количество очков, необходимое для победы
count_helmet = 0 #счетчик колтчества найденных шлемов
count_armor = 0 #счетчик количества найденных armor


RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def score(screen, x, y, font_size):
    # показывает количество очков и время до конца
    font2 = pygame.font.Font(None, font_size)
    helmet_text = "Найдено шлемов: " + str(count_helmet)
    time_text = "Time: " + str(round(maxTime*10 - time//100)/10)
    armor_text = "Найдено каркасов: " + str(count_armor) 
    Time = font2.render(time_text, True, YELLOW)
    helmet = font2.render(helmet_text, True, YELLOW)
    armor = font2.render(armor_text, True, YELLOW)
    #Recor = font2.render(RECORDS[0], True, YELLOW)
    screen.blit(Time, [x, y])
    screen.blit(helmet, [x, y + 35])
    screen.blit(armor, [x, y + 70])

def ending(screen, font_size):
    # функция для завершения игры
    screen.fill(BLACK)
    finished = False
    fontHead = pygame.font.Font(None, font_size)
    winning_text = fontHead.render("ВЫ ОБРАДОВАЛИ ДОРНАНА!", True, YELLOW)
    gameover_text = fontHead.render("ВЫ РАЗОЧАРОВАЛИ ДОРНАНА!", True, RED)
    yourrecord_helmet_text = fontHead.render("Найдено шлемов: " + str(count_helmet), True, RED)
    yourrecord_armor_text = fontHead.render("Найдено каркасов: " + str(count_armor), True, RED)
    if count_helmet >= WINPOINTS_helmet and count_armor >= WINPOINTS_armor: 
        screen.blit(scale_win_serf, (-175, 0))
        screen.blit(winning_text, (500, 500))
        screen.blit(yourrecord_helmet_text, (500, 600))
        screen.blit(yourrecord_armor_text, (500, 700))
        soundsucess.play()
    else:
        screen.blit(scale_fail_serf, (-175, 0))
        screen.blit(gameover_text, (400, 250))
        screen.blit(yourrecord_helmet_text, (500, 500))
        screen.blit(yourrecord_armor_text, (500, 700))
        soundfail.play()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        pygame.display.update()

def new_armor():
    '''рисует новый armor'''
    
    h_size = randint(5, 12)
    x = randint(100, 1100)
    y = randint(100, 900)
    scale = pygame.transform.scale(
        armor_surf, (armor_surf.get_width() // h_size,
                   armor_surf.get_height() // h_size))
    scale_rect = scale.get_rect(
       center=(x, y))  #координаты положения правого угла прямоугольник на экране
    x = scale_rect[0]
    y = scale_rect[1]
    r = h_size
    dx = randint(-15, 15)
    dy = randint(-15, 15)
    w = scale_rect[2]
    h = scale_rect[3]
    B.append([x, y, r, dx, dy, w, h])
    screen.blit(scale, scale_rect)

def drawarmors():
    '''рисует 10-20 шариков'''
    for i in  range(randint(number_armors[0], number_armors[1])):
        new_armor()

def new_helmet():
    
    # уменьшаем в h_size раза
    h_size = randint(4, 15)
    x = randint(100, 1100)
    y = randint(100, 900)
    scale = pygame.transform.scale(
        helmet_surf, (helmet_surf.get_width() // h_size,
                   helmet_surf.get_height() // h_size))
    scale_rect = scale.get_rect(
       center=(x, y))  #координаты положения правого угла прямоугольник на экране
    x1 = scale_rect[0]
    y1 = scale_rect[1]
    r1 = h_size
    dx = randint(-10, 10)
    dy = randint(-10, 10)
    w = scale_rect[2]
    h = scale_rect[3]
    B1.append([x1, y1, r1, dx, dy, w, h])
    screen.blit(scale, scale_rect)

    pygame.display.update(helmet_rect)

def drawhelmets():
    '''рисует 10-20 шлемов'''
    for i in  range(randint(number_helmets[0], number_helmets[1])):
        new_helmet()

    

def click(event):
    '''удаляет шарики и подсчитывает очки, если на шарик кликнуть'''
    global count_helmet, count_armor
    eventx = event.pos[0]
    eventy = event.pos[1]
    sucess = False
    for A in B:   
        if ((A[0] - (A[5] // 2)) <= eventx <= (A[0] + (A[5] // 2))) and (A[1] - (A[6] // 2)) <= eventy <= (A[1] + (A[6] // 2)):
            count_armor = count_armor + 1
            B.remove(A)
            sucess = True
    for A1 in B1:       
        if ((A1[0] - (A1[5] // 2)) <= eventx <= (A1[0] + (A1[5] // 2))) and (A1[1] - (A1[6] // 2)) <= eventy <= (A1[1] + (A1[6] // 2)):
            count_helmet = count_helmet + 1
            B1.remove(A1)
            sucess = True
    if sucess == False:
        sound2.play()


pygame.display.update()
clock = pygame.time.Clock()
finished = False

#drawballs()
soundstart.play()
drawhelmets()
drawarmors()


while not finished:
    clock.tick(FPS)

    for A in B:
        if (0 >= A[0]) or (1200 <= A[0]):
            A[3] = -A[3]
        if (0 >= A[1]) or (900 <= A[1]):
            A[4] = -A[4]

        #circle(screen, BLACK, (A[0], A[1]), A[2])
        A[0] = A[0] + A[3]
        A[1] = A[1] + A[4]
        
        #здесь рисуем armor в новых координатах
        scale_armor = pygame.transform.scale(
        armor_surf, (armor_surf.get_width() // A[2],
                   armor_surf.get_height() // A[2]))
        scale_rect_armor = scale_armor.get_rect(
           center=(A[0], A[1]))
        screen.blit(scale_armor, scale_rect_armor)

    for A1 in B1:
        if (0 >= A1[0]) or (1200 <= A1[0]):
            A1[3] = -A1[3]
        if (0 >= A1[1]) or (900 <= A1[1]):
            A1[4] = -A1[4]
        #rect(screen, BLACK, (A1[0], A1[1], A1[2], A1[2]))
        A1[0] = A1[0] + A1[3]
        A1[1] = A1[1] + A1[4]

        #здесь рисуем шлем в новых координатах
        scale = pygame.transform.scale(
        helmet_surf, (helmet_surf.get_width() // A1[2],
                   helmet_surf.get_height() // A1[2]))
        scale_rect = scale.get_rect(
           center=(A1[0], A1[1]))
        screen.blit(scale, scale_rect)

    pygame.display.update(helmet_rect)
        
    time = pygame.time.get_ticks()
    score(screen, 10, 10, 40)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if time // 1005 >= maxTime:
            ending(screen, 40)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
            



                
                
                pygame.display.update()
                
                click(event)
            elif event.button == 3:
                circle(screen,  BLUE, event.pos, randint(5, 25))
                pygame.display.update()

          
        
        

    pygame.display.update()
    screen.blit(scale1, (-475, 0))


pygame.quit()
