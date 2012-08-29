import sys, pygame

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
XSPEED = 1
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

# Load sound
tag = pygame.mixer.Sound("ChatTag.wav")

test = 0
while 1:

    # Exit if window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # Move alien
    alienrect = alienrect.move(speed)

    # Deflect along left and right walls
    if alienrect.left < 0 or alienrect.right > WIDTH:
        speed[0] = -speed[0]
        tag.play()

    # Deflect along top and bottom walls
    if alienrect.top < 0 or alienrect.bottom > HEIGHT:
        speed[1] = -speed[1]
        tag.play()

    # Draw surface
    surface.fill(BLACK)
    if(test == 0):
        surface.blit(pacmanright, alienrect)
        test = 1
    elif(test == 1):
        surface.blit(pacmanright1, alienrect)
        test = 2
    else:
        surface.blit(pacmanclosed, alienrect)
        test = 0

        
    pygame.display.flip()
    clock.tick(30)
