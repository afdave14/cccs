#514 changes to 490?
import sys, pygame, copy, time
from pygame.locals import *
import random; random.seed()
##################################################################
mouthopening = 0
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
    aBoard.append([(14*RATIO,19*RATIO),(14*RATIO,19*RATIO),(23*RATIO,19*RATIO),(23*RATIO,24*RATIO),(14*RATIO,24*RATIO)])
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
    aBoard.append([(26*RATIO,35*RATIO),(26*RATIO,39*RATIO),(22*RATIO,39*RATIO),(22*RATIO,40*RATIO),(RATIO*34,RATIO*40),(34*RATIO,39*RATIO),(27*RATIO,39*RATIO),
            (27*RATIO,35*RATIO)])
    return(aBoard)
################################################################
################################################################
def createBoarder():
    aBoarder = []
    #draws bottom border
    aBoarder.append([(0,23*RATIO),(7*RATIO, 23*RATIO),(7*RATIO, 28*RATIO),(0, 28*RATIO),(0,35*RATIO),(3*RATIO,35*RATIO),(3*RATIO,RATIO*36),
             (0,RATIO*36),(0,RATIO*43),(WIDTH-RATIO*3,RATIO*43),(WIDTH-RATIO*3,RATIO*36),(WIDTH-(RATIO*6),RATIO*36),(WIDTH-(RATIO*6),RATIO*35),
             (WIDTH-RATIO*3,RATIO*35),(WIDTH-RATIO*3,RATIO*28),(RATIO*30,RATIO*28),(30*RATIO,RATIO*23),(WIDTH-RATIO*3,RATIO*23),])
    #draws top boarder
    aBoarder.append([(0,RATIO*20),(7*RATIO,RATIO*20),(7*RATIO, RATIO*15),(0, RATIO*15),(0,3*RATIO),(18*RATIO, 3*RATIO),(18*RATIO, 8*RATIO),
             (19*RATIO, 8*RATIO),(19*RATIO,3*RATIO),(WIDTH-RATIO*3,3*RATIO),(WIDTH-RATIO*3,RATIO*15),(RATIO*30,RATIO*15),(RATIO*30,RATIO*20),(WIDTH-RATIO*3,RATIO*20)])
    return(aBoarder)
