import sys, pygame, math, random

import TetrisConstants, TetrisFunctions, TetrisDrawFunctions, TetrisMoveFunctions

sys.stdout = file('stdout.txt', 'w')
sys.stderr = file('stderr.txt', 'w')

# Initialize Pygame
pygame.init()
random.seed()

# Load music and sounds
pygame.mixer.music.load('one.mid') # main game music
drop = pygame.mixer.Sound("pop2.wav") # sound to be played when piece hits stack/bottom
blowUp = pygame.mixer.Sound("bomb-03.wav") # sound to be played when bomb explodes

explosion0 = pygame.image.load('explosion0.gif')
explosion1 = pygame.image.load('explosion1.gif')
explosion2 = pygame.image.load('explosion2.gif')
explosion0.set_colorkey(pygame.Color('black'))
explosion1.set_colorkey(pygame.Color('black'))
explosion2.set_colorkey(pygame.Color('black'))

explosions = []
explosions.append(explosion0)
explosions.append(explosion1)
explosions.append(explosion2)

# Load high scores from HighScores.txt
highScores = []

fileScores = open('HighScores.txt', 'r')

for lines in fileScores:
    highScores.append(int(lines))

fileScores.close()

# Set font sizes
titleFont = pygame.font.SysFont('Times New Roman', 90)
framedRectFont = pygame.font.SysFont('Times New Roman', 20)
framedRectFont1 = pygame.font.SysFont('Times New Roman', 45)

# Set words and sizes for beginning screen
title = 'Time Bomb Tetris!!' # also used for main window

titleRender = titleFont.render(title, 1, pygame.Color('white'))
titleSize = titleFont.size(title)
title1Render = framedRectFont.render("Enter - Begin", 1, pygame.Color('white'))
title1Size = framedRectFont.size("Enter - Begin")
title2Render = framedRectFont.render("H - Help menu", 1, pygame.Color('white'))
title2Size = framedRectFont.size("H - Help menu")
title3Render = framedRectFont.render("S - Show high scores", 1, pygame.Color('white'))
title3Size = framedRectFont.size("S - Show high scores")
title4Render = framedRectFont.render("Q - Quit at any time", 1, pygame.Color('white'))
title4Size = framedRectFont.size("Q - Quit at any time")

backToTitleScreenRender = framedRectFont.render("Enter - Back", 1, pygame.Color('white'))
backToTitleScreenSize = framedRectFont.size("Enter - Back")

# Set words and sizes for help screen
helpRender = framedRectFont1.render("Help Menu", 1, pygame.Color('white'))
helpSize = framedRectFont1.size("Help Menu")
help1Render = framedRectFont.render("During game play ...", 1, pygame.Color('white'))
help1Size = framedRectFont.size("During game play ...")
help2Render = framedRectFont.render("Left arrow - moves the tetris piece left", 1, pygame.Color('white'))
help2Size = framedRectFont.size("Left arrow - moves the tetris piece left")
help3Render = framedRectFont.render("Right arrow - moves the tetris piece right", 1, pygame.Color('white'))
help3Size = framedRectFont.size("Right arrow - moves the tetris piece right")
help4Render = framedRectFont.render("Down arrow - moves the tetris piece down", 1, pygame.Color('white'))
help4Size = framedRectFont.size("Down arrow - moves the tetris piece down")
help5Render = framedRectFont.render("Up - arrow rotates the tetris piece clockwise", 1, pygame.Color('white'))
help5Size = framedRectFont.size("Up - arrow rotates the tetris piece clockwise")
help6Render = framedRectFont.render("Up arrow - rotates the tetris piece clockwise", 1, pygame.Color('white'))
help6Size = framedRectFont.size("Up arrow - rotates the tetris piece clockwise")
help7Render = framedRectFont.render("S - rotates the tetris piece counterclockwise", 1, pygame.Color('white'))
help7Size = framedRectFont.size("S - rotates the tetris piece counterclockwise")
help8Render = framedRectFont.render("P - pauses the game", 1, pygame.Color('white'))
help8Size = framedRectFont.size("P - pauses the game")
help9Render = framedRectFont.render("Left shift - is used to hold piece", 1, pygame.Color('white'))
help9Size = framedRectFont.size("Left shift - is used to hold piece")
help10Render = framedRectFont.render("Space - instantly drops the tetris piece", 1, pygame.Color('white'))
help10Size = framedRectFont.size("Space - instantly drops the tetris piece")
help11Render = framedRectFont.render("Q - quits the game", 1, pygame.Color('white'))
help11Size = framedRectFont.size("Q - quits the game")

# Set words and sizes for game screen
holding1Render = framedRectFont.render('Holding', 1, pygame.Color('white'))
holding1Size = framedRectFont.size('Holding')
holding2Render = framedRectFont.render('Area', 1, pygame.Color('white'))
holding2Size = framedRectFont.size('Area')

