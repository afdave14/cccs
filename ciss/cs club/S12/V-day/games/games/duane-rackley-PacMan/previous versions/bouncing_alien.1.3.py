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
XSPEED = 0
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

dot = pygame.image.load("dot.jpg")

dotrect = dot.get_rect()
dotrect = dotrect.move(100,100)

pacmanrect = pacmanclosed.get_rect()



pacmandirection = 0#to determin which mouth direction to draw next
# direction 0 = right
# direction 1 = left
# direction 2 = up
# direction 3 = down
# Load sound
tag = pygame.mixer.Sound("ChatTag.wav")

mouthopening = 0
while 1:


    ################################
    #starting keyboard input
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
    #################################

    # Exit if window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # Move alien
    pacmanrect = pacmanrect.move(speed)

    ###############################################
    #can i eat the dot?
    #if(

    # stop along left and right walls
    if pacmanrect.left < 0:
        pacmandirection = 0
        speed[0] = 0
        tag.play()
    if pacmanrect.right > WIDTH:
        pacmandirection = 1
        speed[0] = 0
        tag.play()

    # stop along top and bottom walls
    if pacmanrect.top < 0:
        speed[1] = 0
        tag.play()
        
    if pacmanrect.bottom > HEIGHT:
        speed[1] = 0
        tag.play()

    # Draw surface
    surface.fill(BLACK)
    surface.blit(dot, dotrect)
    #draws appropriate facing of pacman based on his direction
    if(pacmandirection == 0):
        if(mouthopening == 0):
            surface.blit(pacmanright, pacmanrect)
            mouthopening = 1
        if(mouthopening == 1):
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
            

  
    
    pygame.display.flip()
    clock.tick(25)