################################################################
#list of places pacman can move
def canMove(arect):
    can_move = [(11*RATIO,24.5*RATIO),(24*RATIO,24.5*RATIO),(23.5*RATIO, 16*RATIO),(23.5*RATIO, 16.5*RATIO)]
    #begin left and right
    if (arect.x > can_move[0][0] and arect.x < can_move[1][0] and arect.y == can_move[0][1]):
        return True
    #up from going right from start
    elif (arect.y < 406 and arect.y > can_move[2][1] and arect.x == can_move[2][0]):
        return True
    #left from  the top of them middle
    elif (arect.x > can_move[0][0] and arect.x < can_move[3][0] and arect.y == can_move[3][1]):
        return True
    #down on the left in the middle
    elif (arect.y < 406 and arect.y > can_move[2][1] and arect.x == 11.5*RATIO):
        return True
    #right side of tunnel
    elif (arect.x > can_move[2][0] and arect.x < WIDTH and arect.y == 20.5*RATIO):###################################################################
        return True
    #vertical long path on the right
    elif (arect.y > 42 and arect.y < 518 and arect.x == 385):
        return True
    #left and right from vertical long path on the right
    elif (arect.x > 266 and arect.x < 490 and arect.y == 49):
        return True
    #down from the left side of the above move
    elif (arect.y > 49 and arect.y < 126 and arect.x == 273):
        return True
    #left and right top path
    elif (arect.x > 0 and arect.x < 490 and arect.y == 119):#working here atm
        return True
    #very top right down
    elif (arect.y > 49 and arect.y < 182 and arect.x == 483):
        return True
    #top right, third row, left and right
    elif (arect.x > 385 and arect.x < 483 and arect.y == 175):
        return True
    #down from the top right portion of that T in the top right
    elif (arect.y > 119 and arect.y < 182 and arect.x == 329):
        return True
    #up into the T on the right side
    elif (arect.y > 168 and arect.y < 231 and arect.x == 273):
        return True
    #left and right on the right side of the T
    elif (arect.x > 273 and arect.x < 336 and arect.y == 175):
        return True
    #top left third column
    elif (arect.y > 42 and arect.y < 119 and arect.x == 217):
        return True
    #top left first row
    elif (arect.x > 0 and arect.x < 217 and arect.y == 49):
        return True
    #top left second column
    elif (arect.y > 42 and arect.y < 518 and arect.x == 105):
        return True
    #top left first column
    elif (arect.y > 42 and arect.y < 182 and arect.x == 7):
        return True
    #top left third row
    elif (arect.x > 7 and arect.x < 105 and arect.y == 175):
        return True
    #enter the top left T from the top
    elif (arect.y > 119 and arect.y < 182 and arect.x == 161):
        return True
    #left T left and right
    elif (arect.x > 161 and arect.x < 224 and arect.y == 175):
        return True
    #left T up and down the bottom
    elif (arect.y > 175 and arect.y < 238 and arect.x == 217):
        return True
    #top left third row
    elif (arect.x > 0 and arect.x < 161 and arect.y == 287):
        return True
    #bottom half, first row on the left
    elif (arect.x > 0 and arect.x < 224 and arect.y == 399):
        return True
    #top left third row
    elif (arect.y > 399 and arect.y < 462 and arect.x == 7):
        return True
    #first third of second row on the bottom left
    elif (arect.x > 7 and arect.x < 56 and arect.y == 455):
        return True
    #first column bottom left
    elif (arect.y > 455 and arect.y < 518 and arect.x == 49):
        return True
    #bottom left, first fourth, third row
    elif (arect.x > 0 and arect.x < 105 and arect.y == 511):
        return True
    #bottom left, first column, last portion
    elif (arect.y > 511 and arect.y < 574 and arect.x == 7):
        return True
    #very bottom row
    elif (arect.x > 7 and arect.x < 490 and arect.y == 567):
        return True
    #down from the top T on the bottom on the left side
    elif (arect.y > 399 and arect.y < 462 and arect.x == 217):
        return True
    #bottom, second row, second third
    elif (arect.x > 105 and arect.x < 385 and arect.y == 455):
        return True
    #bottom helf, fourth column
    elif (arect.y > 455 and arect.y < 518 and arect.x == 161):
        return True
    #bottom half, third row, second fourth
    elif (arect.x > 161 and arect.x < 224 and arect.y == 511):
        return True
    #bottom half, bottom T, left side going down
    elif (arect.y > 511 and arect.y < 567 and arect.x == 217):
        return True
    #bottom half, first row, second half
    elif (arect.x > 266 and arect.x < 490 and arect.y == 399):
        return True
    #bottom half, top T, down on the right side
    elif (arect.y > 399 and arect.y < 455 and arect.x == 273):
        return True
    #bottom half, fourth quadrant second column
    elif (arect.y > 455 and arect.y < 518 and arect.x == 329):
        return True
    #bottom half, third row, third fourth
    elif (arect.x > 266 and arect.x < 336 and arect.y == 511):
        return True
    #bottom half, second T, down on the right
    elif (arect.y > 511 and arect.y < 567 and arect.x == 273):
        return True
    #bottom half, final column, top half
    elif (arect.y > 399 and arect.y < 462 and arect.x == 483):
        return True
    #bottom half, second row, fourth fourth
    elif (arect.x > 434 and arect.x < 483 and arect.y == 455):
        return True
    #bottom half, second columb from the right
    elif (arect.y > 455 and arect.y < 518 and arect.x == 441):
        return True
    #bottom half, third row, final fourth
    elif (arect.x > 385 and arect.x < 490 and arect.y == 511):
        return True
    #bottom half, up and down bottom right corner
    elif (arect.y > 511 and arect.y < 574 and arect.x == 483):
        return True
    else:
        return False
