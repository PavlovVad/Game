import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 60
screen = pygame.display.set_mode((1200, 900))

A = [0, 0, 0, 0, 0, 0] #массив хранящий координаты шариков, их радиус, их скорости, цвет
B = [] #массив хранящий шарики
A1 = [0, 0, 0, 0, 0, 0, 0] #массив хранящий координаты квадратов, их сторону, их скорости, цвет, расширение за один кадр
B1 = [] #массив хранящий квадраты
for i in range (20):
    B.append(A)
for i in range (20):
    B1.append(A1)
maxTime = 10
pygame.mixer.music.load("march1.ogg")
soundstart = pygame.mixer.Sound('start.ogg')
sound2 = pygame.mixer.Sound('idiot.ogg')
soundfail = pygame.mixer.Sound('fail.ogg')
soundsucess = pygame.mixer.Sound('Sucess.ogg')
#pygame.mixer.music.play()


'''
pygame.mixer.music.load('file_name.ogg')
pygame.mixer.music.play()
pygame.mixer.music.pause()
'''
WINPOINTS = 10 #количество очков, необходимое для победы
expa = 0 #счетчик очков
k = 0 #подсчет количества шаров в ящике
k1 = 0 #подсчет количества квадратов на экране
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
    score_text = "Score: " + str(expa)
    time_text = "Time: " + str(round(maxTime*10 - time//100)/10) 
    Time = font2.render(time_text, True, YELLOW)
    score = font2.render(score_text, True, YELLOW)
    #Recor = font2.render(RECORDS[0], True, YELLOW)
    screen.blit(Time, [x, y])
    screen.blit(score, [x, y + 35])

def ending(screen, font_size):
    # функция для завершения игры
    screen.fill(BLACK)
    finished = False
    fontHead = pygame.font.Font(None, font_size)
    winning_text = fontHead.render("ВЫ ОБРАДОВАЛИ ДОРНАНА!", True, YELLOW)
    gameover_text = fontHead.render("ПУСТОШЬ ПОГЛАТИЛА ВАС", True, RED)
    yourrecord_text = fontHead.render("СЧЕТ: " + str(expa), True, RED)
    if expa >= WINPOINTS:  
        screen.blit(winning_text, (500, 500))
        screen.blit(yourrecord_text, (500, 600))
        soundsucess.play()
    else:
        screen.blit(gameover_text, (400, 250))
        screen.blit(yourrecord_text, (500, 500))
        soundfail.play()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        pygame.display.update()

def new_ball():
    '''рисует новый шарик'''
    global x, y, r, k
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(20, 100)
    dx = randint(-10, 10)
    dy = randint(-10, 10)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    B[k] = [x, y, r, dx, dy, color]
    k = k + 1
def drawballs():
    '''рисует 10-20 шариков'''
    for i in  range(randint(10, 20)):
        new_ball()
def new_square():
    '''рисует новый квадрат'''
    global x1, y1, r1, k1, ext
    x1 = randint(100, 900)
    y1 = randint(100, 900)
    r1 = randint(20, 60)
    dx = randint(-10, 10)
    dy = randint(-10, 10)
    ext = randint(-1, 1)
    color = COLORS[randint(0, 5)]
    rect(screen, color, (x1, y1, r1, r1))
    B1[k1] = [x1, y1, r1, dx, dy, color, ext]
    k1 = k1 + 1
def drawsquares():
    '''рисует 10-20 квадратов'''
    for i in  range(randint(10, 20)):
        new_square()

    

def click(event):
    '''удаляет шарики и подсчитывает очки, если на шарик кликнуть'''
    global expa   
    eventx = event.pos[0]
    eventy = event.pos[1]
    sucess = False
    for A in B:   
        if (eventx-A[0])**2 + (eventy-A[1])**2 <= A[2]**2:
            expa = expa + 1 
            B.remove(A)
            circle(screen, BLACK, (A[0], A[1]), A[2])
            sucess = True
    for A1 in B1:       
        if (A1[0] <= eventx <= (A1[0] + A1[2])) and (A1[1] <= eventy <= (A1[1] + A1[2])):
            expa = expa + 5 
            B1.remove(A1)
            rect(screen, BLACK, (A1[0], A1[1], A1[2], A1[2]))
            sucess = True
    if sucess == False:
        sound2.play()


pygame.display.update()
clock = pygame.time.Clock()
finished = False
drawsquares()
drawballs()
soundstart.play()

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
        circle(screen, A[5], (A[0], A[1]), A[2])
    for A1 in B1:
        if (0 >= A1[0]) or (1200 <= A1[0]):
            A1[3] = -A1[3]
        if (0 >= A1[1]) or (900 <= A1[1]):
            A1[4] = -A1[4]
        #rect(screen, BLACK, (A1[0], A1[1], A1[2], A1[2]))
        A1[0] = A1[0] + A1[3]
        A1[1] = A1[1] + A1[4]
        if (A1[2] > 60):
            A1[6] = -1
        if (A1[2] < 5):
            A1[6] = 1 
        A1[2] = A1[2] + A1[6] 
        rect(screen, A1[5], (A1[0], A1[1], A1[2], A1[2]))
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
                #sound1.play()



                
                
                pygame.display.update()
                
                click(event)
            elif event.button == 3:
                circle(screen,  BLUE, event.pos, randint(5, 25))
                pygame.display.update()

    
            
        
        

    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