score1Render = framedRectFont.render('Score', 1, pygame.Color('white'))
score1Size = framedRectFont.size('Score')
score2Render = framedRectFont.render('Multiplier', 1, pygame.Color('white'))
score2Size = framedRectFont.size('Multiplier')
scoreXRender = framedRectFont1.render('x', 1, pygame.Color('white'))
scoreXSize = framedRectFont1.size('x')

levelRender = framedRectFont.render('Level', 1, pygame.Color('white'))
levelSize = framedRectFont.size('Level')

next1Render = framedRectFont.render('Next 2', 1, pygame.Color('white'))
next1Size = framedRectFont.size('Next 2')
next2Render = framedRectFont.render('Pieces', 1, pygame.Color('white'))
next2Size = framedRectFont.size('Pieces')

            # This section is also used for high score screen and game screen #
scores1Render = framedRectFont.render('High Scores', 1, pygame.Color('white'))
scores1Size = framedRectFont.size('High Scores')
scores2Render = framedRectFont1.render('High Scores', 1, pygame.Color('white'))
scores2Size = framedRectFont1.size('High Scores')
scoreNum1Render = framedRectFont.render('1.', 1, pygame.Color('white'))
scoreNum1Size = framedRectFont.size('1.')
scoreNum1aRender = framedRectFont.render(str(highScores[0]), 1, pygame.Color('white'))
scoreNum1aSize = framedRectFont.size(str(highScores[0]))
scoreNum2Render = framedRectFont.render('2.', 1, pygame.Color('white'))
scoreNum2Size = framedRectFont.size('2.')
scoreNum2aRender = framedRectFont.render(str(highScores[1]), 1, pygame.Color('white'))
scoreNum2aSize = framedRectFont.size(str(highScores[1]))
scoreNum3Render = framedRectFont.render('3.', 1, pygame.Color('white'))
scoreNum3Size = framedRectFont.size('3.')
scoreNum3aRender = framedRectFont.render(str(highScores[2]), 1, pygame.Color('white'))
scoreNum3aSize = framedRectFont.size(str(highScores[2]))
scoreNum4Render = framedRectFont.render('4.', 1, pygame.Color('white'))
scoreNum4Size = framedRectFont.size('4.')
scoreNum4aRender = framedRectFont.render(str(highScores[3]), 1, pygame.Color('white'))
scoreNum4aSize = framedRectFont.size(str(highScores[3]))
scoreNum5Render = framedRectFont.render('5.', 1, pygame.Color('white'))
scoreNum5Size = framedRectFont.size('5.')
scoreNum5aRender = framedRectFont.render(str(highScores[4]), 1, pygame.Color('white'))
scoreNum5aSize = framedRectFont.size(str(highScores[4]))
scoreNum6Render = framedRectFont.render('6.', 1, pygame.Color('white'))
scoreNum6Size = framedRectFont.size('6.')
scoreNum6aRender = framedRectFont.render(str(highScores[5]), 1, pygame.Color('white'))
scoreNum6aSize = framedRectFont.size(str(highScores[5]))
scoreNum7Render = framedRectFont.render('7.', 1, pygame.Color('white'))
scoreNum7Size = framedRectFont.size('7.')
scoreNum7aRender = framedRectFont.render(str(highScores[6]), 1, pygame.Color('white'))
scoreNum7aSize = framedRectFont.size(str(highScores[6]))
scoreNum8Render = framedRectFont.render('8.', 1, pygame.Color('white'))
scoreNum8Size = framedRectFont.size('8.')
scoreNum8aRender = framedRectFont.render(str(highScores[7]), 1, pygame.Color('white'))
scoreNum8aSize = framedRectFont.size(str(highScores[7]))
scoreNum9Render = framedRectFont.render('9.', 1, pygame.Color('white'))
scoreNum9Size = framedRectFont.size('9.')
scoreNum9aRender = framedRectFont.render(str(highScores[8]), 1, pygame.Color('white'))
scoreNum9aSize = framedRectFont.size(str(highScores[8]))
scoreNum10Render = framedRectFont.render('10.', 1, pygame.Color('white'))
scoreNum10Size = framedRectFont.size('10.')
scoreNum10aRender = framedRectFont.render(str(highScores[9]), 1, pygame.Color('white'))
scoreNum10aSize = framedRectFont.size(str(highScores[9]))


score3Render = framedRectFont.render('Current', 1, pygame.Color('white'))
score3Size = framedRectFont.size('Current')
score4Render = framedRectFont.render('Score', 1, pygame.Color('white'))
score4Size = framedRectFont.size('Score')

# Set words and sizes for gameOver screen
gameOverRender = titleFont.render('Game Over!!', 1, pygame.Color('white'))
gameOverSize = titleFont.size('Game Over!!')