#################################################################
#drawing the dots
def drawDots():
    dotsX = RATIO+5
    dotsY= 4.5*RATIO#row 1
    for i in range(12):
        singleDot = dot.get_rect()
        singleDot = singleDot.move(dotsX, dotsY)
        dotArray.append(singleDot)
        dotsX += 518/26
        
    dotsX = 20*RATIO+5
    dotsY= 4.5*RATIO#row 1
    for i in range(12):
        singleDot = dot.get_rect()
        singleDot = singleDot.move(dotsX, dotsY)
        dotArray.append(singleDot)
        dotsX += 518/26
    
    dotsX = RATIO+5
    dotsY= 9.5*RATIO#row 2
    for i in range(26):
        singleDot = dot.get_rect()
        singleDot = singleDot.move(dotsX, dotsY)
        dotArray.append(singleDot)
        dotsX += 518/26
        
    dotsX = RATIO+5
    dotsY= 13.5*RATIO#row 3
    for i in range(6):
        singleDot = dot.get_rect()
        singleDot = singleDot.move(dotsX, dotsY)
        dotArray.append(singleDot)
        dotsX += 518/26

    dotsX = 12*RATIO+5
    dotsY= 13.5*RATIO#row 3
    for i in range(4):
        singleDot = dot.get_rect()
        singleDot = singleDot.move(dotsX, dotsY)
        dotArray.append(singleDot)
        dotsX += 518/26

    dotsX = 20*RATIO+5
    dotsY= 13.5*RATIO#row 3
    for i in range(4):
        singleDot = dot.get_rect()
        singleDot = singleDot.move(dotsX, dotsY)
        dotArray.append(singleDot)
        dotsX += 518/26

    dotsX = 28*RATIO+5
    dotsY= 13.5*RATIO#row 3
    for i in range(6):
        singleDot = dot.get_rect()
        singleDot = singleDot.move(dotsX, dotsY)
        dotArray.append(singleDot)
        dotsX += 518/26
        
    dotsX = RATIO+5
    dotsY= 29.5*RATIO#row 4
    for i in range(12):
        singleDot = dot.get_rect()
        singleDot = singleDot.move(dotsX, dotsY)
        dotArray.append(singleDot)
        dotsX += 518/26
        
    dotsX = 20*RATIO+5
    dotsY= 29.5*RATIO#row 4
    for i in range(12):
        singleDot = dot.get_rect()
        singleDot = singleDot.move(dotsX, dotsY)
        dotArray.append(singleDot)
        dotsX += 518/26
        
    dotsX = (RATIO+5) + (518/26)
    dotsY= 33.5*RATIO#row 5
    for i in range(2):
        singleDot = dot.get_rect()
        singleDot = singleDot.move(dotsX, dotsY)
        dotArray.append(singleDot)
        dotsX += 518/26

    dotsX = 8*RATIO+5
    dotsY= 33.5*RATIO#row 5
    for i in range(7):
        singleDot = dot.get_rect()
        singleDot = singleDot.move(dotsX, dotsY)
        dotArray.append(singleDot)
        dotsX += 518/26
        
    dotsX = 20*RATIO+5
    dotsY= 33.5*RATIO#row 5
    for i in range(7):
        singleDot = dot.get_rect()
        singleDot = singleDot.move(dotsX, dotsY)
        dotArray.append(singleDot)
        dotsX += 518/26

    dotsX = 32*RATIO+5
    dotsY= 33.5*RATIO#row 5
    for i in range(2):
        singleDot = dot.get_rect()
        singleDot = singleDot.move(dotsX, dotsY)
        dotArray.append(singleDot)
        dotsX += 518/26
        
    dotsX = RATIO+5
    dotsY= 37.5*RATIO#row 6
    for i in range(6):
        singleDot = dot.get_rect()
        singleDot = singleDot.move(dotsX, dotsY)
        dotArray.append(singleDot)
        dotsX += 518/26
    dotsX = 12*RATIO+5
    dotsY= 37.5*RATIO#row 6
    for i in range(4):
        singleDot = dot.get_rect()
        singleDot = singleDot.move(dotsX, dotsY)
        dotArray.append(singleDot)
        dotsX += 518/26
    dotsX = 20*RATIO+5
    dotsY= 37.5*RATIO#row 6
    for i in range(4):
        singleDot = dot.get_rect()
        singleDot = singleDot.move(dotsX, dotsY)
        dotArray.append(singleDot)
        dotsX += 518/26
    dotsX = 28*RATIO+5
    dotsY= 37.5*RATIO#row 6
    for i in range(6):
        singleDot = dot.get_rect()
        singleDot = singleDot.move(dotsX, dotsY)
        dotArray.append(singleDot)
        dotsX += 518/26

    dotsX = RATIO+5
    dotsY= 41.5*RATIO#row 7
    for i in range(26):
        singleDot = dot.get_rect()
        singleDot = singleDot.move(dotsX, dotsY)
        dotArray.append(singleDot)
        dotsX += 518/26

    # first column
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5, (4.5*RATIO)+518/26)
    dotArray.append(singleDot)

    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5, (4.5*RATIO)+(518/26)*3)
    dotArray.append(singleDot)
    
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5, 11*RATIO)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5, (11*RATIO)+518/26)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5, (29.5*RATIO)+518/26)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5, (31*RATIO)+518/26)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5, (37.5*RATIO)+518/26)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5, (39*RATIO)+518/26)
    dotArray.append(singleDot)
    #second column, which only exists on the bottom
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*2, (33.5*RATIO)+518/26)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*2, (35*RATIO)+518/26)
    dotArray.append(singleDot)

    #third column
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*5, (4.5*RATIO)+518/26)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*5, (4.5*RATIO)+(518/26)*2)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*5, (4.5*RATIO)+(518/26)*3)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*5, (9.5*RATIO)+518/26)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*5, (11*RATIO)+518/26)
    dotArray.append(singleDot)
    
    dotsX = RATIO+5+(518/26)*5
    dotsY= (13.5*RATIO)+518/26
    for i in range(11):
        singleDot = dot.get_rect()
        singleDot = singleDot.move(dotsX, dotsY)
        dotArray.append(singleDot)
        dotsY += 518/26
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*5, (29.5*RATIO)+518/26)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*5, (31*RATIO)+518/26)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*5, (33.5*RATIO)+518/26)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*5, (35*RATIO)+518/26)
    dotArray.append(singleDot)

    #fourth column
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*8, (9.5*RATIO)+518/26)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*8, (11*RATIO)+(518/26))
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*8, (33.5*RATIO)+518/26)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*8, (35*RATIO)+518/26)
    dotArray.append(singleDot)

    #fifth column
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*11, (4.5*RATIO)+518/26)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*11, (4.5*RATIO)+(518/26)*2)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*11, (4.5*RATIO)+(518/26)*3)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*11, (29.5*RATIO)+518/26)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*11, (31*RATIO)+518/26)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*11, (37.5*RATIO)+518/26)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*11, (39*RATIO)+518/26)
    dotArray.append(singleDot)

    #column -1
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*25, 4.5*RATIO+518/26)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*25, 4.5*RATIO+(518/26)*3)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*25, 11*RATIO)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*25, (11*RATIO)+518/26)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*25, (29.5*RATIO)+518/26)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*25, (31*RATIO)+518/26)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*25, (37.5*RATIO)+518/26)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*25, (39*RATIO)+518/26)
    dotArray.append(singleDot)

    #Column -2
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*23, (33.5*RATIO)+518/26)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*23, (35*RATIO)+518/26)
    dotArray.append(singleDot)

    #column -3
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*20, (4.5*RATIO)+518/26)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*20, (4.5*RATIO)+(518/26)*2)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*20, (4.5*RATIO)+(518/26)*3)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*20, (9.5*RATIO)+518/26)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*20, (11*RATIO)+518/26)
    dotArray.append(singleDot)
    
    dotsX = RATIO+5+(518/26)*20
    dotsY= (13.5*RATIO)+518/26
    for i in range(11):
        singleDot = dot.get_rect()
        singleDot = singleDot.move(dotsX, dotsY)
        dotArray.append(singleDot)
        dotsY += 518/26
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*20, (29.5*RATIO)+518/26)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*20, (31*RATIO)+518/26)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*20, (33.5*RATIO)+518/26)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*20, (35*RATIO)+518/26)
    dotArray.append(singleDot)

    #negative fourth column
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*17, (9.5*RATIO)+518/26)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*17, (11*RATIO)+518/26)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*17, (33.5*RATIO)+518/26)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*17, (35*RATIO)+518/26)
    dotArray.append(singleDot)

    # negative fifth column
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*14, (4.5*RATIO)+518/26)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*14, (4.5*RATIO)+(518/26)*2)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*14, (4.5*RATIO)+(518/26)*2)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*14, (29.5*RATIO)+518/26)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*14, (31*RATIO)+518/26)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*14, (37.5*RATIO)+518/26)
    dotArray.append(singleDot)
    singleDot = dot.get_rect()
    singleDot = singleDot.move(RATIO+5+(518/26)*14, (39*RATIO)+518/26)
    dotArray.append(singleDot)

    for i in range(len(dotArray)):
        drawDotArray.append(True)
