"""Escap game"""
###############  game set display  ############################
import pygame
#from pygame.constants import BIG_ENDIAN																				
pygame.init() 																				
screen = pygame.display.set_mode((1000,750)) 												
pygame.display.set_caption("ESCAPE GAME") 													
icon = pygame.image.load("picture/Button/icon.png")  														
pygame.display.set_icon(icon)    															
player = pygame.image.load("picture/Player/tjakchar.png") 														
player1 = pygame.transform.scale(player,(25,25)) 											
#################### bg bg backgound สี ######################
def down_bg2():
	"""bg สี """
	BG = (255, 128, 0) 																			
	screen.fill(BG) 

#################### map ที่ 1 ################################
def map1():
	"""BG หลังการเดิน"""
	BG = pygame.image.load("picture/Button/BG/back_103.png")
	bg = pygame.transform.scale(BG,(1000,750))
	wall = pygame.image.load("picture/map/block_stone.png")	
	wall2 = pygame.transform.scale(wall,(30,30))																
	point_x = 0
	point_y = 0
	screen.blit(bg,(0,0))
	map_print = """
	                                 o
	                                 o                                   
	xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxy
	xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxy
	xxxx        x       xxx   xxxxxxxy
	xxxx xxx xx  x xxx xxxx x xxxxxxxy
	xxx  xx   xxxx xxx      x        y
	xx  x xx xx   xxxxxx xxxx xxxxxx y
	xx xx xx xxx xxxx xx xxxx   xxxx y
	xx x       x xx           x    x y
	xx x xxxxxxx xxx xxxxxxxxxxxxx xxy
	xx x xx xxxx  xx x xxxx    xx  xxy
	xx x xx   xxx xx   xxxx xx xx xxxy
	     xx x xx   xxx x    xx       o
	xx xxxx x xx x       xxxxxxx xxxxy
	xx      x x  xxxxx xxxx    x xxxxy
	xxx xx xxxxxxxxxxx      xxxx xxxxy
	xxx xx    x    xxxx xxxxxxxx x xxy
	xx  xxxxx x xx    x xxxx     x xxy
	xx xxx xx x xxxxxxx xxxx xxxx  xxy
	xx xx  x    x            xxxx xxxy
	xx xx xxxx xx x xxxxx xxxxxxx xxxy
	xx    xxxx    x   xxx         xxxy
	xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxy
	xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxy""" # กว้าง 25 ยาว 34
	for i in map_print:
		if i == "x":
			screen.blit(wall2,(point_x,point_y))
			point_x += 30
		if i == " ":
			point_x += 30
		if i == "y":
			screen.blit(wall2,(point_x,point_y))
			point_x = 0
			point_y += 30
		if i == "o":
			point_y += 30
			point_x = 0	
		
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
			if event.type == pygame.MOUSEBUTTONDOWN and  mx > 10 and mx < 200 and my > 14 and my < 96:
				credit()
		screen.blit(bg_intro,(0,0))
		screen.blit(bg_1,(415,587))
		screen.blit(bg_3,(880,12))
		screen.blit(bg_5,(6,12))

######################  credit #########################
def credit():
	"""CREDIT"""
	message1 = "TANATIP SINGHANON"
	message2 = "AKHAPOP KHUNKITI"
	message3 = "KEN MURAKI"
	message4 = "JEERACHAYA CHAREONPOL"
	back_bt = pygame.image.load("picture/Button/Back/back1.png")
	back_bt2 = pygame.image.load("picture/Button/Back/back2.png")
	sc_b1 = pygame.transform.scale(back_bt,(70,70))
	sc_b2 = pygame.transform.scale(back_bt2,(70,70))
	font = pygame.font.SysFont("Courier", 50)
	blue = (0, 0, 153)
	msg = font.render(message1, True, blue)
	msg2 = font.render(message2, True, blue)
	msg3 = font.render(message3, True, blue)
	msg4 = font.render(message4, True, blue)
	posi3 = msg3.get_rect(center=(screen.get_rect().centerx,
								screen.get_rect().centery))
	down_bg2()
	screen.blit(sc_b1,(10,10))
	screen.blit(msg, (353,164))
	screen.blit(msg2, (353,259))
	screen.blit(msg3, posi3)
	screen.blit(msg4, (351, 438))
	pygame.display.update()
	BG = (0, 0, 0) 
	while True:
		for event in pygame.event.get():
			mx, my = pygame.mouse.get_pos() 													
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.MOUSEMOTION and mx > 10 and mx < 70 and my > 13 and my < 67:
				screen.blit(sc_b2,(10,10))
				pygame.display.update()
			if event.type == pygame.MOUSEBUTTONDOWN and mx > 10 and mx < 70 and my > 13 and my < 67:
				intro()
			if mx > 70 or my > 52:
				down_bg2()
				screen.blit(sc_b1,(10,10))
				screen.blit(msg, (353,164))
				screen.blit(msg2, (353,259))
				screen.blit(msg3, posi3)
				screen.blit(msg4, (351, 438))
				pygame.display.update()
				
######################  RUN GAME #########################
def main():
	"""RUN"""
    
	posX = 0         																		
	posY = 395  																		
	move = 2																				
	""" loop รันเกม """
	while True:
		pygame.time.delay(7) 																
		map1()																			
		for event in pygame.event.get(): 													
			if event.type == pygame.QUIT:
				quit()
		""" key ในการกด  """
		keys = pygame.key.get_pressed() 													
		if keys[pygame.K_a] and posX > 0:													
			posX -= move
		if keys[pygame.K_d] and posX < 1000-25: 											
			posX += move
		if keys[pygame.K_w] and posY > 0: 													
			posY -= move
		if keys[pygame.K_s] and posY < 680: 											
			posY += move
		screen.blit(player1,(posX, posY)) 													
		pygame.display.update()
		print(posX, posY)														
#################### ฟังก์ชั้น ##################################
intro()	
