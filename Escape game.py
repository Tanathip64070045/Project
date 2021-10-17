"""Escap game"""

import pygame 																				# import
def main():
######### game set display   ################
	pygame.init() 																			# create
	screen = pygame.display.set_mode((1000,800)) 											# display
	pygame.display.set_caption("ESCAPE GAME") 												# title game
	icon = pygame.image.load("icon.png")  													# icon game
	pygame.display.set_icon(icon)    														# set icon
	player = pygame.image.load("0.png") 													# image ตัวละคร
	player1 = pygame.transform.scale(player,(30,30)) 										# ขนาด player
##################### ตำแหน่ง PLAYER #########################
	posX = 0         																		#แกน x (ซ้าย- ขวา)
	posY = 800-30   																		# แกน y  (ขึ้น - ลง)
	move = 2		 																		# จำนวนย้าย

######################  RUN GAME #########################
	while True:
		pygame.time.delay(20) 																# delay 
		BG = (0, 0, 0) 																		# BG สีดำ (RGB)
		screen.fill(BG) 																	# ใส่ พื้นหลัง
		for event in pygame.event.get(): 													# ทำอีเว้น
			if event.type == pygame.QUIT:
				quit()																		# ออก


	#################### PRESS KEY ############################
		keys = pygame.key.get_pressed() 													# กำหนด keys เป็น การกด
		if keys[pygame.K_a] and posX > 0: 													# LEFT
			posX -= move
		if keys[pygame.K_d] and posX < 1000 - 30: 											# RIGHT
			posX += move
		if keys[pygame.K_w] and posY > 0: 													# UP
			posY -= move
		if keys[pygame.K_s] and posY < 770: 												# DOWN
			posY += move
	
	###################### แสดงผล ################################
		screen.blit(player1,(posX, posY)) 													# แสดงผลตัวละคร
		pygame.display.update()   															# อัปเดรตหน้าจอ
main()
