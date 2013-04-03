import _mysql
import sys

con = None

try:
	con = _mysql.connect('localhost', 'root', 'matthew 6:33', 'lahman')

	con.query("SELECT VERSION()")
	result = con.use_result()

	print "MySQL version: %s" % \
	result.fetch_row()[0]

except _mysql.Error, e:

	print "Error %d: %s" % (e.args[0], e.args[1])
	sys.exit(1)

finally:

	if con:
		con.close()