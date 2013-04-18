import MySQLdb as mdb
import csv
import sys


con = mdb.connect('localhost', 'root', 
    'matthew 6:33', 'baseball');

with open('/home/david/Documents/GitHub/cccs/ciss/ciss494/csv/wOBA_by_year.csv', 'rb') as csvfile:
	wOBA_per_year = csv.reader(csvfile, delimiter='\t', quotechar='|')
	for row in wOBA_per_year:
		print', '.join(row)

"""with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM master")

    numrows = int(cur.rowcount)

    for i in range(numrows):
        row = cur.fetchone()
        print row[0], row[1]"""