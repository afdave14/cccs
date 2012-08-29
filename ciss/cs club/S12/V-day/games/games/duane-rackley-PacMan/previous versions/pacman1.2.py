import sys, pygame
from pygame.locals import *
import random; random.seed()
################################################################
def collideList():
    colList = [[(3*RATIO,6*RATIO)],[(7*RATIO,6*RATIO)],[(7*RATIO,8*RATIO)],[(3*RATIO,8*RATIO)],[(3*RATIO,11*RATIO)],[(7*RATIO,11*RATIO)],[(7*RATIO,12*RATIO)],
            [(3*RATIO,12*RATIO)],[(10*RATIO,6*RATIO)],[(15*RATIO,6*RATIO)],[(15*RATIO,8*RATIO)],[(10*RATIO,8*RATIO)]]
    return(colList)

################################################################
def createBoard():
    aBoard = []
    #Quadrant 1 block 1
    aBoard.append([(3*RATIO,6*RATIO),(7*RATIO,6*RATIO),(7*RATIO,8*RATIO),(3*RATIO,8*RATIO)])
    #Quadrant 1 block 3
    aBoard.append([(3*RATIO,11*RATIO),(7*RATIO,11*RATIO),(7*RATIO,12*RATIO),(3*RATIO,12*RATIO)])
    #Quadrant 1 block 2
    aBoard.append([(10*RATIO,6*RATIO),(15*RATIO,6*RATIO),(15*RATIO,8*RATIO),(10*RATIO,8*RATIO)])
    #Quadrant 1 block 4
    aBoard.append([(10*RATIO,11*RATIO),(10*RATIO,20*RATIO),(11*RATIO,20*RATIO),
            (11*RATIO,16*RATIO),(15*RATIO,16*RATIO),(15*RATIO,15*RATIO),(11*RATIO,15*RATIO),(11*RATIO,11*RATIO)])
    #Quadrant 1 block 5
    aBoard.append([(14*RATIO,11*RATIO),(14*RATIO,12*RATIO),(18*RATIO,12*RATIO),
            (18*RATIO,16*RATIO),(19*RATIO,16*RATIO),(19*RATIO,12*RATIO),(23*RATIO,12*RATIO),(23*RATIO,11*RATIO)])
    #Quadrant 2 block 1
    aBoard.append([(22*RATIO,6*RATIO),(22*RATIO,8*RATIO),(27*RATIO,8*RATIO),(27*RATIO,6*RATIO)])
    #Quadrant 2 block 2
    aBoard.append([(30*RATIO,6*RATIO),(30*RATIO,8*RATIO),(34*RATIO,8*RATIO),(34*RATIO,6*RATIO)])
    #Quadrant 2 block 3
    aBoard.append([(26*RATIO,11*RATIO),(26*RATIO,15*RATIO),(22*RATIO,15*RATIO),
            (22*RATIO,16*RATIO),(26*RATIO,16*RATIO),(26*RATIO,20*RATIO),(27*RATIO,20*RATIO),(27*RATIO,11*RATIO)])
    #Quadrant 2 block 4
    aBoard.append([(30*RATIO,11*RATIO),(30*RATIO,12*RATIO),(34*RATIO,12*RATIO),(34*RATIO,11*RATIO)])
    #Haunted House, where the ghosts start
    aBoard.append([(14*RATIO,19*RATIO),(23*RATIO,19*RATIO),(23*RATIO,24*RATIO),(14*RATIO,24*RATIO)])
    #Quadrant 3 block 1
    aBoard.append([(10*RATIO,23*RATIO),(10*RATIO,28*RATIO),(11*RATIO,28*RATIO),(11*RATIO,23*RATIO)])
    #Quadrant 3 block 2
    aBoard.append([(3*RATIO,31*RATIO),(3*RATIO,32*RATIO),(6*RATIO,32*RATIO),(6*RATIO,36*RATIO),(7*RATIO,36*RATIO),(7*RATIO,31*RATIO)])
    #Quadrant 3 block 3
    aBoard.append([(10*RATIO,31*RATIO),(10*RATIO,32*RATIO),(15*RATIO,32*RATIO),(15*RATIO,31*RATIO)])
    #Quadrant 3 block 4
    aBoard.append([(10*RATIO,35*RATIO),(10*RATIO,39*RATIO),(3*RATIO,39*RATIO),(3*RATIO,40*RATIO),(RATIO*15,RATIO*40),(15*RATIO,39*RATIO),(11*RATIO,39*RATIO),
            (11*RATIO,35*RATIO)])
    #Quadrant 3 block 5
    aBoard.append([(14*RATIO,27*RATIO),(14*RATIO,28*RATIO),(18*RATIO,28*RATIO),(18*RATIO,32*RATIO),(RATIO*19,RATIO*32),(19*RATIO,28*RATIO),(23*RATIO,28*RATIO),
            (23*RATIO,27*RATIO)])
    #Quadrant 3 block 6
    aBoard.append([(14*RATIO,35*RATIO),(14*RATIO,36*RATIO),(18*RATIO,36*RATIO),(18*RATIO,40*RATIO),(RATIO*19,RATIO*40),(19*RATIO,36*RATIO),(23*RATIO,36*RATIO),
            (23*RATIO,35*RATIO)])
    #Quadrant 4 block 1
    aBoard.append([(26*RATIO,23*RATIO),(26*RATIO,28*RATIO),(27*RATIO,28*RATIO),(27*RATIO,23*RATIO)])
    #Quadrant 4 block 2
    aBoard.append([(22*RATIO,31*RATIO),(22*RATIO,32*RATIO),(27*RATIO,32*RATIO),(27*RATIO,31*RATIO)])
    #Quadrant 3 block 3
    aBoard.append([(30*RATIO,31*RATIO),(30*RATIO,36*RATIO),(31*RATIO,36*RATIO),(31*RATIO,32*RATIO),(34*RATIO,32*RATIO),(34*RATIO,31*RATIO)])
    #Quadrant 4 block 4
    aBoard.append([(26*RATIO,35*RATIO),(26*RATIO,39*RATIO),(22*RATIO,39*RATIO),(22*RATIO,40*RATIO),(RATIO*36,RATIO*40),(36*RATIO,39*RATIO),(27*RATIO,39*RATIO),
            (27*RATIO,35*RATIO)])
    return(aBoard)
