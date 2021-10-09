"""escape game"""
import pygame
def control():
    """ควบคุม"""
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("TEST")
    
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit()
control()
    