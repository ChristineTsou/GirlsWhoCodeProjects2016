import pygame
import random
import time

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
color_list=[BLACK,WHITE,GREEN,RED,BLUE]

# pygame boilerplate
pygame.init()
size = (1200, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("City Scroller 0.1")
clock = pygame.time.Clock()

# setup
done = False
circle= False
BACKGROUND = WHITE

# loop

while not done:
	
	# event handling
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True	
	screen.fill(BACKGROUND)
	if event.type== pygame.MOUSEBUTTONDOWN:
		circle=True
		xspeed=random.randint(-20,20)
		yspeed=random.randint(-20,20)
		(x,y)=pygame.mouse.get_pos()
		print("Click")
		time.sleep(.2)
	if event.type==pygame.key.get_pressed()[pygame.K_SPACE]:
		(x_rect,y_rect)=pygame.mouse.get_pos()
		pygame.draw.rect(screen,RED,(x_rect,y_rect),50,0)
		rect_speed=20
		
	# update logic
	press=pygame.key.get_pressed()
	if pygame.key.get_pressed()[pygame.K_DOWN]:
		rect_y=rect_y-rect_speed
	if pygame.key.get_pressed()[pygame.K_DOWN]:
		rect_y=rect_y+rect_speed
	if pygame.key.get_pressed()[pygame.K_LEFT]:
		rect_y=rect_x-rect_speed
	if pygame.key.get_pressed()[pygame.K_RIGHT]:
		rect_y=rect_x+rect_speed
	# draw
	
	if circle==True:
		circle_size=random.randint(20,80)
		pygame.draw.circle(screen,random.choice(color_list),(x,y),circle_size,0)
		x+=xspeed
		y+=yspeed
		if x>=(1200-circle_size*2) or x<=circle_size*2:
			xspeed=-xspeed
		if y>=(800-circle_size*2) or y<=circle_size*2:
			yspeed=-yspeed
	
	pygame.display.flip()
	clock.tick(60)


# exit
pygame.quit()
exit()
