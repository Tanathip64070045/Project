"""Escap game"""
###############  game set display  ############################
import pygame 																				
pygame.init() 																				
screen = pygame.display.set_mode((1000,750)) 												
pygame.display.set_caption("ESCAPE GAME") 													
icon = pygame.image.load("picture/icon.png")  														
pygame.display.set_icon(icon)    															
player = pygame.image.load("picture/tjakchar.png") 														
player1 = pygame.transform.scale(player,(80,80)) 											
																																	
#################### bg หลังการเดิน 1 ครั้ง ######################
def down_bg():
	"""BG หลังการเดิน"""
	BG = (0, 0, 0) 																			
	screen.fill(BG) 

######################    หน้าเกม   ##########################
def intro():																				
	"""หน้าเกม"""
	bg_intro = pygame.image.load("picture/intro2.png")
	bg1 = pygame.image.load("picture/button.png")													
	bg2 = pygame.image.load("picture/start.png")
	bg3 = pygame.image.load("picture/logout.png")
	bg4 = pygame.image.load("picture/logout2.png")
	""" ปรับ sale """
	bg_1 = pygame.transform.scale(bg1,(300,300))
	bg_2 = pygame.transform.scale(bg2,(300,300))
	bg_3 = pygame.transform.scale(bg3,(100,100))
	bg_4 = pygame.transform.scale(bg4,(100,100))
	intro = True					
	""" loop intro """
	while intro:
		for event in pygame.event.get():
			mx, my = pygame.mouse.get_pos()																	
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				""" เมาส์ในการกด กลางหน้าจอ """
			if mx > 320 and mx < 619 and my > 314 and my < 443:
				screen.blit(bg_2,(320,230))
			pygame.display.update()
			if mx > 438 and mx < 532 and my > 530 and my < 619:
				screen.blit(bg_4,(435,526))
			pygame.display.update()
			if event.type == pygame.MOUSEBUTTONDOWN and mx > 320 and mx < 619 and my > 314 and my < 443:
				main()
			if event.type == pygame.MOUSEBUTTONDOWN and mx > 438 and mx < 532 and my > 530 and my < 619:
				quit()
		screen.blit(bg_intro,(0,0))
		screen.blit(bg_1,(320,230))
		screen.blit(bg_3,(435,526))
		
		
######################  RUN GAME #########################
def main():
	"""RUN"""
    
	posX = 0         																		
	posY = 750-80   																		
	move = 2																				
	""" loop รันเกม """
	while True:
		pygame.time.delay(20) 																
		down_bg()																			
		for event in pygame.event.get(): 													
			if event.type == pygame.QUIT:
				quit()																		

		""" key ในการกด  """
		keys = pygame.key.get_pressed() 													
		if keys[pygame.K_a] and posX > 0: 													
			posX -= move
		if keys[pygame.K_d] and posX < 1000 - 80: 											
			posX += move
		if keys[pygame.K_w] and posY > 0: 													
			posY -= move
		if keys[pygame.K_s] and posY < 750 - 80: 											
			posY += move
		screen.blit(player1,(posX, posY)) 													
		pygame.display.update()   															

#################### ฟังก์ชั้น ##################################
intro()	
