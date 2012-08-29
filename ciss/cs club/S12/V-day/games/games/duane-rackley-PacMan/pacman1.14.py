#514 changes to 490?
import sys, pygame, copy, time
from pygame.locals import *
import random; random.seed()
##################################################################
mouthopening = 0
#starts pacmans mouth closed
pacmandirection = 0#to determin which mouth direction to draw next
# direction 0 = right
# direction 1 = left
# direction 2 = up
# direction 3 = down
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
             (0,RATIO*36),(0,RATIO*43),(560-RATIO*3,RATIO*43),(560-RATIO*3,RATIO*36),(560-(RATIO*6),RATIO*36),(560-(RATIO*6),RATIO*35),
             (560-RATIO*3,RATIO*35),(560-RATIO*3,RATIO*28),(RATIO*30,RATIO*28),(30*RATIO,RATIO*23),(560-RATIO*3,RATIO*23),])
    #draws top boarder
    aBoarder.append([(0,RATIO*20),(7*RATIO,RATIO*20),(7*RATIO, RATIO*15),(0, RATIO*15),(0,3*RATIO),(18*RATIO, 3*RATIO),(18*RATIO, 8*RATIO),
             (19*RATIO, 8*RATIO),(19*RATIO,3*RATIO),(560-RATIO*3,3*RATIO),(560-RATIO*3,RATIO*15),(RATIO*30,RATIO*15),(RATIO*30,RATIO*20),(560-RATIO*3,RATIO*20)])
    return(aBoarder)
def createHhouse():
    ahouse = []
    ahouse.append([(17*RATIO,19*RATIO),(14*RATIO,19*RATIO),(14*RATIO,24*RATIO),(23*RATIO,24*RATIO),(23*RATIO,19*RATIO),(20*RATIO,19*RATIO)])
    return(ahouse)
    
################################################################
#list of places pacman can move
def canMove(arect):
    can_move = [(11*RATIO,24.5*RATIO),(24*RATIO,24.5*RATIO),(23.5*RATIO, 16*RATIO),(23.5*RATIO, 16.5*RATIO)]
    #inside the ghost house
    if(arect.y > 231 and arect.y < 294 and arect.x == 245):
        return True
    if(arect.x > 196 and arect.x < 294 and arect.y == 287):
        return True
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
    elif (arect.x > can_move[2][0] and arect.x < 539 and arect.y == 20.5*RATIO):#################################################################            
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
    elif (arect.x > 0 and arect.x < 490 and arect.y == 119):
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
    elif (arect.x > -35 and arect.x < 161 and arect.y == 287):
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
def pacmanMouth(mouthopening, pacmanrect, pacmandirection):###############################################added pacman rect here
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
def getDirection(xspeed,yspeed):
    if (xspeed == -7):
        return(1)
    if (xspeed == 7):
        return(0)
    if (yspeed == -7):
        return(2)
    if (yspeed == 7):
        return(3)
    else:
        return(pacmandirection)
