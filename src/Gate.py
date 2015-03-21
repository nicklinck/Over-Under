import pygame

class gate(pygame.sprite.Sprite):
	def __init__(self,location):
		pygame.sprite.Sprite.__init__(self)
		# call parent class constructorpygame.sprite.Sprite.__init__(self)
		# load the image, converting the pixel format for optimization
		self.image = pygame.image.load("../resources/gate.png").convert()
		# make 'color' transparent on the image
		self.image.set_colorkey((102,255,255)) 
		# resize image to 40x40 px
		self.image = pygame.transform.scale(self.image, (60,120))    
		# set the rectangle defined for this image for collision detection
		self.rect = self.image.get_rect()
		# position the image
		self.rect.x = location[0]-60+20
		self.rect.y = location[1]-120+20
	
