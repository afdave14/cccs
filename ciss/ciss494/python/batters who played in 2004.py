import MySQLdb as mdb
import sys

con = mdb.connect('localhost', 'root', 'matthew 6:33', 'baseball');

with con:

	cur = con.cursor()
	cur.execute("SELECT playerID FROM Batting WHERE yearID = 2004")

	numrows = int(cur.rowcount)

	for i in range(numrows):
		row = cur.fetchone()
		print row[0]