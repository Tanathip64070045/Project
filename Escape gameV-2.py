import pygame
import csv

pygame.init()

screen_width = 1000
screen_height = 750

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Escape Game")

clock = pygame.time.Clock()
FPS = 100

ROWS = 25
COLS = 34
TILE_SIZE = 30
TILE_TYPES = 21
level = 0


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


class player(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.direction = 1
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        for i in range(5):
            img = pygame.image.load(f"picture/animation/stand/{i}.png")
            img = pygame.transform.scale(img, (25,25))
            self.animation_list.append(img)
        self.image = self.animation_list[self.frame_index]
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
            self.direction = -1
        if move_right:
            dx = self.speed
            self.flip = False
            self.direction = 1
        if move_top:
            dy = -self.speed
            self.flip = False
            self.direction = 1
        if move_down:
            dy = self.speed
            self.flip = False
            self.direction = 1

        for tile in world.obstacle_list:
            if tile[1].colliderect(self.rect.x + dx, self.rect.y + dy, self.width, self.height):
                dx = 0
                dy = 0
       
        self.rect.x += dx
        self.rect.y += dy
       

    def update_animation(self):
        ANIMATION_COOLDOWN = 100

        self.image = self.animation_list[self.frame_index]
        
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0
    
    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

class World():
    def __init__(self):
        self.obstacle_list = []
    
    def process_data(self, data):
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if tile >= 0:
                    img =img_list[tile]
                    img_rect = img.get_rect()
                    img_rect.x = x * 30
                    img_rect.y = y * 30
                    tile_data = (img, img_rect)
                    if tile > 0:
                        self.obstacle_list.append(tile_data)
    
    def draw(self):
        for tile in self.obstacle_list:
            screen.blit(tile[0], tile[1])

player = player(20, 375, 3, 1)

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


run = True
while run:
    clock.tick(FPS)
    draw_bg()
    world.draw()
    player.update_animation()
    player.draw()
    
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