import pygame
import random
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
ORCHID=(218,112,214)
THISTLE=(216,191,216)
CORAL=(255,127,80)
DARKSALMON=(233,150,122)
pygame.init()
# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Bouncing Ball Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


color_list=[BLACK,WHITE,RED,BLUE,GREY,ORCHID,THISTLE,CORAL,DARKSALMON]
class Ball:
	def __init__(self,x_pos,y_pos):
		self.color=random.choice(color_list)
		self.size=random.randint(20,80)
		self.x_speed=random.randint(-10,10)
		self.y_speed=random.randint(-10,10)
		self.x_pos=x_pos
		self.y_pos=y_pos
	def move(self):
		self.x_pos+=self.x_speed
		self.y_pos+=self.y_speed
		if self.x_pos>SCREEN_WIDTH or self.x_pos<0:
			self.x_speed=-1*self.x_speed
			self.change_color()
		if self.y_pos>SCREEN_HEIGHT or self.y_pos<0:
			self.y_speed=-1*self.y_speed
			self.change_color()
	def change_color(self):
		self.color=random.choice(color_list)
	def draw(self):
		pygame.draw.circle(screen,self.color,(self.x_pos,self.y_pos),self.size)
ball_1=Ball(100,200)
ball_2=Ball(300,42)
while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	screen.fill(WHITE)
	screen.fill(GREEN)
	ball_1.draw()
	ball_1.move()
	ball_2.move()
	ball_1.draw()
	ball_2.draw()
# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
# --- Limit to 60 frames per second
	clock.tick(60)
# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
		