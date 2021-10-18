"""Escap game"""

import pygame 																				# import
######### game set display   ################
pygame.init() 																				# create
screen = pygame.display.set_mode((1000,800)) 												# display
pygame.display.set_caption("ESCAPE GAME") 													# title game
icon = pygame.image.load("icon.png")  														# icon game
pygame.display.set_icon(icon)    															# set icon
player = pygame.image.load("0.png") 														# image ตัวละคร
player1 = pygame.transform.scale(player,(40,40)) 											# ขนาด player

##################### ตำแหน่ง PLAYER #########################
posX = 0         																			#แกน x (ซ้าย- ขวา)
posY = 800-30   																			# แกน y  (ขึ้น - ลง)
move = 2																					# จำนวนย้าย														
####################backgound หลังจากการเดิน####################

def down_bg():
	"""BG หลังการเดิน"""
	BG = (0, 0, 0) 																							# BG สีดำ (RGB)
	screen.fill(BG) 

def intro():																								# ฟังก์ชั่น หน้าเกม
	"""หน้าเกม"""
	bg_intro = pygame.image.load("bg_intro.jpg")															# ใส่รูป
	intro = True					
	
	while intro:
		for event in pygame.event.get():
			mx, my = pygame.mouse.get_pos()																	#ทำ อีเว้น
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.MOUSEBUTTONDOWN and mx > 249 and mx < 700 and my > 270 and my < 600:     # กดกลางหน้าจอ
				main()
		screen.blit(bg_intro,(0,0))
		pygame.display.update()

######################  RUN GAME #########################
def main():
	"""RUN"""
    ################# ตำแหน่ง PLAYER #########################
	posX = 0         																		#แกน x (ซ้าย- ขวา)
	posY = 800-30   																		# แกน y  (ขึ้น - ลง)
	move = 2																				# จำนวนย้าย
	
	while True:
		pygame.time.delay(20) 																# delay 
		down_bg()																			# ใส่ พื้นหลัง
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
		screen.blit(player1,(posX, posY)) 													# แสดงผลตัวละคร
		pygame.display.update()   															# อัปเดรตหน้าจอ

intro()	
