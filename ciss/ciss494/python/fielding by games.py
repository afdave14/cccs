import MySQLdb as mdb
import sys

con = mdb.connect('localhost', 'root', 'matthew 6:33', 'baseball');

with con:

	cur = con.cursor()
	cur.execute("SELECT playerID, yearID, stint, teamID, lgID, POS, G FROM Fielding")

	numrows = int(cur.rowcount)

	for i in range(numrows):
		row = cur.fetchone()
		print row[0], row[1], row[2], row[3], row[4], row[5]