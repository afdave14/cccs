import MySQLdb as mdb
import sys


con = mdb.connect('localhost', 'root', 
    'matthew 6:33', 'lahman');

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM master")

    numrows = int(cur.rowcount)

    for i in range(numrows):
        row = cur.fetchone()
        print row[0], row[1]