"""Escap game"""

import pygame
######### game set display   ################
pygame.init()
screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption("ESCAPE GAME")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
player = pygame.image.load("0.png")
player1 = pygame.transform.scale(player,(50,50))

##################### ตำแหน่ง PLAYER #########################
posX = 0
posY = 800-50
move = 5

######################  RUN GAME #########################
while True:
	pygame.time.delay(12)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit() # ออก


	#################### PRESS KEY ############################
	keys = pygame.key.get_pressed()
	if keys[pygame.K_a] and posX > 0: # LEFT
		posX -= move
	if keys[pygame.K_d] and posX < 1000 - 50: # RIGHT
		posX += move
	if keys[pygame.K_w] and posY > 0: # UP
		posY -= move
	if keys[pygame.K_s] and posY < 750: # DOWN
		posY += move
	
	###################### แสดงผล ################################
	screen.blit(player1,(posX, posY)) # แสดงผลตัวละคร
	pygame.display.update()   # อัปเดรตหน้าจอ