import sys, pygame

import TetrisConstants




def drawFramedRect(x, y, w, h, tileSize):
    #Draw circles at corners of rect (4 slight bigger than 4 inner)
    pygame.draw.circle(TetrisConstants.SURFACE, TetrisConstants.RECTOUTERBORDER, (x * tileSize ,y * tileSize), tileSize/2+3)
    pygame.draw.circle(TetrisConstants.SURFACE, TetrisConstants.RECTOUTERBORDER, (x * tileSize + w * tileSize + 2, y * tileSize), tileSize/2+3)
    pygame.draw.circle(TetrisConstants.SURFACE, TetrisConstants.RECTOUTERBORDER, (x * tileSize, y * tileSize + h * tileSize + 2), tileSize/2+3)
    pygame.draw.circle(TetrisConstants.SURFACE, TetrisConstants.RECTOUTERBORDER, (x * tileSize + w * tileSize + 2, y * tileSize + h * tileSize + 2), tileSize/2+3)
    pygame.draw.circle(TetrisConstants.SURFACE, TetrisConstants.RECTINNERBORDER, (x * tileSize ,y * tileSize), tileSize/2-1)
    pygame.draw.circle(TetrisConstants.SURFACE, TetrisConstants.RECTINNERBORDER, (x * tileSize + w * tileSize + 2, y * tileSize), tileSize/2-1)
    pygame.draw.circle(TetrisConstants.SURFACE, TetrisConstants.RECTINNERBORDER, (x * tileSize, y * tileSize + h * tileSize + 2), tileSize/2-1)
    pygame.draw.circle(TetrisConstants.SURFACE, TetrisConstants.RECTINNERBORDER, (x * tileSize + w * tileSize + 2, y * tileSize + h * tileSize + 2), tileSize/2-1)
    
    #Draw thick lines around the rect (4)
    pygame.draw.line(TetrisConstants.SURFACE, TetrisConstants.RECTOUTERBORDER, (x * tileSize - tileSize/4, y * tileSize), (x * tileSize - tileSize/4, y * tileSize + h * tileSize), tileSize/2+8)
    pygame.draw.line(TetrisConstants.SURFACE, TetrisConstants.RECTOUTERBORDER, (x * tileSize + w * tileSize + tileSize/4, y * tileSize), (x * tileSize + w * tileSize + tileSize/4, y * tileSize + h * tileSize), tileSize/2+8)
    pygame.draw.line(TetrisConstants.SURFACE, TetrisConstants.RECTOUTERBORDER, (x * tileSize, y * tileSize - tileSize/4), (x * tileSize + w * tileSize, y * tileSize - tileSize/4), tileSize/2+8)
    pygame.draw.line(TetrisConstants.SURFACE, TetrisConstants.RECTOUTERBORDER, (x * tileSize, y * tileSize + h * tileSize + tileSize/4), (x * tileSize + w * tileSize, y * tileSize + h * tileSize + tileSize/4), tileSize/2+8)
    pygame.draw.line(TetrisConstants.SURFACE, TetrisConstants.RECTINNERBORDER, (x * tileSize - tileSize/4, y * tileSize), (x * tileSize - tileSize/4, y * tileSize + h * tileSize), tileSize/2)
    pygame.draw.line(TetrisConstants.SURFACE, TetrisConstants.RECTINNERBORDER, (x * tileSize + w * tileSize + tileSize/4, y * tileSize), (x * tileSize + w * tileSize + tileSize/4, y * tileSize + h * tileSize), tileSize/2)
    pygame.draw.line(TetrisConstants.SURFACE, TetrisConstants.RECTINNERBORDER, (x * tileSize, y * tileSize - tileSize/4), (x * tileSize + w * tileSize, y * tileSize - tileSize/4), tileSize/2)
    pygame.draw.line(TetrisConstants.SURFACE, TetrisConstants.RECTINNERBORDER, (x * tileSize, y * tileSize + h * tileSize + tileSize/4), (x * tileSize + w * tileSize, y * tileSize + h * tileSize + tileSize/4), tileSize/2)
    
    #Draw the rect
    GameRect = pygame.Rect(x * tileSize - 1, y * tileSize - 1, w * tileSize + 3, h * tileSize + 3)
    pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.GAMEBACKGROUND, GameRect)




