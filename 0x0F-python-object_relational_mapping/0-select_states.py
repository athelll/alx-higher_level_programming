#!/usr/bin/python3
"""
retruns sql query
result
"""

# imports
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    # cursor instance
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states ORDER BY id ASC;')

    # prints the rowa
    for row in cursor.fetchall():
        print(row)

    # closes connections
    cursor.close()
    db.close()
