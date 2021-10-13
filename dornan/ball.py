import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 60
screen = pygame.display.set_mode((1200, 900))

A = [0, 0, 0, 0, 0, 0] #массив хранящий координаты шариков, их радиус, их скорости, цвет
B = [] #массив хранящий шарики
A1 = [0, 0, 0, 0, 0, 0] #массив хранящий координаты квадратов, их сторону, их скорости, цвет
B1 = [] #массив хранящий квадраты
for i in range (20):
    B.append(A)
for i in range (20):
    B1.append(A1)

expa = 0
k = 0
k1 = 0
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

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
    global x1, y1, r1, k1
    x1 = randint(100, 900)
    y1 = randint(100, 900)
    r1 = randint(20, 100)
    dx = randint(-10, 10)
    dy = randint(-10, 10)
    color = COLORS[randint(0, 5)]
    rect(screen, color, (x1, y1, r1, r1))
    B1[k1] = [x1, y1, r1, dx, dy, color]
    print(B1)
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
    for A in B:   
        if (eventx-A[0])**2 + (eventy-A[1])**2 <= A[2]**2:
            expa = expa + 1 
            B.remove(A)
            circle(screen, BLACK, (A[0], A[1]), A[2])
    for A1 in B1:       
        if (A1[0] <= eventx <= (A1[0] + A1[2])) and (A1[1] <= eventy <= (A1[1] + A1[2])):
            expa = expa + 5 
            B1.remove(A1)
            rect(screen, BLACK, (A1[0], A1[1], A1[2], A1[2]))
    print('текущий счет:', expa)        

pygame.display.update()
clock = pygame.time.Clock()
finished = False
drawsquares()
drawballs()

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
        rect(screen, A1[5], (A1[0], A1[1], A1[2], A1[2]))
    pygame.display.update()
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                
                
                pygame.display.update()
                
                click(event)
            elif event.button == 3:
                circle(screen,  BLUE, event.pos, randint(5, 25))
                pygame.display.update()

    
            
        
        

    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