def drawGameBoard(gameStats, gameBoard, tileSize):

    for i in range(gameStats['rows']):
        for j in range(gameStats['cols']):
            if gameBoard[i][j] == 'i':
                pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.CYAN, (gameStats['x'] * tileSize + j * tileSize, gameStats['y'] + 1 * tileSize + i * tileSize, tileSize, tileSize))
                pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (gameStats['x'] * tileSize + j * tileSize, gameStats['y'] + 1 * tileSize + i * tileSize, tileSize, tileSize), 1)
            elif gameBoard[i][j] == 'j':
                pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.BLUE, (gameStats['x'] * tileSize + j * tileSize, gameStats['y'] + 1 * tileSize + i * tileSize, tileSize, tileSize))
                pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (gameStats['x'] * tileSize + j * tileSize, gameStats['y'] + 1 * tileSize + i * tileSize, tileSize, tileSize), 1)
            elif gameBoard[i][j] == 'l':
                pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.ORANGE, (gameStats['x'] * tileSize + j * tileSize, gameStats['y'] + 1 * tileSize + i * tileSize, tileSize, tileSize))
                pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (gameStats['x'] * tileSize + j * tileSize, gameStats['y'] + 1 * tileSize + i * tileSize, tileSize, tileSize), 1)
            elif gameBoard[i][j] == 'o':
                pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.YELLOW, (gameStats['x'] * tileSize + j * tileSize, gameStats['y'] + 1 * tileSize + i * tileSize, tileSize, tileSize))
                pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (gameStats['x'] * tileSize + j * tileSize, gameStats['y'] + 1 * tileSize + i * tileSize, tileSize, tileSize), 1)
            elif gameBoard[i][j] == 's':
                pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.GREEN, (gameStats['x'] * tileSize + j * tileSize, gameStats['y'] + 1 * tileSize + i * tileSize, tileSize, tileSize))
                pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (gameStats['x'] * tileSize + j * tileSize, gameStats['y'] + 1 * tileSize + i * tileSize, tileSize, tileSize), 1)
            elif gameBoard[i][j] == 't':
                pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.PURPLE, (gameStats['x'] * tileSize + j * tileSize, gameStats['y'] + 1 * tileSize + i * tileSize, tileSize, tileSize))
                pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (gameStats['x'] * tileSize + j * tileSize, gameStats['y'] + 1 * tileSize + i * tileSize, tileSize, tileSize), 1)
            elif gameBoard[i][j] == 'z':
                pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.RED, (gameStats['x'] * tileSize + j * tileSize, gameStats['y'] + 1 * tileSize + i * tileSize, tileSize, tileSize))
                pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (gameStats['x'] * tileSize + j * tileSize, gameStats['y'] + 1 * tileSize + i * tileSize, tileSize, tileSize), 1)
            elif gameBoard[i][j] == '0' or gameBoard[i][j] == '1' or gameBoard[i][j] == '2' or gameBoard[i][j] == '3' or gameBoard[i][j] == '4':
                pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.pygame.Color('grey'), (gameStats['x'] * tileSize + j * tileSize, gameStats['y'] + 1 * tileSize + i * tileSize, tileSize, tileSize))
                pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (gameStats['x'] * tileSize + j * tileSize, gameStats['y'] + 1 * tileSize + i * tileSize, tileSize, tileSize), 1)
            



