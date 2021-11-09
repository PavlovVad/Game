import math
import random
import pygame


FPS = 60

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

R_BALL = 10
list_of_targets = []
list_of_bullets = []
x_borders = [0, 800]
y_borders = [0, 600]
number_of_targets = [2, 4] #случайное количество от 1 до 3
count = 0
class Bomb:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса bomb

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = R_BALL
        self.vx = 0
        self.vy = 0
        self.color = random.choice(GAME_COLORS)
        self.live = 30
        self.explotion = False
        self.grav = [0.4, 0] #вектор граитации по направлениям x и y

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        
        #self.x += self.vx
        #self.y -= self.vy
        if not (x_borders[0] <= (self.x + self.vx) <= x_borders[1]):
            self.vx = -self.vx
        if not (y_borders[0] <= (self.y + self.vy) <= y_borders[1]):
            self.vy = -self.vy
        
        self.x += self.vx
        self.y += self.vy

        self.vx += self.grav[0]
        self.vy += self.grav[1]

    def draw(self):
        self.live -= 0.25
        if self.live == 0:
            self.explotion = True
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, list_of_targets):
        for obj in list_of_targets:
            if (obj.x - self.x)**2 + (obj.y - self.y)**2 <= (obj.r + self.r)**2:
                list_of_targets.remove(obj)
                return True
        return False


class Ball:
    def __init__(self, screen: pygame.Surface, x = 40, y = 450, color = -1):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = R_BALL
        self.vx = 0
        self.vy = 0
        if color == -1:
            self.color = random.choice(GAME_COLORS)
        else:
            self.color = color
        self.live = 40
        self.grav = [0, 0.4] #вектор граитации по направлениям x и y
        self.explotion = False

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        
        #self.x += self.vx
        #self.y -= self.vy
        if not (x_borders[0] <= (self.x + self.vx) <= x_borders[1]):
            self.vx = -self.vx
        if not (y_borders[0] <= (self.y + self.vy) <= y_borders[1]):
            self.vy = -self.vy
        
        self.x += self.vx
        self.y += self.vy

        self.vx += self.grav[0]
        self.vy += self.grav[1]


    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, list_of_targets):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        for obj in list_of_targets:
            if (obj.x - self.x)**2 + (obj.y - self.y)**2 <= (obj.r + self.r)**2:
                list_of_targets.remove(obj)
                return True
        return False


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.LENGHT = 50
        self.WIDTH = 20
        self.x = 35
        self.y = 460
        self.vx = 3
        self.vy = 1
        self.r = 1.35*R_BALL

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event, type_of_bullet = 1, x = -1, y = -1, color = -1, vx = 0, vy = 0):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        if x == -1:
            x = self.x
        if y == -1:
            y = self.y
        bullet += 1
        if type_of_bullet == 1:
            new_ball = Ball(self.screen, x, y, color)
            new_ball.r += 5
            if vx == 0:
                self.an = math.atan2((event[1]-new_ball.y), (event[0]-new_ball.x))
                new_ball.vx = self.f2_power * math.cos(self.an)
                new_ball.vy = self.f2_power * math.sin(self.an)
            else:
                new_ball.vx = vx
                new_ball.vy = vy
            balls.append(new_ball)
        if type_of_bullet == 2:
            new_ball = Bomb(self.screen, x, y)
            new_ball.r += 5
            self.an = math.atan2((event[1]-new_ball.y), (event[0]-new_ball.x))
            new_ball.vx = self.f2_power * math.cos(self.an)
            new_ball.vy = self.f2_power * math.sin(self.an)
            balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        '''
        self.guns_length = event.pos[0] - x
        self.guns_width = event.pos[1] - y
        normirovka = ((event.pos[0] - x)**2 + (event.pos[1] - y)**2) / 50
        self.coordinate_x = (self.guns_length / normirovka) + x
        self.coordinate_y = (self.guns_width / normirovka) + y
        pygame.draw.line(screen, BLUE, (x, y + 40), (self.coordinate_x, self.coordinate_y), width = 5)
        '''
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.LENGHT, self.WIDTH))
        pygame.draw.circle(screen, BLUE, (self.x, self.y), self.r)

        
        # FIXIT don't know how to do it

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY

    def move(self, direction):
        if not (x_borders[0] <= (self.x + self.vx) <= x_borders[1]):
            self.x = 0
        if not (y_borders[0] <= (self.y + self.vy) <= y_borders[1]):
            self.vy = -self.vy
        if direction == 2:
            self.x += self.vx
        if direction == 1:
            self.x -= self.vx
        #self.y += self.vy



class Target:
    def __init__(self, screen):
        self.points = 0
        self.live = 1
    # FIXME: don't work!!! How to call this functions when object is created?
        self.new_target()
    #def __init__(self, screen)

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = random.randint(600, 780)
        y = self.y = random.randint(300, 550)
        r = self.r = random.randint(15, 50)
        color = self.color = RED
        self.vx = random.randint(-10, 10)
        self.vy = random.randint(-10, 10)
    def hit(self, points=1):
        """Попадание шарика в цель."""
        global count
        count += points
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r )
    def move(self):
        if not (x_borders[0] <= (self.x + self.vx) <= x_borders[1]):
            self.vx = -self.vx
        if not (y_borders[0] <= (self.y + self.vy) <= y_borders[1]):
            self.vy = -self.vy
        self.x += self.vx
        self.y += self.vy

def fill_list_of_targets():
    for i in range(random.randint(number_of_targets[0], number_of_targets[1])):
        new_target = Target(screen)
        list_of_targets.append(new_target)

def score(screen, x, y, font_size):
    # показывает количество очков и время до конца
    font2 = pygame.font.Font(None, font_size)
    helmet_text = "ОЧКИ: " + str(count)
    helmet = font2.render(helmet_text, True, YELLOW)
    screen.blit(helmet, [x, y])

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
target = Target(screen)
finished = False
fill_list_of_targets()
while not finished:
    screen.fill(WHITE)
    gun.draw()
    for target in list_of_targets:
        target.draw()
        target.move()
    for b in balls:
        b.draw()
    score(screen, 100, 100, 40)
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
        pygame.display.update()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        gun.fire2_end(pygame.mouse.get_pos(), 2)
    if keys[pygame.K_UP]:
        gun.fire2_end(pygame.mouse.get_pos())
    if keys[pygame.K_LEFT]:
        gun.move(1)
    if keys[pygame.K_RIGHT]:
        gun.move(2)

    for b in balls:
        b.move()
        if b.explotion == True:
            gun.fire2_end(pygame.mouse.get_pos(), 1, b.x, b.y, BLACK, b.vy, b.vx)
            gun.fire2_end(pygame.mouse.get_pos(), 1, b.x, b.y, b.color, -b.vy, -b.vx)
            balls.remove(b)
        elif b.hittest(list_of_targets):
            target.hit()
            new_target = Target(screen)
            list_of_targets.append(new_target)
    gun.power_up()

pygame.quit()
