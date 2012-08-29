import sys, pygame

# Size of each tile - game sizes are based off of this
TILESIZE = 25

WIDTH = TILESIZE * 32
HEIGHT = TILESIZE * 26
SIZE = (WIDTH, HEIGHT)

# Set TetrisConstants.SURFACE size
SURFACE = pygame.display.set_mode(SIZE)

FRAME_RATE = 1000.0 / 60

#Colors for the game
BACKGROUND = pygame.Color(25,25,112) # Background for main window
GAMEBACKGROUND = pygame.Color('black') # Background for framed Rect
RECTINNERBORDER = pygame.Color(192, 192, 192)
RECTOUTERBORDER = pygame.Color(0, 0, 255)

CYAN = pygame.Color(0,255,255) # I
BLUE = pygame.Color(0,0,255) # J
ORANGE = pygame.Color(255,165,0) # L
YELLOW = pygame.Color(255,255,0) # O
GREEN = pygame.Color(0,190,0) # S
PURPLE = pygame.Color(150,0,150) # T
RED = pygame.Color(215,0,0) # Z

#Pieces in the game
PIECES = ['L', 'J', 'S', 'Z', 'O', 'I', 'T']