################################################################
################################################################
def createBoarder():
    aBoarder = []
    #draws bottom border
    aBoarder.append([(0,23*RATIO),(7*RATIO, 23*RATIO),(7*RATIO, 28*RATIO),(0, 28*RATIO),(0,35*RATIO),(3*RATIO,35*RATIO),(3*RATIO,RATIO*36),
             (0,RATIO*36),(0,RATIO*43),(WIDTH-16,RATIO*43),(WIDTH-16,RATIO*36),(WIDTH-(RATIO*2)-16,RATIO*36),(WIDTH-(RATIO*2)-16,RATIO*35),
             (WIDTH-16,RATIO*35),(WIDTH-16,RATIO*28),(RATIO*30,RATIO*28),(30*RATIO,RATIO*23),(WIDTH-16,RATIO*23),])
    #draws top boarder
    aBoarder.append([(0,RATIO*20),(7*RATIO,RATIO*20),(7*RATIO, RATIO*15),(0, RATIO*15),(0,3*RATIO),(18*RATIO, 3*RATIO),(18*RATIO, 8*RATIO),
             (19*RATIO, 8*RATIO),(19*RATIO,3*RATIO),(WIDTH-16,3*RATIO),(WIDTH-16,RATIO*15),(RATIO*30,RATIO*15),(RATIO*30,RATIO*20),(WIDTH-16,RATIO*20)])
    return(aBoarder)
################################################################

#################################################################
# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

# Set surface to 680x480
RATIO = 14#was 16
WIDTH = (RATIO * (28 + 12))#added 1 to the offset to the right edge can be seen
HEIGHT = (RATIO * (36 + 10))
SIZE = (WIDTH, HEIGHT)
surface = pygame.display.set_mode(SIZE)
BLACK = (0, 0, 0)

# Set speed of alien to [1,2]
XSPEED = 0
YSPEED = 0
speed = [XSPEED, YSPEED]

# Load pacman images
pacmanright = pygame.image.load("pmor.jpg")#open right
pacmanright1 = pygame.image.load("pmoor.jpg")#big open right
pacmanclosed = pygame.image.load("pmc.jpg")#closed
pacmandown = pygame.image.load("pmod.jpg")#open down
pacmandown1 = pygame.image.load("pmood.jpg")#big open down
pacmanleft = pygame.image.load("pmol.jpg")#open left
pacmanleft1 = pygame.image.load("pmool.jpg")#big open left
pacmanup = pygame.image.load("pmou.jpg")#open up
pacmanup1 = pygame.image.load("pmoou.jpg")#bigopen up

#####################################################################
#This section could be a function, creating the dots
dotArray = []#creates an array to hold all the dots
drawDotArray = []#partner array to determine if a dot should be drawn. will make dotArray two dimensional eventually
dot = pygame.image.load("dot.jpg")

dotsX = 1.5*RATIO
dotsY= 4.5*RATIO
for i in range(12):
    singleDot = dot.get_rect()
    singleDot = singleDot.move(dotsX, dotsY)
    dotArray.append(singleDot)
    dotsX += RATIO*38/26

