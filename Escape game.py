"""Escap game"""
###############  game set display  ############################
import pygame 																				# import
pygame.init() 																				# create
screen = pygame.display.set_mode((1000,750)) 												# display
pygame.display.set_caption("ESCAPE GAME") 													# title game
icon = pygame.image.load("icon.png")  														# icon game
pygame.display.set_icon(icon)    															# set icon
player = pygame.image.load("0.png") 														# image ตัวละคร
player1 = pygame.transform.scale(player,(40,40)) 											# ขนาด player

""" ตำแหน่งตัวละคร """
posX = 0         																			#แกน x (ซ้าย- ขวา)
posY = 750-40  																				# แกน y  (ขึ้น - ลง)
move = 2																					# จำนวนย้าย														

#################### bg หลังการเดิน 1 ครั้ง ######################
def down_bg():
	"""BG หลังการเดิน"""
	BG = (0, 0, 0) 																			# BG สีดำ (RGB)
	screen.fill(BG) 

######################    หน้าเกม   ##########################
def intro():																				# ฟังก์ชั่น หน้าเกม
	"""หน้าเกม"""
	bg_intro = pygame.image.load("bg_intro.jpg")											# ใส่รูป
	intro = True					
	""" loop intro """
	while intro:
		for event in pygame.event.get():
			mx, my = pygame.mouse.get_pos()																	
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				""" เมาส์ในการกด กลางหน้าจอ """
			if event.type == pygame.MOUSEBUTTONDOWN and mx > 249 and mx < 700 and my > 270 and my < 600:
				main()
		screen.blit(bg_intro,(0,0))
		pygame.display.update()

######################  RUN GAME #########################
def main():
	"""RUN"""
    
	posX = 0         																		#แกน x (ซ้าย- ขวา)
	posY = 750-40   																		# แกน y  (ขึ้น - ลง)
	move = 2																				# จำนวนย้าย
	""" loop รันเกม """
	while True:
		pygame.time.delay(20) 																# delay 
		down_bg()																			# ใส่ พื้นหลัง
		for event in pygame.event.get(): 													# ทำอีเว้น
			if event.type == pygame.QUIT:
				quit()																		# ออก

		""" key ในการกด  """
		keys = pygame.key.get_pressed() 													# กำหนด keys เป็น การกด
		if keys[pygame.K_a] and posX > 0: 													# LEFT
			posX -= move
		if keys[pygame.K_d] and posX < 1000 - 40: 											# RIGHT
			posX += move
		if keys[pygame.K_w] and posY > 0: 													# UP
			posY -= move
		if keys[pygame.K_s] and posY < 750 - 40: 											# DOWN
			posY += move
		screen.blit(player1,(posX, posY)) 													# แสดงผลตัวละคร
		pygame.display.update()   															# อัปเดรตหน้าจอ

#################### ฟังก์ชั้น ##################################
intro()	
