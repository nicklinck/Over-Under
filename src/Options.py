#Options Menu
import pygame
from pygame.locals import *

pygame.init()

class Image(pygame.sprite.Sprite):
    def __init__(self, color, filename, location, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(color) 
        self.image = pygame.transform.scale(self.image, (size))
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]

def load():
    
    pygame.display.set_caption('Options')

    screenSize = 1100, 700
    white = 255, 255, 255
    black = 0, 0, 0

    screen = pygame.display.set_mode(screenSize)
    
    titleLoc = (0, 0)
    title = Image((white), "../resources/optionsScreen.png", titleLoc, screenSize)
    
    backLoc = (50, 550)
    backSize = (128, 128)
    backButton = Image((black), "../resources/back.png", backLoc, backSize)
    
    global game
    game = 0
    while game == 0 :
        
        screen.fill(white)
        
        screen.blit(title.image, title)
        screen.blit(backButton.image, backButton)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                game = 1
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseLoc = pygame.mouse.get_pos()
                if (mouseLoc[0] > backLoc[0] and mouseLoc[0] < (backLoc[0] + backSize[0])):
                    if (mouseLoc[1] > backLoc[1] and mouseLoc[1] < (backLoc[1] + backSize[1])):
                        game = 1
                        
        
        pygame.display.update()     
