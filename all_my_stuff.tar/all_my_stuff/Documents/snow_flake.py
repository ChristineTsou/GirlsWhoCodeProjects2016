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
wind_choice=[True,False]
pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow")



class SnowFlake():
    '''
    This class will be used to create the SnowFlake Objects.
    It takes: 
        size - an integer that tells us how big we want the snowflake
        position - a 2 item list that tells us the coordinates of the snowflake (x,y) 
        wind - a boolean that lets us know if there is any wind or not.  
    '''
	
    def __init__(self):
 	   	self.size=random.randint(5,10)
 	   	self.x_pos=random.randint(0,700)
 	   	self.y_pos=0
 	   	self.wind=random.choice(wind_choice)
 	   	self.speed=random.randint(2,10)
    def fall(self, speed):
        """
        Take in a integer that represnts the speed at which the snowflake is falling in the y-direction.  
        A positive integer will have the snowflake falling down the screen. 
        A negative integer will have the snowflake falling up the screen. 
        
        If wind = True
            - the x direction of the snowflake changes
        """
        self.y_pos+=self.speed
        if self.wind==True:
        	self.x_pos+=self.speed	
        if self.y_pos<500:
        	self.y_pos=0	
        
    def draw(self):
        """
        Uses pygame and the global screen variable to draw the snowflake on the screen
        """
        pygame.draw.circle(screen,WHITE,(self.x_pos,self.y_pos),self.size)
        

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



# Speed
speed = 1


#INITIALIZE YOUR SNOWFLAKE HERE! 

# Snow List
snow_list = SnowFlake()
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here
	
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here
    # Begin Snow
    snow_list().fall(20)
    snow_list().draw()
    snow_list.remove((5))
    snow_list.apprend((5))
	
    



    


    # End Snow
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
