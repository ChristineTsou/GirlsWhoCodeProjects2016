"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
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


# WRITE YOUR CODE HERE





# -------- Main Program Loop -----------
x=350
y=250
random_numbersize=random.randint(20,80)
size=random_numbersize
random_numberx=random.randint(-10,10)
random_numbery=random.randint(-10,10)
color=[BLACK,WHITE,GREEN,RED,BLUE,GREY,ORCHID,THISTLE,CORAL,DARKSALMON]
num_color=len(color)
color_choice=random.randint(0,num_color-1)
COLOR=color[color_choice]

while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	#def ball():
    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.

		screen.fill(WHITE)
	def ball():
    # --- Drawing code should go here
	
		screen.fill(GREEN)
		circle=pygame.draw.circle(screen,COLOR,(x,y),size)
		x+=random_numberx
		y+=random_numbery
		if x>670:
			random_numberx=random.randint(-10,0)
			color_choice=random.randint(0,num_color-1)
			COLOR=color[color_choice]
		if x<20:
			random_numberx=random.randint(0,10)
			color_choice=random.randint(0,num_color-1)
			COLOR=color[color_choice]
		if y>480:
		 	random_numbery=random.randint(-10,0)
		 	color_choice=random.randint(0,num_color-1)
		 	COLOR=color[color_choice]
		if y<20:
			random_numbery=random.randint(0,10)
			color_choice=random.randint(0,num_color-1)
			COLOR=color[color_choice]
        
	# --- Go ahead and update the screen with what we've drawn.
		pygame.display.flip()

    # --- Limit to 60 frames per second
		clock.tick(60)
ball()
ball()
#ball()
# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
