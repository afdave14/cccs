import sys, pygame
import math
import random
import time

# Initialize Pygame
pygame.init()
pygame.mixer.init()
random.seed()

# print error message
sys.stdout = file("stdout.txt", "w")
sys.stderr = file("stderr.txt", "w")
#HighScoresFile = open("HighScores.txt", "r+")


# Set surface to 680x480
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TRANSPARENT = (1, 2, 3)
RED = (255, 0, 0)


XPOS = WIDTH / 2
YPOS = HEIGHT / 2

FPS = 30
NSTARS = 1000
NASTEROIDS = 3
NLASERS = 6


#####################################################################
# Load image function
def load_image(name):
    """ Load image """
    image = pygame.image.load(name)
    return image, image.get_rect()

######################### Laser Class #################################
class Laser(pygame.Rect):

    def __init__(self):
        self.rect = pygame.Rect(0, 0, 4, 4)
        self.speed = 0
        self.vel = 15.0
        self.vx = 0
        self.vy = 0
        self.angle = 0
        self.alive = False

    def position(self, x, y, angle):
        self.rect.x = x
        self.rect.y = y
        self.angle = angle

    def draw(self, surface):
        self.fire()
        pygame.draw.rect(surface, RED, self.rect)

    def update(self):
        self.rect.move_ip(self.vx, self.vy)

    def fire(self):
        self.vx = self.vel * math.cos(math.radians(self.angle))
        self.vy = self.vel * math.sin(math.radians(self.angle))
        self.update()

####################### Ship Class #############################
class Ship(pygame.sprite.Sprite):

    turnSpeed = 10
    thrustValue = 1.0
    maxSpeed = 10.0

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("Asteroids_Spaceship.png")
        self.image = self.image.convert()
        self.original = self.image
        self.rect.center = (XPOS, YPOS)
        self.angle = 0
        self.vx = 0
        self.vy = 0
        self.alive = True
        self.lasers = []
        self.numLasers = 0
     
        
    def update(self):
        self.rect.move_ip(self.vx, self.vy)
        self.wrap()

    # wrap the ship around the screen
    def wrap(self):
        if (self.rect.center[0] < 0):
            self.rect.move_ip(WIDTH, 0)
        elif (self.rect.center[0] >= WIDTH):
            self.rect.move_ip(-WIDTH, 0)

        if (self.rect.center[1] < 0):
            self.rect.move_ip(0, HEIGHT)
        elif (self.rect.center[1] >= HEIGHT):
            self.rect.move_ip(0, -HEIGHT)

    # used for moving the ship in the right direction
    def thrust(self):
        self.vx += self.thrustValue * math.cos(math.radians(self.angle))
        self.vy += self.thrustValue * math.sin(math.radians(self.angle))

        # increase the speed of the ship until it reaches the max speed
        vel = math.sqrt(self.vx * self.vx + self.vy * self.vy)
        if (vel > self.maxSpeed):
            self.vx = self.vx * self.maxSpeed / vel
            self.vy = self.vy * self.maxSpeed / vel

    def reverse(self):
        self.vx += math.cos(math.radians(self.angle)) * -1
        self.vy += math.sin(math.radians(self.angle)) * -1

        # increase the speed of the ship until it reaches the max speed
        vel = math.sqrt(self.vx * self.vx + self.vy * self.vy)
        if (vel > self.maxSpeed):
            self.vx = self.vx * self.maxSpeed / vel
            self.vy = self.vy * self.maxSpeed / vel

    def turn(self, direction):
        self.angle += self.turnSpeed * direction
        while (self.angle < 0):
            self.angle += 360

        while (self.angle >= 360):
            self.angle -= 360

        self.image = pygame.transform.rotate(self.original, -self.angle)
        self.rect = self.image.get_rect(center = self.rect.center)

    def fire(self):
        laser = Laser()
        laser.position(self.rect.centerx, self.rect.centery, self.angle)
        laser.alive = True
        self.lasers.append(laser)
        self.numLasers += 1
        pygame.mixer.Sound("FIRE.WAV").play()

    def hyperSpace(self):
        x = int(WIDTH * random.random())
        y = int(HEIGHT * random.random())
        self.rect.move_ip(x,y)

        