#################################################################
#drawing BIG dots
def bigDotDrawDots():
    singleDot = bigdot.get_rect()
    singleDot = singleDot.move(12, 33.25*RATIO)
    bigDotArray.append(singleDot)
    singleDot = bigdot.get_rect()
    singleDot = singleDot.move(RATIO+(518/26)*25, 33.25*RATIO)
    bigDotArray.append(singleDot)
    singleDot = bigdot.get_rect()
    singleDot = singleDot.move(12, 5.5*RATIO+(518/26))
    bigDotArray.append(singleDot)
    singleDot = bigdot.get_rect()
    singleDot = singleDot.move(RATIO+(518/26)*25, 5.5*RATIO+(518/26))
    bigDotArray.append(singleDot)
    
    for i in range(len(bigDotArray)):
        bigDotDrawDotArray.append(True)
#################################################################
def pacmanMouth(mouthopening):
    #draws appropriate facing of pacman based on his direction
    ##########################################################
    if(pacmandirection == 0):
        if(mouthopening == 0):
            surface.blit(pacmanright, pacmanrect)
            return  1
        elif(mouthopening == 1):
            surface.blit(pacmanright1, pacmanrect)
            return 2
        else:
            surface.blit(pacmanclosed, pacmanrect)
            return 0
    if(pacmandirection == 1):
        if(mouthopening == 0):
            surface.blit(pacmanleft, pacmanrect)
            return 1
        elif(mouthopening == 1):
            surface.blit(pacmanleft1, pacmanrect)
            return 2
        else:
            surface.blit(pacmanclosed, pacmanrect)
            return 0
    if(pacmandirection == 2):
        if(mouthopening == 0):
            surface.blit(pacmanup, pacmanrect)
            return 1
        elif(mouthopening == 1):
            surface.blit(pacmanup1, pacmanrect)
            return 2
        else:
            surface.blit(pacmanclosed, pacmanrect)
            return 0
    if(pacmandirection == 3):
        if(mouthopening == 0):
            surface.blit(pacmandown, pacmanrect)
            return 1
        elif(mouthopening == 1):
            surface.blit(pacmandown1, pacmanrect)
            return 2
        else:
            surface.blit(pacmanclosed, pacmanrect)
            return 0
    