##dotsX = 1*RATIO
##dotsY= 4*RATIO
##for i in range(8):
##    singleDot = dot.get_rect()
##    singleDot = singleDot.move(dotsX, dotsY)
##    dotArray.append(singleDot)
##    dotsY += RATIO*(43/26)*1.5
    
dotsX = 1.5*RATIO
dotsY= 9.5*RATIO
for i in range(26):
    singleDot = dot.get_rect()
    singleDot = singleDot.move(dotsX, dotsY)
    dotArray.append(singleDot)
    dotsX += RATIO*38/26

for i in range(45):
    drawDotArray.append(True)

########################################################################

pacmanrect = pacmanclosed.get_rect()#initializes pacman rec to closed mouth
pacmanrect = pacmanrect.move(18*RATIO, 24.5*RATIO)#Pacmans init place
movePath = [(10*RATIO,24.5*RATIO, 20*RATIO, 24.5*RATIO)]
mouthopening = 0#starts pacmans mouth closed
pacmandirection = 0#to determin which mouth direction to draw next
# direction 0 = right
# direction 1 = left
# direction 2 = up
# direction 3 = down

# Load sound
eating = pygame.mixer.Sound("eating.wav")

############################################################################
#Initialize the board
board = []
board = createBoard()
boarder = []
boarder = createBoarder()
#Getting the colision list
colisionList = []
colisionList = collideList()
#############################################################################

##############################################################################
while 1:
    ################################
    #START get keyboard input
    #eating.play() #plays sounds
    key = pygame.key.get_pressed()  #checking pressed keys
    if key[pygame.K_LEFT]:
        pacmandirection = 1
        speed[1] = 0
        speed[0] = -5
    if key[pygame.K_RIGHT]:
        pacmandirection = 0
        speed[1] = 0
        speed[0] = 5
    if key[pygame.K_UP]:
        pacmandirection = 2
        speed[1] = -5
        speed[0] = 0
    if key[pygame.K_DOWN]:
        pacmandirection = 3
        speed[1] = 5
        speed[0] = 0
    #END get keyboard input
    #################################

    # Exit if window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # Move pacman
    pacmanrect = pacmanrect.move(speed)

    ###############################################
    #can i eat the dot?
    for i in range(len(dotArray)):
        if(pacmanrect.colliderect(dotArray[i])):
            drawDotArray[i] = False
    ################################################
    
    #################################################
    # STOP when i hit the edge of the screen
    if pacmanrect.left < 0:
        speed[0] = 0
    if pacmanrect.right > WIDTH-16:
        speed[0] = 0
    if pacmanrect.top < 0:
        speed[1] = 0
    if pacmanrect.bottom > HEIGHT:
        speed[1] = 0
    #END stop when hits the edge
    ##################################################
    
    ##################################################
    # Draw surface
    surface.fill(BLACK)
    #drawing board
    for i in range(len(board)):
        pygame.draw.lines(surface, (0,0,255),True, board[i], 3)
    for i in range(len(boarder)):
        pygame.draw.lines(surface, (0,0,255),False, boarder[i], 3)
    #end drawing board
    ############################################################
    

    #Drawing the dots
    for i in range(len(dotArray)):
        if(drawDotArray[i] == True):
            surface.blit(dot, dotArray[i])
    #draws appropriate facing of pacman based on his direction
    ##########################################################
    if(pacmandirection == 0):
        if(mouthopening == 0):
            surface.blit(pacmanright, pacmanrect)
            mouthopening = 1
        elif(mouthopening == 1):
            surface.blit(pacmanright1, pacmanrect)
            mouthopening = 2
        else:
            surface.blit(pacmanclosed, pacmanrect)
            mouthopening = 0
    if(pacmandirection == 1):
        if(mouthopening == 0):
            surface.blit(pacmanleft, pacmanrect)
            mouthopening = 1
        elif(mouthopening == 1):
            surface.blit(pacmanleft1, pacmanrect)
            mouthopening = 2
        else:
            surface.blit(pacmanclosed, pacmanrect)
            mouthopening = 0
    if(pacmandirection == 2):
        if(mouthopening == 0):
            surface.blit(pacmanup, pacmanrect)
            mouthopening = 1
        elif(mouthopening == 1):
            surface.blit(pacmanup1, pacmanrect)
            mouthopening = 2
        else:
            surface.blit(pacmanclosed, pacmanrect)
            mouthopening = 0
    if(pacmandirection == 3):
        if(mouthopening == 0):
            surface.blit(pacmandown, pacmanrect)
            mouthopening = 1
        elif(mouthopening == 1):
            surface.blit(pacmandown1, pacmanrect)
            mouthopening = 2
        else:
            surface.blit(pacmanclosed, pacmanrect)
            mouthopening = 0
    #END drawing pacman in correct direction
    ######################################################################
    pygame.display.flip()
    clock.tick(25)