# Set words for paused screen
pauseRender = framedRectFont1.render('Paused', 1, pygame.Color('white'))
pauseSize = framedRectFont1.size('Paused')
pause1Render = framedRectFont.render("Press p to resume", 1, pygame.Color('white'))
pause1Size = framedRectFont.size("Press p to resume")

pygame.display.set_caption(title) ## Set the title of the window

# Variables
gameStats = {}

gameStats['x'] = 10
gameStats['y'] = 1
gameStats['rows'] = 24
gameStats['cols'] = 12
gameStats['currentScore'] = 0
gameStats['currentLevel'] = 1
gameStats['nextLevelScore'] = 1000
gameStats['currentMultiplier'] = 1
gameStats['cleared'] = 0
gameStats['combo'] = 0
gameStats['landed'] = False
gameStats['hardDropped'] = False
gameStats['gameOver'] = False
gameStats['toDropTime'] = 500
gameStats['soundPlayed'] = False
gameStats['titleScreen'] = True
gameStats['gameScreen'] = False
gameStats['helpScreen'] = False
gameStats['scoreScreen'] = False
gameStats['gameOverScreen'] = False
gameStats['paused'] = False

bombs = {}

bombs['bombsTotal'] = 0
bombs['toBlowUpTime'] = 30000
bombs['bomb'] = [False, False, False, False, False]
bombs['bombTime'] = [-1, -1, -1, -1, -1] 
bombs['bombLevel'] = [0, 0, 0, 0, 0]
bombs['bombLocation'] = [None, None, None, None, None]
bombs['bombExplosion'] = [False, False, False, False, False]
bombs['bombExplosionLocation'] = [None, None, None, None, None]
bombs['bombExplosionTime'] = [-1, -1, -1, -1, -1]
bombs['bombExplosionToShow'] = 300

pieces = {}

pieces['row'] = 0
pieces['col'] = 5
pieces['rotation'] = 0
pieces['swapped'] = False
pieces['currentPiece'] = TetrisConstants.PIECES[random.randint(0, len(TetrisConstants.PIECES)-1)]
pieces['heldPiece'] = ' '
pieces['nextPiece0'] = TetrisConstants.PIECES[random.randint(0, len(TetrisConstants.PIECES)-1)]
pieces['nextPiece1'] = TetrisConstants.PIECES[random.randint(0, len(TetrisConstants.PIECES)-1)]


gameBoard = []

for i in range(gameStats['rows']):
    gameBoard.append([])
    for j in range(gameStats['cols']):
        gameBoard[i].append(' ')


# Set the repeat rate for holding down keys
pygame.key.set_repeat(100, 100)


