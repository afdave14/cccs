import sys, pygame, random

import TetrisConstants, TetrisFunctions



def switchPiece(pieces):
    pieces['swapped'] = True
    if pieces['heldPiece'] == ' ':
        pieces['heldPiece'] = pieces['currentPiece']
        pieceDown(pieces)
    else:
        pieces['row'] = 0
        pieces['col'] = 5
        pieces['rotation'] = 0
        switchPiece = pieces['heldPiece'] 
        pieces['heldPiece'] = pieces['currentPiece']
        pieces['currentPiece'] = switchPiece

    return pieces

def pieceDown(pieces):
    pieces['row'] = 0
    pieces['col'] = 5
    pieces['rotation'] = 0
    pieces['currentPiece'] = pieces['nextPiece0']
    pieces['nextPiece0'] = pieces['nextPiece1']
    pieces['nextPiece1'] = TetrisConstants.PIECES[random.randint(0, len(TetrisConstants.PIECES)-1)]

    return pieces


def hardDrop(gameStats, gameBoard, pieces):
    currentPiece = pieces['currentPiece']

    for i in range(gameStats['rows']):
        gameStats, gameBoard, pieces = moveDown(gameStats, gameBoard, pieces)
        if gameStats['landed'] == True:
            break

    if gameStats['hardDropped'] == False:
        gameStats['hardDropped'] = True
        gameStats['currentMultiplier'] += .5

    return gameStats, gameBoard, pieces




def forcedDrop(gameStats, gameBoard, pieces):
    gameStats, gameBoard, pieces = moveDown(gameStats, gameBoard, pieces)

    return gameStats, gameBoard, pieces
    

def rotateClockWise(gameStats, gameBoard, pieces):
    if pieces['currentPiece'] == 'I':
        if pieces['rotation'] == 0:
            if (gameBoard[pieces['row'] - 1][pieces['col']] == ' ') \
           and (gameBoard[pieces['row'] + 1][pieces['col']] == ' ') \
           and (gameBoard[pieces['row'] + 2][pieces['col']] == ' '):
                pieces['rotation'] = (pieces['rotation'] + 1) % 4
        elif pieces['rotation'] == 1:
            if  2 <= pieces['col'] and pieces['col'] <= gameStats['cols'] - 2 \
           and (gameBoard[pieces['row']][pieces['col'] - 2] == ' ') \
           and (gameBoard[pieces['row']][pieces['col'] - 1] == ' ') \
           and (gameBoard[pieces['row']][pieces['col'] + 1] == ' '):
                pieces['rotation'] = (pieces['rotation'] + 1) % 4
        elif pieces['rotation'] == 2:
            if (gameBoard[pieces['row'] - 2][pieces['col']] == ' ') \
           and (gameBoard[pieces['row'] - 1][pieces['col']] == ' ') \
           and (gameBoard[pieces['row'] + 1][pieces['col']] == ' '):
                pieces['rotation'] = (pieces['rotation'] + 1) % 4
        elif pieces['rotation'] == 3:
            if 1 <= pieces['col'] and pieces['col'] <= gameStats['cols'] - 3 \
           and (gameBoard[pieces['row']][pieces['col'] - 1] == ' ') \
           and (gameBoard[pieces['row']][pieces['col'] + 1] == ' ') \
           and (gameBoard[pieces['row']][pieces['col'] + 2] == ' '):
                pieces['rotation'] = (pieces['rotation'] + 1) % 4

    elif pieces['currentPiece'] == 'J':
        if pieces['rotation'] == 0:
            if (gameBoard[pieces['row'] - 1][pieces['col']] == ' ') \
           and (gameBoard[pieces['row'] + 1][pieces['col']] == ' ') \
           and (gameBoard[pieces['row'] + 1][pieces['col'] - 1] == ' '):
                pieces['rotation'] = (pieces['rotation'] + 1) % 4
        elif pieces['rotation'] == 1:
            if pieces['col'] <= gameStats['cols'] - 2 \
           and (gameBoard[pieces['row'] - 1][pieces['col'] - 1] == ' ') \
           and (gameBoard[pieces['row']][pieces['col'] - 1] == ' ') \
           and (gameBoard[pieces['row']][pieces['col'] + 1] == ' '):
                pieces['rotation'] = (pieces['rotation'] + 1) % 4
        elif pieces['rotation'] == 2:
            if (gameBoard[pieces['row'] - 1][pieces['col']] == ' ') \
           and (gameBoard[pieces['row'] - 1][pieces['col'] + 1] == ' ') \
           and (gameBoard[pieces['row'] + 1][pieces['col']] == ' '):
                pieces['rotation'] = (pieces['rotation'] + 1) % 4
        elif pieces['rotation'] == 3:
            if 1 <= pieces['col'] \
           and (gameBoard[pieces['row']][pieces['col'] - 1] == ' ') \
           and (gameBoard[pieces['row']][pieces['col'] + 1] == ' ') \
           and (gameBoard[pieces['row'] + 1][pieces['col'] + 1] == ' '):
                pieces['rotation'] = (pieces['rotation'] + 1) % 4

    elif pieces['currentPiece'] == 'L':
        if pieces['rotation'] == 0:
            if (gameBoard[pieces['row'] - 1][pieces['col'] - 1] == ' ') \
           and (gameBoard[pieces['row'] - 1][pieces['col']] == ' ') \
           and (gameBoard[pieces['row'] + 1][pieces['col']] == ' '):
                pieces['rotation'] = (pieces['rotation'] + 1) % 4
        elif pieces['rotation'] == 1:
            if pieces['col'] <= gameStats['cols'] - 2 \
           and (gameBoard[pieces['row']][pieces['col'] - 1] == ' ') \
           and (gameBoard[pieces['row'] - 1][pieces['col'] + 1] == ' ') \
           and (gameBoard[pieces['row']][pieces['col'] + 1] == ' '):
                pieces['rotation'] = (pieces['rotation'] + 1) % 4
        elif pieces['rotation'] == 2:
            if (gameBoard[pieces['row'] - 1][pieces['col']] == ' ') \
           and (gameBoard[pieces['row'] + 1][pieces['col'] + 1] == ' ') \
           and (gameBoard[pieces['row'] + 1][pieces['col']] == ' '):
                pieces['rotation'] = (pieces['rotation'] + 1) % 4
        elif pieces['rotation'] == 3:
            if 1 <= pieces['col'] \
           and (gameBoard[pieces['row']][pieces['col'] - 1] == ' ') \
           and (gameBoard[pieces['row'] + 1][pieces['col'] - 1] == ' ') \
           and (gameBoard[pieces['row']][pieces['col'] + 1] == ' '):
                pieces['rotation'] = (pieces['rotation'] + 1) % 4
        
    elif pieces['currentPiece'] == 'O':
        pass
                
    elif pieces['currentPiece'] == 'S':
        if pieces['rotation'] == 0:
            if (gameBoard[pieces['row'] - 1][pieces['col'] - 1] == ' ') \
           and (gameBoard[pieces['row']][pieces['col'] - 1] == ' '):
                pieces['rotation'] = (pieces['rotation'] + 1) % 4
        elif pieces['rotation'] == 1:
            if pieces['col'] <= gameStats['cols'] - 2 \
           and (gameBoard[pieces['row'] - 1][pieces['col']] == ' ') \
           and (gameBoard[pieces['row'] - 1][pieces['col'] + 1] == ' '):
                pieces['rotation'] = (pieces['rotation'] + 1) % 4
        elif pieces['rotation'] == 2:
            if (gameBoard[pieces['row']][pieces['col'] + 1] == ' ') \
           and (gameBoard[pieces['row'] + 1][pieces['col'] + 1] == ' '):
                pieces['rotation'] = (pieces['rotation'] + 1) % 4
        elif pieces['rotation'] == 3:
            if 1 <= pieces['col'] \
           and (gameBoard[pieces['row'] + 1][pieces['col'] - 1] == ' ') \
           and (gameBoard[pieces['row'] + 1][pieces['col']] == ' '):
                pieces['rotation'] = (pieces['rotation'] + 1) % 4
                
    elif pieces['currentPiece'] == 'Z':
        if pieces['rotation'] == 0:
            if (gameBoard[pieces['row'] - 1][pieces['col']] == ' ') \
           and (gameBoard[pieces['row'] + 1][pieces['col'] - 1] == ' '):
                pieces['rotation'] = (pieces['rotation'] + 1) % 4
        elif pieces['rotation'] == 1:
            if pieces['col'] <= gameStats['cols'] - 2 \
           and (gameBoard[pieces['row'] - 1][pieces['col'] - 1] == ' ') \
           and (gameBoard[pieces['row']][pieces['col'] + 1] == ' '):
                pieces['rotation'] = (pieces['rotation'] + 1) % 4
        elif pieces['rotation'] == 2:
            if (gameBoard[pieces['row'] - 1][pieces['col'] + 1] == ' ') \
           and (gameBoard[pieces['row'] + 1][pieces['col']] == ' '):
                pieces['rotation'] = (pieces['rotation'] + 1) % 4
        elif pieces['rotation'] == 3:
            if 1 <= pieces['col'] \
           and (gameBoard[pieces['row']][pieces['col'] - 1] == ' ') \
           and (gameBoard[pieces['row'] + 1][pieces['col'] + 1] == ' '):
                pieces['rotation'] = (pieces['rotation'] + 1) % 4

    elif pieces['currentPiece'] == 'T':
        if pieces['rotation'] == 0:
            if (gameBoard[pieces['row'] - 1][pieces['col']] == ' '):
                pieces['rotation'] = (pieces['rotation'] + 1) % 4
        elif pieces['rotation'] == 1:
            if pieces['col'] <= gameStats['cols'] - 2 \
           and (gameBoard[pieces['row']][pieces['col'] + 1] == ' '):
                pieces['rotation'] = (pieces['rotation'] + 1) % 4
        elif pieces['rotation'] == 2:
            if (gameBoard[pieces['row'] + 1][pieces['col']] == ' '):
                pieces['rotation'] = (pieces['rotation'] + 1) % 4
        elif pieces['rotation'] == 3:
            if 1 <= pieces['col'] \
           and (gameBoard[pieces['row']][pieces['col'] - 1] == ' '):
                pieces['rotation'] = (pieces['rotation'] + 1) % 4

    return pieces




