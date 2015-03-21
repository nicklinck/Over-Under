# Over Under Main Menu

import pygame
from pygame.locals import * 
import Options, Instructions, main, EndScreen

pygame.init()

#Setting the caption
pygame.display.set_caption("Main Menu")

screenSize= 1100, 700
white= 255,255, 255
blue = 102, 255, 255

#sets the size of the screen
screen = pygame.display.set_mode(screenSize)

class Image(pygame.sprite.Sprite):
    def __init__(self, color, filename, location, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(color) 
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]
        
    def mouseClick(self, buttonSize, location, file):
        
        mouseLoc = pygame.mouse.get_pos()
        
        if (mouseLoc[0] > location[0] and mouseLoc[0] < (location[0] + buttonSize[0])):
            if (mouseLoc[1] > location[1] and mouseLoc[1] < (location[1] + buttonSize[1])):
                level = file.load()
                
                if (level == 2 and file == main):
                    EndScreen.load()
                    
#bg_music = pygame.mixer.music
#bg_music.load("bgmusic.mp3")
                
def menu():
 
    #setting variables for buttons
    startLoc = (50, 50)
    startSize = (200, 75)
    bgLoc = (-5,-5)
    bgSize = (1294, 788)
    optionsLoc = (50, 175)
    optionsSize = (316, 80)
    instructionsLoc = (50, 300)
    instructionsSize = (512, 80)
    
    bg = Image((white), "../resources/homeScreen5.png", bgLoc, bgSize)
    start = Image((white), "../resources/start.png", startLoc, startSize)
    options = Image((white), "../resources/options.png", optionsLoc, optionsSize)
    instructions = Image((white), "../resources/instructions.png", instructionsLoc, instructionsSize)
    
    game = 0
    
    while game == 0:
        screen.fill(blue) 
        
        #printing the images to the screen
        screen.blit(bg.image, bg)
        screen.blit(start.image, start)
        screen.blit(options.image, options)
        screen.blit(instructions.image, instructions)
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                game = 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                game = 2
               
    #used to go to other screens
    if (game == 2):
        Image.mouseClick(start, startSize, startLoc, main) 
        Image.mouseClick(options, optionsSize, optionsLoc, Options) 
        Image.mouseClick(instructions, instructionsSize, instructionsLoc, Instructions)
        menu()
        
menu()
