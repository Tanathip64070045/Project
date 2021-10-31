import pygame

pygame.init()

screen_width = 1000
screen_height = 750

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Escape Game")

clock = pygame.time.Clock()
FPS = 100

move_left = False
move_right = False
move_top = False
move_down = False

BG = (0, 0, 0)

def draw_bg():
    screen.fill(BG)

class player(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.direction = 1
        self.flip = False
        img = pygame.image.load("picture/Player/tjakchar.png")
        self.image = pygame.transform.scale(img, (30,30))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
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

        self.rect.x += dx
        self.rect.y += dy
    
    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

player = player(200, 200, 3, 1)


run = True
while run:
    clock.tick(FPS)
    draw_bg()
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