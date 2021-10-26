"""Escap game"""
import pygame																		
pygame.init() 																				
screen = pygame.display.set_mode((1000, 750))
bg_intro = pygame.image.load("test/intro animation/Kid ice1.png")
image_sprite = [pygame.image.load("test/intro animation/Kid ice1.png"),
                pygame.image.load("test/intro animation/Kid ice2.png"),
                pygame.image.load("test/intro animation/Kid ice3.png"),
                pygame.image.load("test/intro animation/Kid ice4.png"),
                pygame.image.load("test/intro animation/Kid ice5.png"),
                pygame.image.load("test/intro animation/Kid ice6.png"),
                pygame.image.load("test/intro animation/Kid ice7.png"),
                pygame.image.load("test/intro animation/Kid ice8.png"),
                pygame.image.load("test/intro animation/Kid ice9.png"),
                pygame.image.load("test/intro animation/Kid ice10.png"),
                pygame.image.load("test/intro animation/Kid ice11.png"),
                pygame.image.load("test/intro animation/Kid ice12.png"),
                pygame.image.load("test/intro animation/Kid ice13.png"),
                pygame.image.load("test/intro animation/Kid ice14.png"),
                pygame.image.load("test/intro animation/Kid-ice15_1.png"),
                pygame.image.load("test/intro animation/Kid ice19.png"),
                pygame.image.load("test/intro animation/Kid ice20.png"),
                pygame.image.load("test/intro animation/Kid ice25.png"),
                pygame.image.load("test/intro animation/Kid-ice23.png"),
                pygame.image.load("test/intro animation/Kid-ice23.png"),
                pygame.image.load("test/intro animation/Kid-ice23.png"),
                pygame.image.load("test/intro animation/Kid ice25.png"),
                pygame.image.load("test/intro animation/Kid ice25.png")]
clock = pygame.time.Clock()
value = 0
moving = False
while True:
    for event in pygame.event.get():
        mx, my = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and mx > 412 and mx < 608 and my > 183 and my < 540:
            for i in range(len(image_sprite)):
                clock.tick(9)
                image = image_sprite[i]
                image = pygame.transform.scale(image, (1000, 750))
                screen.blit(image, (0, 0))
                pygame.display.update()
