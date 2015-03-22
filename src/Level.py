import pygame, Key, Gate

def generate(levnum):
    levelMap = 0
    if levnum == 1:
        levelMap = [
    "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                             K                                P",
    "P                  PPPPPPPPPPPPPPPPPPPPPPPPP                   P",
    "P                  PPPPPPPPPPPPPPPPPPPPPPPPP                   P",
    "P                  PPPPPPPPPPPPPPPPPPPPPPPPP                   P",
    "P                  PPPPPPPPPPPPPPPPPPPPPPPPP                   P",
    "P                  PPPPPPPPPPPPPPPPPPPPPPPPP                   P",
    "P                  PPPPPPPPPPPPPPPPPPPPPPPPP                   P",
    "P                                                              P",
    "P                                                              P",
    "P                              K                              GP",
    "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"]
        
    elif levnum == 2:
        levelMap = [
    "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "P                                                              P",
    "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"]
    
    #return levelMap
    if (levnum > 0):
        return Level(levelMap)

class Level(object):
    platform_list = None
            
    def __init__(self, levelNum):
        self.platform_list = pygame.sprite.Group()
        self.button_list = []
        x = 0
        y = 0
        
        if levelNum == 1:
            levelMap = [
                "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                             K                                P",
                "P                  PPPPPPPPPPPPPPPPPPPPPPPPP                   P",
                "P                  PPPPPPPPPPPPPPPPPPPPPPPPP                   P",
                "P                  PPPPPPPPPPPPPPPPPPPPPPPPP                   P",
                "P                  PPPPPPPPPPPPPPPPPPPPPPPPP                   P",
                "P                  PPPPPPPPPPPPPPPPPPPPPPPPP                   P",
                "P                  PPPPPPPPPPPPPPPPPPPPPPPPP                   P",
                "P                                                              P",
                "P                                                              P",
                "P                              K                              GP",
                "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"]
        
        elif levelNum == 2:
            levelMap = [
                "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                                                              P",
                "P                   K                        K                GP",
                "PPPPPPPPPPPPPPPPPPPP PPPPPPPPPPPPPPPPPPPPPPPP PPPPPPPPPPPPPPPPPP"]
        
        for row in levelMap:
                for col in row:
                    if col == "P":
                        p = Platform(x, y)
                        self.platform_list.add(p)
                    elif col =="K":
                        k = Key.key((x,y))
                        self.platform_list.add(k)
                    elif col =="G":
                        g = Gate.gate((x,y))
                        self.platform_list.add(g)
                    x += 20
                y += 20
                x = 0
        
        if levelNum == 2:
            self.wall = Wall(200, 200, 630, 100, 10)
            self.platform_list.add(self.wall)
            
            self.button = Button(400, 700, self.wall)
            self.platform_list.add(self.button)
            self.button_list.append(self.button)
            
            self.wall = Wall(600, 500, 700, 100, 10)
            self.platform_list.add(self.wall)
            
            self.button = Button(900, 700, self.wall)
            self.platform_list.add(self.button)
            self.button_list.append(self.button)
            
            
    def update(self, playerOne, playerTwo):
        for button in self.button_list:
            button.wall.update(button.activated, playerOne, playerTwo)
            button.deactivate()
        
    def draw(self, screen):
        screen.fill((255, 255, 255))
        self.platform_list.draw(screen)
        

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20, 20])
        
        self.image.fill((0, 0, 0))
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
class Wall(Platform):
    def __init__(self, x, y, bottom, maxIncrease, speedY):
        Platform.__init__(self, x, y)
        self.image = pygame.Surface([20, bottom - y])
        self.image.fill((0, 0, 255))
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.bottomY = y
        self.topY = y - maxIncrease
        self.speedY = speedY
        
        self.disabled = False
        
    def update(self, activated, playerOne, playerTwo):
        if(activated):
            self.rect.y = self.rect.y - self.speedY
            
            if self.rect.y < self.topY:
                self.rect.y = self.topY
                
        elif self.disabled:
            self.disabled = False
            
        else:
            self.rect.y = self.rect.y + self.speedY
            
            if pygame.sprite.collide_rect(self, playerOne) and self.rect.bottom > playerOne.rect.y:
                self.rect.bottom = playerOne.rect.y + 1
                playerOne.disabled = True
                self.disabled = True
                
            elif pygame.sprite.collide_rect(self, playerTwo) and self.rect.bottom > playerTwo.rect.y:
                self.rect.bottom = playerTwo.rect.y + 1
                playerTwo.disabled = True
                self.disabled = True
            
            elif self.rect.y > self.bottomY:
                self.rect.y = self.bottomY
           
        
class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, wall):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface([20,20])
        self.image.fill((0, 255, 0))
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.wall = wall
        self.activated = False
        
    def activate(self):
        self.activated = True
        
    def deactivate(self):
        self.activated = False   