##########################Large Asteroid Class#################################
class Asteroid(pygame.sprite.Sprite):
    
    min_speed = 3
    max_speed = 6
    SPACE = 100
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("AsteroidBig.png")

        num = random.randint(1, 2)
        if num == 1:
            x = int(WIDTH * random.random())
            y = HEIGHT + self.SPACE
        else:
            x = WIDTH + self.SPACE
            y = int(HEIGHT * random.random())
            
        self.rect = self.image.get_rect(center=(x,y))
        
            
        velocity = random.uniform(self.min_speed, self.max_speed)
        angle = 2.0 * math.pi * random.random() # radians
        self.vx = math.cos(angle) * velocity
        self.vy = math.sin(angle) * velocity
        while int(self.vx) == 0 or int(self.vy) == 0:
            angle = 2.0 * math.pi * random.random() # radians
            self.vx = math.cos(angle) * velocity
            self.vy = math.sin(angle) * velocity
            
     
    def update(self):
        self.rect.move_ip(self.vx, self.vy)
        self.wrap()

    def wrap(self):
        if (self.rect.centerx < -self.SPACE):
                self.rect.move_ip(WIDTH + self.SPACE, 0)
        elif (self.rect.centerx >= WIDTH + self.SPACE):
                self.rect.move_ip(-(WIDTH + self.SPACE), 0)
            
        if (self.rect.centery < -self.SPACE):
                self.rect.move_ip(0, HEIGHT + self.SPACE)          
        elif (self.rect.centery >= HEIGHT + self.SPACE):
                self.rect.move_ip(0, -(HEIGHT + self.SPACE))


##################### Small Asteroid Class ###########################
class SmAsteroid(pygame.sprite.Sprite):
    
    min_speed = 5
    max_speed = 10
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("AsteroidSmall.png")
            
        velocity = random.randint(self.min_speed, self.max_speed)
        angle = 2.0 * math.pi * random.random() # radians
        self.vx = math.cos(angle) * velocity
        self.vy = math.sin(angle) * velocity     
     
    def update(self):
        self.rect.move_ip(self.vx, self.vy)
        self.wrap()

    def wrap(self):
        if (self.rect.center[0] < 0):
            self.rect.move_ip(WIDTH, 0)            
        elif (self.rect.center[0] >= WIDTH):
            self.rect.move_ip(-WIDTH, 0)            
            
        if (self.rect.center[1] < 0):
           self.rect.move_ip(0, HEIGHT)            
        elif (self.rect.center[1] >= HEIGHT):
           self.rect.move_ip(0, -HEIGHT)


#######################################################################