#################################################################
def openingSequence(pacmanrect,pacmandirection):
    #i am changing pacman rects x,y coordinates for the opening sequence, i need to ensure i move them back when i want to move from the opening sequence
    #to the start of the game
    mouthopening = 0
    #pacmanrect = pacmanclosed.get_rect()#initializes pacman rec to closed mouth
    runback = False
    pacmanrect.x = -14
    pacmanrect.y = 200
    cobraGhostRect = cobraGhost.get_rect()#initializes the cobra ghosts rectangle
    cobraGhostRect.x = -54
    cobraGhostRect.y = 200
    #end above comment)
    font = pygame.font.Font(None, 50)
    racktext = font.render("RackLeet Software Presents", 1, (0, 178, 238))
    highscores_text = font.render("High Scores (press H)", 1, (0, 178, 238))
    newgame_text = font.render("New Game (press N)", 1, (0, 178, 238))
    puckman_text = font.render("PUCKMAN", 1, (255, 255, 0))
    textpos = (25,0)
    rackleet = pygame.image.load("rackleet4.jpg")
    rackleetRect = rackleet.get_rect()
    surface_rect = rackleetRect.move((WIDTH - rackleetRect.w)/2, (HEIGHT - rackleetRect.h)/2)#where the rect shows up on the screen
    rackleet_image_rect = pygame.Rect(0, 0, 0, rackleetRect.h)
    while rackleet_image_rect.w < rackleetRect.w:
        rackleet_image_rect.w = rackleet_image_rect.w + 1
        surface.blit(rackleet, surface_rect, rackleet_image_rect)
        pygame.display.flip()
    pygame.time.delay(1000)
    surface.fill(BLACK)

    #now we try to move pacman to one side of the screen, eventually he will be being chased by the ghosts, then eat a big dot, then chase and eat the ghosts
    #for this attempt I am going to go ahead and change the speed variable, i MUST return the varialbes to zero to start the game.
    speed[0] = 7
    while(1):
        key = pygame.key.get_pressed()
        if key[pygame.K_n]:
            return(0)
        if key[pygame.K_h]:
            highScores()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        if(pacmanrect.x < 450 and runback == False):
            pacmandirection = 0
            surface.blit(bigdot, (455,210))
            pacmanrect = pacmanrect.move(speed)
            mouthopening = pacmanMouth(mouthopening,pacmanrect, pacmandirection)#################################added pacman rect here
            surface.blit(cobraGhost, cobraGhostRect)
            cobraGhostRect = cobraGhostRect.move(speed)
        else:
            runback = True
        if(runback == True):
            speed[0] = -7
            pacmandirection = 1
            #surface.blit(bigdot, (455,210))
            pacmanrect = pacmanrect.move(speed)
            mouthopening = pacmanMouth(mouthopening,pacmanrect, pacmandirection)#################################added pacman rect here
            surface.blit(eyes, cobraGhostRect)
            cobraGhostRect = cobraGhostRect.move(speed)
    #end previous comment
        surface.blit(racktext, textpos)
        surface.blit(newgame_text, (100,450))
        surface.blit(highscores_text, (100,550))
        surface.blit(puckman_text, (150,100))
        pygame.display.flip()
        pygame.time.delay(50)
        surface.fill(BLACK)
#################################################################
def drawLives(num):
    anX = 300
    for i in range(num-1):
        surface.blit(pacmanleft1, (anX,610))
        anX += 30
    surface.blit(cherry, (500,610))
#################################################################
def pacmanDies(lives):
        pacman_dies.play() #plays sound
        surface.fill(BLACK)
        for i in range(len(dotArray)):
            if(drawDotArray[i] == True):
                surface.blit(dot, dotArray[i])
        for i in range(len(bigDotArray)):
            if(bigDotDrawDotArray[i] == True):
                if(mouthopening  == 1):
                    surface.blit(bigdot, bigDotArray[i])
                else:
                    surface.blit(bbigdot, bigDotArray[i])
        #drawing board
        for i in range(len(board)):
            pygame.draw.lines(surface, (0,255,0),True, board[i], 3)
        for i in range(len(boarder)):
            pygame.draw.lines(surface, (0,255,0),False, boarder[i], 3)
        # Display some text
        font = pygame.font.Font(None, 36)
        scoreText = font.render("Score: "+str(score), 1, (255, 255, 255))
        livesText = font.render("Lives: ", 1, (255, 255, 255))
        drawLives(lives)
        textpos = (50,610)
        surface.blit(scoreText, textpos)
        textpos = (225,610)
        surface.blit(livesText, textpos)
        surface.blit(pacmanup, pacmanrect)
        pygame.display.flip()
        pygame.time.delay(300)
        surface.blit(pacmanup1, pacmanrect)
        pygame.display.flip()
        pygame.time.delay(300)
        surface.blit(dead1, pacmanrect)
        pygame.display.flip()
        pygame.time.delay(300)
        surface.blit(dead2, pacmanrect)
        pygame.display.flip()
        pygame.time.delay(300)
        surface.blit(black, pacmanrect)
        pygame.display.flip()
        pygame.time.delay(300)
        redGhostRect.x = 245
        redGhostRect.y = 231
        pacmanrect.x = 17.5*RATIO
        pacmanrect.y = 32.5*RATIO
        cobraGhostRect.x = 203
        cobraGhostRect.y = 20.5*RATIO
        blueGhostRect.x = 245
        blueGhostRect.y = 20.5*RATIO
        pinkGhostRect.x = 287
        pinkGhostRect.y = 20.5*RATIO
        speed[0] = -7
        speed[1] = 0
        surface.blit(pacmanleft1, pacmanrect)
        pygame.display.flip()
        pygame.time.delay(2000)
        return(lives-1)
