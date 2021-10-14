import pygame

pygame.init()


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Shooter')


class Soldier(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('0.png')
        self.image = pygame.transform.scale(img, (int(40), int(40)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self):
        screen.blit(self.image, self.rect)



player = Soldier(200, 200, 3)




run = True
while run:

    
    player.draw()
    

    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()

pygame.quit()