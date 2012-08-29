import sys, pygame
from pygame.locals import *



# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()



# Set surface to 680x480
WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)
surface = pygame.display.set_mode(SIZE)
BLACK = (0, 0, 0)

# Set speed of alien to [1,2]
XSPEED = 5
YSPEED = 0
speed = [XSPEED, YSPEED]

# Load alien image and get image rect
pacmanright = pygame.image.load("pmor.jpg")#open right
pacmanright1 = pygame.image.load("pmoor.jpg")#big open right
pacmanclosed = pygame.image.load("pmc.jpg")#closed
pacmandown = pygame.image.load("pmod.jpg")#open down
pacmandown1 = pygame.image.load("pmood.jpg")#big open down
pacmanleft = pygame.image.load("pmol.jpg")#open left
pacmanleft1 = pygame.image.load("pmool.jpg")#big open left
pacmanup = pygame.image.load("pmou.jpg")#open up
pacmanup1 = pygame.image.load("pmoou.jpg")#bigopen up
alienrect = pacmanclosed.get_rect()

pacmandirection = 0#to determin which mouth direction to draw next

# Load sound
tag = pygame.mixer.Sound("ChatTag.wav")

test = 0
while 1:

    pygame.draw.line(surface, (0,0,255), (5, 5), (5,470), 10)
    while 1:
        print "r"

    ################################
    #starting keyboard input
    key = pygame.key.get_pressed()  #checking pressed keys
    if key[pygame.K_LEFT]:
        speed[0] = -speed[0]
    if key[pygame.K_RIGHT]:
        speed[0] = -speed[0]




    #################################

    # Exit if window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # Move alien
    alienrect = alienrect.move(speed)

    # Deflect along left and right walls
    if alienrect.left < 0:
        pacmandirection = 0
        speed[0] = -speed[0]
        tag.play()
    if alienrect.right > WIDTH:
        pacmandirection = 1
        speed[0] = -speed[0]
        tag.play()

    # Deflect along top and bottom walls
    if alienrect.top < 0:
        speed[1] = -speed[1]
        tag.play()
        
    if alienrect.bottom > HEIGHT:
        speed[1] = -speed[1]
        tag.play()

    # Draw surface
    surface.fill(BLACK)
    print pacmandirection
    if(pacmandirection == 0):
        if(test == 0):
            surface.blit(pacmanright, alienrect)
            test = 1
        elif(test == 1):
            surface.blit(pacmanright1, alienrect)
            test = 2
        else:
            surface.blit(pacmanclosed, alienrect)
            test = 0
    if(pacmandirection == 1):
        if(test == 0):
            surface.blit(pacmanleft, alienrect)
            test = 1
        elif(test == 1):
            surface.blit(pacmanleft1, alienrect)
            test = 2
        else:
            surface.blit(pacmanclosed, alienrect)
            test = 0

        
    pygame.display.flip()
    clock.tick(30)