#################################################################
def startLevel():
    opening_song.play() #plays sounds
    #Drawing the dots
    for i in range(len(dotArray)):
        if(drawDotArray[i] == True):
            surface.blit(dot, dotArray[i])
    for i in range(len(bigDotArray)):
        surface.blit(bigdot, bigDotArray[i])
    #drawing board
    for i in range(len(board)):
        pygame.draw.lines(surface, (0,255,0),True, board[i], 3)
    for i in range(len(boarder)):
        pygame.draw.lines(surface, (0,255,0),False, boarder[i], 3)
    for i in range(len(hhouse)):
        pygame.draw.lines(surface, (0,255,0),False, hhouse[i], 3)
    # Display some text
    font = pygame.font.Font(None, 36)
    scoreText = font.render("Score: "+str(score), 1, (255, 255, 255))
    livesText = font.render("Lives: ", 1, (255, 255, 255))
    getReadyText = font.render("Get Ready", 1, (255, 255, 0))
    textpos = (50,610)
    surface.blit(scoreText, textpos)
    textpos = (225,610)
    surface.blit(livesText, textpos)
    textpos = (200,345)
    surface.blit(getReadyText, textpos)
    surface.blit(red, redGhostRect)
    surface.blit(blueGhost, blueGhostRect)
    surface.blit(cobraGhost, cobraGhostRect)
    surface.blit(pinkGhost, pinkGhostRect)
    surface.blit(pacmanleft, pacmanrect)
    pygame.display.flip()
    pygame.time.delay(5000)#5000 seemed to work well
################################################################
def getScores():
    font = pygame.font.Font(None, 36)
    f = file("hiscores.txt", "r")
    s = f.read()
    lines = s.split('\n')
    newlines = []
    for x in lines:
        if x != '':
            newlines.append(x)
    lines = newlines
    names = []
    hiscores = []
    for line in lines:
        name, hiscore = line.split(' ')
        names.append(name)
        hiscores.append(hiscore)
    return(names,hiscores)