def drawCurrentPiece(gameStats, currentPiece, tileSize = TetrisConstants.TILESIZE):
    if currentPiece['currentPiece'] == 'I':
        drawI(gameStats['x'] * tileSize + currentPiece['col'] * tileSize, gameStats['y'] + 1 * tileSize + currentPiece['row'] * tileSize, currentPiece['rotation'])
    elif currentPiece['currentPiece'] == 'J':
        drawJ(gameStats['x'] * tileSize + currentPiece['col'] * tileSize, gameStats['y'] + 1 * tileSize + currentPiece['row'] * tileSize, currentPiece['rotation'])
    elif currentPiece['currentPiece'] == 'L':
        drawL(gameStats['x'] * tileSize + currentPiece['col'] * tileSize, gameStats['y'] + 1 * tileSize + currentPiece['row'] * tileSize, currentPiece['rotation'])
    elif currentPiece['currentPiece'] == 'O':
        drawO(gameStats['x'] * tileSize + currentPiece['col'] * tileSize, gameStats['y'] + 1 * tileSize + currentPiece['row'] * tileSize, currentPiece['rotation'])
    elif currentPiece['currentPiece'] == 'S':
        drawS(gameStats['x'] * tileSize + currentPiece['col'] * tileSize, gameStats['y'] + 1 * tileSize + currentPiece['row'] * tileSize, currentPiece['rotation'])
    elif currentPiece['currentPiece'] == 'T':
        drawT(gameStats['x'] * tileSize + currentPiece['col'] * tileSize, gameStats['y'] + 1 * tileSize + currentPiece['row'] * tileSize, currentPiece['rotation'])
    elif currentPiece['currentPiece'] == 'Z':
        drawZ(gameStats['x'] * tileSize + currentPiece['col'] * tileSize, gameStats['y'] + 1 * tileSize + currentPiece['row'] * tileSize, currentPiece['rotation'])




def drawI(x, y, pos, tileSize = TetrisConstants.TILESIZE): # I
    if pos == 0:
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.CYAN, (x, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y, tileSize, tileSize),1)
        
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.CYAN, (x - tileSize, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize, y, tileSize, tileSize),1)
            
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.CYAN, (x + tileSize, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize, y, tileSize, tileSize),1)
        
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.CYAN, (x + 2 * tileSize, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + 2 * tileSize, y, tileSize, tileSize),1)
    elif pos == 1:
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.CYAN, (x, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y, tileSize, tileSize),1)
        
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.CYAN, (x, y - tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y - tileSize, tileSize, tileSize),1)
            
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.CYAN, (x, y + tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y + tileSize, tileSize, tileSize),1)
        
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.CYAN, (x, y + 2 * tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y + 2 * tileSize, tileSize, tileSize),1)
    elif pos == 2:
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.CYAN, (x, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y, tileSize, tileSize),1)
        
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.CYAN, (x - tileSize, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize, y, tileSize, tileSize),1)
            
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.CYAN, (x + tileSize, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize, y, tileSize, tileSize),1)
        
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.CYAN, (x - 2 * tileSize, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - 2 * tileSize, y, tileSize, tileSize),1)
    elif pos == 3:
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.CYAN, (x, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y, tileSize, tileSize),1)
        
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.CYAN, (x, y - tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y - tileSize, tileSize, tileSize),1)
            
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.CYAN, (x, y + tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y + tileSize, tileSize, tileSize),1)
        
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.CYAN, (x, y - 2 * tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y - 2 * tileSize, tileSize, tileSize),1)
    



