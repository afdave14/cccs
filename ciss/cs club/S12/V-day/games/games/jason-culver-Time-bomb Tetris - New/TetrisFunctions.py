import sys, pygame, random

import TetrisConstants

def scanFullRows(gameBoard, gameStats):
    for i in range(gameStats['rows'] - 1, -1, -1):
        full = True
        for j in range(gameStats['cols']):
            if gameBoard[i][j] == ' ':
                full = False
            if full == False:
                break
        
        if full == True:
            gameBoard = dropStack(gameBoard, i, gameStats['cols'])
            gameStats['cleared'] += 1
            gameBoard, gameStats = scanFullRows(gameBoard, gameStats)

    return gameBoard, gameStats




def dropStack(gameBoard, rows, cols):
    for i in range(rows, 0, -1):
        for j in range(cols):
            gameBoard[i][j] = gameBoard[i - 1][j]

    return gameBoard



def addScore(gameStats):
    return 120 * gameStats['currentLevel'] * gameStats['cleared'] * gameStats['currentMultiplier']




def bombsAway(bombs, gameBoard, gameStats, time, explosions):
    boardFilled = []
    bombSound = False

    if random.randint(0, 999) < 9:
        if bombs['bombsTotal'] < 5:
            for i in range(gameStats['rows']):
                for j in range(gameStats['cols']):
                    if gameBoard[i][j] != ' ':
                        if gameBoard[i][j] == '0':
                            pass
                        elif gameBoard[i][j] == '1':
                            pass
                        elif gameBoard[i][j] == '2':
                            pass
                        elif gameBoard[i][j] == '3':
                            pass
                        elif gameBoard[i][j] == '4':
                            pass
                        else:
                            boardFilled.append((i,j))

        if len(boardFilled) != 0:
            rand = random.randint(0, len(boardFilled) - 1) 

            for i in range(5):
                if bombs['bomb'][i] == False:
                    bombs['bomb'][i] = True
                    gameBoard[boardFilled[rand][0]][boardFilled[rand][1]] = str(i)
                    bombs['bombsTotal'] += 1
                    bombs['bombLocation'][i] = boardFilled[rand]
                    bombs['bombTime'][i] = pygame.time.get_ticks()
                    bombs['bombLevel'][i] = gameStats['currentLevel']/8
                    break

    for i in range(gameStats['rows']):
        for j in range(gameStats['cols']):
            if gameBoard[i][j] != ' ':
                if gameBoard[i][j] == '0':
                    bombs['bombLocation'][0] = (i,j)
                elif gameBoard[i][j] == '1':
                    bombs['bombLocation'][1] = (i,j)
                elif gameBoard[i][j] == '2':
                    bombs['bombLocation'][2] = (i,j)
                elif gameBoard[i][j] == '3':
                    bombs['bombLocation'][3] = (i,j)
                elif gameBoard[i][j] == '4':
                    bombs['bombLocation'][4] = (i,j)
    
    for i in range(5):
        if bombs['bomb'][i] == True:
            if gameBoard[bombs['bombLocation'][i][0]][bombs['bombLocation'][i][1]] != str(i):
                bombs['bomb'][i] = False
                bombs['bombsTotal'] -= 1
                bombs['bombLocation'][i] = None 
                bombs['bombTime'][i] = -1
                bombs['bombLevel'][i] = -1

    for i in range(5):
        if bombs['bomb'][i] == True:
            if time - bombs['bombTime'][i] >= bombs['toBlowUpTime']:
                bombs['bomb'][i] = False
                bombs['bombsTotal'] -= 1
                if bombs['bombLevel'][i] == 0:
                    gameBoard[bombs['bombLocation'][i][0]][bombs['bombLocation'][i][1]] = ' '
                elif bombs['bombLevel'][i] == 1:
                    selectBombBlast = random.randint(0,1)
                    if selectBombBlast == 0:
                        if bombs['bombLocation'][i][0] - 1 >= 0:
                            gameBoard[bombs['bombLocation'][i][0] - 1][bombs['bombLocation'][i][1]] = ' '
                        if bombs['bombLocation'][i][1] - 1 >= 0:
                            gameBoard[bombs['bombLocation'][i][0]][bombs['bombLocation'][i][1] - 1] = ' '
                        gameBoard[bombs['bombLocation'][i][0]][bombs['bombLocation'][i][1]] = ' '
                        if bombs['bombLocation'][i][0] + 1 < gameStats['rows'] - 1:
                            gameBoard[bombs['bombLocation'][i][0] + 1][bombs['bombLocation'][i][1]] = ' '
                        if bombs['bombLocation'][i][1] + 1 < gameStats['cols'] - 1:
                            gameBoard[bombs['bombLocation'][i][0]][bombs['bombLocation'][i][1] + 1] = ' '
                    elif selectBombBlast == 1:
                        if bombs['bombLocation'][i][0] - 1 >= 0 and bombs['bombLocation'][i][1] - 1 >= 0:
                            gameBoard[bombs['bombLocation'][i][0] - 1][bombs['bombLocation'][i][1] - 1] = ' '
                        if bombs['bombLocation'][i][0] - 1 >= 0 and bombs['bombLocation'][i][1] + 1 < gameStats['cols'] - 1:
                            gameBoard[bombs['bombLocation'][i][0] - 1][bombs['bombLocation'][i][1] + 1] = ' '
                        gameBoard[bombs['bombLocation'][i][0]][bombs['bombLocation'][i][1]] = ' '
                        if bombs['bombLocation'][i][1] - 1 >= 0 and bombs['bombLocation'][i][0] + 1 < gameStats['rows'] - 1:
                            gameBoard[bombs['bombLocation'][i][0] + 1][bombs['bombLocation'][i][1] - 1] = ' '
                        if bombs['bombLocation'][i][0] + 1 < gameStats['rows'] - 1 and bombs['bombLocation'][i][1] + 1 < gameStats['cols'] - 1:
                            gameBoard[bombs['bombLocation'][i][0] + 1][bombs['bombLocation'][i][1] + 1] = ' '
                elif bombs['bombLevel'][i] == 2:
                    selectBombBlast = random.randint(0,1)
                    if selectBombBlast == 0:
                        if bombs['bombLocation'][i][0] - 2 >= 0:
                            gameBoard[bombs['bombLocation'][i][0] - 2][bombs['bombLocation'][i][1]] = ' '
                        if bombs['bombLocation'][i][0] - 1 >= 0:
                            gameBoard[bombs['bombLocation'][i][0] - 1][bombs['bombLocation'][i][1]] = ' '
                        if bombs['bombLocation'][i][1] - 2 >= 0:
                            gameBoard[bombs['bombLocation'][i][0]][bombs['bombLocation'][i][1] - 2] = ' '
                        if bombs['bombLocation'][i][1] - 1 >= 0:
                            gameBoard[bombs['bombLocation'][i][0]][bombs['bombLocation'][i][1] - 1] = ' '
                        gameBoard[bombs['bombLocation'][i][0]][bombs['bombLocation'][i][1]] = ' '
                        if bombs['bombLocation'][i][0] + 1 < gameStats['rows'] - 1:
                            gameBoard[bombs['bombLocation'][i][0] + 1][bombs['bombLocation'][i][1]] = ' '
                        if bombs['bombLocation'][i][0] + 2 < gameStats['rows'] - 1:
                            gameBoard[bombs['bombLocation'][i][0] + 2][bombs['bombLocation'][i][1]] = ' '
                        if bombs['bombLocation'][i][1] + 1 < gameStats['cols'] - 1:
                            gameBoard[bombs['bombLocation'][i][0]][bombs['bombLocation'][i][1] + 1] = ' '
                        if bombs['bombLocation'][i][1] + 2 < gameStats['cols'] - 1:
                            gameBoard[bombs['bombLocation'][i][0]][bombs['bombLocation'][i][1] + 2] = ' '
                    elif selectBombBlast == 1:
                        if bombs['bombLocation'][i][0] - 2 >= 0 and bombs['bombLocation'][i][1] - 2 >= 0:
                            gameBoard[bombs['bombLocation'][i][0] - 2][bombs['bombLocation'][i][1] - 2] = ' '
                        if bombs['bombLocation'][i][0] - 1 >= 0 and bombs['bombLocation'][i][1] - 1 >= 0:
                            gameBoard[bombs['bombLocation'][i][0] - 1][bombs['bombLocation'][i][1] - 1] = ' '
                        if bombs['bombLocation'][i][0] - 2 >= 0 and bombs['bombLocation'][i][1] + 2 < gameStats['cols'] - 1:
                            gameBoard[bombs['bombLocation'][i][0] - 2][bombs['bombLocation'][i][1] + 2] = ' '
                        if bombs['bombLocation'][i][0] - 1 >= 0 and bombs['bombLocation'][i][1] + 1 < gameStats['cols'] - 1:
                            gameBoard[bombs['bombLocation'][i][0] - 1][bombs['bombLocation'][i][1] + 1] = ' '
                        gameBoard[bombs['bombLocation'][i][0]][bombs['bombLocation'][i][1]] = ' '
                        if bombs['bombLocation'][i][1] - 1 >= 0 and bombs['bombLocation'][i][0] + 1 < gameStats['rows'] - 1:
                            gameBoard[bombs['bombLocation'][i][0] + 1][bombs['bombLocation'][i][1] - 1] = ' '
                        if bombs['bombLocation'][i][1] - 2 >= 0 and bombs['bombLocation'][i][0] + 2 < gameStats['rows'] - 1:
                            gameBoard[bombs['bombLocation'][i][0] + 2][bombs['bombLocation'][i][1] - 2] = ' '
                        if bombs['bombLocation'][i][0] + 1 < gameStats['rows'] - 1 and bombs['bombLocation'][i][1] + 1 < gameStats['cols'] - 1:
                            gameBoard[bombs['bombLocation'][i][0] + 1][bombs['bombLocation'][i][1] + 1] = ' '
                        if bombs['bombLocation'][i][0] + 2 < gameStats['rows'] - 1 and bombs['bombLocation'][i][1] + 2 < gameStats['cols'] - 1:
                            gameBoard[bombs['bombLocation'][i][0] + 2][bombs['bombLocation'][i][1] + 2] = ' '
                
                bombs['bombExplosionLocation'][i] = bombs['bombLocation'][i]
                bombs['bombExplosion'][i] = True
                bombs['bombExplosionTime'][i] = pygame.time.get_ticks()
                bombs['bombLocation'][i] = None 
                bombs['bombTime'][i] = -1
                bombSound = True

    for i in range(5):
        if bombs['bombExplosion'][i] == True:
            if time - bombs['bombExplosionTime'][i] <= bombs['bombExplosionToShow']:
                if bombs['bombLevel'][i] == 0:
                    TetrisConstants.SURFACE.blit(explosions[0], (gameStats['x'] * TetrisConstants.TILESIZE + (bombs['bombExplosionLocation'][i][1] * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2 - explosions[0].get_width()/2), gameStats['y'] + 1 * TetrisConstants.TILESIZE + (bombs['bombExplosionLocation'][i][0] * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2 - explosions[0].get_height()/2)))
                elif bombs['bombLevel'][i] == 1:
                    TetrisConstants.SURFACE.blit(explosions[1], (gameStats['x'] * TetrisConstants.TILESIZE + (bombs['bombExplosionLocation'][i][1] * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2 - explosions[1].get_width()/2), gameStats['y'] + 1 * TetrisConstants.TILESIZE + (bombs['bombExplosionLocation'][i][0] * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2 - explosions[1].get_height()/2)))
                elif bombs['bombLevel'][i] == 2:
                    TetrisConstants.SURFACE.blit(explosions[2], (gameStats['x'] * TetrisConstants.TILESIZE + (bombs['bombExplosionLocation'][i][1] * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2 - explosions[2].get_width()/2), gameStats['y'] + 1 * TetrisConstants.TILESIZE + (bombs['bombExplosionLocation'][i][0] * TetrisConstants.TILESIZE + TetrisConstants.TILESIZE/2 - explosions[2].get_height()/2)))
                
                
    return bombs, gameBoard, bombSound



    