# Main game loop
while gameStats['gameOver'] != True:
    startTime = pygame.time.get_ticks() #

    # Get game events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Exit with 'X'
            sys.exit()
        if event.type == pygame.KEYDOWN:
            keypressed = pygame.key.get_pressed()
            if keypressed[pygame.K_LEFT]: # Move left
                if gameStats['gameScreen'] == True:
                    pieces = TetrisMoveFunctions.moveLeft(gameStats, gameBoard, pieces)
            elif keypressed[pygame.K_RIGHT]: # Move right
                if gameStats['gameScreen'] == True:
                    pieces = TetrisMoveFunctions.moveRight(gameStats, gameBoard, pieces)
            elif keypressed[pygame.K_DOWN]: # Move down
                if gameStats['gameScreen'] == True:
                    gameStats, gameBoard, pieces = TetrisMoveFunctions.moveDown(gameStats, gameBoard, pieces)
            elif keypressed[pygame.K_h]: # Go to help screen from title screen
                if gameStats['titleScreen'] == True:
                    gameStats['titleScreen'] = False
                    gameStats['helpScreen'] = True
            elif keypressed[pygame.K_UP]: #Rotate cw
                if gameStats['gameScreen'] == True:
                    pieces = TetrisMoveFunctions.rotateClockWise(gameStats, gameBoard, pieces)
            elif keypressed[pygame.K_s]: # Rotate ccw or go to high score screen
                if gameStats['titleScreen'] == True:
                    gameStats['titleScreen'] = False
                    gameStats['scoreScreen'] = True
                if gameStats['gameScreen'] == True:
                    pieces = TetrisMoveFunctions.rotateCounterClockWise(gameStats, gameBoard, pieces)
            elif keypressed[pygame.K_p]: # Pause
                if gameStats['gameScreen'] == True:
                    if gameStats['paused'] == False:
                        gameStats['paused'] = True
                        pygame.mixer.music.stop()
                    else:
                        gameStats['paused'] = False
                        pygame.mixer.music.play(-1)
            elif keypressed[pygame.K_LSHIFT]: # Hold piece
                if gameStats['gameScreen'] == True:
                    if pieces['swapped'] == False:
                        pieces = TetrisMoveFunctions.switchPiece(pieces)
            elif keypressed[pygame.K_SPACE]: # Hard drop
                if gameStats['gameScreen'] == True:
                    gameStats, gameBoard, pieces = TetrisMoveFunctions.hardDrop(gameStats, gameBoard, pieces)
            elif keypressed[pygame.K_RETURN]: # Switch to game screen from title screen
                if gameStats['titleScreen'] == True:
                    gameStats['titleScreen'] = False
                    gameStats['gameScreen'] = True
                    pygame.mixer.music.play(-1) # Turn on music
                    dropTime = pygame.time.get_ticks() # Get time to check for forced drop
                elif gameStats['helpScreen'] == True:
                    gameStats['helpScreen'] = False
                    gameStats['titleScreen'] = True
                elif gameStats['scoreScreen'] == True:
                    gameStats['scoreScreen'] = False
                    gameStats['titleScreen'] = True
            elif keypressed[pygame.K_q]: # Exit game
                sys.exit()

    # Insert pause feature
    if gameStats['paused'] == False:
        # Play title screen
        if gameStats['titleScreen'] == True:
            TetrisConstants.SURFACE.fill(TetrisConstants.BACKGROUND) ## Draw back color
            TetrisConstants.SURFACE.blit(titleRender, ((TetrisConstants.WIDTH / 2) - (titleSize[0]/2), (TetrisConstants.HEIGHT / 2) - (titleSize[1]/2) - (2 * TetrisConstants.TILESIZE)))
            TetrisConstants.SURFACE.blit(title1Render, ((TetrisConstants.WIDTH / 2) - (title1Size[0]/2), (TetrisConstants.HEIGHT / 2) - (title1Size[1]/2) + (2 * TetrisConstants.TILESIZE)))
            TetrisConstants.SURFACE.blit(title2Render, ((TetrisConstants.WIDTH / 2) - (title2Size[0]/2), (TetrisConstants.HEIGHT / 2) - (title2Size[1]/2) + (3 * TetrisConstants.TILESIZE)))
            TetrisConstants.SURFACE.blit(title3Render, ((TetrisConstants.WIDTH / 2) - (title3Size[0]/2), (TetrisConstants.HEIGHT / 2) - (title3Size[1]/2) + (4 * TetrisConstants.TILESIZE)))
            TetrisConstants.SURFACE.blit(title4Render, ((TetrisConstants.WIDTH / 2) - (title4Size[0]/2), (TetrisConstants.HEIGHT / 2) - (title4Size[1]/2) + (5 * TetrisConstants.TILESIZE)))

        # Play help screen
        if gameStats['helpScreen'] == True:
            TetrisConstants.SURFACE.fill(TetrisConstants.BACKGROUND) ## Draw back color
            TetrisConstants.SURFACE.blit(helpRender, ((TetrisConstants.WIDTH / 2) - (helpSize[0]/2), (TetrisConstants.HEIGHT / 2) - (helpSize[1]/2) - (9 * TetrisConstants.TILESIZE)))
            TetrisConstants.SURFACE.blit(help1Render, ((TetrisConstants.WIDTH / 2) - (help1Size[0]/2), (TetrisConstants.HEIGHT / 2) - (help1Size[1]/2) - (7 * TetrisConstants.TILESIZE)))
            TetrisConstants.SURFACE.blit(help2Render, ((TetrisConstants.WIDTH / 2) - (help2Size[0]/2), (TetrisConstants.HEIGHT / 2) - (help2Size[1]/2) - (6 * TetrisConstants.TILESIZE)))
            TetrisConstants.SURFACE.blit(help3Render, ((TetrisConstants.WIDTH / 2) - (help3Size[0]/2), (TetrisConstants.HEIGHT / 2) - (help3Size[1]/2) - (5 * TetrisConstants.TILESIZE)))
            TetrisConstants.SURFACE.blit(help4Render, ((TetrisConstants.WIDTH / 2) - (help4Size[0]/2), (TetrisConstants.HEIGHT / 2) - (help4Size[1]/2) - (4 * TetrisConstants.TILESIZE)))
            TetrisConstants.SURFACE.blit(help5Render, ((TetrisConstants.WIDTH / 2) - (help5Size[0]/2), (TetrisConstants.HEIGHT / 2) - (help5Size[1]/2) - (3 * TetrisConstants.TILESIZE)))
            TetrisConstants.SURFACE.blit(help6Render, ((TetrisConstants.WIDTH / 2) - (help6Size[0]/2), (TetrisConstants.HEIGHT / 2) - (help6Size[1]/2) - (2 * TetrisConstants.TILESIZE)))
            TetrisConstants.SURFACE.blit(help7Render, ((TetrisConstants.WIDTH / 2) - (help7Size[0]/2), (TetrisConstants.HEIGHT / 2) - (help7Size[1]/2) - (1 * TetrisConstants.TILESIZE)))
            TetrisConstants.SURFACE.blit(help8Render, ((TetrisConstants.WIDTH / 2) - (help8Size[0]/2), (TetrisConstants.HEIGHT / 2) - (help8Size[1]/2) + (0 * TetrisConstants.TILESIZE)))
            TetrisConstants.SURFACE.blit(help9Render, ((TetrisConstants.WIDTH / 2) - (help9Size[0]/2), (TetrisConstants.HEIGHT / 2) - (help9Size[1]/2) + (1 * TetrisConstants.TILESIZE)))
            TetrisConstants.SURFACE.blit(help10Render, ((TetrisConstants.WIDTH / 2) - (help10Size[0]/2), (TetrisConstants.HEIGHT / 2) - (help10Size[1]/2) + (2 * TetrisConstants.TILESIZE)))
            TetrisConstants.SURFACE.blit(help11Render, ((TetrisConstants.WIDTH / 2) - (help11Size[0]/2), (TetrisConstants.HEIGHT / 2) - (help11Size[1]/2) + (3 * TetrisConstants.TILESIZE)))
            TetrisConstants.SURFACE.blit(backToTitleScreenRender, ((TetrisConstants.WIDTH / 2) - (backToTitleScreenSize[0]/2), (TetrisConstants.HEIGHT / 2) - (backToTitleScreenSize[1]/2) + (7 * TetrisConstants.TILESIZE)))
            
        # Play help screen
        if gameStats['scoreScreen'] == True:
            TetrisConstants.SURFACE.fill(TetrisConstants.BACKGROUND) ## Draw back color
            TetrisConstants.SURFACE.blit(scores2Render, ((TetrisConstants.WIDTH / 2) - (scores2Size[0]/2), (TetrisConstants.HEIGHT / 2) - (scores2Size[1]/2) - (9 * TetrisConstants.TILESIZE)))

            TetrisConstants.SURFACE.blit(scoreNum1Render, ((TetrisConstants.WIDTH / 2) - (scoreNum1Size[0]/2) - 2 * TetrisConstants.TILESIZE, (TetrisConstants.HEIGHT / 2) - (scoreNum1Size[1]/2) - (5 * TetrisConstants.TILESIZE)))
            TetrisConstants.SURFACE.blit(scoreNum1aRender, ((TetrisConstants.WIDTH / 2) - TetrisConstants.TILESIZE, (TetrisConstants.HEIGHT / 2) - (scoreNum1aSize[1]/2) - (5 * TetrisConstants.TILESIZE)))

            TetrisConstants.SURFACE.blit(scoreNum2Render, ((TetrisConstants.WIDTH / 2) - (scoreNum2Size[0]/2) - 2 * TetrisConstants.TILESIZE, (TetrisConstants.HEIGHT / 2) - (scoreNum2Size[1]/2) - (4 * TetrisConstants.TILESIZE)))
            TetrisConstants.SURFACE.blit(scoreNum2aRender, ((TetrisConstants.WIDTH / 2) - TetrisConstants.TILESIZE, (TetrisConstants.HEIGHT / 2) - (scoreNum2aSize[1]/2) - (4 * TetrisConstants.TILESIZE)))

            TetrisConstants.SURFACE.blit(scoreNum3Render, ((TetrisConstants.WIDTH / 2) - (scoreNum3Size[0]/2) - 2 * TetrisConstants.TILESIZE, (TetrisConstants.HEIGHT / 2) - (scoreNum3Size[1]/2) - (3 * TetrisConstants.TILESIZE)))
            TetrisConstants.SURFACE.blit(scoreNum3aRender, ((TetrisConstants.WIDTH / 2) - TetrisConstants.TILESIZE, (TetrisConstants.HEIGHT / 2) - (scoreNum3aSize[1]/2) - (3 * TetrisConstants.TILESIZE)))

            TetrisConstants.SURFACE.blit(scoreNum4Render, ((TetrisConstants.WIDTH / 2) - (scoreNum4Size[0]/2) - 2 * TetrisConstants.TILESIZE, (TetrisConstants.HEIGHT / 2) - (scoreNum4Size[1]/2) - (2 * TetrisConstants.TILESIZE)))
            TetrisConstants.SURFACE.blit(scoreNum4aRender, ((TetrisConstants.WIDTH / 2) - TetrisConstants.TILESIZE, (TetrisConstants.HEIGHT / 2) - (scoreNum4aSize[1]/2) - (2 * TetrisConstants.TILESIZE)))

            TetrisConstants.SURFACE.blit(scoreNum5Render, ((TetrisConstants.WIDTH / 2) - (scoreNum5Size[0]/2) - 2 * TetrisConstants.TILESIZE, (TetrisConstants.HEIGHT / 2) - (scoreNum5Size[1]/2) - (1 * TetrisConstants.TILESIZE)))
            TetrisConstants.SURFACE.blit(scoreNum5aRender, ((TetrisConstants.WIDTH / 2) - TetrisConstants.TILESIZE, (TetrisConstants.HEIGHT / 2) - (scoreNum5aSize[1]/2) - (1 * TetrisConstants.TILESIZE)))

            TetrisConstants.SURFACE.blit(scoreNum6Render, ((TetrisConstants.WIDTH / 2) - (scoreNum6Size[0]/2) - 2 * TetrisConstants.TILESIZE, (TetrisConstants.HEIGHT / 2) - (scoreNum6Size[1]/2) + (0 * TetrisConstants.TILESIZE)))
            TetrisConstants.SURFACE.blit(scoreNum6aRender, ((TetrisConstants.WIDTH / 2) - TetrisConstants.TILESIZE, (TetrisConstants.HEIGHT / 2) - (scoreNum6aSize[1]/2) + (0 * TetrisConstants.TILESIZE)))

            TetrisConstants.SURFACE.blit(scoreNum7Render, ((TetrisConstants.WIDTH / 2) - (scoreNum7Size[0]/2) - 2 * TetrisConstants.TILESIZE, (TetrisConstants.HEIGHT / 2) - (scoreNum7Size[1]/2) + (1 * TetrisConstants.TILESIZE)))
            TetrisConstants.SURFACE.blit(scoreNum7aRender, ((TetrisConstants.WIDTH / 2) - TetrisConstants.TILESIZE, (TetrisConstants.HEIGHT / 2) - (scoreNum7aSize[1]/2) + (1 * TetrisConstants.TILESIZE)))

            TetrisConstants.SURFACE.blit(scoreNum8Render, ((TetrisConstants.WIDTH / 2) - (scoreNum8Size[0]/2) - 2 * TetrisConstants.TILESIZE, (TetrisConstants.HEIGHT / 2) - (scoreNum8Size[1]/2) + (2 * TetrisConstants.TILESIZE)))
            TetrisConstants.SURFACE.blit(scoreNum8aRender, ((TetrisConstants.WIDTH / 2) - TetrisConstants.TILESIZE, (TetrisConstants.HEIGHT / 2) - (scoreNum8aSize[1]/2) + (2 * TetrisConstants.TILESIZE)))

            TetrisConstants.SURFACE.blit(scoreNum9Render, ((TetrisConstants.WIDTH / 2) - (scoreNum9Size[0]/2) - 2 * TetrisConstants.TILESIZE, (TetrisConstants.HEIGHT / 2) - (scoreNum9Size[1]/2) + (3 * TetrisConstants.TILESIZE)))
            TetrisConstants.SURFACE.blit(scoreNum9aRender, ((TetrisConstants.WIDTH / 2) - TetrisConstants.TILESIZE, (TetrisConstants.HEIGHT / 2) - (scoreNum9aSize[1]/2) + (3 * TetrisConstants.TILESIZE)))

            TetrisConstants.SURFACE.blit(scoreNum10Render, ((TetrisConstants.WIDTH / 2) - (scoreNum10Size[0]/2) - 2 * TetrisConstants.TILESIZE, (TetrisConstants.HEIGHT / 2) - (scoreNum10Size[1]/2) + (4 * TetrisConstants.TILESIZE)))
            TetrisConstants.SURFACE.blit(scoreNum10aRender, ((TetrisConstants.WIDTH / 2) - TetrisConstants.TILESIZE, (TetrisConstants.HEIGHT / 2) - (scoreNum10aSize[1]/2) + (4 * TetrisConstants.TILESIZE)))


        
        # Play game over screen
        if gameStats['gameOverScreen'] == True:
            TetrisConstants.SURFACE.fill(TetrisConstants.BACKGROUND) ## Draw back color
            TetrisConstants.SURFACE.blit(gameOverRender, ((TetrisConstants.WIDTH / 2) - (gameOverSize[0]/2), (TetrisConstants.HEIGHT / 2) - (titleSize[1]/2) - (2 * TetrisConstants.TILESIZE)))
            pygame.mixer.music.stop()

        # Play game
        if gameStats['gameScreen'] == True:
            currentTime = pygame.time.get_ticks()

            # If time is after determined drop time, force drop
            if currentTime - dropTime >= gameStats['toDropTime']:
                dropTime = pygame.time.get_ticks()
                gameStats, gameBoard, pieces = TetrisMoveFunctions.forcedDrop(gameStats, gameBoard, pieces)
            
            # Play drop sound if piece touches stack/base
            if gameStats['landed'] == True and gameStats['soundPlayed'] == True:
                gameStats['soundPlayed'] = False
                drop.play()

            # Set gameOver to true if gameBoard[0][5] is occupied
            if gameBoard[0][5] != ' ':
                # Add scores to highscore.txt
                highScores.append(gameStats['currentScore'])
                highScores.sort()

                fileScores = open('HighScores.txt', 'w')

                for i in range(len(highScores) - 1, 0, -1):
                    fileScores.write(str(highScores[i]) + '\n')

                fileScores.close()

                # Pause game so they can check board
                pygame.time.delay(10000)
                gameStats['gameScreen'] = False
                gameStats['gameOverScreen'] = True
            
            # Increment level and drop speed as score goes up
            if gameStats['currentScore'] >= gameStats['nextLevelScore']:
                gameStats['currentLevel'] += 1
                gameStats['toDropTime'] -= 25
                gameStats['nextLevelScore'] += gameStats['currentLevel'] * 1000
            

            # Draw framed rectangles
            TetrisConstants.SURFACE.fill(TetrisConstants.BACKGROUND) ## Draw back color
            TetrisDrawFunctions.drawFramedRect(1, 2, 7, 5, TetrisConstants.TILESIZE) ## Draw holding area
            TetrisDrawFunctions.drawFramedRect(2, 10, 5, 6, TetrisConstants.TILESIZE) ## Draw multiplier area
            TetrisDrawFunctions.drawFramedRect(2, 19, 5, 5, TetrisConstants.TILESIZE) ## Draw level area
            TetrisDrawFunctions.drawFramedRect(gameStats['x'], gameStats['y'], gameStats['cols'], gameStats['rows'], TetrisConstants.TILESIZE) ## Draw game area
            TetrisDrawFunctions.drawFramedRect(24, 1, 7, 8, TetrisConstants.TILESIZE) ## Draw next 2 pieces area
            TetrisDrawFunctions.drawFramedRect(24, 11, 7, 6, TetrisConstants.TILESIZE) ## Draw high scores area
            TetrisDrawFunctions.drawFramedRect(24, 20, 7, 5, TetrisConstants.TILESIZE) ## Draw current score area

            # Draw Held Piece
            TetrisDrawFunctions.drawHeldOnBoard(pieces['heldPiece'])
               
            # Draw Next 2 Pieces
            TetrisDrawFunctions.drawNextOnBoard(pieces['nextPiece0'], pieces['nextPiece1'])

            # Draw Game Board
            TetrisDrawFunctions.drawGameBoard(gameStats, gameBoard, TetrisConstants.TILESIZE)

            # Draw Current Piece
            TetrisDrawFunctions.drawCurrentPiece(gameStats, pieces)

            # Set variable texts
            currentScore1Render = framedRectFont1.render(str(gameStats['currentScore']), 1, pygame.Color('white'))
            currentScore1Size = framedRectFont1.size(str(gameStats['currentScore']))

            currentLevel1Render = framedRectFont1.render(str(gameStats['currentLevel']), 1, pygame.Color('white'))
            currentLevel1Size = framedRectFont1.size(str(gameStats['currentLevel']))

            currentMultiplier1Render = framedRectFont1.render(str(gameStats['currentMultiplier']), 1, pygame.Color('white'))
            currentMultiplier1Size = framedRectFont1.size(str(gameStats['currentMultiplier']))

            
            
            # Draw TetrisConstants.SURFACE
            TetrisConstants.SURFACE.blit(holding1Render, ((1 * TetrisConstants.TILESIZE + ((7 * TetrisConstants.TILESIZE) / 2 - holding1Size[0]/2)), 2 * TetrisConstants.TILESIZE))
            TetrisConstants.SURFACE.blit(holding2Render, ((1 * TetrisConstants.TILESIZE + ((7 * TetrisConstants.TILESIZE) / 2 - holding2Size[0]/2)), 6 * TetrisConstants.TILESIZE))

            TetrisConstants.SURFACE.blit(score1Render, ((2 * TetrisConstants.TILESIZE + ((5 * TetrisConstants.TILESIZE) / 2 - score1Size[0]/2)), 10 * TetrisConstants.TILESIZE))
            TetrisConstants.SURFACE.blit(score2Render, ((2 * TetrisConstants.TILESIZE + ((5 * TetrisConstants.TILESIZE) / 2 - score2Size[0]/2)), 11 * TetrisConstants.TILESIZE))
            TetrisConstants.SURFACE.blit(scoreXRender, ((2 * TetrisConstants.TILESIZE + ((2 * TetrisConstants.TILESIZE) / 2 - scoreXSize[0]/2)), 13 * TetrisConstants.TILESIZE))
            TetrisConstants.SURFACE.blit(currentMultiplier1Render, ((3 * TetrisConstants.TILESIZE + ((5 * TetrisConstants.TILESIZE) / 2 - currentMultiplier1Size[0]/2)), 13 * TetrisConstants.TILESIZE))


            TetrisConstants.SURFACE.blit(levelRender, ((2 * TetrisConstants.TILESIZE + ((5 * TetrisConstants.TILESIZE) / 2 - levelSize[0]/2)), 19 * TetrisConstants.TILESIZE))
            TetrisConstants.SURFACE.blit(currentLevel1Render, ((2 * TetrisConstants.TILESIZE + ((5 * TetrisConstants.TILESIZE) / 2 - currentLevel1Size[0]/2)), 21 * TetrisConstants.TILESIZE))
            
            TetrisConstants.SURFACE.blit(next1Render, ((24 * TetrisConstants.TILESIZE + ((7 * TetrisConstants.TILESIZE) / 2 - next1Size[0]/2)), 1 * TetrisConstants.TILESIZE))
            TetrisConstants.SURFACE.blit(next2Render, ((24 * TetrisConstants.TILESIZE + ((7 * TetrisConstants.TILESIZE) / 2 - next2Size[0]/2)), 8 * TetrisConstants.TILESIZE))

            TetrisConstants.SURFACE.blit(scores1Render, ((24 * TetrisConstants.TILESIZE + ((7 * TetrisConstants.TILESIZE) / 2 - scores1Size[0]/2)), 11 * TetrisConstants.TILESIZE))
            TetrisConstants.SURFACE.blit(scoreNum1Render, (24 * TetrisConstants.TILESIZE, 12 * TetrisConstants.TILESIZE))
            TetrisConstants.SURFACE.blit(scoreNum1aRender, (25 * TetrisConstants.TILESIZE, 12 * TetrisConstants.TILESIZE))
            TetrisConstants.SURFACE.blit(scoreNum2Render, (24 * TetrisConstants.TILESIZE, 13 * TetrisConstants.TILESIZE))
            TetrisConstants.SURFACE.blit(scoreNum2aRender, (25 * TetrisConstants.TILESIZE, 13 * TetrisConstants.TILESIZE))
            TetrisConstants.SURFACE.blit(scoreNum3Render, (24 * TetrisConstants.TILESIZE, 14 * TetrisConstants.TILESIZE))
            TetrisConstants.SURFACE.blit(scoreNum3aRender, (25 * TetrisConstants.TILESIZE, 14 * TetrisConstants.TILESIZE))
            TetrisConstants.SURFACE.blit(scoreNum4Render, (24 * TetrisConstants.TILESIZE, 15 * TetrisConstants.TILESIZE))
            TetrisConstants.SURFACE.blit(scoreNum4aRender, (25 * TetrisConstants.TILESIZE, 15 * TetrisConstants.TILESIZE))
            TetrisConstants.SURFACE.blit(scoreNum5Render, (24 * TetrisConstants.TILESIZE, 16 * TetrisConstants.TILESIZE))
            TetrisConstants.SURFACE.blit(scoreNum5aRender, (25 * TetrisConstants.TILESIZE, 16 * TetrisConstants.TILESIZE))

            TetrisConstants.SURFACE.blit(score3Render, ((24 * TetrisConstants.TILESIZE + ((7 * TetrisConstants.TILESIZE) / 2 - score3Size[0]/2)), 20 * TetrisConstants.TILESIZE))
            TetrisConstants.SURFACE.blit(score4Render, ((24 * TetrisConstants.TILESIZE + ((7 * TetrisConstants.TILESIZE) / 2 - score4Size[0]/2)), 21 * TetrisConstants.TILESIZE))
            TetrisConstants.SURFACE.blit(currentScore1Render, ((24 * TetrisConstants.TILESIZE + ((7 * TetrisConstants.TILESIZE) / 2 - currentScore1Size[0]/2)), 23 * TetrisConstants.TILESIZE))

            
            # Increment score if lines are cleared
            if gameStats['cleared'] != 0:
                gameStats['currentScore'] += TetrisFunctions.addScore(gameStats)
                gameStats['currentScore'] = int(gameStats['currentScore'])

                if gameStats['cleared'] == 2:
                    gameStats['currentMultiplier'] -= .5
                elif gameStats['cleared'] == 3:
                    gameStats['currentMultiplier'] -= 1
                elif gameStats['cleared'] == 4:
                    gameStats['currentMultiplier'] -= 2
                
                gameStats['cleared'] = 0

            bombs, gameBoard, bombSound = TetrisFunctions.bombsAway(bombs, gameBoard, gameStats, currentTime, explosions)

            if bombSound == True:
                blowUp.play()
                

        endTime = pygame.time.get_ticks()
        totalTime = endTime - startTime
        timeLeft = int(TetrisConstants.FRAME_RATE - totalTime)
        if timeLeft > 0:
            pygame.time.delay(timeLeft)
    else:
        # Draw paused 
        TetrisConstants.SURFACE.fill(TetrisConstants.BACKGROUND) ## Draw back color
        TetrisConstants.SURFACE.blit(pauseRender, ((TetrisConstants.WIDTH / 2) - (pauseSize[0]/2), (TetrisConstants.HEIGHT / 2) - (pauseSize[1]/2) - (2 * TetrisConstants.TILESIZE)))
        TetrisConstants.SURFACE.blit(pause1Render, ((TetrisConstants.WIDTH / 2) - (pause1Size[0]/2), (TetrisConstants.HEIGHT / 2) - (pause1Size[1]/2) + (2 * TetrisConstants.TILESIZE)))


    pygame.display.flip()


sys.exit()
