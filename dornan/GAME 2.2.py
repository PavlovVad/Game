import pygame
import sys
import json
from pygame.draw import *
from random import randint
pygame.init()

FPS = 120
screen = pygame.display.set_mode((1200, 900))
B = [] #массив хранящий все шлемы
B1 = [] #массив хранящий каркасы
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
maxTime = 15000
maxMiss = 10
number_helmets = [10, 15]
number_armors = [5, 8]
push_button1 = False
push_button2 = False
Flag = True
WINPOINTS_helmet = 3
WINPOINTS_armor = 3 #количество очков, необходимое для победы
count_helmet = 0 #счетчик колтчества найденных шлемов
count_armor = 0 #счетчик количества найденных armor
count_miss = 0 #счетчик кооличества промахов
speed_armor = [-20, 20]
speed_helmet = [-15, 15]
level = 2
Data = []
name = "Рядовой"
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
if level == 1:
    lVl = "easy"
elif level == 2:
    lVl = "normal"
elif level == 3:
    lVl = "hard"

pygame.mixer.music.load("march1.ogg")
soundstart = pygame.mixer.Sound('start.ogg')
sound2 = pygame.mixer.Sound('idiot.ogg')
soundfail = pygame.mixer.Sound('fail.ogg')
soundsucess = pygame.mixer.Sound('Sucess.ogg')
soundwelcome = pygame.mixer.Sound('welcome.ogg')
background_serf = pygame.image.load(
            'background2.png').convert()
background_rect = background_serf.get_rect(
            center=(0, 0))