def rotateCounterClockWise(gameStats, gameBoard, pieces):
    if pieces['currentPiece'] == 'I':
        if pieces['rotation'] == 0:
            if (gameBoard[pieces['row'] - 2][pieces['col']] == ' ') \
           and (gameBoard[pieces['row'] - 1][pieces['col']] == ' ') \
           and (gameBoard[pieces['row'] + 1][pieces['col']] == ' '):
                pieces['rotation'] = (pieces['rotation'] - 1) % 4
        elif pieces['rotation'] == 1:
            if 1 <= pieces['col'] and pieces['col'] <= gameStats['cols'] - 3 \
           and (gameBoard[pieces['row']][pieces['col'] - 1] == ' ') \
           and (gameBoard[pieces['row']][pieces['col'] + 1] == ' ') \
           and (gameBoard[pieces['row']][pieces['col'] + 2] == ' '):
                pieces['rotation'] = (pieces['rotation'] - 1) % 4
        elif pieces['rotation'] == 2:
            if (gameBoard[pieces['row'] - 1][pieces['col']] == ' ') \
           and (gameBoard[pieces['row'] + 1][pieces['col']] == ' ') \
           and (gameBoard[pieces['row'] + 2][pieces['col']] == ' '):
                pieces['rotation'] = (pieces['rotation'] - 1) % 4
        elif pieces['rotation'] == 3:
            if  2 <= pieces['col'] and pieces['col'] <= gameStats['cols'] - 2 \
           and (gameBoard[pieces['row']][pieces['col'] - 2] == ' ') \
           and (gameBoard[pieces['row']][pieces['col'] - 1] == ' ') \
           and (gameBoard[pieces['row']][pieces['col'] + 1] == ' '):
                pieces['rotation'] = (pieces['rotation'] - 1) % 4

    elif pieces['currentPiece'] == 'J':
        if pieces['rotation'] == 0:
            if (gameBoard[pieces['row'] - 1][pieces['col']] == ' ') \
           and (gameBoard[pieces['row'] - 1][pieces['col'] + 1] == ' ') \
           and (gameBoard[pieces['row'] + 1][pieces['col']] == ' '):
                pieces['rotation'] = (pieces['rotation'] - 1) % 4
        elif pieces['rotation'] == 1:
            if pieces['col'] <= gameStats['cols'] - 2 \
           and (gameBoard[pieces['row']][pieces['col'] - 1] == ' ') \
           and (gameBoard[pieces['row']][pieces['col'] + 1] == ' ') \
           and (gameBoard[pieces['row'] + 1][pieces['col'] + 1] == ' '):
                pieces['rotation'] = (pieces['rotation'] - 1) % 4
        elif pieces['rotation'] == 2:
            if (gameBoard[pieces['row'] - 1][pieces['col']] == ' ') \
           and (gameBoard[pieces['row'] + 1][pieces['col']] == ' ') \
           and (gameBoard[pieces['row'] + 1][pieces['col'] - 1] == ' '):
                pieces['rotation'] = (pieces['rotation'] - 1) % 4
        elif pieces['rotation'] == 3:
            if 1 <= pieces['col'] \
           and (gameBoard[pieces['row'] - 1][pieces['col'] - 1] == ' ') \
           and (gameBoard[pieces['row']][pieces['col'] - 1] == ' ') \
           and (gameBoard[pieces['row']][pieces['col'] + 1] == ' '):
                pieces['rotation'] = (pieces['rotation'] - 1) % 4

    elif pieces['currentPiece'] == 'L':
        if pieces['rotation'] == 0:
            if (gameBoard[pieces['row'] - 1][pieces['col']] == ' ') \
           and (gameBoard[pieces['row'] + 1][pieces['col'] + 1] == ' ') \
           and (gameBoard[pieces['row'] + 1][pieces['col']] == ' '):
                pieces['rotation'] = (pieces['rotation'] - 1) % 4
        elif pieces['rotation'] == 1:
            if pieces['col'] <= gameStats['cols'] - 2 \
           and (gameBoard[pieces['row']][pieces['col'] - 1] == ' ') \
           and (gameBoard[pieces['row'] + 1][pieces['col'] - 1] == ' ') \
           and (gameBoard[pieces['row']][pieces['col'] + 1] == ' '):
                pieces['rotation'] = (pieces['rotation'] - 1) % 4
        elif pieces['rotation'] == 2:
            if (gameBoard[pieces['row'] - 1][pieces['col'] - 1] == ' ') \
           and (gameBoard[pieces['row'] - 1][pieces['col']] == ' ') \
           and (gameBoard[pieces['row'] + 1][pieces['col']] == ' '):
                pieces['rotation'] = (pieces['rotation'] - 1) % 4
        elif pieces['rotation'] == 3:
            if 1 <= pieces['col'] \
           and (gameBoard[pieces['row']][pieces['col'] - 1] == ' ') \
           and (gameBoard[pieces['row'] - 1][pieces['col'] + 1] == ' ') \
           and (gameBoard[pieces['row']][pieces['col'] + 1] == ' '):
                pieces['rotation'] = (pieces['rotation'] - 1) % 4
        
    elif pieces['currentPiece'] == 'O':
        pass
                
    elif pieces['currentPiece'] == 'S':
        if pieces['rotation'] == 0:
            if (gameBoard[pieces['row'] - 1][pieces['col']] == ' ') \
           and (gameBoard[pieces['row'] + 1][pieces['col'] + 1] == ' '):
                pieces['rotation'] = (pieces['rotation'] - 1) % 4
        elif pieces['rotation'] == 1:
            if pieces['col'] <= gameStats['cols'] - 2 \
           and (gameBoard[pieces['row']][pieces['col'] + 1] == ' ') \
           and (gameBoard[pieces['row'] + 1][pieces['col'] - 1] == ' '):
                pieces['rotation'] = (pieces['rotation'] - 1) % 4
        elif pieces['rotation'] == 2:
            if (gameBoard[pieces['row'] - 1][pieces['col'] - 1] == ' ') \
           and (gameBoard[pieces['row'] + 1][pieces['col']] == ' '):
                pieces['rotation'] = (pieces['rotation'] - 1) % 4
        elif pieces['rotation'] == 3:
            if 1 <= pieces['col'] \
           and (gameBoard[pieces['row']][pieces['col'] - 1] == ' ') \
           and (gameBoard[pieces['row'] - 1][pieces['col'] + 1] == ' '):
                pieces['rotation'] = (pieces['rotation'] - 1) % 4
                
    elif pieces['currentPiece'] == 'Z':
        if pieces['rotation'] == 0:
            if (gameBoard[pieces['row'] - 1][pieces['col'] + 1] == ' ') \
           and (gameBoard[pieces['row']][pieces['col'] + 1] == ' '):
                pieces['rotation'] = (pieces['rotation'] - 1) % 4
        elif pieces['rotation'] == 1:
            if pieces['col'] <= gameStats['cols'] - 2 \
           and (gameBoard[pieces['row'] + 1][pieces['col']] == ' ') \
           and (gameBoard[pieces['row'] + 1][pieces['col'] + 1] == ' '):
                pieces['rotation'] = (pieces['rotation'] - 1) % 4
        elif pieces['rotation'] == 2:
            if (gameBoard[pieces['row']][pieces['col'] - 1] == ' ') \
           and (gameBoard[pieces['row'] + 1][pieces['col'] - 1] == ' '):
                pieces['rotation'] = (pieces['rotation'] - 1) % 4
        elif pieces['rotation'] == 3:
            if 1 <= pieces['col'] \
           and (gameBoard[pieces['row'] - 1][pieces['col'] - 1] == ' ') \
           and (gameBoard[pieces['row'] - 1][pieces['col']] == ' '):
                pieces['rotation'] = (pieces['rotation'] - 1) % 4

    elif pieces['currentPiece'] == 'T':
        if pieces['rotation'] == 0:
            if (gameBoard[pieces['row'] - 1][pieces['col']] == ' '):
                pieces['rotation'] = (pieces['rotation'] - 1) % 4
        elif pieces['rotation'] == 1:
            if pieces['col'] <= gameStats['cols'] - 2 \
           and (gameBoard[pieces['row']][pieces['col'] + 1] == ' '):
                pieces['rotation'] = (pieces['rotation'] - 1) % 4
        elif pieces['rotation'] == 2:
            if (gameBoard[pieces['row'] + 1][pieces['col']] == ' '):
                pieces['rotation'] = (pieces['rotation'] - 1) % 4
        elif pieces['rotation'] == 3:
            if 1 <= pieces['col'] \
           and (gameBoard[pieces['row']][pieces['col'] - 1] == ' '):
                pieces['rotation'] = (pieces['rotation'] - 1) % 4

    return pieces