def main():
    while 1:
        # in game constants
        GAME = False
        SCORE = 0
        LIVES = 3
        LAPSECOUNT = 0
        HighScoresFile = open("HighScores.txt", "r")

        # picture for lives
        livesImage, livesRect = load_image("Asteroids_Lives.png")
        
        
        # intialise screen
        surface = pygame.display.set_mode(SIZE)
        pygame.display.set_caption('Astroid')
        surface.fill(BLACK)
        
        # initialize starting sprite
        ship = Ship()

        # initialize sprite groups
        render = pygame.sprite.RenderUpdates()
        render.add(ship)

        # create asteroid sprite groups
        asteroids = pygame.sprite.Group()
        smAsteroids = pygame.sprite.Group()

        # Set up asteroids for Welcome Screen
        for i in range(0,6):
            # new asteriods are stored in group
            asteroid = Asteroid()
            asteroids.add(asteroid)
        ################ Get High Scores ############################
        Rank = []
        Name = []
        Score = []
        for i in range(0, 10):
            HighScore = HighScoresFile.readline()
            part = HighScore.partition('$')
            Rank.append(part[0])
            part = part[2].partition('$')
            Name.append(part[0])
            part = part[2].partition('$')
            Score.append(part[0])
            
        HighScoresFile.close()
        print Rank
        print Name
        print Score
         
        ##### WElCOME SCREEN ############################################
        HelpMenu = False
        while(GAME == False):

            ############### EVENTS ######################################
            # Exit if window is closed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    key = pygame.key.get_pressed()

                    if key[pygame.K_RETURN]:
                        GAME = True

                    elif key[pygame.K_h]:
                        HelpMenu = True

                    elif key[pygame.K_m]:
                        HelpMenu = False

                    if key[pygame.K_f]:
                        surface = pygame.display.set_mode(SIZE, pygame.FULLSCREEN)

                    if key[pygame.K_w]:
                        surface = pygame.display.set_mode(SIZE)

            ################## FONTS ####################################
            font = pygame.font.Font(None, 50)
            fontGameName = font.render("ASTEROIDS", 1, WHITE)
            fontGameNameRect = fontGameName.get_rect()
            fontGameNameRect.centerx = XPOS
            fontGameNameRect.centery = fontGameNameRect.h
            font = pygame.font.Font(None, 30)
            fontDeveloper = font.render("By Justin Eggemeyer", 1, WHITE)
            fontDeveloperRect = fontDeveloper.get_rect()
            fontDeveloperRect.centerx = XPOS
            fontDeveloperRect.centery = fontGameNameRect.h + fontDeveloperRect.h + 20

            #################### Score Fonts ############################
            fontScore1 = font.render(Rank[0] + ". " + Name[0] + "          " + Score[0], 1, WHITE)
            fontScore2 = font.render(Rank[1] + ". " + Name[1] + "          " + Score[1], 1, WHITE)
            fontScore3 = font.render(Rank[2] + ". " + Name[2] + "          " + Score[2], 1, WHITE)
            fontScore4 = font.render(Rank[3] + ". " + Name[3] + "          " + Score[3], 1, WHITE)
            fontScore5 = font.render(Rank[4] + ". " + Name[4] + "          " + Score[4], 1, WHITE)
            fontScore6 = font.render(Rank[5] + ". " + Name[5] + "          " + Score[5], 1, WHITE)
            fontScore7 = font.render(Rank[6] + ". " + Name[6] + "          " + Score[6], 1, WHITE)
            fontScore8 = font.render(Rank[7] + ". " + Name[7] + "          " + Score[7], 1, WHITE)
            fontScore9 = font.render(Rank[8] + ". " + Name[8] + "          " + Score[8], 1, WHITE)
            fontScore10 = font.render(Rank[9] + ". " + Name[9] + "          " + Score[9], 1, WHITE)

            fontScore1Rect = fontScore1.get_rect()
            fontScore1Rect.centerx = XPOS
            fontScore1Rect.centery = fontGameNameRect.h + fontScore1Rect.h + 50
            fontScore2Rect = fontScore2.get_rect()
            fontScore2Rect.centerx = XPOS
            fontScore2Rect.centery = fontGameNameRect.h + (fontScore2Rect.h * 2) + 60
            fontScore3Rect = fontScore3.get_rect()
            fontScore3Rect.centerx = XPOS
            fontScore3Rect.centery = fontGameNameRect.h + (fontScore3Rect.h * 3) + 70
            fontScore4Rect = fontScore4.get_rect()
            fontScore4Rect.centerx = XPOS
            fontScore4Rect.centery = fontGameNameRect.h + (fontScore4Rect.h * 4) + 80
            fontScore5Rect = fontScore5.get_rect()
            fontScore5Rect.centerx = XPOS
            fontScore5Rect.centery = fontGameNameRect.h + (fontScore5Rect.h * 5) + 90
            fontScore6Rect = fontScore6.get_rect()
            fontScore6Rect.centerx = XPOS
            fontScore6Rect.centery = fontGameNameRect.h + (fontScore6Rect.h * 6) + 100
            fontScore7Rect = fontScore7.get_rect()
            fontScore7Rect.centerx = XPOS
            fontScore7Rect.centery = fontGameNameRect.h + (fontScore7Rect.h * 7) + 110
            fontScore8Rect = fontScore8.get_rect()
            fontScore8Rect.centerx = XPOS
            fontScore8Rect.centery = fontGameNameRect.h + (fontScore8Rect.h * 8) + 120
            fontScore9Rect = fontScore9.get_rect()
            fontScore9Rect.centerx = XPOS
            fontScore9Rect.centery = fontGameNameRect.h + (fontScore9Rect.h * 9) + 130
            fontScore10Rect = fontScore10.get_rect()
            fontScore10Rect.centerx = XPOS
            fontScore10Rect.centery = fontGameNameRect.h + (fontScore10Rect.h * 10) + 140
            
            #############################################################
                
            fontPlay = font.render("PLAY GAME: Press ENTER", 1, WHITE)
            fontPlayRect = fontPlay.get_rect()
            fontPlayRect.centerx = XPOS
            if HelpMenu:
                fontPlayRect.centery = YPOS + (YPOS / 2)
            else:
                fontPlayRect.centery = fontScore10Rect.centery + 100

            fontHelp = font.render("HELP MENU: Press H", 1, WHITE)
            fontHelpRect = fontHelp.get_rect()
            fontHelpRect.centerx = XPOS
            fontHelpRect.centery = fontPlayRect.centery + fontHelpRect.h

            fontMain = font.render("MAIN MENU: PRESS M", 1, WHITE)
            fontMainRect = fontMain.get_rect()
            fontMainRect.centerx = XPOS
            fontMainRect.centery = fontPlayRect.centery + fontMainRect.h

            fontUp = font.render("Move Forward - Press Up Arrow", 1, WHITE)
            fontUpRect = fontUp.get_rect()
            fontUpRect.centerx = XPOS 
            fontUpRect.centery = YPOS / 2

            fontDown = font.render("Move Backward - Press Down Arrow", 1, WHITE)
            fontDownRect = fontDown.get_rect()
            fontDownRect.centerx = XPOS 
            fontDownRect.centery = (YPOS / 2) + fontDownRect.h

            fontLeft = font.render("Rotate Left - Press Left Arrow", 1, WHITE)
            fontLeftRect = fontLeft.get_rect()
            fontLeftRect.centerx = XPOS 
            fontLeftRect.centery = (YPOS / 2) + (fontLeftRect.h + fontDownRect.h)

            fontRight = font.render("Rotate Right - Press Right Arrow", 1, WHITE)
            fontRightRect = fontRight.get_rect()
            fontRightRect.centerx = XPOS 
            fontRightRect.centery = (YPOS / 2) + (fontRightRect.h + fontLeftRect.h + fontDownRect.h)

            fontFire = font.render("Fire Laser - Press Spacebar", 1, WHITE)
            fontFireRect = fontFire.get_rect()
            fontFireRect.centerx = XPOS 
            fontFireRect.centery = (YPOS / 2) + (fontFireRect.h + fontRightRect.h + fontLeftRect.h + fontDownRect.h)

            fontHyper = font.render("Hyperspace - Press H", 1, WHITE)
            fontHyperRect = fontHyper.get_rect()
            fontHyperRect.centerx = XPOS 
            fontHyperRect.centery = fontFireRect.centery + fontHyperRect.h

            fontPause = font.render("Pause - Press P", 1, WHITE)
            fontPauseRect = fontPause.get_rect()
            fontPauseRect.centerx = XPOS 
            fontPauseRect.centery = fontHyperRect.centery + fontPauseRect.h

            fontFull = font.render("Fullscreen - Press F", 1, WHITE)
            fontFullRect = fontFull.get_rect()
            fontFullRect.centerx = XPOS 
            fontFullRect.centery = fontPauseRect.centery + fontFullRect.h

            fontWindow = font.render("Window Screen - Press W", 1, WHITE)
            fontWindowRect = fontWindow.get_rect()
            fontWindowRect.centerx = XPOS 
            fontWindowRect.centery = fontFullRect.centery + fontWindowRect.h
            ##################### DRAW SCREEN ###########################
            surface.fill(BLACK)
            asteroids.draw(surface)
            asteroids.update()
            if HelpMenu:
                surface.blit(fontGameName, fontGameNameRect)
                surface.blit(fontDeveloper, fontDeveloperRect)
                surface.blit(fontUp, fontUpRect)
                surface.blit(fontDown, fontDownRect)
                surface.blit(fontLeft, fontLeftRect)
                surface.blit(fontRight, fontRightRect)
                surface.blit(fontFire, fontFireRect)
                surface.blit(fontHyper, fontHyperRect)
                surface.blit(fontPause, fontPauseRect)
                surface.blit(fontFull, fontFullRect)
                surface.blit(fontWindow, fontWindowRect)
                surface.blit(fontPlay, fontPlayRect)
                surface.blit(fontMain, fontMainRect)
            else:
                surface.blit(fontGameName, fontGameNameRect)
                surface.blit(fontDeveloper, fontDeveloperRect)
                surface.blit(fontScore1, fontScore1Rect)
                surface.blit(fontScore2, fontScore2Rect)
                surface.blit(fontScore3, fontScore3Rect)
                surface.blit(fontScore4, fontScore4Rect)
                surface.blit(fontScore5, fontScore5Rect)
                surface.blit(fontScore6, fontScore6Rect)
                surface.blit(fontScore7, fontScore7Rect)
                surface.blit(fontScore8, fontScore8Rect)
                surface.blit(fontScore9, fontScore9Rect)
                surface.blit(fontScore10, fontScore10Rect)
                surface.blit(fontPlay, fontPlayRect)
                surface.blit(fontHelp, fontHelpRect)
            pygame.display.flip()

        ##### GAME STARTS HERE #####
            
        # Reset font size for Score
        font = pygame.font.Font(None, 25)

        # Reset asteroids
        asteroids.empty()
        for i in range(0,NASTEROIDS):
            # new asteriods are stored in group
            asteroid = Asteroid()
            render.add(asteroid)
            asteroids.add(asteroid)
        
        # key repeat
        pygame.key.set_repeat(50, 50)

        #set Clock
        clock = pygame.time.Clock()

        """ GAME LOOP """
        while GAME:
            #cap the framerate
            lapse = clock.tick(FPS)

                
            ############### EVENTS###############################################
            # Exit if window is closed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            
                if event.type == pygame.KEYDOWN:
                    key = pygame.key.get_pressed()

                    if key[pygame.K_UP]:
                       ship.thrust()

                    elif key[pygame.K_DOWN]:
                        ship.reverse()

                    direction = key[pygame.K_RIGHT] - key[pygame.K_LEFT]
                    if (direction != 0):
                        ship.turn(direction)

                    if key[pygame.K_SPACE]:
                        if ship.alive:
                            if ship.numLasers < NLASERS:
                                ship.fire()

                    if key[pygame.K_h]:
                        ship.hyperSpace()

                    if key[pygame.K_p]:
                        pause = True
                        while pause:
                            font = pygame.font.Font(None, 40)
                            fontPause = font.render("PAUSED", 1, WHITE)
                            surface.blit(fontPause, (XPOS - 50, YPOS - 10))
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    sys.exit()
                                if event.type == pygame.KEYDOWN:
                                    if key[pygame.K_p]:
                                        pause = False

                    if key[pygame.K_f]:
                        surface = pygame.display.set_mode(SIZE, pygame.FULLSCREEN)

                    if key[pygame.K_d]:
                        surface = pygame.display.set_mode(SIZE)

                            
            ######################################################################		    
            #############LASER COLLISION DETECTION################################        
            # check for asteroid and laser collision
            for i in range(len(ship.lasers)):
                if ship.lasers[i].alive:
                    for asteroid in asteroids:
                        if ship.lasers[i].rect.colliderect(asteroid):
                            ship.numLasers -= 1
                            ship.lasers[i].alive = False
                            for j in range(0, 2):
                                #create smaller asteroids for destroyed large asteroid
                                smAsteroid = SmAsteroid()
                                smAsteroid.rect.center = asteroid.rect.center
                                render.add(smAsteroid)
                                smAsteroids.add(smAsteroid)

                            asteroid.kill()
                            SCORE += 50
                            
                            if SCORE % 10000 == 0 and SCORE > 0:
                                LIVES += 1

                            pygame.mixer.Sound("EXPLODE2.WAV").play()

                            
                    
            # check for small asteroid and laser collision
            for i in range(len(ship.lasers)):
                if ship.lasers[i].alive:
                    for smAsteroid in smAsteroids:
                        if ship.lasers[i].rect.colliderect(smAsteroid):
                            ship.numLasers -= 1
                            ship.lasers[i].alive = False
                            
                            smAsteroid.kill()
                            SCORE += 100
                            
                            if SCORE % 10000 == 0 and SCORE > 0:
                                LIVES += 1

                            pygame.mixer.Sound("EXPLODE3.WAV").play()
                            
            #####################################################################          
            ####################SHIP COLLISION DECTION###########################
            # check for ship and asteroid collision
            for asteroid in pygame.sprite.spritecollide(ship, asteroids, False):
                if ship.alive:
                    ship.kill()
                    LIVES -= 1
                    ship.alive = False
                    pygame.mixer.Sound("EXPLODE1.WAV").play()

            # check for ship and small asteroid collision
            for smAsteroid in pygame.sprite.spritecollide(ship, smAsteroids, False):
                if ship.alive:
                    ship.kill()
                    LIVES -= 1
                    ship.alive = False
                    pygame.mixer.Sound("EXPLODE1.WAV").play()
            ####################################################################
            ###################Laser Distance###################################
            for i in range(len(ship.lasers)):
                if ship.lasers[i].alive:
                    if (ship.lasers[i].rect.x <= 0 or ship.lasers[i].rect.x >= WIDTH):
                        ship.lasers[i].alive = False
                        ship.numLasers -= 1
                        
                    if (ship.lasers[i].rect.y <= 0 or ship.lasers[i].rect.y >= HEIGHT):
                        ship.lasers[i].alive = False
                        ship.numLasers -= 1

            ####################################################################
            # clear ship.lasers[]
            temp = []
            for laser in ship.lasers:
                if laser.alive:
                    temp.append(laser)

            ship.lasers = list(temp)

            ################# Resetting Destroyed ships#########################
            # if ship destroyed and lives left create new ship
            if LIVES > 0:
                if ship.alive == False:
                    LAPSECOUNT += lapse
                    if LAPSECOUNT > 1000:
                        ship = Ship()
                        render.add(ship)
                        LAPSECOUNT = 0

            ################# Starting New Levels###############################
            # check if all asteroids destroyed
            if len(asteroids) == 0 and len(smAsteroids) == 0:
                LAPSECOUNT += lapse
                if LAPSECOUNT > 3000:
                    render.update()
                    render.clear(surface, surface)
                    render.draw(surface)
                    numAsteroids = NASTEROIDS + random.randint(1, 3)
                    
                    for i in range(0, numAsteroids):
                        # new asteriods are stored in group
                        asteroid = Asteroid()
                        render.add(asteroid)
                        asteroids.add(asteroid)
                        LAPSECOUNT = 0
            ####################################################################
                    
            
            ##########################DRAWING THE GAME##########################
            # fill in background
            surface.fill(BLACK)
            #update sprites
            render.update()
            #draw the scene
            render.clear(surface, surface)
            render.draw(surface)

            for i in range(len(ship.lasers)):
                ship.lasers[i].draw(surface)
            
            # Display Score and Lives
            font = pygame.font.Font(None, 30)
            fontScore = font.render("Score: " + str(SCORE), 1, WHITE)
            fontScoreRect = fontScore.get_rect()
            surface.blit(fontScore, fontScoreRect)

            for i in range(LIVES):
                livesRect.x = WIDTH - (livesRect.w * i)
                surface.blit(livesImage, livesRect)

            pygame.display.flip()
            pygame.display.flip()

            ######################################################################
            if LIVES == 0:
                GAME = False

        ################### END of GAME ###################################
        #set Clock
        clock = pygame.time.Clock()
        LAPSECOUNT = 0
        while True:
            #cap the framerate
            lapse = clock.tick(FPS)
            font = pygame.font.Font(None, 100)
            fontGameOver = font.render("GAME OVER", 1, WHITE)
            fontGameOverRect = fontGameOver.get_rect()
            fontGameOverRect.centerx = XPOS
            fontGameOverRect.centery = YPOS - 150
            surface.blit(fontGameOver, fontGameOverRect)
            pygame.display.flip()
            LAPSECOUNT += lapse
            if (LAPSECOUNT >= 2000):
                break

        
        surface.fill(BLACK)
        nameEntered = False
        name = ""
        while nameEntered == False:
            font = pygame.font.Font(None, 30)
            fontGetName = font.render("Enter 3 letters for name: ", 1, WHITE)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    x = pygame.key.name(event.key)
                    name = name + str(x)
                    name = name.upper()
                    txtName = font.render(name, 1, WHITE)
                    surface.blit(txtName, (XPOS,YPOS + 20))
                    print len(name), "::NAME::", name
                    if len(name) >= 3:
                        nameEntered = True
                        #txtName = font.render(name, 1, WHITE)
                        #surface.blit(txtName, (XPOS,YPOS))
                    
            fontGetNameRect = fontGetName.get_rect()
            fontGetNameRect.centerx = XPOS
            fontGetNameRect.centery = YPOS - (fontGetNameRect.h + 20)

            surface.blit(fontGetName,fontGetNameRect)
            
            pygame.display.flip()

        for i in range(0, len(Score)):
            if SCORE > int(Score[i]):
                Score.insert(i, str(SCORE))
                Name.insert(i, name)
                Score.pop()
                Name.pop()
                break;

        #insert New High Score into File
        HighScoresFile = open("HighScores.txt", "w")
        for i in range(0, 10):
            inputStr = Rank[i] + "$" + Name[i] + "$" + Score[i] + "$\n"
            print inputStr
            HighScoresFile.write(inputStr)

        # close the High Scores File
        HighScoresFile.close()
        
        
if __name__ == '__main__': main()


    