#################################################################
#################################################################
#MAIN BEGINS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Initialize Pygame
score = 0
pygame.init()
clock = pygame.time.Clock()

# Set surface to 680x480
RATIO = 14#was 16
WIDTH = (RATIO * (28 + 12))#added 1 to the offset to the right edge can be seen
HEIGHT = (RATIO * (36 + 10))
SIZE = (WIDTH, HEIGHT)
surface = pygame.display.set_mode(SIZE)
BLACK = (0, 0, 0)

# Set speed of pacman
XSPEED = 0
YSPEED = 0
speed = [XSPEED, YSPEED]
# set speed of red ghose
XRGSPEED = 0
YRGSPEED = 0
rgspeed = [XRGSPEED, YRGSPEED]

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
redGhost = pygame.image.load("red.jpg")#red ghost
eyes = pygame.image.load("eyes.jpg")#ghost eyes
bbigdot = pygame.image.load("bbigdot.jpg")

#variables for dot creation
dotArray = []#creates an array to hold all the dots
drawDotArray = []#partner array to determine if a dot should be drawn. will make dotArray two dimensional eventually
bigDotArray = []
bigDotDrawDotArray = []
dot = pygame.image.load("dot.jpg")
bigdot = pygame.image.load("bigdot.jpg")

#####################################################################
#This section could be a function, creating the dots
drawDots()
bigDotDrawDots()
########################################################################

pacmanrect = pacmanclosed.get_rect()#initializes pacman rec to closed mouth
pacmanrect = pacmanrect.move(17.5*RATIO, 32.5*RATIO)#Pacmans init place
redGhostRect = redGhost.get_rect()#initializes the red ghosts rectangle
redGhostRect = redGhostRect.move(245, 231)#red ghost start position 245 231
movePath = [(10*RATIO,24.5*RATIO, 20*RATIO, 24.5*RATIO)]
#starts pacmans mouth closed
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
#############################################################################

