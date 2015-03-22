import pygame, Key, Gate, Level

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

#called by the Main Menu
def load():
    pygame.init()
    
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    
    pygame.display.set_caption("Over Under")
    
    #Does not work properly on Macs
    timer = pygame.time.Clock()
    
    #Initializes the starting locations of player
    #TODO: initialize them in a different location depending on the level number
    playerOne = Player(20, SCREEN_HEIGHT - 20 - 80, 1)
    playerTwo = Player(80, SCREEN_HEIGHT - 20 - 80, 2)
    
    #Creates the array of level objects
    level_list = []
    i = 0
    while i < 2:
        i += 1
        level_list.append(Level.Level(i))
    
    #sets this to the current level
    current_level_num = 0
    current_level = level_list[current_level_num]
    
    
    #main game loop
    done = False
    while not done:
        #if the player exits the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                
            #checks for various key presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    playerOne.jump()
                if event.key == pygame.K_a:
                    playerOne.go_left()
                if event.key == pygame.K_d:
                    playerOne.go_right()
                
                if event.key == pygame.K_LEFT:
                    playerTwo.go_left()
                if event.key == pygame.K_RIGHT:
                    playerTwo.go_right()
                if event.key == pygame.K_UP: 
                    if playerTwo.crouching:
                        playerTwo.standUp(current_level.platform_list)
                    else:
                        playerTwo.jump()  
                elif event.key == pygame.K_DOWN and playerTwo.onGround and (playerTwo.crouching == False):
                    playerTwo.crouch()   
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a and playerOne.speedX < 0:
                    playerOne.stop()
                if event.key == pygame.K_d and playerOne.speedX > 0:
                    playerOne.stop()
                
                if event.key == pygame.K_LEFT and playerTwo.speedX < 0:
                    playerTwo.stop()
                if event.key == pygame.K_RIGHT and playerTwo.speedX > 0:
                    playerTwo.stop()
 
        
 
        #updates the players and sees if they have the conditions to finish the level
        levelCompleteOne = playerOne.update(current_level.platform_list, playerTwo)
        levelCompleteTwo = playerTwo.update(current_level.platform_list, playerOne)
        
        current_level.update(playerOne, playerTwo)
        
        if levelCompleteOne and levelCompleteTwo:
            #if there are still levels remaining
            if current_level_num < len(level_list) - 1:
                #restarts the players and loads the next level
                #TODO: make a separate function for this, set players at different locations depending on the level
                playerOne.rect.x = 20
                playerOne.rect.y = SCREEN_HEIGHT - 20 - 80
                playerTwo.rect.x = 80
                playerTwo.rect.y = SCREEN_HEIGHT - 20 - 80
                playerOne.speedX = 0
                playerOne.speedY = 0
                playerTwo.speedX = 0
                playerTwo.speedY = 0
                playerOne.hasKey = False
                playerTwo.hasKey = False
                if playerTwo.crouching:
                    playerTwo.standUp(current_level.platform_list)
                current_level_num += 1
                current_level = level_list[current_level_num]
            
            #no levels left, return and exit back to the main menu
            else:
                current_level_num += 1
                return current_level_num
        
        #draw the platforms
        current_level.draw(screen)
        
        #draw the players
        playerOne.draw(screen)
        playerTwo.draw(screen)
        
        #for 60fps
        #DOESN'T WORK ON MACS
        timer.tick(60)
        
        pygame.display.update()
    
    return current_level_num

#Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, playerNum):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("../resources/player.png").convert()
        self.image.set_colorkey(pygame.Color("white"))
        
        self.width = 40
        self.height = 80
        
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.speedX = 0
        self.speedY = 0
        
        self.onGround = True
        self.crouching = False
        self.playerNum = playerNum #1 for jumping player, 2 for crouching player
        self.hasKey = False
        
        self.disabled = True
        
    def update(self, platform_list, otherPlayer):        
        levelComplete = False

        #calculates new y speed
        self.calcGrav()
        
        if self.disabled:
            self.speedX = 0
            if self.onGround == True:
                self.speedY = 0
            self.disabled = False
            
        self.onGround = False
 
        #moves in x direction
        self.rect.x += self.speedX
 
        #checks if the player collides with anything
        collision_list = pygame.sprite.spritecollide(self, platform_list, False)
        for block in collision_list:
            #if it's a platform
            if isinstance(block, Level.Platform):
                #if moving left, place the player to the right of the platform
                if self.speedX > 0:
                    self.rect.right = block.rect.left
                #if moving right, place the player to the left of the platform
                elif self.speedX < 0:
                    self.rect.left = block.rect.right
            #if it's a key
            elif isinstance(block,Key.key) and not self.hasKey:
                #player now has a key
                self.hasKey = True
                #removes the key from the screen
                block.rect.x=-50
            #if it's a gate
            elif isinstance(block, Gate.gate) and self.hasKey:
                #if they have a key, levelComplete is true and is return later
                levelComplete = True
                
        #checks for collision with the other player, similar to a platform
        if pygame.sprite.collide_rect(self, otherPlayer):
            if self.speedX > 0:
                self.rect.right = otherPlayer.rect.left
            elif self.speedX < 0:
                self.rect.left = otherPlayer.rect.right
         
        #moves in y direction    
        self.rect.y += self.speedY
 
        #checks for collisions
        collision_list = pygame.sprite.spritecollide(self, platform_list, False)
        for block in collision_list:
            
            #if the player is on top of a button, activate the button
            if isinstance(block, Level.Button):
                block.activate()
            
            #just like collisions with x direction
            if isinstance(block, Level.Platform):
                #If the player is under a wall, stop the player's and the wall's movement
                if isinstance(block, Level.Wall) and self.rect.y > block.rect.y:
                    block.rect.bottom = self.rect.top + 1
                    block.disabled = True
                    self.disabled = True
                    
                else:
                    if self.speedY > 0:
                        self.rect.bottom = block.rect.top
                        self.onGround = True
                    elif self.speedY < 0:
                        self.rect.top = block.rect.bottom
                
                # Stop moving vertically if we hit a platform
                self.speedY = 0
                    
            if isinstance(block,Key.key) and not self.hasKey:
                self.hasKey = True
                block.rect.x=-50
            elif isinstance(block,Gate.gate) and self.hasKey:
                levelComplete = True
            
        if pygame.sprite.collide_rect(self, otherPlayer):
            if self.speedY > 0:
                self.rect.bottom = otherPlayer.rect.top
                if otherPlayer.onGround:
                    self.onGround = True
            elif self.speedY < 0:
                self.rect.top = otherPlayer.rect.bottom
            self.speedY = 0
         
        #returns True if the player has a key and is at the gate, false otherwise
        return levelComplete   
            
    def calcGrav(self):
        #initial y speed if they walk off a platform or hit the top of a platform
        if self.speedY == 0:
            self.speedY = 1
        #acceleration for gravity
        else:
            self.speedY += .35
 
        #checks if they are past the bottom of the screen
        #not really needed since platforms will cover the bottom of the screen
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.speedY >= 0:
            self.speedY = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height
            self.onGround = True

    #function for player Two
    #TODO: perhaps make a new class for PlayerTwo that inherits from Player
    def standUp(self, platform_list):
        #create new sprite for standing up
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("../resources/player.png").convert()
        self.image.set_colorkey(pygame.Color("white"))


        self.height = 80
        
        #storing old location
        x = self.rect.x
        y = self.rect.y
        
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        #updating new location
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - 20
        
        self.crouching = False
        
        #if standing up makes you collide with another platform, go back to crouching
        #TODO: FIX BUG: can't stand up while at the gate
        collision_list = pygame.sprite.spritecollide(self, platform_list, False)
        #print (len(collision_list))
        for block in collision_list:
            if isinstance(block, Level.Platform):
                self.crouch()
                break
        
    #only for player Two       
    def crouch(self):
        #create new sprite for crouching player
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("../resources/playerCrouch.png").convert()
        self.image.set_colorkey(pygame.Color("white"))


        self.height = 60
        
        #stores previous location
        x = self.rect.x
        y = self.rect.y
        
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        #new location
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y + 20

        self.crouching = True       

    def jump(self):
        if self.onGround:
            self.speedY = -12 + (4.5 * (self.playerNum - 1)) #different values for different players
            self.onGround = False
 
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def go_left(self):
        self.speedX = -6
 
    def go_right(self):
        self.speedX = 6
 
    def stop(self):
        self.speedX = 0        
    
        
        
if(__name__ == "__main__"):
    load()