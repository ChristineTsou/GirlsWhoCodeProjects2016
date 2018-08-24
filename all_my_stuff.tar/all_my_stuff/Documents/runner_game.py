import pygame
import random
import time

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


# pygame boilerplate
pygame.init()
size = (600, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("City Scroller 0.1")
clock = pygame.time.Clock()







# setup
done = False
class player_sprite(pygame.sprite.Sprite):
	def __init__(self, file):
		pygame.sprite.Sprite.__init__(self)
		self.color=RED
		self.speed=50
		self.playerw=20
		self.playerh=20
		self.image = pygame.image.load(file)		# determines HOW sprite is drawn
		#self.image.fill(RED)								# for now, it's just a filled rectangle
		self.rect = self.image.get_rect()
		self.rect.x=578
		self.rect.y=370
		
	def draw(self):
		pygame.draw.rect(screen,self.color,(self.playerx,self.playery,self.playerw,self.playerh),0)
	def handle_keys(self):
		key=pygame.key.get_pressed()
		dist=10
		if key[pygame.K_DOWN]:
			self.rect.y+=dist
		if key[pygame.K_UP]:
			self.rect.y-=dist
		if key[pygame.K_RIGHT]:
			self.rect.x+=dist
		if key[pygame.K_LEFT]:
			self.rect.x-=dist
	def loop_around(self):	
		if self.rect.x>=588:
			self.rect.x=2
		if self.rect.x<=1:
			self.rect.x=583
		if self.rect.y>=398:
			self.rect.y=12
		if self.rect.y<=10:
			self.rect.y=395
class GoodSprites(player_sprite):
	def __init__(self):
		player_sprite.__init__(self, "giftbox.png")	
# 		self.w=8
# 		self.h=8
# 		self.image = pygame.Surface([self.w, self.h])		# determines HOW sprite is drawn
# 		self.image.fill(BLUE)								# for now, it's just a filled rectangle
		self.rect = self.image.get_rect()
		self.rect.x=-10
		self.rect.y=random.randint(0,400)
	def move(self):
		for i in range(10):
			self.speed=1	
			self.rect.x+=self.speed
	
class BadSprites(player_sprite):
	def __init__(self):
		player_sprite.__init__(self,"icicle.png")
		# self.w=5
# 		self.h=8
# 		self.image = pygame.Surface([self.w, self.h])		# determines HOW sprite is drawn
# 		self.image.fill(GREEN)								# for now, it's just a filled rectangle
		self.rect = self.image.get_rect()
		self.rect.x=-10
		self.rect.y=random.randint(0,400)
	def move(self):
		for i in range(10):
			self.speed=1	
			self.rect.x+=self.speed				
			
	#def draw(self):
	#		pygame.draw.rect(screen,BLUE,(self.goodx,self.goody,5,5)0)
good_1=GoodSprites()
good_2=GoodSprites()
good_3=GoodSprites()
bad_1=BadSprites()
bad_2=BadSprites()
bad_sprites=pygame.sprite.Group(bad_1,bad_2)
main_sprite=player_sprite("santa.png")
all_sprites = pygame.sprite.Group()
all_sprites.add(main_sprite,good_1,good_2,good_3,bad_1,bad_2)
good_sprites=pygame.sprite.Group()
good_sprites.add(good_1,good_2,good_3)
BACKGROUND = WHITE

score=0
lives=5

# loop
while not done:

	# event handling
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True	
	
	# update logic
	# draw
	screen.fill(BACKGROUND)
	#main_sprite.draw()
	#scores!!!
	collide_list=pygame.sprite.spritecollide(main_sprite,good_sprites,True)
	for collide in collide_list:
		score+=1
		score_str="Score:"
		print (score_str,score)
	#Bad guys
	death_list=pygame.sprite.spritecollide(main_sprite,bad_sprites,False)
	for death in death_list:
		lives-=.5
		
		
		
	
	
	
	
	
	
	all_sprites.draw(screen)
	main_sprite.handle_keys()
	good_1.loop_around()
	good_2.loop_around()
	good_3.loop_around()
	bad_1.loop_around()
	bad_2.loop_around()
	bad_1.move()
	bad_2.move()
	main_sprite.loop_around()
	all_sprites.update()
	good_1.move()
	good_2.move()
	good_3.move()
	
	#print to screen
	font=pygame.font.SysFont('Times',24,True,False)
	text=font.render("Score: "+str(score),True,BLACK)
	screen.blit(text,[20,40])
	text=font.render("Lives: "+str(lives),True,BLACK)
	screen.blit(text,[20,20])
	
	
		
		
	
	
	
	
	
	
	
	pygame.display.flip()
	clock.tick(60)


# exit
pygame.quit()
exit()
