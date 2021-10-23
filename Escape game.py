"""Escap game"""
###############  game set display  ############################
import pygame 																				
pygame.init() 																				
screen = pygame.display.set_mode((1000,750)) 												
pygame.display.set_caption("ESCAPE GAME") 													
icon = pygame.image.load("picture/icon.png")  														
pygame.display.set_icon(icon)    															
player = pygame.image.load("picture/Player/tjakchar.png") 														
player1 = pygame.transform.scale(player,(40,40)) 											
																																	
#################### bg หลังการเดิน 1 ครั้ง ######################
def down_bg():
	"""BG หลังการเดิน"""
	BG = (0, 0, 0) 																			
	screen.fill(BG) 

######################    หน้าเกม   ##########################
def intro():																				
	"""หน้าเกม"""
	bg_intro = pygame.image.load("picture/Button/BG/intro2.png")
	bg1 = pygame.image.load("picture/Button/Start/StartN.png")													
	bg2 = pygame.image.load("picture/Button/Start/StartP.png")
	bg3 = pygame.image.load("picture/Button/Exit/ExitN.png")
	bg4 = pygame.image.load("picture/Button/Exit/ExitP.png")
	bg5 = pygame.image.load("picture/Button/TJAK (Credit)/TJAK.png")
	bg6 = pygame.image.load("picture/Button/TJAK (Credit)/TJAKmap.png")
	""" ปรับ sale """
	bg_1 = pygame.transform.scale(bg1,(150,100))
	bg_2 = pygame.transform.scale(bg2,(150,100))
	bg_3 = pygame.transform.scale(bg3,(100,100))
	bg_4 = pygame.transform.scale(bg4,(100,100))
	bg_5 = pygame.transform.scale(bg5,(200,90))
	bg_6 = pygame.transform.scale(bg6,(200,90))
	intro = True					
	""" loop intro """
	while intro:
		for event in pygame.event.get():
			mx, my = pygame.mouse.get_pos()																	
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				""" เมาส์ในการกด กลางหน้าจอ """
			if mx > 423 and mx < 555 and my > 588 and my < 684:
				screen.blit(bg_2,(415,587))
			pygame.display.update()
			if mx > 888 and mx < 973 and my > 14 and my < 97:
				screen.blit(bg_4,(880, 12))
			pygame.display.update()
			if mx > 10 and mx < 200 and my > 14 and my < 96:
				screen.blit(bg_6,(6,12))
			pygame.display.update()
			if event.type == pygame.MOUSEBUTTONDOWN and mx > 423 and mx < 555 and my > 588 and my < 684:
				main()
			if event.type == pygame.MOUSEBUTTONDOWN and mx > 888 and mx < 973 and my > 14 and my < 97:
				quit()
		screen.blit(bg_intro,(0,0))
		screen.blit(bg_1,(415,587))
		screen.blit(bg_3,(880,12))
		screen.blit(bg_5,(6,12))
		
######################  RUN GAME #########################
def main():
	"""RUN"""
    
	posX = 0         																		
	posY = 750-40   																		
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
		if keys[pygame.K_d] and posX < 1000 - 40: 											
			posX += move
		if keys[pygame.K_w] and posY > 0: 													
			posY -= move
		if keys[pygame.K_s] and posY < 750 - 40: 											
			posY += move
		screen.blit(player1,(posX, posY)) 													
		pygame.display.update()   															
#################### ฟังก์ชั้น ##################################
intro()	
