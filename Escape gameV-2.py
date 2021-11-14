import pygame
import csv

pygame.init()

screen_width = 1000
screen_height = 750

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Escape Game")

clock = pygame.time.Clock()
FPS = 60

ROWS = 25
COLS = 34
TILE_SIZE = 30
TILE_TYPES = 21
level = 0
start_game = False

move_left = False
move_right = False
move_top = False
move_down = False

img_list = []
for x in range(TILE_TYPES):
    img = pygame.image.load(f'picture/map/{x}.png')
    img = pygame.transform.scale(img, (30,30))
    img_list.append(img)

BG = (0, 0, 0)

def draw_bg():
    screen.fill(BG)



class player():
    def __init__(self, x, y, speed):
        self.speed = speed
        self.direction = 1
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        temp_list = [] 
        for i in range(5):
            img = pygame.image.load(f"picture/animation/stand/{i}.png")
            img = pygame.transform.scale(img, (20,20))
            temp_list.append(img)
        self.animation_list.append(temp_list) 
        temp_list = []
        for i in range(25):
            img = pygame.image.load(f"picture/animation/walk/{i}.png")
            img = pygame.transform.scale(img, (20,20))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
    
    def move(self, move_left, move_right, move_top, move_down):
        dx = 0
        dy = 0

        if move_left:
            dx = -self.speed
            self.flip = True
            self.direction = -2
        if move_right:
            dx = self.speed
            self.flip = False
            self.direction = 2
        if move_top:
            dy = -self.speed
            self.flip = False
            self.direction = 2
        if move_down:
            dy = self.speed
            self.flip = False
            self.direction = 2

        for tile in world.obstacle_list:
            if tile[1].colliderect(self.rect.x + dx, self.rect.y + dy, self.width, self.height):
                dx = 0
                dy = 0
       
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.x > 999 and self.rect.y > 360 and level == 0:
            quit()
        if (self.rect.x >= 330 and self.rect.x <= 357 and self.rect.y == 130) \
            or (self.rect.x == 360 and self.rect.y >= 130 and self.rect.y <= 180) or \
                self.rect.x >= 330 and self.rect.x <= 360 and self.rect.y == 180 and level == 0:
            over = pygame.image.load("picture/Button/over2.png")
            g_1 = pygame.transform.scale(over, (150,100))
            while True:
                screen.blit(g_1,(428,300))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
        print(self.rect.x, self.rect.y)

    def update_animation(self):
        ANIMATION_COOLDOWN = 100

        self.image = self.animation_list[self.action][self.frame_index]
        
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0
    
    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()


    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

class World():
    def __init__(self):
        self.obstacle_list = []
    
    def process_data(self, data):
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if tile >= 0:
                    img = img_list[tile]
                    img_rect = img.get_rect()
                    img_rect.x = x * 30
                    img_rect.y = y * 30
                    tile_data = (img, img_rect)
                    if tile > 0:
                        self.obstacle_list.append(tile_data)
    
    def draw(self):
        for tile in self.obstacle_list: 
            screen.blit(tile[0], tile[1])

player = player(20, 375, 1)

world_data = []
for row in range(ROWS):
    r = [-1] * COLS
    world_data.append(r)

with open(f'level{level}_data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')               
    for x, row in enumerate(reader):
        for y, tile in enumerate(row):
            world_data[x][y] = int(tile)

world = World()
player2 = world.process_data(world_data)

######################## INTRO ############################################
bg_intro = pygame.image.load("picture/Button/BG/intro2.png")
bg1 = pygame.image.load("picture/Button/Start/StartN.png")													
bg2 = pygame.image.load("picture/Button/Start/StartP.png")
bg3 = pygame.image.load("picture/Button/Exit/ExitN.png")
bg4 = pygame.image.load("picture/Button/Exit/ExitP.png")
bg5 = pygame.image.load("picture/Button/TJAK (Credit)/TJAK.png")
bg6 = pygame.image.load("picture/Button/TJAK (Credit)/TJAKmap.png")
bg7 = pygame.image.load("picture/Button/BG/orange.png")
bg8 = pygame.image.load("picture/Player/player_flip.png")

bg_1 = pygame.transform.scale(bg1,(150,100))
bg_2 = pygame.transform.scale(bg2,(150,100))
bg_3 = pygame.transform.scale(bg3,(100,100))
bg_4 = pygame.transform.scale(bg4,(100,100))
bg_5 = pygame.transform.scale(bg5,(200,90))
bg_6 = pygame.transform.scale(bg6,(200,90))
bg_7 = pygame.transform.scale(bg7,(336,444))
bg_8 = pygame.transform.scale(bg8,(900,800))

############################################################################

run = True
while run:
    mx, my = pygame.mouse.get_pos()
    clock.tick(FPS)
    if start_game == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEMOTION and mx > 423 and mx < 555 and my > 588 and my < 684:
                screen.blit(bg_2,(415,587))
            pygame.display.update()
            if event.type == pygame.MOUSEMOTION and mx > 888 and mx < 973 and my > 14 and my < 97:
                screen.blit(bg_4,(880, 12))
            pygame.display.update()
            if event.type == pygame.MOUSEMOTION and mx > 10 and mx < 200 and my > 14 and my < 96:
                screen.blit(bg_6,(6,12))
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN and mx > 423 and mx < 555 and my > 588 and my < 684:
                if event.button == 1:
                    start_game = True
            if event.type == pygame.MOUSEBUTTONDOWN and mx > 888 and mx < 973 and my > 14 and my < 97:
                if event.button == 1:
                    quit()
            if event.type == pygame.MOUSEBUTTONDOWN and mx > 398 and mx < 621 and my > 142 and my < 542:
                screen.blit(bg_7,(317,103))
                screen.blit(bg_8,(60,-45))
            screen.blit(bg_intro,(0,0))
            screen.blit(bg_1,(415,587))
            screen.blit(bg_3,(880,12))
            screen.blit(bg_5,(6,12))

    else:
        draw_bg()
        world.draw()
        player.update_animation()
        player.draw()

        if move_left or move_right or move_top or move_down:
            player.update_action(1)
        else:
            player.update_action(0)
        player.move(move_left, move_right, move_top, move_down)
    
        for event in  pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    move_left = True
                
                if event.key == pygame.K_d:
                    move_right = True
                
                if event.key == pygame.K_w:
                    move_top = True
               
                if event.key == pygame.K_s:
                    move_down = True
               
    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    move_left = False
                if event.key == pygame.K_d:
                    move_right = False
                if event.key == pygame.K_w:
                    move_top = False
                if event.key == pygame.K_s:
                    move_down = False
        pygame.display.update()
pygame.quit()