keyPressed = "none"
pSpeed = [0,0]
dead = False#changes to True if pacman hits a ghost
poweruP = False #whether or not the power up is in effect
poweruPTime = 0 #how much time till the power up expires
##############################################################################
while dead == False:
    ################################
    #START get keyboard input
    #eating.play() #plays sounds
    key = pygame.key.get_pressed()  #checking pressed keys
    
    
    if key[pygame.K_LEFT] and keyPressed != "left":
        keyPressed = "left"
        pSpeed = copy.deepcopy(speed)
        pacmandirection = 1
        speed[1] = 0
        speed[0] = -7
    if key[pygame.K_RIGHT] and keyPressed != "right":
        pSpeed = copy.deepcopy(speed)
        keyPressed = "right"
        pacmandirection = 0
        speed[1] = 0
        speed[0] = 7
    if key[pygame.K_UP] and keyPressed != "up":
        pSpeed = copy.deepcopy(speed)
        keyPressed = "up"
        pacmandirection = 2
        speed[1] = -7
        speed[0] = 0
    if key[pygame.K_DOWN] and keyPressed != "down":
        pSpeed = copy.deepcopy(speed)
        keyPressed = "down"
        pacmandirection = 3
        speed[1] = 7
        speed[0] = 0

    #END get keyboard input
    #################################

    # Exit if window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # Move pacman
    pacmanrect = pacmanrect.move(speed)
    if (canMove(pacmanrect) == True):
        pSpeed = copy.deepcopy(speed)
        #print "x = ", pacmanrect.x
        #print "y = ", pacmanrect.y
    else:
        pacmanrect = pacmanrect.move(-speed[0],-speed[1])
        pacmanrect = pacmanrect.move(pSpeed[0],pSpeed[1])
        if(canMove(pacmanrect) == False):
            speed = [0,0]
            pacmanrect = pacmanrect.move(-pSpeed[0],-pSpeed[1])
        #print "x = ", pacmanrect.x
        #print "y = ", pacmanrect.y

    ###############################################
    #can i eat the dot?
    for i in range(len(dotArray)):
        if(pacmanrect.colliderect(dotArray[i]) and drawDotArray[i] == True):
            score+= 10
            drawDotArray[i] = False
    for i in range(len(bigDotArray)):
        if(pacmanrect.colliderect(bigDotArray[i]) and bigDotDrawDotArray[i] == True):
            #need to set a variable to know if we hit a power pill
            poweruP = True
            poweruPTime = time.clock()
            score += 50
            bigDotDrawDotArray[i] = False
    #now i need a counter to say how long the power up has been running
    ################################################
    if(poweruPTime+10 < time.clock()):
        poweruP = False
    print poweruP

    ##################################################
    # Draw surface
    surface.fill(BLACK)
    #drawing board
    for i in range(len(board)):
        pygame.draw.lines(surface, (0,255,0),True, board[i], 3)
    for i in range(len(boarder)):
        pygame.draw.lines(surface, (0,255,0),False, boarder[i], 3)
    # Display some text
    font = pygame.font.Font(None, 36)
    scoreText = font.render("Score: "+str(score), 1, (255, 255, 255))
    textpos = (50,610)
    #textpos.centerx = surface.get_rect().centerx
    surface.blit(scoreText, textpos)


    #end drawing board
    changeDirection = random.randint(1, 4)
    if(changeDirection == 1):
        rgmove = random.randint(1, 4)
        if(rgmove == 1):
            rgspeed[1] = -7
            rgspeed[0] = 0
        if(rgmove == 2):
            rgspeed[1] = 7
            rgspeed[0] = 0
        if(rgmove == 3):
            rgspeed[1] = 0
            rgspeed[0] = 7
        if(rgmove == 4):
            rgspeed[1] = 0
            rgspeed[0] = -7
    redGhostRect = redGhostRect.move(rgspeed)
    if (canMove(redGhostRect) == True):
        pass
    else:
        redGhostRect = redGhostRect.move(-rgspeed[0],-rgspeed[1])
           
    surface.blit(redGhost, redGhostRect)
    #check to see if pacman hits a ghost
    if(pacmanrect.colliderect(redGhostRect) and poweruP == False):
        dead = True
    if(pacmanrect.colliderect(redGhostRect) and poweruP == True):
        #redGhostRect = redGhostRect.move(245, 231)
        surface.blit(eyes, redGhostRect)# changes the ghost to eyes since it has been eaten
    ############################################################
    
    #Drawing the dots
    for i in range(len(dotArray)):
        if(drawDotArray[i] == True):
            surface.blit(dot, dotArray[i])
    for i in range(len(bigDotArray)):
        if(bigDotDrawDotArray[i] == True):
            if(mouthopening  == 1):
                surface.blit(bigdot, bigDotArray[i])
            else:
                surface.blit(bbigdot, bigDotArray[i])

    mouthopening = pacmanMouth(mouthopening)
    #END drawing pacman in correct direction
    ######################################################################
    pygame.display.flip()
    clock.tick(19)