def drawJ(x, y, pos, tileSize = TetrisConstants.TILESIZE): # J
    if pos == 0:
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.BLUE, (x, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.BLUE, (x - tileSize, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.BLUE, (x + tileSize, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.BLUE, (x + tileSize, y + tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize, y + tileSize, tileSize, tileSize),1)
    elif pos == 1:
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.BLUE, (x, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.BLUE, (x, y - tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y - tileSize, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.BLUE, (x, y + tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y + tileSize, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.BLUE, (x - tileSize, y + tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize, y + tileSize, tileSize, tileSize),1)
    elif pos == 2:
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.BLUE, (x, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.BLUE, (x - tileSize, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.BLUE, (x + tileSize, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.BLUE, (x - tileSize, y - tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize, y - tileSize, tileSize, tileSize),1)
    elif pos == 3:
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.BLUE, (x, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.BLUE, (x, y - tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y - tileSize, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.BLUE, (x, y + tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y + tileSize, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.BLUE, (x + tileSize, y - tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize, y - tileSize, tileSize, tileSize),1)
        



def drawL(x, y, pos, tileSize = TetrisConstants.TILESIZE): # L
    if pos == 0:
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.ORANGE, (x, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.ORANGE, (x - tileSize, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.ORANGE, (x + tileSize, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.ORANGE, (x - tileSize, y + tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize, y + tileSize, tileSize, tileSize),1)
    elif pos == 1:
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.ORANGE, (x, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.ORANGE, (x, y - tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y - tileSize, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.ORANGE, (x, y + tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y + tileSize, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.ORANGE, (x - tileSize, y - tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize, y - tileSize, tileSize, tileSize),1)
    elif pos == 2:
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.ORANGE, (x, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.ORANGE, (x - tileSize, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.ORANGE, (x + tileSize, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.ORANGE, (x + tileSize, y - tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize, y - tileSize, tileSize, tileSize),1)
    elif pos == 3:
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.ORANGE, (x, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.ORANGE, (x, y - tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y - tileSize, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.ORANGE, (x, y + tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y + tileSize, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.ORANGE, (x + tileSize, y + tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize, y + tileSize, tileSize, tileSize),1)




def drawO(x, y, pos, tileSize = TetrisConstants.TILESIZE): # O
    if pos == 0:
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.YELLOW, (x, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.YELLOW, (x + tileSize, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.YELLOW, (x, y + tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y + tileSize, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.YELLOW, (x + tileSize, y + tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize, y + tileSize, tileSize, tileSize),1)
    elif pos == 1:
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.YELLOW, (x, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.YELLOW, (x + tileSize, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.YELLOW, (x, y + tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y + tileSize, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.YELLOW, (x + tileSize, y + tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize, y + tileSize, tileSize, tileSize),1)
    elif pos == 2:
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.YELLOW, (x, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.YELLOW, (x + tileSize, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.YELLOW, (x, y + tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y + tileSize, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.YELLOW, (x + tileSize, y + tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize, y + tileSize, tileSize, tileSize),1)
    elif pos == 3:
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.YELLOW, (x, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.YELLOW, (x + tileSize, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.YELLOW, (x, y + tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y + tileSize, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.YELLOW, (x + tileSize, y + tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize, y + tileSize, tileSize, tileSize),1)



    
def drawS(x, y, pos, tileSize = TetrisConstants.TILESIZE): # S
    if pos == 0:
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.GREEN, (x, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.GREEN, (x + tileSize, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.GREEN, (x - tileSize, y + tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize, y + tileSize, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.GREEN, (x, y + tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y + tileSize, tileSize, tileSize),1)
    elif pos == 1:
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.GREEN, (x, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.GREEN, (x, y + tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y + tileSize, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.GREEN, (x - tileSize, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.GREEN, (x - tileSize, y - tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize, y - tileSize, tileSize, tileSize),1)
    elif pos == 2:
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.GREEN, (x, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.GREEN, (x - tileSize, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.GREEN, (x, y - tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y - tileSize, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.GREEN, (x + tileSize, y - tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize, y - tileSize, tileSize, tileSize),1)
    elif pos == 3:
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.GREEN, (x, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.GREEN, (x, y - tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y - tileSize, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.GREEN, (x + tileSize, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.GREEN, (x + tileSize, y + tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize, y + tileSize, tileSize, tileSize),1)




def drawT(x, y, pos, tileSize = TetrisConstants.TILESIZE): # T 
    if pos == 0:
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.PURPLE, (x, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.PURPLE, (x - tileSize, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.PURPLE, (x + tileSize, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.PURPLE, (x, y + tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y + tileSize, tileSize, tileSize),1)
    elif pos == 1:
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.PURPLE, (x, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.PURPLE, (x, y - tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y - tileSize, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.PURPLE, (x - tileSize, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.PURPLE, (x, y + tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y + tileSize, tileSize, tileSize),1)
    elif pos == 2:
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.PURPLE, (x, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.PURPLE, (x + tileSize, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.PURPLE, (x, y - tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y - tileSize, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.PURPLE, (x - tileSize, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize, y, tileSize, tileSize),1)
    elif pos == 3:
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.PURPLE, (x, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.PURPLE, (x, y + tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y + tileSize, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.PURPLE, (x + tileSize, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize, y, tileSize, tileSize),1)
        
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.PURPLE, (x, y - tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y - tileSize, tileSize, tileSize),1)




def drawZ(x, y, pos, tileSize = TetrisConstants.TILESIZE): # Z 
    if pos == 0:
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.RED, (x, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.RED, (x - tileSize, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.RED, (x + tileSize, y + tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize, y + tileSize, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.RED, (x, y + tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y + tileSize, tileSize, tileSize),1)
    elif pos == 1:
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.RED, (x, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.RED, (x, y - tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y - tileSize, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.RED, (x - tileSize, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.RED, (x - tileSize, y + tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize, y + tileSize, tileSize, tileSize),1)
    elif pos == 2:
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.RED, (x, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.RED, (x + tileSize, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.RED, (x, y - tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y - tileSize, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.RED, (x - tileSize, y - tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize, y - tileSize, tileSize, tileSize),1)
    elif pos == 3:
        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.RED, (x, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.RED, (x, y + tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y + tileSize, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.RED, (x + tileSize, y, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize, y, tileSize, tileSize),1)

        pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.RED, (x + tileSize, y - tileSize, tileSize, tileSize))
        pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize, y - tileSize, tileSize, tileSize),1)



    
def drawHeldOnBoard(heldPiece):
    if heldPiece == 'L':
        drawLonBoard(4 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2, 4 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2)
    elif heldPiece == 'J':
        drawJonBoard(4 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2, 4 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2)
    elif heldPiece == 'S':
        drawSonBoard(4 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2, 4 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2)
    elif heldPiece =='Z':
        drawZonBoard(4 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2, 4 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2)
    elif heldPiece =='O':
        drawOonBoard(4 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2, 4 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2)
    elif heldPiece =='I':
        drawIonBoard(4 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2, 4 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2)
    elif heldPiece =='T':
        drawTonBoard(4 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2, 4 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2)
     



def drawNextOnBoard(nextPiece0, nextPiece1):
    if nextPiece0 == 'L':
        drawLonBoard(27 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2, 3 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2)
    elif nextPiece0 == 'J':
        drawJonBoard(27 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2, 3 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2)
    elif nextPiece0 == 'S':
        drawSonBoard(27 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2, 3 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2)
    elif nextPiece0 =='Z':
        drawZonBoard(27 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2, 3 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2)
    elif nextPiece0 =='O':
        drawOonBoard(27 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2, 3 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2)
    elif nextPiece0 =='I':
        drawIonBoard(27 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2, 3 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2)
    elif nextPiece0 =='T':
        drawTonBoard(27 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2, 3 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2)

    if nextPiece1 == 'L':
        drawLonBoard(27 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2, 6 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2)
    elif nextPiece1 == 'J':
        drawJonBoard(27 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2, 6 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2)
    elif nextPiece1 == 'S':
        drawSonBoard(27 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2, 6 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2)
    elif nextPiece1 =='Z':
        drawZonBoard(27 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2, 6 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2)
    elif nextPiece1 =='O':
        drawOonBoard(27 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2, 6 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2)
    elif nextPiece1 =='I':
        drawIonBoard(27 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2, 6 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2)
    elif nextPiece1 =='T':
        drawTonBoard(27 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2, 6 * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2)



    
def drawIonBoard(x, y, pos = 'I0', tileSize = TetrisConstants.TILESIZE): # I

    pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.CYAN, (x - 2*tileSize, y - tileSize/2, tileSize, tileSize))
    pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - 2*tileSize, y - tileSize/2, tileSize, tileSize),1)
        
    pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.CYAN, (x - tileSize, y - tileSize/2, tileSize, tileSize))
    pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize, y - tileSize/2, tileSize, tileSize),1)
            
    pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.CYAN, (x, y - tileSize/2, tileSize, tileSize))
    pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y - tileSize/2, tileSize, tileSize),1)
        
    pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.CYAN, (x + tileSize, y - tileSize/2, tileSize, tileSize))
    pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize, y - tileSize/2, tileSize, tileSize),1)
    



def drawJonBoard(x, y, pos = 'J0', tileSize = TetrisConstants.TILESIZE): # J
    pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.BLUE, (x - tileSize - tileSize/2, y - tileSize, tileSize, tileSize))
    pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize - tileSize/2, y - tileSize, tileSize, tileSize),1)

    pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.BLUE, (x - tileSize/2, y - tileSize, tileSize, tileSize))
    pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize/2, y - tileSize, tileSize, tileSize),1)

    pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.BLUE, (x + tileSize/2, y - tileSize, tileSize, tileSize))
    pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize/2, y - tileSize, tileSize, tileSize),1)

    pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.BLUE, (x + tileSize/2, y, tileSize, tileSize))
    pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize/2, y, tileSize, tileSize),1)      
    



def drawLonBoard(x, y, pos = 'L0', tileSize = TetrisConstants.TILESIZE): # L
    pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.ORANGE, (x - tileSize - tileSize/2, y - tileSize, tileSize, tileSize))
    pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize - tileSize/2, y - tileSize, tileSize, tileSize),1)

    pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.ORANGE, (x - tileSize/2, y - tileSize, tileSize, tileSize))
    pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize/2, y - tileSize, tileSize, tileSize),1)

    pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.ORANGE, (x + tileSize/2, y - tileSize, tileSize, tileSize))
    pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize/2, y - tileSize, tileSize, tileSize),1)

    pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.ORANGE, (x - tileSize - tileSize/2, y, tileSize, tileSize))
    pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize - tileSize/2, y, tileSize, tileSize),1)
    



def drawOonBoard(x, y, pos = 'O0', tileSize = TetrisConstants.TILESIZE): # O
    pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.YELLOW, (x - tileSize, y - tileSize, tileSize, tileSize))
    pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize, y - tileSize, tileSize, tileSize),1)

    pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.YELLOW, (x - tileSize, y, tileSize, tileSize))
    pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize, y, tileSize, tileSize),1)

    pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.YELLOW, (x, y - tileSize, tileSize, tileSize))
    pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y - tileSize, tileSize, tileSize),1)

    pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.YELLOW, (x, y, tileSize, tileSize))
    pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x, y, tileSize, tileSize),1)



    