def moveLeft(gameStats, gameBoard, pieces):
    if pieces['currentPiece'] == 'I':
        if pieces['rotation'] == 0:
            if pieces['col'] >= 2 and (gameBoard[pieces['row']][pieces['col'] - 2] == ' '):
                pieces['col'] = pieces['col'] - 1
        elif pieces['rotation'] == 1:
            if pieces['col'] >= 1 and (gameBoard[pieces['row'] - 1][pieces['col'] - 1] == ' ') \
                                  and (gameBoard[pieces['row']][pieces['col'] - 1] == ' ') \
                                  and (gameBoard[pieces['row'] + 1][pieces['col'] - 1] == ' ') \
                                  and (gameBoard[pieces['row'] + 2][pieces['col'] - 1] == ' '):
                pieces['col'] = pieces['col'] - 1
        elif pieces['rotation'] == 2:
            if pieces['col'] >= 3 and (gameBoard[pieces['row']][pieces['col'] - 3] == ' '):
                pieces['col'] = pieces['col'] - 1
        elif pieces['rotation'] == 3:
            if pieces['col'] >= 1 and (gameBoard[pieces['row'] - 2][pieces['col'] - 1] == ' ') \
                                  and (gameBoard[pieces['row'] - 1][pieces['col'] - 1] == ' ') \
                                  and (gameBoard[pieces['row']][pieces['col'] - 1] == ' ') \
                                  and (gameBoard[pieces['row'] + 1][pieces['col'] - 1] == ' '):
                pieces['col'] = pieces['col'] - 1

    elif pieces['currentPiece'] == 'J':
        if pieces['rotation'] == 0:
            if pieces['col'] >= 2 and (gameBoard[pieces['row']][pieces['col'] - 2] == ' ') \
                                  and (gameBoard[pieces['row'] + 1][pieces['col']] == ' '):
                pieces['col'] = pieces['col'] - 1
        elif pieces['rotation'] == 1:
            if pieces['col'] >= 2 and (gameBoard[pieces['row'] - 1][pieces['col'] - 1] == ' ') \
                                  and (gameBoard[pieces['row']][pieces['col'] - 1] == ' ') \
                                  and (gameBoard[pieces['row'] + 1][pieces['col'] - 2] == ' '):
                pieces['col'] = pieces['col'] - 1
        elif pieces['rotation'] == 2:
            if pieces['col'] >= 2 and (gameBoard[pieces['row'] - 1][pieces['col'] - 2] == ' ') \
                                  and (gameBoard[pieces['row']][pieces['col'] - 2] == ' '):
                pieces['col'] = pieces['col'] - 1
        elif pieces['rotation'] == 3:
            if pieces['col'] >= 1 and (gameBoard[pieces['row'] - 1][pieces['col'] - 1] == ' ') \
                                  and (gameBoard[pieces['row']][pieces['col'] - 1] == ' ') \
                                  and (gameBoard[pieces['row'] + 1][pieces['col'] - 1] == ' '):
                pieces['col'] = pieces['col'] - 1

    elif pieces['currentPiece'] == 'L':
        if pieces['rotation'] == 0:
            if pieces['col'] >= 2 and (gameBoard[pieces['row']][pieces['col'] - 2] == ' ') \
                                  and (gameBoard[pieces['row'] + 1][pieces['col'] - 2] == ' '):
                pieces['col'] = pieces['col'] - 1
        elif pieces['rotation'] == 1:
            if pieces['col'] >= 2 and (gameBoard[pieces['row'] - 1][pieces['col'] - 2] == ' ') \
                                  and (gameBoard[pieces['row']][pieces['col'] - 1] == ' ') \
                                  and (gameBoard[pieces['row'] + 1][pieces['col'] - 1] == ' '):
                pieces['col'] = pieces['col'] - 1
        elif pieces['rotation'] == 2:
            if pieces['col'] >= 2 and (gameBoard[pieces['row'] - 1][pieces['col']] == ' ') \
                                  and (gameBoard[pieces['row']][pieces['col'] - 2] == ' '):
                pieces['col'] = pieces['col'] - 1
        elif pieces['rotation'] == 3:
            if pieces['col'] >= 1 and (gameBoard[pieces['row'] - 1][pieces['col'] - 1] == ' ') \
                                  and (gameBoard[pieces['row']][pieces['col'] - 1] == ' ') \
                                  and (gameBoard[pieces['row'] + 1][pieces['col'] - 1] == ' '):
                pieces['col'] = pieces['col'] - 1
        
    elif pieces['currentPiece'] == 'O':
        if pieces['col'] >= 1 and (gameBoard[pieces['row']][pieces['col'] - 1] == ' ') \
                              and (gameBoard[pieces['row'] + 1][pieces['col'] - 1] == ' '):
            pieces['col'] = pieces['col'] - 1
                
    elif pieces['currentPiece'] == 'S':
        if pieces['rotation'] == 0:
            if pieces['col'] >= 2 and (gameBoard[pieces['row']][pieces['col'] - 1] == ' ') \
                                  and (gameBoard[pieces['row'] + 1][pieces['col'] - 2] == ' '):
                pieces['col'] = pieces['col'] - 1
        elif pieces['rotation'] == 1:
            if pieces['col'] >= 2 and (gameBoard[pieces['row'] - 1][pieces['col'] - 2] == ' ') \
                                  and (gameBoard[pieces['row']][pieces['col'] - 2] == ' ') \
                                  and (gameBoard[pieces['row'] + 1][pieces['col'] - 1] == ' '):
                pieces['col'] = pieces['col'] - 1
        elif pieces['rotation'] == 2:
            if pieces['col'] >= 2 and (gameBoard[pieces['row'] - 1][pieces['col'] - 1] == ' ') \
                                  and (gameBoard[pieces['row']][pieces['col'] - 2] == ' '):
                pieces['col'] = pieces['col'] - 1
        elif pieces['rotation'] == 3:
            if pieces['col'] >= 1 and (gameBoard[pieces['row'] - 1][pieces['col'] - 1] == ' ') \
                                  and (gameBoard[pieces['row']][pieces['col'] - 1] == ' ') \
                                  and (gameBoard[pieces['row'] + 1][pieces['col']] == ' '):
                pieces['col'] = pieces['col'] - 1
                
    elif pieces['currentPiece'] == 'Z':
        if pieces['rotation'] == 0:
            if pieces['col'] >= 2 and (gameBoard[pieces['row']][pieces['col'] - 2] == ' ') \
                                  and (gameBoard[pieces['row'] + 1][pieces['col'] - 1] == ' '):
                pieces['col'] = pieces['col'] - 1
        elif pieces['rotation'] == 1:
            if pieces['col'] >= 2 and (gameBoard[pieces['row'] - 1][pieces['col'] - 1] == ' ') \
                                  and (gameBoard[pieces['row']][pieces['col'] - 2] == ' ') \
                                  and (gameBoard[pieces['row'] + 1][pieces['col'] - 2] == ' '):
                pieces['col'] = pieces['col'] - 1
        elif pieces['rotation'] == 2:
            if pieces['col'] >= 2 and (gameBoard[pieces['row'] - 1][pieces['col'] - 2] == ' ') \
                                  and (gameBoard[pieces['row']][pieces['col'] - 1] == ' '):
                pieces['col'] = pieces['col'] - 1
        elif pieces['rotation'] == 3:
            if pieces['col'] >= 1 and (gameBoard[pieces['row'] - 1][pieces['col']] == ' ') \
                                  and (gameBoard[pieces['row']][pieces['col'] - 1] == ' ') \
                                  and (gameBoard[pieces['row'] + 1][pieces['col'] - 1] == ' '):
                pieces['col'] = pieces['col'] - 1

    elif pieces['currentPiece'] == 'T':
        if pieces['rotation'] == 0:
            if pieces['col'] >= 2 and (gameBoard[pieces['row']][pieces['col'] - 2] == ' ') \
                                  and (gameBoard[pieces['row'] + 1][pieces['col'] - 1] == ' '):
                pieces['col'] = pieces['col'] - 1
        elif pieces['rotation'] == 1:
            if pieces['col'] >= 2 and (gameBoard[pieces['row'] - 1][pieces['col'] - 1] == ' ') \
                                  and (gameBoard[pieces['row']][pieces['col'] - 2] == ' ') \
                                  and (gameBoard[pieces['row'] + 1][pieces['col'] - 1] == ' '):
                pieces['col'] = pieces['col'] - 1
        elif pieces['rotation'] == 2:
            if pieces['col'] >= 2 and (gameBoard[pieces['row'] - 1][pieces['col'] - 1] == ' ') \
                                  and (gameBoard[pieces['row']][pieces['col'] - 2] == ' '):
                pieces['col'] = pieces['col'] - 1
        elif pieces['rotation'] == 3:
            if pieces['col'] >= 1 and (gameBoard[pieces['row'] - 1][pieces['col'] - 1] == ' ') \
                                  and (gameBoard[pieces['row']][pieces['col'] - 1] == ' ') \
                                  and (gameBoard[pieces['row'] + 1][pieces['col'] - 1] == ' '):
                pieces['col'] = pieces['col'] - 1

    return pieces

