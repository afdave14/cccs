import sys, pygame

# Initialize Pygame
pygame.init()

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

# Load differnt pac man images
popen = pygame.image.load("pacmanopen.jpg")
pclosed = pygame.image.load("pacman.jpg")

openOrClosed = 1


pacmanrect = popen.get_rect()

# Load sound
tag = pygame.mixer.Sound("ChatTag.wav")

while 1:

    # Exit if window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # Move pac man
    pacmanrect = pacmanrect.move(speed)


    # Deflect along left and right walls
    if pacmanrect.left < 0 or pacmanrect.right > WIDTH:
        speed[0] = -speed[0]
        tag.play()

    # Deflect along top and bottom walls
    if pacmanrect.top < 0 or pacmanrect.bottom > HEIGHT:
        speed[1] = -speed[1]
        tag.play()

    # Draw surface
    surface.fill(BLACK)
    if(openOrClosed == 1):
        surface.blit(pclosed, pacmanrect)
        openOrClose = 0
    else:
        surface.blit(popen, pacmanrect)
        openOrClosed = 1
    pygame.display.flip()

    pygame.time.delay(5)