def drawSonBoard(x, y, pos = 'S0', tileSize = TetrisConstants.TILESIZE): # S
    pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.GREEN, (x - tileSize - tileSize/2, y, tileSize, tileSize))
    pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize - tileSize/2, y, tileSize, tileSize),1)

    pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.GREEN, (x - tileSize/2, y - tileSize, tileSize, tileSize))
    pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize/2, y - tileSize, tileSize, tileSize),1)

    pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.GREEN, (x - tileSize/2, y, tileSize, tileSize))
    pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize/2, y, tileSize, tileSize),1)

    pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.GREEN, (x + tileSize/2, y - tileSize, tileSize, tileSize))
    pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize/2, y - tileSize, tileSize, tileSize),1)




def drawTonBoard(x, y, pos = 'T0', tileSize = TetrisConstants.TILESIZE): # T 
    pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.PURPLE, (x - tileSize - tileSize/2, y - tileSize, tileSize, tileSize))
    pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize - tileSize/2, y - tileSize, tileSize, tileSize),1)

    pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.PURPLE, (x - tileSize/2, y - tileSize, tileSize, tileSize))
    pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize/2, y - tileSize, tileSize, tileSize),1)

    pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.PURPLE, (x - tileSize/2, y, tileSize, tileSize))
    pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize/2, y, tileSize, tileSize),1)

    pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.PURPLE, (x + tileSize/2, y - tileSize, tileSize, tileSize))
    pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize/2, y - tileSize, tileSize, tileSize),1)




def drawZonBoard(x, y, pos = 'Z0', tileSize = TetrisConstants.TILESIZE): # Z 
    pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.RED, (x - tileSize - tileSize/2, y - tileSize, tileSize, tileSize))
    pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize - tileSize/2, y - tileSize, tileSize, tileSize),1)

    pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.RED, (x - tileSize/2, y - tileSize, tileSize, tileSize))
    pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize/2, y - tileSize, tileSize, tileSize),1)

    pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.RED, (x - tileSize/2, y, tileSize, tileSize))
    pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x - tileSize/2, y, tileSize, tileSize),1)

    pygame.draw.rect(TetrisConstants.SURFACE, TetrisConstants.RED, (x + tileSize/2, y, tileSize, tileSize))
    pygame.draw.rect(TetrisConstants.SURFACE, pygame.Color('white'), (x + tileSize/2, y, tileSize, tileSize),1)



    