def moveRight(gameStats, gameBoard, pieces):
    if pieces['currentPiece'] == 'I':
        if pieces['rotation'] == 0:
            if pieces['col'] <= gameStats['cols'] - 4 and (gameBoard[pieces['row']][pieces['col'] + 3] == ' '):
                pieces['col'] = pieces['col'] + 1
        elif pieces['rotation'] == 1:
            if pieces['col'] <= gameStats['cols'] - 2 and (gameBoard[pieces['row'] - 1][pieces['col'] + 1] == ' ') \
                                                 and (gameBoard[pieces['row']][pieces['col'] + 1] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col'] + 1] == ' ') \
                                                 and (gameBoard[pieces['row'] + 2][pieces['col'] + 1] == ' '):
                pieces['col'] = pieces['col'] + 1
        elif pieces['rotation'] == 2:
            if pieces['col'] <= gameStats['cols'] - 3 and (gameBoard[pieces['row']][pieces['col'] + 2] == ' '):
                pieces['col'] = pieces['col'] + 1
        elif pieces['rotation'] == 3:
            if pieces['col'] <= gameStats['cols'] - 2 and (gameBoard[pieces['row'] - 2][pieces['col'] + 1] == ' ') \
                                                 and (gameBoard[pieces['row'] - 1][pieces['col'] + 1] == ' ') \
                                                 and (gameBoard[pieces['row']][pieces['col'] + 1] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col'] + 1] == ' '):
                pieces['col'] = pieces['col'] + 1

    elif pieces['currentPiece'] == 'J':
        if pieces['rotation'] == 0:
            if pieces['col'] <= gameStats['cols'] - 3 and (gameBoard[pieces['row']][pieces['col'] + 2] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col'] + 2] == ' '):
                pieces['col'] = pieces['col'] + 1
        elif pieces['rotation'] == 1:
            if pieces['col'] <= gameStats['cols'] - 2 and (gameBoard[pieces['row'] - 1][pieces['col'] + 1] == ' ') \
                                                 and (gameBoard[pieces['row']][pieces['col'] + 1] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col'] + 1] == ' '):
                pieces['col'] = pieces['col'] + 1
        elif pieces['rotation'] == 2:
            if pieces['col'] <= gameStats['cols'] - 3 and (gameBoard[pieces['row'] - 1][pieces['col']] == ' ') \
                                                 and (gameBoard[pieces['row']][pieces['col'] + 2] == ' '):
                pieces['col'] = pieces['col'] + 1
        elif pieces['rotation'] == 3:
            if pieces['col'] <= gameStats['cols'] - 3 and (gameBoard[pieces['row'] - 1][pieces['col'] + 2] == ' ') \
                                                 and (gameBoard[pieces['row']][pieces['col'] + 1] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col'] + 1] == ' '):
                pieces['col'] = pieces['col'] + 1

    elif pieces['currentPiece'] == 'L':
        if pieces['rotation'] == 0:
            if pieces['col'] <= gameStats['cols'] - 3 and (gameBoard[pieces['row']][pieces['col'] + 2] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col']] == ' '):
                pieces['col'] = pieces['col'] + 1
        elif pieces['rotation'] == 1:
            if pieces['col'] <= gameStats['cols'] - 2 and (gameBoard[pieces['row'] - 1][pieces['col'] + 1] == ' ') \
                                                 and (gameBoard[pieces['row']][pieces['col'] + 1] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col'] + 1] == ' '):
                pieces['col'] = pieces['col'] + 1
        elif pieces['rotation'] == 2:
            if pieces['col'] <= gameStats['cols'] - 3 and (gameBoard[pieces['row'] - 1][pieces['col'] + 2] == ' ') \
                                                 and (gameBoard[pieces['row']][pieces['col'] + 2] == ' '):
                pieces['col'] = pieces['col'] + 1
        elif pieces['rotation'] == 3:
            if pieces['col'] <= gameStats['cols'] - 3 and (gameBoard[pieces['row'] - 1][pieces['col'] + 1] == ' ') \
                                                 and (gameBoard[pieces['row']][pieces['col'] + 1] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col'] + 2] == ' '):
                pieces['col'] = pieces['col'] + 1
        
    elif pieces['currentPiece'] == 'O':
        if pieces['col'] <= gameStats['cols'] - 3 and (gameBoard[pieces['row']][pieces['col'] + 2] == ' ') \
                                             and (gameBoard[pieces['row'] + 1][pieces['col'] + 2] == ' '):
            pieces['col'] = pieces['col'] + 1
                
    elif pieces['currentPiece'] == 'S':
        if pieces['rotation'] == 0:
            if pieces['col'] <= gameStats['cols'] - 3 and (gameBoard[pieces['row']][pieces['col'] + 2] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col'] + 1] == ' '):
                pieces['col'] = pieces['col'] + 1
        elif pieces['rotation'] == 1:
            if pieces['col'] <= gameStats['cols'] - 2 and (gameBoard[pieces['row'] - 1][pieces['col']] == ' ') \
                                                 and (gameBoard[pieces['row']][pieces['col'] + 1] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col'] + 1] == ' '):
                pieces['col'] = pieces['col'] + 1
        elif pieces['rotation'] == 2:
            if pieces['col'] <= gameStats['cols'] - 3 and (gameBoard[pieces['row'] - 1][pieces['col'] + 2] == ' ') \
                                                 and (gameBoard[pieces['row']][pieces['col'] + 1] == ' '):
                pieces['col'] = pieces['col'] + 1
        elif pieces['rotation'] == 3:
            if pieces['col'] <= gameStats['cols'] - 3 and (gameBoard[pieces['row'] - 1][pieces['col'] + 1] == ' ') \
                                                 and (gameBoard[pieces['row']][pieces['col'] + 2] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col'] + 2] == ' '):
                pieces['col'] = pieces['col'] + 1
                
    elif pieces['currentPiece'] == 'Z':
        if pieces['rotation'] == 0:
            if pieces['col'] <= gameStats['cols'] - 3 and (gameBoard[pieces['row']][pieces['col'] + 1] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col'] + 2] == ' '):
                pieces['col'] = pieces['col'] + 1
        elif pieces['rotation'] == 1:
            if pieces['col'] <= gameStats['cols'] - 2 and (gameBoard[pieces['row'] - 1][pieces['col'] + 1] == ' ') \
                                                 and (gameBoard[pieces['row']][pieces['col'] + 1] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col']] == ' '):
                pieces['col'] = pieces['col'] + 1
        elif pieces['rotation'] == 2:
            if pieces['col'] <= gameStats['cols'] - 3 and (gameBoard[pieces['row'] - 1][pieces['col'] + 1] == ' ') \
                                                 and (gameBoard[pieces['row']][pieces['col'] + 2] == ' '):
                pieces['col'] = pieces['col'] + 1
        elif pieces['rotation'] == 3:
            if pieces['col'] <= gameStats['cols'] - 3 and (gameBoard[pieces['row'] - 1][pieces['col'] + 2] == ' ') \
                                                 and (gameBoard[pieces['row']][pieces['col'] + 2] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col'] + 1] == ' '):
                pieces['col'] = pieces['col'] + 1

    elif pieces['currentPiece'] == 'T':
        if pieces['rotation'] == 0:
            if pieces['col'] <= gameStats['cols'] - 3 and (gameBoard[pieces['row']][pieces['col'] + 2] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col'] + 1] == ' '):
                pieces['col'] = pieces['col'] + 1
        elif pieces['rotation'] == 1:
            if pieces['col'] <= gameStats['cols'] - 2 and (gameBoard[pieces['row'] - 1][pieces['col'] + 1] == ' ') \
                                                 and (gameBoard[pieces['row']][pieces['col'] + 1] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col'] + 1] == ' '):
                pieces['col'] = pieces['col'] + 1
        elif pieces['rotation'] == 2:
            if pieces['col'] <= gameStats['cols'] - 3 and (gameBoard[pieces['row'] - 1][pieces['col'] + 1] == ' ') \
                                                 and (gameBoard[pieces['row']][pieces['col'] + 2] == ' '):
                pieces['col'] = pieces['col'] + 1
        elif pieces['rotation'] == 3:
            if pieces['col'] <= gameStats['cols'] - 3 and (gameBoard[pieces['row'] - 1][pieces['col'] + 1] == ' ') \
                                                 and (gameBoard[pieces['row']][pieces['col'] + 2] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col'] + 1] == ' '):
                pieces['col'] = pieces['col'] + 1

    return pieces

def moveDown(gameStats, gameBoard, pieces):
    gameStats['landed'] = False
    if pieces['currentPiece'] == 'I':
        if pieces['rotation'] == 0:
            if pieces['row'] <= gameStats['rows'] - 2 and (gameBoard[pieces['row'] + 1][pieces['col'] - 1] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col']] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col'] + 1] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col'] + 2] == ' '):
                pieces['row'] = pieces['row'] + 1
            else:
                gameBoard[pieces['row']][pieces['col'] - 1] = 'i'
                gameBoard[pieces['row']][pieces['col']] = 'i'
                gameBoard[pieces['row']][pieces['col'] + 1] = 'i'
                gameBoard[pieces['row']][pieces['col'] + 2] = 'i'
                
                gameStats['landed'] = True

        elif pieces['rotation'] == 1:
            if pieces['row'] <= gameStats['rows'] - 4 and (gameBoard[pieces['row'] + 3][pieces['col']] == ' '):
                pieces['row'] = pieces['row'] + 1
            else:
                gameBoard[pieces['row'] - 1][pieces['col']] = 'i'
                gameBoard[pieces['row']][pieces['col']] = 'i'
                gameBoard[pieces['row'] + 1][pieces['col']] = 'i'
                gameBoard[pieces['row'] + 2][pieces['col']] = 'i'
                
                gameStats['landed'] = True
                
        elif pieces['rotation'] == 2:
            if pieces['row'] <= gameStats['rows'] - 2 and (gameBoard[pieces['row'] + 1][pieces['col'] - 2] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col'] - 1] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col']] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col'] + 1] == ' '):
                pieces['row'] = pieces['row'] + 1
            else:
                gameBoard[pieces['row']][pieces['col'] - 2] = 'i'
                gameBoard[pieces['row']][pieces['col'] - 1] = 'i'
                gameBoard[pieces['row']][pieces['col']] = 'i'
                gameBoard[pieces['row']][pieces['col'] + 1] = 'i'
                
                gameStats['landed'] = True
                
        elif pieces['rotation'] == 3:
            if pieces['row'] <= gameStats['rows'] - 3 and (gameBoard[pieces['row'] + 2][pieces['col']] == ' '):
                pieces['row'] = pieces['row'] + 1
            else:
                gameBoard[pieces['row'] - 2][pieces['col']] = 'i'
                gameBoard[pieces['row'] - 1][pieces['col']] = 'i'
                gameBoard[pieces['row']][pieces['col']] = 'i'
                gameBoard[pieces['row'] + 1][pieces['col']] = 'i'
                
                gameStats['landed'] = True
                
    elif pieces['currentPiece'] == 'J':
        if pieces['rotation'] == 0:
            if pieces['row'] <= gameStats['rows'] - 3 and (gameBoard[pieces['row'] + 1][pieces['col'] - 1] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col']] == ' ') \
                                                 and (gameBoard[pieces['row'] + 2][pieces['col'] + 1] == ' '):
                pieces['row'] = pieces['row'] + 1
            else:
                gameBoard[pieces['row']][pieces['col'] - 1] = 'j'
                gameBoard[pieces['row']][pieces['col']] = 'j'
                gameBoard[pieces['row']][pieces['col'] + 1] = 'j'
                gameBoard[pieces['row'] + 1][pieces['col'] + 1] = 'j'
                
                gameStats['landed'] = True
                
        elif pieces['rotation'] == 1:
            if pieces['row'] <= gameStats['rows'] - 3 and (gameBoard[pieces['row'] + 2][pieces['col'] - 1] == ' ') \
                                                 and (gameBoard[pieces['row'] + 2][pieces['col']] == ' '):
                pieces['row'] = pieces['row'] + 1
            else:
                gameBoard[pieces['row'] - 1][pieces['col']] = 'j'
                gameBoard[pieces['row']][pieces['col']] = 'j'
                gameBoard[pieces['row'] + 1][pieces['col'] -1] = 'j'
                gameBoard[pieces['row'] + 1][pieces['col']] = 'j'
                
                gameStats['landed'] = True
                
        elif pieces['rotation'] == 2:
            if pieces['row'] <= gameStats['rows'] - 2 and (gameBoard[pieces['row'] + 1][pieces['col'] - 1] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col']] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col'] + 1] == ' '):
                pieces['row'] = pieces['row'] + 1
            else:
                gameBoard[pieces['row'] - 1][pieces['col'] - 1] = 'j'
                gameBoard[pieces['row']][pieces['col'] - 1] = 'j'
                gameBoard[pieces['row']][pieces['col']] = 'j'
                gameBoard[pieces['row']][pieces['col'] + 1] = 'j'
                
                gameStats['landed'] = True
                
        elif pieces['rotation'] == 3:
            if pieces['row'] <= gameStats['rows'] - 3 and (gameBoard[pieces['row'] + 2][pieces['col']] == ' ') \
                                                 and (gameBoard[pieces['row']][pieces['col'] + 1] == ' '):
                pieces['row'] = pieces['row'] + 1
            else:
                gameBoard[pieces['row'] - 1][pieces['col']] = 'j'
                gameBoard[pieces['row'] - 1][pieces['col'] + 1] = 'j'
                gameBoard[pieces['row']][pieces['col']] = 'j'
                gameBoard[pieces['row'] + 1][pieces['col']] = 'j'
                
                gameStats['landed'] = True
                

    elif pieces['currentPiece'] == 'L':
        if pieces['rotation'] == 0:
            if pieces['row'] <= gameStats['rows'] - 3 and (gameBoard[pieces['row'] + 2][pieces['col'] - 1] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col']] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col'] + 1] == ' '):
                pieces['row'] = pieces['row'] + 1
            else:
                gameBoard[pieces['row']][pieces['col'] - 1] = 'l'
                gameBoard[pieces['row'] + 1][pieces['col'] - 1] = 'l'
                gameBoard[pieces['row']][pieces['col']] = 'l'
                gameBoard[pieces['row']][pieces['col'] + 1] = 'l'
                
                gameStats['landed'] = True
                
        elif pieces['rotation'] == 1:
            if pieces['row'] <= gameStats['rows'] - 3 and (gameBoard[pieces['row']][pieces['col'] - 1] == ' ') \
                                                 and (gameBoard[pieces['row'] + 2][pieces['col']] == ' '):
                pieces['row'] = pieces['row'] + 1
            else:
                gameBoard[pieces['row'] - 1][pieces['col'] - 1] = 'l'
                gameBoard[pieces['row'] - 1][pieces['col']] = 'l'
                gameBoard[pieces['row']][pieces['col']] = 'l'
                gameBoard[pieces['row'] + 1][pieces['col']] = 'l'
                
                gameStats['landed'] = True
                
        elif pieces['rotation'] == 2:
            if pieces['row'] <= gameStats['rows'] - 2 and (gameBoard[pieces['row'] + 1][pieces['col'] - 1] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col']] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col'] + 1] == ' '):
                pieces['row'] = pieces['row'] + 1
            else:
                gameBoard[pieces['row']][pieces['col'] - 1] = 'l'
                gameBoard[pieces['row']][pieces['col']] = 'l'
                gameBoard[pieces['row']][pieces['col'] + 1] = 'l'
                gameBoard[pieces['row'] - 1][pieces['col'] + 1] = 'l'
                
                gameStats['landed'] = True
                
        elif pieces['rotation'] == 3:
            if pieces['row'] <= gameStats['rows'] - 3 and (gameBoard[pieces['row'] + 2][pieces['col']] == ' ') \
                                                 and (gameBoard[pieces['row'] + 2][pieces['col'] + 1] == ' '):
                pieces['row'] = pieces['row'] + 1
            else:
                gameBoard[pieces['row'] - 1][pieces['col']] = 'l'
                gameBoard[pieces['row']][pieces['col']] = 'l'
                gameBoard[pieces['row'] + 1][pieces['col']] = 'l'
                gameBoard[pieces['row'] + 1][pieces['col'] + 1] = 'l'
                
                gameStats['landed'] = True
        
    elif pieces['currentPiece'] == 'O':
        if pieces['row'] <= gameStats['rows'] - 3 and (gameBoard[pieces['row'] + 2][pieces['col']] == ' ') \
                                             and (gameBoard[pieces['row'] + 2][pieces['col'] + 1] == ' '):
            pieces['row'] = pieces['row'] + 1
        else:
            gameBoard[pieces['row']][pieces['col']] = 'o'
            gameBoard[pieces['row']][pieces['col'] + 1] = 'o'
            gameBoard[pieces['row'] + 1][pieces['col']] = 'o'
            gameBoard[pieces['row'] + 1][pieces['col'] + 1] = 'o'
                
            gameStats['landed'] = True
                
    elif pieces['currentPiece'] == 'S':
        if pieces['rotation'] == 0:
            if pieces['row'] <= gameStats['rows'] - 3 and (gameBoard[pieces['row'] + 2][pieces['col'] - 1] == ' ') \
                                                 and (gameBoard[pieces['row'] + 2][pieces['col']] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col'] + 1] == ' '):
                pieces['row'] = pieces['row'] + 1
            else:
                gameBoard[pieces['row'] + 1][pieces['col'] - 1] = 's'
                gameBoard[pieces['row']][pieces['col']] = 's'
                gameBoard[pieces['row'] + 1][pieces['col']] = 's'
                gameBoard[pieces['row']][pieces['col'] + 1] = 's'
                
                gameStats['landed'] = True
                
        elif pieces['rotation'] == 1:
            if pieces['row'] <= gameStats['rows'] - 3 and (gameBoard[pieces['row'] + 1][pieces['col'] - 1] == ' ') \
                                                 and (gameBoard[pieces['row'] + 2][pieces['col']] == ' '):
                pieces['row'] = pieces['row'] + 1
            else:
                gameBoard[pieces['row'] - 1][pieces['col'] - 1] = 's'
                gameBoard[pieces['row']][pieces['col'] - 1] = 's'
                gameBoard[pieces['row']][pieces['col']] = 's'
                gameBoard[pieces['row'] + 1][pieces['col']] = 's'
                
                gameStats['landed'] = True
                
        elif pieces['rotation'] == 2:
            if pieces['row'] <= gameStats['rows'] - 2 and (gameBoard[pieces['row'] + 1][pieces['col'] - 1] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col']] == ' ') \
                                                 and (gameBoard[pieces['row']][pieces['col'] + 1] == ' '):
                pieces['row'] = pieces['row'] + 1
            else:
                gameBoard[pieces['row']][pieces['col'] - 1] = 's'
                gameBoard[pieces['row']][pieces['col']] = 's'
                gameBoard[pieces['row'] - 1][pieces['col']] = 's'
                gameBoard[pieces['row'] - 1][pieces['col'] + 1] = 's'
                
                gameStats['landed'] = True
                
        elif pieces['rotation'] == 3:
            if pieces['row'] <= gameStats['rows'] - 3 and (gameBoard[pieces['row'] + 1][pieces['col']] == ' ') \
                                                 and (gameBoard[pieces['row'] + 2][pieces['col'] + 1] == ' '):
                pieces['row'] = pieces['row'] + 1
            else:
                gameBoard[pieces['row'] - 1][pieces['col']] = 's'
                gameBoard[pieces['row']][pieces['col']] = 's'
                gameBoard[pieces['row']][pieces['col'] + 1] = 's'
                gameBoard[pieces['row'] + 1][pieces['col'] + 1] = 's'
                
                gameStats['landed'] = True
                
                
    elif pieces['currentPiece'] == 'Z':
        if pieces['rotation'] == 0:
            if pieces['row'] <= gameStats['rows'] - 3 and (gameBoard[pieces['row'] + 1][pieces['col'] - 1] == ' ') \
                                                 and (gameBoard[pieces['row'] + 2][pieces['col']] == ' ') \
                                                 and (gameBoard[pieces['row'] + 2][pieces['col'] + 1] == ' '):
                pieces['row'] = pieces['row'] + 1
            else:
                gameBoard[pieces['row']][pieces['col'] - 1] = 'z'
                gameBoard[pieces['row']][pieces['col']] = 'z'
                gameBoard[pieces['row'] + 1][pieces['col']] = 'z'
                gameBoard[pieces['row'] + 1][pieces['col'] + 1] = 'z'
                
                gameStats['landed'] = True
                
        elif pieces['rotation'] == 1:
            if pieces['row'] <= gameStats['rows'] - 3 and (gameBoard[pieces['row'] + 2][pieces['col'] - 1] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col']] == ' '):
                pieces['row'] = pieces['row'] + 1
            else:
                gameBoard[pieces['row']][pieces['col'] - 1] = 'z'
                gameBoard[pieces['row'] + 1][pieces['col'] - 1] = 'z'
                gameBoard[pieces['row']][pieces['col']] = 'z'
                gameBoard[pieces['row'] - 1][pieces['col']] = 'z'
                
                gameStats['landed'] = True
                
        elif pieces['rotation'] == 2:
            if pieces['row'] <= gameStats['rows'] - 2 and (gameBoard[pieces['row']][pieces['col'] - 1] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col']] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col'] + 1] == ' '):
                pieces['row'] = pieces['row'] + 1
            else:
                gameBoard[pieces['row'] - 1][pieces['col'] - 1] = 'z'
                gameBoard[pieces['row'] - 1][pieces['col']] = 'z'
                gameBoard[pieces['row']][pieces['col']] = 'z'
                gameBoard[pieces['row']][pieces['col'] + 1] = 'z'
                
                gameStats['landed'] = True
                
        elif pieces['rotation'] == 3:
            if pieces['row'] <= gameStats['rows'] - 3 and (gameBoard[pieces['row'] + 2][pieces['col']] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col'] + 1] == ' '):
                pieces['row'] = pieces['row'] + 1
            else:
                gameBoard[pieces['row']][pieces['col']] = 'z'
                gameBoard[pieces['row'] + 1][pieces['col']] = 'z'
                gameBoard[pieces['row']][pieces['col'] + 1] = 'z'
                gameBoard[pieces['row'] - 1][pieces['col'] + 1] = 'z'
                
                gameStats['landed'] = True
                

    elif pieces['currentPiece'] == 'T':
        if pieces['rotation'] == 0:
            if pieces['row'] <= gameStats['rows'] - 3 and (gameBoard[pieces['row'] + 1][pieces['col'] - 1] == ' ') \
                                                 and (gameBoard[pieces['row'] + 2][pieces['col']] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col'] + 1] == ' '):
                pieces['row'] = pieces['row'] + 1
            else:
                gameBoard[pieces['row']][pieces['col'] - 1] = 't'
                gameBoard[pieces['row']][pieces['col']] = 't'
                gameBoard[pieces['row']][pieces['col'] + 1] = 't'
                gameBoard[pieces['row'] + 1][pieces['col']] = 't'
                
                gameStats['landed'] = True
                
        elif pieces['rotation'] == 1:
            if pieces['row'] <= gameStats['rows'] - 3 and (gameBoard[pieces['row'] + 1][pieces['col'] - 1] == ' ') \
                                                 and (gameBoard[pieces['row'] + 2][pieces['col']] == ' '):
                pieces['row'] = pieces['row'] + 1
            else:
                gameBoard[pieces['row']][pieces['col'] - 1] = 't'
                gameBoard[pieces['row'] - 1][pieces['col']] = 't'
                gameBoard[pieces['row']][pieces['col']] = 't'
                gameBoard[pieces['row'] + 1][pieces['col']] = 't'
                
                gameStats['landed'] = True
                
        elif pieces['rotation'] == 2:
            if pieces['row'] <= gameStats['rows'] - 2 and (gameBoard[pieces['row'] + 1][pieces['col'] - 1] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col']] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col'] + 1] == ' '):
                pieces['row'] = pieces['row'] + 1
            else:
                gameBoard[pieces['row']][pieces['col'] - 1] = 't'
                gameBoard[pieces['row']][pieces['col']] = 't'
                gameBoard[pieces['row'] - 1][pieces['col']] = 't'
                gameBoard[pieces['row']][pieces['col'] + 1] = 't'
                
                gameStats['landed'] = True
                
        elif pieces['rotation'] == 3:
            if pieces['row'] <= gameStats['rows'] - 3 and (gameBoard[pieces['row'] + 2][pieces['col']] == ' ') \
                                                 and (gameBoard[pieces['row'] + 1][pieces['col'] + 1] == ' '):
                pieces['row'] = pieces['row'] + 1
            else:
                gameBoard[pieces['row'] - 1][pieces['col']] = 't'
                gameBoard[pieces['row']][pieces['col']] = 't'
                gameBoard[pieces['row'] + 1][pieces['col']] = 't'
                gameBoard[pieces['row']][pieces['col'] + 1] = 't'
                
                gameStats['landed'] = True

    if gameStats['landed'] == True:
        gameStats['soundPlayed'] = True
        pieces['swapped'] = False
        if gameStats['hardDropped'] == True:
            gameStats['hardDropped'] = False
            gameStats['currentMultiplier'] -= .5
        pieces = pieceDown(pieces)
        gameBoard, gameStats = TetrisFunctions.scanFullRows(gameBoard, gameStats)

        if gameStats['cleared'] > 0:
            if gameStats['cleared'] == 2:
                gameStats['currentMultiplier'] += .5
            elif gameStats['cleared'] == 3:
                gameStats['currentMultiplier'] += 1
            elif gameStats['cleared'] == 4:
                gameStats['currentMultiplier'] += 2
            gameStats['combo'] += 1
            if gameStats['combo'] > 1:
                gameStats['currentMultiplier'] += .25
        else:
            while gameStats['combo'] > 1:
                gameStats['currentMultiplier'] -= .25
                gameStats['combo'] -= 1
            gameStats['combo'] = 0

    return gameStats, gameBoard, pieces