scale1 = pygame.transform.scale(
        background_serf, (int((background_serf.get_width() * 1.4) // 1),
                   int(background_serf.get_height() * 1.4)))
scale_rect = scale1.get_rect(
           center=(0, 0))

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
welcome_serf = pygame.image.load(
            'Welcome.png').convert()
scale_welcome = pygame.transform.scale(
        welcome_serf, (int((welcome_serf.get_width() * 2)),
                   int(welcome_serf.get_height() * 2.2)))
def new_button(x, y, button_size_w, button_size_h, text, button):
    push_button = False
    BUTTON = draw_button(x, y, button_size_w, button_size_h, text)

def draw_button(x, y, button_size_w, button_size_h, text):
    BUT = rect(screen, RED, (x, y, button_size_w, button_size_h))
    fontHead = pygame.font.Font(None, button_size_w // 4)
    yes_text = fontHead.render(text, True, YELLOW)
    screen.blit(yes_text, (x + button_size_h // 4, y + button_size_w // 25))
    return BUT 

EASY = draw_button(200, 660, 100, 50, "ЛЕГКО")
NORMAL = draw_button(200, 730, 100, 50, "НОРМА")
HARD = draw_button(200, 800, 100, 50, "СЛОЖНО")
START = draw_button(400, 650, 400, 100, "Так точон!")
LEAVE = draw_button(400, 770, 400, 100, "Никак нет.")


def difficult(lev):
    global level, WINPOINTS_helmet, WINPOINTS_armor, speed_armor, speed_helmet, count_miss
    if lev == 3:
        WINPOINTS_helmet = 6
        WINPOINTS_armor = 6
        maxMiss = 8
        speed_armor = [-20, 20]
        speed_helmet = [-15, 15]
        level = 3
    if lev == 2:
        WINPOINTS_helmet = 5
        WINPOINTS_armor = 5
        speed_armor = [-15, 15]
        speed_helmet = [-10, 10]
        level = 2
        maxMiss = 10
    if lev == 1:
        WINPOINTS_helmet = 3
        WINPOINTS_armor = 3
        speed_armor = [-10, 10]
        speed_helmet = [-5, 5]
        level = 1
        maxMiss = 12

difficult(2) #уровень сложности по дефолту

def score(screen, x, y, font_size):
    # показывает количество очков и время до конца
    font2 = pygame.font.Font(None, font_size)
    helmet_text = "Найдено шлемов: " + str(count_helmet)
    time_text = "Осталось секунд: " + str(round((maxTime - time) // 1000) + 1)
    armor_text = "Найдено каркасов: " + str(count_armor) 
    miss_text = "Промахов до поражения: " + str(maxMiss - count_miss)
    Time = font2.render(time_text, True, YELLOW)
    Miss = font2.render(miss_text, True, YELLOW)
    helmet = font2.render(helmet_text, True, YELLOW)
    armor = font2.render(armor_text, True, YELLOW)
    screen.blit(Miss, [x, y])
    screen.blit(Time, [x, y + 35])
    screen.blit(helmet, [x, y + 70])
    screen.blit(armor, [x, y + 105])

def ending(screen, font_size):
    # функция для завершения игры
    screen.fill(BLACK)
    finished = False
    fontHead = pygame.font.Font(None, font_size)
    winning_text = fontHead.render("ВЫ ОБРАДОВАЛИ ДОРНАНА!", True, RED)
    table_of_record = fontHead.render("РЕКОРД ПО КОЛИЧЕСТВУ:", True, RED)
    gameover_text = fontHead.render("ВЫ РАЗОЧАРОВАЛИ ДОРНАНА!", True, RED)
    new_record()
    yourrecord_helmet_text = fontHead.render("Найдено шлемов: " + str(count_helmet), True, RED)
    yourrecord_armor_text = fontHead.render("Найдено каркасов: " + str(count_armor), True, RED)
    table_of_record_armor_text = fontHead.render("каркасов: " + str((Data['leaders'][lVl][name]['armor'])), True, RED)
    table_of_record_helmet_text = fontHead.render("шлемов: " + str((Data['leaders'][lVl][name]['helmet'])), True, RED)
    if count_helmet >= WINPOINTS_helmet and count_armor >= WINPOINTS_armor: 
        screen.blit(scale_welcome, (-175, 0))
        screen.blit(winning_text, (10, 20))
        screen.blit(yourrecord_helmet_text, (10, 70))
        screen.blit(yourrecord_armor_text, (10, 120))
        soundsucess.play()
    else:
        screen.blit(scale_fail_serf, (-175, 0))
        screen.blit(gameover_text, (10, 20))
        screen.blit(yourrecord_helmet_text, (10, 70))
        screen.blit(yourrecord_armor_text, (10, 120))
        soundfail.play()
    screen.blit(table_of_record, (860, 20))
    screen.blit(table_of_record_helmet_text, (1000, 70))
    screen.blit(table_of_record_armor_text, (1000, 120))
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
    dx = randint(speed_armor[0], speed_armor[1])
    dy = randint(speed_armor[0], speed_armor[1])
    w = scale_rect[2]
    h = scale_rect[3]
    B.append([x, y, r, dx, dy, w, h, 0, 0])

def drawarmors():
    '''рисует 10-20 шариков'''
    for i in  range(randint(number_armors[0], number_armors[1])):
        new_armor()

def new_helmet():

    global speed_armor, speed_helmet
    
    # уменьшаем в h_size раза
    h_size = randint(4, 10)
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
    dx = randint(speed_helmet[0], speed_helmet[1])
    dy = randint(speed_helmet[0], speed_helmet[1])
    w = scale_rect[2]
    h = scale_rect[3]
    B1.append([x1, y1, r1, dx, dy, w, h])

def drawhelmets():
    '''рисует 10-20 шлемов'''
    for i in  range(randint(number_helmets[0], number_helmets[1])):
        new_helmet()

def new_record():
        global lVl
        print("Your record: "+str([count_armor,count_helmet]))
        name = "Рядовой"
        if level == 1:
            lVl = "easy"
        elif level == 2:
            lVl = "normal"
        elif level == 3:
            lVl = "hard"
        if not(name in Data['leaders'][lVl]):
            Data['leaders'][lVl][name] = {"armor": 0, "helmet":0 }
        if Data['leaders'][lVl][name]['armor']<count_armor:
            Data['leaders'][lVl][name]['armor'] = count_armor
        if Data['leaders'][lVl][name]['helmet']<count_helmet:
            Data['leaders'][lVl][name]['helmet'] = count_helmet

        for lev in Data['leaders']:
            print("\n"+'"'+lev+'"')
            for res in Data['leaders'][lev]:
                print(res + " : " + str(Data['leaders'][lev][res]))
                draw_button(400, 770, 400, 100, (str(Data['leaders'][lVl][name]['armor'])))
        dataDown()


def dataUp():
    global Data
    with open("table.json", "r") as read_file: 
        Data = json.load(read_file)

def dataDown():
    global Data
    with open("table.json","w") as write_file:
        json.dump(Data,write_file) 

def click(event):
    '''удаляет шарики и подсчитывает очки, если на шарик кликнуть'''
    global count_helmet, count_armor, BUT, push_button1, count_miss
    eventx = event.pos[0]
    eventy = event.pos[1]
    sucess = False
    if (EASY[0] <= eventx <= EASY[0] + EASY[2]) and (EASY[1] <= eventy <= EASY[1] + EASY[3]):
        difficult(1)
    if (NORMAL[0] <= eventx <= NORMAL[0] + NORMAL[2]) and (NORMAL[1] <= eventy <= NORMAL[1] + NORMAL[3]):
        difficult(2)
    if (HARD[0] <= eventx <= HARD[0] + HARD[2]) and (HARD[1] <= eventy <= HARD[1] + HARD[3]):
        difficult(3)
    if (LEAVE[0] <= eventx <= LEAVE[0] + LEAVE[2]) and (LEAVE[1] <= eventy <= LEAVE[1] + LEAVE[3]) and (push_button1 == False):
        sound2.play()
        pygame.quit()
    if push_button1 == True:
        for A in B:   
            if ((A[0] - (A[5] // 2)) <= eventx <= (A[0] + (A[5] // 2))) and (A[1] - (A[6] // 2)) <= eventy <= (A[1] + (A[6] // 2)):
                
                A[7] += 1
                if A[7] == 2:
                    count_armor = count_armor + 1
                    B.remove(A)
                sucess = True
        for A1 in B1:       
            if ((A1[0] - (A1[5] // 2)) <= eventx <= (A1[0] + (A1[5] // 2))) and (A1[1] - (A1[6] // 2)) <= eventy <= (A1[1] + (A1[6] // 2)):
                count_helmet = count_helmet + 1
                B1.remove(A1)
                sucess = True
    if sucess == False and push_button1 == True:
        count_miss += 1
        sound2.play()

pygame.display.update()
dataUp()
clock = pygame.time.Clock()
finished = False
soundwelcome.play()
drawhelmets()
drawarmors()
dt = 0
time = -1

while not finished:
    clock.tick(FPS)

    if push_button1 == True:

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

            if A[7] == 1:
                if A[8] == 0:
                    screen.blit(scale_armor, scale_rect_armor)
                    A[8] += 1
                else:
                    A[8] -=1 
                    
            else:
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
        score(screen, 10, 10, 40)
        pygame.display.update()
        
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            finished = True
        #elif event.type == pygame.KEYDOWN:

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                eventx = event.pos[0]
                eventy = event.pos[1]
                click(event)   
                if Flag == True:
                    if (START[0] <= eventx <= START[0] + START[2]) and (START[1] <= eventy <= START[1] + START[3]):
                        dt = pygame.time.get_ticks()
                        push_button1 = True
                        Flag = False
                        soundstart.play()    
            elif event.button == 3:
                circle(screen,  BLUE, event.pos, randint(5, 25))
                pygame.display.update()
    if push_button1 == False:
        time = -1
    else:
        time = pygame.time.get_ticks() - dt
    if time >= maxTime or count_miss >= maxMiss:
            if count_miss >= maxMiss:
                count_helmet = 0
                count_armor = 0
            ending(screen, 35)
    pygame.display.update()
    if push_button1 == True:
        screen.blit(scale1, (-475, 0))
    else:
        screen.blit(scale_welcome, (-200, 0))
        draw_button(200, 660, 100, 50, "ЛЕГКО")
        draw_button(200, 730, 100, 50, "НОРМА")
        draw_button(200, 800, 100, 50, "СЛОЖНО")
        draw_button(400, 650, 400, 100, "Так точно!")
        draw_button(400, 770, 400, 100, "Никак нет.")
        if level == 1:
            circle(screen, GREEN, (160, 680), 20)
        elif level == 2:
            circle(screen, GREEN, (160, 750), 20)
        elif level == 3:
            circle(screen, GREEN, (160, 820), 20)
pygame.quit()

