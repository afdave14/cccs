import MySQLdb as mdb
import sys

con = mdb.connect('localhost', 'root', 'matthew 6:33', 'lahman');

with con:

	cur = con.cursor()

	query = raw_input(": ")
	cur.execute(query)

	rows = cur.fetchall()

	for row in rows:
		print row