################################################################
def highScores():
    surface.fill(BLACK)
    font = pygame.font.Font(None, 36)
    names, hiscores = getScores()
    textX = 50
    textY = 100
    for i in range(len(names)):
        randomRColor = random.randint(0,255)
        randomGColor = random.randint(0,255)
        randomBColor = random.randint(0,255)
        highText = font.render(str(i)+".", 1, (randomRColor, randomGColor, randomBColor))
        textpos = (textX-35,textY)
        surface.blit(highText, textpos)
        highText = font.render(names[i], 1, (randomRColor, randomGColor, randomBColor))
        textpos = (textX,textY)
        surface.blit(highText, textpos)
        highText = font.render(hiscores[i], 1, (randomRColor, randomGColor, randomBColor))
        textpos = (textX+250,textY)
        surface.blit(highText, textpos)
        textY += 40

    
    while(1):
        key = pygame.key.get_pressed()
        if key[pygame.K_r]:
            return(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        highText = font.render("HIGHSCORES!!!", 1, (255, 255, 0))
        textpos = (100,0)
        surface.blit(highText, textpos)
        highText = font.render("Return to menu(Press R)", 1, (255, 255, 0))
        textpos = (50,600)
        surface.blit(highText, textpos)
        pygame.display.flip()
        clock.tick(19)
    return(0)
#################################################################
def saveScores(n,h, newscore,s):
    f = file("hiscores.txt", "w")
    for i in range(len(n)):
        if(int(newscore) > int(h[i])):
            for j in reversed(xrange(i,9,1)):
                n[j+1] = copy.deepcopy(n[j])
                h[j+1] = copy.deepcopy(h[j])
            h[i] = str(newscore)
            n[i] = s
            break
    
    for i in range(len(n)):
        s = n[i] + ' ' + h[i] + '\n'
        f.write(s)
#################################################################
def reset(drawDotArray,bigDotDrawDotArray):#,crect,drect,erect
    for i in range(len(bigDotArray)):
        bigDotDrawDotArray[i] = True
    for i in range(len(dotArray)):
        drawDotArray[i] = True
    score = 0
    #return fruitCounter,dotsEaten, lives,bigDotDrawDotArray,drawDotArray,score
    return(0,0,3,bigDotDrawDotArray,drawDotArray,0)
##################################################################
def movexghost(move):
    if(move<18):
        return -7,0
    if(move >= 18 and move < 45):
        return 0,7
    if(move >= 45 and move < 67):
        return -7,0
    if(move >= 67 and move < 85):
        return 0,7
    if(move >= 85 and move < 95):
        return 7,0
    if(move >= 95 and move < 105):
        return 0,7
    if(move >= 105 and move < 115):
        return 7,0
    if(move >= 115 and move < 147):
        return 0,-7
    if(move >= 147 and move < 157):
        return 7,0
    if(move >= 157 and move < 167):
        return 0,-7
    if(move >= 167 and move < 179):
        return 7,0
    else:
        return 0,0
##################################################################
def moveblueghost(counter, blueGhostRect):
    flag = True
    if(counter < 8):
        blueGhostRect = blueGhostRect.move(0,-acceleration)
    elif(counter < 18):
        blueGhostRect = blueGhostRect.move(acceleration,0)
    else:
        blueXD = pacmanrect.x - blueGhostRect.x
        blueYD = pacmanrect.y - blueGhostRect.y

        if(blueXD > 0 and blueYD > 0):
            blueGhostRect = blueGhostRect.move(acceleration,0)
            if (canMove(blueGhostRect) != True):
                blueGhostRect = blueGhostRect.move(-acceleration,0)
                blueGhostRect = blueGhostRect.move(0,acceleration)
                if (canMove(blueGhostRect) != True):
                    blueGhostRect = blueGhostRect.move(0,-acceleration)
                    blueGhostRect = blueGhostRect.move(-acceleration,0)
                    if (canMove(blueGhostRect) != True):
                        blueGhostRect = blueGhostRect.move(acceleration,0)
                        flag = False
        if((blueXD > 0 and blueYD < 0) or flag == False):
            flag = True
            blueGhostRect = blueGhostRect.move(acceleration,0)
            if (canMove(blueGhostRect) != True):
                blueGhostRect = blueGhostRect.move(-acceleration,0)
                blueGhostRect = blueGhostRect.move(0,-acceleration)
                if (canMove(blueGhostRect) != True):
                    blueGhostRect = blueGhostRect.move(0,acceleration)
                    blueGhostRect = blueGhostRect.move(-acceleration,0)
                    if (canMove(blueGhostRect) != True):
                        blueGhostRect = blueGhostRect.move(acceleration,0)
                        flag = False
        if((blueXD < 0 and blueYD > 0) or flag == False):
            flag = True
            blueGhostRect = blueGhostRect.move(-acceleration,0)
            if (canMove(blueGhostRect) != True):
                blueGhostRect = blueGhostRect.move(acceleration,0)
                blueGhostRect = blueGhostRect.move(0,acceleration)
                if (canMove(blueGhostRect) != True):
                    blueGhostRect = blueGhostRect.move(0,-acceleration)
                    blueGhostRect = blueGhostRect.move(acceleration,0)
                    if (canMove(blueGhostRect) != True):
                        blueGhostRect = blueGhostRect.move(-acceleration,0)
                        flag = False
        if((blueXD < 0 and blueYD <= 0) or flag == False):
            blueGhostRect = blueGhostRect.move(-acceleration,0)
            if (canMove(blueGhostRect) != True):
                blueGhostRect = blueGhostRect.move(acceleration,0)
                blueGhostRect = blueGhostRect.move(0,-acceleration)
                if (canMove(blueGhostRect) != True):
                    blueGhostRect = blueGhostRect.move(0,acceleration)
                    blueGhostRect = blueGhostRect.move(acceleration,0)
                    if (canMove(blueGhostRect) != True):
                        blueGhostRect = blueGhostRect.move(-acceleration,0)
        if(blueXD == 0 and blueYD > 0):
            blueGhostRect = blueGhostRect.move(0,acceleration)
            if (canMove(blueGhostRect) != True):
                blueGhostRect = blueGhostRect.move(0,-acceleration)
        if(blueXD == 0 and blueYD < 0):
            blueGhostRect = blueGhostRect.move(0,-acceleration)
            if (canMove(blueGhostRect) != True):
                blueGhostRect = blueGhostRect.move(0,acceleration)
                
##        if(blueXD < 0 and flag == False):
##            blueGhostRect = blueGhostRect.move(-acceleration,0)
##            if (canMove(blueGhostRect) != True):
##                blueGhostRect = blueGhostRect.move(acceleration,0)
##            else:
##                flag = True
##        if(blueYD > 0 and flag == False):
##            blueGhostRect = blueGhostRect.move(0,acceleration)
##            if (canMove(blueGhostRect) != True):
##                blueGhostRect = blueGhostRect.move(0,-acceleration)
##            else:
##                flag = True
##        if(blueYD < 0 and flag == False):
##            blueGhostRect = blueGhostRect.move(0,-acceleration)
##            if (canMove(blueGhostRect) != True):
##                blueGhostRect = blueGhostRect.move(0,acceleration)
    return(blueGhostRect)
    
    
#################################################################
#################################################################
#MAIN BEGINS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Initialize Pygame
score = 0
pygame.init()
clock = pygame.time.Clock()

# Set surface to 680x480
RATIO = 14#was 16
WIDTH = (RATIO * (28 + 10))#added 1 to the offset to the right edge can be seen
HEIGHT = (RATIO * (36 + 10))
SIZE = (WIDTH, HEIGHT)
surface = pygame.display.set_mode(SIZE)
BLACK = (0, 0, 0)

# Set speed of pacman
XSPEED = 0
YSPEED = 0
speed = [XSPEED, YSPEED]
# set speed of red ghost
XRGSPEED = 0
YRGSPEED = 0
xrgspeed = []
xrgspeed.append(0)
xrgspeed.append(0)
xrgspeed.append(0)
xrgspeed.append(0)
yrgspeed = []
yrgspeed.append(0)
yrgspeed.append(0)
yrgspeed.append(0)
yrgspeed.append(0)

# Load pacman images
pacmanright = pygame.image.load("pics/pmor.jpg")#open right
pacmanright1 = pygame.image.load("pics/pmoor.jpg")#big open right
pacmanclosed = pygame.image.load("pics/pmc.jpg")#closed
pacmandown = pygame.image.load("pics/pmod.jpg")#open down
pacmandown1 = pygame.image.load("pics/pmood.jpg")#big open down
pacmanleft = pygame.image.load("pics/pmol.jpg")#open left
pacmanleft1 = pygame.image.load("pics/pmool.jpg")#big open left
pacmanup = pygame.image.load("pics/pmou.jpg")#open up
pacmanup1 = pygame.image.load("pics/pmoou.jpg")#bigopen up
redGhost = pygame.image.load("pics/red.jpg")#red ghost
blueGhost = pygame.image.load("pics/blue.jpg")#red ghost
pinkGhost = pygame.image.load("pics/pink.jpg")#red ghost
cobraGhost = pygame.image.load("pics/cobra.jpg")#red ghost
eyes = pygame.image.load("pics/eyes.jpg")#ghost eyes
bbigdot = pygame.image.load("pics/bbigdot.jpg")
darkblueGhost = pygame.image.load("pics/darkblue.jpg")
whiteGhost = pygame.image.load("pics/whiteghost.jpg")
cherry = pygame.image.load("pics/fruit/cherry.png")
dead1 = pygame.image.load("pics/dead1.jpg")
dead2 = pygame.image.load("pics/dead2.jpg")
black = pygame.image.load("pics/black.jpg")

###########################################################
#because the ghosts can change into eyes, i need a variable for each that says whether or not i am supposed to draw eyes or draw ghost, those follow
red = redGhost
blue = blueGhost
pink = pinkGhost
cobra = cobraGhost

#variables for dot creation
dotArray = []#creates an array to hold all the dots
drawDotArray = []#partner array to determine if a dot should be drawn. could make dotArray two dimensional eventually
bigDotArray = []
bigDotDrawDotArray = []
dot = pygame.image.load("pics/dot.jpg")#little dot image
bigdot = pygame.image.load("pics/bigdot.jpg")#big dot image

#####################################################################
#Draw ALL of the dots onto the screen
drawDots()
bigDotDrawDots()
########################################################################
#Create all of the RECTS neeeded
pacmanrect = pacmanclosed.get_rect()#initializes pacman rec to closed mouth
pacmanrect = pacmanrect.move(17.5*RATIO, 32.5*RATIO)#Pacmans init place
redGhostRect = redGhost.get_rect()#initializes the red ghosts rectangle
redGhostRect = redGhostRect.move(245, 231)#red ghost start position 245 231
cobraGhostRect = cobraGhost.get_rect()#initializes the cobra ghosts rectangle
cobraGhostRect = cobraGhostRect.move(203, 20.5*RATIO)#cobra ghost start position 245 231
blueGhostRect = blueGhost.get_rect()#initializes the cobra ghosts rectangle
blueGhostRect = blueGhostRect.move(245, 20.5*RATIO)#cobra ghost start position 245 231
pinkGhostRect = pinkGhost.get_rect()#initializes the cobra ghosts rectangle
pinkGhostRect = pinkGhostRect.move(287, 20.5*RATIO)#cobra ghost start position 245 231
movePath = [(10*RATIO,24.5*RATIO, 20*RATIO, 24.5*RATIO)]# i think i can delete this...kinda sad i dont know
fruitRect = cherry.get_rect()#initializes fruit rect
fruitRect = fruitRect.move(17.5*RATIO, 24.5*RATIO)#cobra ghost start position 245 231


# Load sound
eating = pygame.mixer.Sound("pacman_wav/eating.short.wav")
opening_song = pygame.mixer.Sound("pacman_wav/opening_song.wav")
pacman_dies = pygame.mixer.Sound("pacman_wav/pacman_dies.wav")

############################################################################
#Initialize the board
board = []
board = createBoard()
boarder = []
boarder = createBoarder()
#Haunted House, where the ghosts start
hhouse = []
hhouse = createHhouse()
#############################################################################

keyPressed = "none"
pSpeed = [0,0]
dead = False#changes to True if pacman hits a ghost and not under power up effect
poweruP = False #whether or not the power up is in effect
poweruPTime = 0 #how much time till the power up expires
##############################################################################
openingSequence(pacmanrect,pacmandirection)
pacmanrect.x = 17.5*RATIO
pacmanrect.y = 32.5*RATIO
startLevel()
speed[0] = -7
speed[1] = 0
lives = 3#number of lives pacman has
dotsEaten = 0
fruitCounter = 0
ghostsEaten = 1
ghostPoweruP = []
#the ghostpowerup is to know if the ghost has been eaten during that power up phase, they return to being able to kill pacman,
#and they wont give additional points for being eaten.
ghostPoweruP.append(False)#red
ghostPoweruP.append(False)#cobra
ghostPoweruP.append(False)#blue
ghostPoweruP.append(False)#pink
testmovevalue = 0
bluemove = 0
while lives > 0:#this was while dead == false
    ################################
    #START get keyboard input       
    key = pygame.key.get_pressed()  #checking pressed keys
    
    
    if key[pygame.K_LEFT] and keyPressed != "left":
        keyPressed = "left"
        pSpeed = copy.deepcopy(speed)
        #pacmandirection = 1
        speed[1] = 0
        speed[0] = -7
    if key[pygame.K_RIGHT] and keyPressed != "right":
        pSpeed = copy.deepcopy(speed)
        keyPressed = "right"
        #pacmandirection = 0
        speed[1] = 0
        speed[0] = 7
    if key[pygame.K_UP] and keyPressed != "up":
        pSpeed = copy.deepcopy(speed)
        keyPressed = "up"
        #pacmandirection = 2
        speed[1] = -7
        speed[0] = 0
    if key[pygame.K_DOWN] and keyPressed != "down":
        pSpeed = copy.deepcopy(speed)
        keyPressed = "down"
        #pacmandirection = 3
        speed[1] = 7
        speed[0] = 0

    #END get keyboard input
    #################################

    # Exit if window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
##############################################################################################
    # Move pacman
    pacmanrect = pacmanrect.move(speed)
    if (canMove(pacmanrect) == True):
        pSpeed = copy.deepcopy(speed)
        pacmandirection = getDirection(speed[0],speed[1])
        if(pacmanrect.x == 532):
            pacmanrect.x = -21
            speed[0] = 7
            pacmandirection = getDirection(speed[0],speed[1])
        elif(pacmanrect.x == -21):
            pacmanrect.x = 532
            speed[0] = -7
            pacmandirection = getDirection(speed[0],speed[1])
    else:
        pacmanrect = pacmanrect.move(-speed[0],-speed[1])
        pacmanrect = pacmanrect.move(pSpeed[0],pSpeed[1])
        pacmandirection = getDirection(pSpeed[0],pSpeed[1])
        if(canMove(pacmanrect) == False):
            speed = [0,0]
            pacmanrect = pacmanrect.move(-pSpeed[0],-pSpeed[1])      

    ###############################################
    #can i eat the dot?
    for i in range(len(dotArray)):
        if(pacmanrect.colliderect(dotArray[i]) and drawDotArray[i] == True):
            if pygame.mixer.get_busy() == False:
                pass
                eating.play() #plays sounds
            score+= 10
            drawDotArray[i] = False
            dotsEaten += 1
    for i in range(len(bigDotArray)):
        if(pacmanrect.colliderect(bigDotArray[i]) and bigDotDrawDotArray[i] == True):
            #need to set a variable to know if we hit a power pill
            poweruP = True
            poweruPTime = time.clock()
            score += 50
            dotsEaten += 1
            bigDotDrawDotArray[i] = False
    #now i need a counter to say how long the power up has been running
    ################################################
    if(poweruPTime+6 < time.clock()):
        ghostsEaten = 1
        poweruP = False
    #print poweruP

    ##################################################
    # Draw surface
    surface.fill(BLACK)
    surface.set_colorkey((0,0,0))
#################################################################################
    ###############################################
    #can i eat the FRUIT
    if(dotsEaten > 30 and fruitCounter == 0):
        surface.blit(cherry, fruitRect)
        if(pacmanrect.colliderect(fruitRect)):
            score += 100
            fruitCounter = 1
    if(dotsEaten > 100 and fruitCounter == 1):
        surface.blit(cherry, fruitRect)
        if(pacmanrect.colliderect(fruitRect)):
            score += 100
            fruitCounter = 2
                                         
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
    #drawing board
    for i in range(len(board)):
        pygame.draw.lines(surface, (0,255,0),True, board[i], 3)
    for i in range(len(boarder)):
        pygame.draw.lines(surface, (0,255,0),False, boarder[i], 3)
    for i in range(len(hhouse)):
        pygame.draw.lines(surface, (0,255,0),False, hhouse[i], 3)
    # Display some text
    font = pygame.font.Font(None, 36)
    scoreText = font.render("Score: "+str(score), 1, (255, 255, 255))
    livesText = font.render("Lives: ", 1, (255, 255, 255))
    titleText = font.render("Puckman                        Duane Rackley II", 1, (255, 255, 0))
    textpos = (50,610)
    surface.blit(scoreText, textpos)
    textpos = (225,610)
    surface.blit(livesText, textpos)
    textpos = (0,0)
    surface.blit(titleText, textpos)


    #end drawing board
    #being random ghost movements
#####################################################################################################
    if(poweruP == True):
        acceleration = 3.5
    else:
        acceleration = 7
    for i in range(4):
        changeDirection = random.randint(1, 4)
        if(changeDirection == 1):
            rgmove = random.randint(1, 4)
            if(rgmove == 1):
                xrgspeed[i] = -acceleration
                yrgspeed[i] = 0
            if(rgmove == 2):
                xrgspeed[i] = acceleration
                yrgspeed[i] = 0
            if(rgmove == 3):
                xrgspeed[i] = 0
                yrgspeed[i] = acceleration
            if(rgmove == 4):
                xrgspeed[i] = 0
                yrgspeed[i] = -acceleration
    cobraGhostRect = cobraGhostRect.move(xrgspeed[3],yrgspeed[3])
    
    #blueGhostRect = blueGhostRect.move(xrgspeed[1],yrgspeed[1])
    pinkGhostRect = pinkGhostRect.move(xrgspeed[2],yrgspeed[2])

    
    thismove, thatmove = movexghost(testmovevalue)
    redGhostRect = redGhostRect.move(thismove,thatmove)
    if (canMove(redGhostRect) != True):
        redGhostRect = redGhostRect.move(-thismove,-thatmove)
    #thismove, thatmove = moveblueghost(testmovevalue)
##    blueGhostRect = blueGhostRect.move(thismove,thatmove)
##    if (canMove(blueGhostRect) != True):
##        blueGhostRect = blueGhostRect.move(-thismove,-thatmove)
    blueGhostRect = moveblueghost(bluemove, blueGhostRect)
        
    testmovevalue += 1
    bluemove += 1
    if(testmovevalue == 180):
        testmovevalue = 0
############################################################################################################################################################### 
    if (canMove(redGhostRect) == True):
        pass
    else:
        redGhostRect = redGhostRect.move(-thismove,-thatmove)
    if (canMove(pinkGhostRect) == True):
        pass
    else:
        pinkGhostRect = pinkGhostRect.move(-xrgspeed[2],-yrgspeed[2])
    if (canMove(cobraGhostRect) == True):
        pass
    else:
        cobraGhostRect = cobraGhostRect.move(-xrgspeed[3],-yrgspeed[3])

######################################################################################################
    #end random ghost movements
           
    #check to see if pacman hits a ghost
    #moved the check to see if pacman should die from collision to the last line
    if(pacmanrect.colliderect(redGhostRect) and poweruP == True):
        score += (2**ghostsEaten)*100
        ghostsEaten += 1
        redGhostRect.x = 245#245
        redGhostRect.y = 231#231
        red = eyes
    if(pacmanrect.colliderect(blueGhostRect) and poweruP == True):
        score += (2**ghostsEaten)*100
        ghostsEaten += 1
        blueGhostRect.x = 245#245
        blueGhostRect.y = 231#231
        blue = eyes
    if(pacmanrect.colliderect(pinkGhostRect) and poweruP == True):
        score += (2**ghostsEaten)*100
        ghostsEaten += 1
        pinkGhostRect.x = 245#245
        pinkGhostRect.y = 231#231
        pink = eyes
    if(pacmanrect.colliderect(cobraGhostRect) and poweruP == True):
        score += (2**ghostsEaten)*100
        ghostsEaten += 1
        cobraGhostRect.x = 245#245
        cobraGhostRect.y = 231#231
        cobra = eyes
    if(poweruP == False):#this means the ghost returns to a ghost when the power up ends, eventually it will be for when he returns to the house
        blue = blueGhost
        pink = pinkGhost
        cobra = cobraGhost
        red = redGhost
    if poweruP == True and mouthopening == 1 and poweruPTime+4 < time.clock():
        red = whiteGhost
        pink = whiteGhost
        cobra = whiteGhost
        blue = whiteGhost
    elif poweruP == True and mouthopening != 1 and poweruPTime+4 < time.clock():
        red = darkblueGhost
        pink = darkblueGhost
        cobra = darkblueGhost
        blue = darkblueGhost
    elif poweruP == True:
        red = darkblueGhost
        pink = darkblueGhost
        cobra = darkblueGhost
        blue = darkblueGhost
    surface.blit(red, redGhostRect)
    surface.blit(blue, blueGhostRect)
    surface.blit(cobra, cobraGhostRect)
    surface.blit(pink, pinkGhostRect)
    ############################################################

    mouthopening = pacmanMouth(mouthopening, pacmanrect, pacmandirection)
    drawLives(lives)
    #END drawing pacman in correct direction
    ######################################################################
    if(pacmanrect.colliderect(redGhostRect) and poweruP == False):
        testmovevalue = 0
        bluemove = 0
        lives = pacmanDies(lives)
    elif(pacmanrect.colliderect(cobraGhostRect) and poweruP == False):
        testmovevalue = 0
        bluemove = 0
        lives = pacmanDies(lives)
    elif(pacmanrect.colliderect(blueGhostRect) and poweruP == False):
        testmovevalue = 0
        bluemove = 0
        lives = pacmanDies(lives)
    elif(pacmanrect.colliderect(pinkGhostRect) and poweruP == False):
        testmovevalue = 0
        bluemove = 0
        lives = pacmanDies(lives)
    pygame.display.flip()
    clock.tick(19)
    
    ###Begin code for 0 lives
    if(lives == 0):
        font = pygame.font.Font(None, 80)
        GAMEOVERText = font.render("GAME OVER", 1, (255, 0, 0))
        textpos = (100,200)
        surface.blit(GAMEOVERText, textpos)
        pygame.display.flip()
        pygame.time.delay(2000)
        namess, high = getScores()
        if(int(score) > int(high[9])):
            font = pygame.font.Font(None, 40)
            highscorerText = font.render("Enter your name high scorer", 1, (255, 255, 0))
            textpos = (75,300)
            surface.blit(highscorerText, textpos)
            pygame.display.flip()
            scorerName = raw_input("Enter your name, high scorer")
            saveScores(namess,high, score, scorerName)
            highScores()
        else:
            highScores()
        fruitCounter,dotsEaten, lives,bigDotDrawDotArray,drawDotArray,score = reset(drawDotArray,bigDotDrawDotArray)
        openingSequence(pacmanrect,pacmandirection)
        pacmanrect.x = 17.5*RATIO
        pacmanrect.y = 32.5*RATIO
        redGhostRect.x = 245
        redGhostRect.y = 231
        cobraGhostRect.x = 203
        cobraGhostRect.y = 20.5*RATIO
        blueGhostRect.x = 245
        blueGhostRect.y = 20.5*RATIO
        pinkGhostRect.x = 287
        pinkGhostRect.y = 20.5*RATIO
        startLevel()
        speed[0] = -7
        speed[1] = 0
        testmovevalue = 0
        bluemove = 0
