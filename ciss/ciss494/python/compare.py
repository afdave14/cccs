import MySQLdb as mdb
import math
import sys

con = mdb.connect('localhost', 'root', 'matthew 6:33', 'baseball');



def getSSDist(x, y):
    ss = \
    Gdif(x[3], y[3]) + \
    ABdif(x[4], y[4]) + \
    Rdif(x[5], y[5])

    return ss





def Gdif(x, g):
    return math.fabs(x - g) / 20    

def ABdif(x, ab):
    return math.fabs(x - ab) / 75

def Rdif(x, r):
    return math.fabs(x - r) / 10

def Hdif(x, h):
    return math.fabs(x - h) / 15

def Doubdif(x, doub):
    return math.fabs(x - doub) / 5

def Tripdif(x, trip):
    return math.fabs(x - trip) / 4

def HRdif(x, hr):
    return math.fabs(x - hr) / 2

def RBIdif(x, rbi):
    return math.fabs(x - rbi) / 10

def BBdif(x, bb):
    return math.fabs(x - bb) / 25

def SOdif(x, so):
    return math.fabs(x - so) / 150

def SBdif(x, sb):
    return math.fabs(x - sb) / 20

def BAdif(x, ba):
    return math.fabs(x - ba) / .001

def SLGdif(x, slg):
    return math.fabs(x - slg) / .002




def containsNone(list):
    for x in range(0, len(list)):
        if list[x] == None:
            return True
    return False


with con:

    cur = con.cursor()
    SELECT_First = "select nameFirst as First, nameLast as Last, yearID as Year, \
    G, AB, R, H, 2B, 3B, HR, RBI, BB, SO, SB, (H / AB) as AVG, \
    (((H - 2B - 3B - HR) + (2 * 2B) + (3 * 3B) + (4 * HR)) / AB) as SLG \
    from Master m join Batting b \
    on m.playerID = b.playerID \
    where yearID = 2001 and nameFirst = \"Ichiro\" and nameLast = \"Suzuki\""
    cur.execute(SELECT_First)

    currPlayer = cur.fetchone()
    for x in range(0, len(currPlayer)):
    	print currPlayer[x],
    print

    SELECT_Rest = "select nameFirst as First, nameLast as Last, yearID as Year, \
    G, AB, R, H, 2B, 3B, HR, RBI, BB, SO, SB, (H / AB) as AVG, \
    (((H - 2B - 3B - HR) + (2 * 2B) + (3 * 3B) + (4 * HR)) / AB) as SLG \
    from Master m join Batting b \
    on m.playerID = b.playerID \
    where yearID = 2001"
    cur.execute(SELECT_Rest)

    numrows = int(cur.rowcount)

    for i in range(numrows):
        next = cur.fetchone()

        if containsNone(next) == False:
            SSDist = getSSDist(currPlayer, next)
            print round(SSDist, 1)