#!/usr/bin/python3

"""
something
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cursor = db.cursor()
    prompt = """SELECT *
             FROM states
             WHERE name = '{}'
             ORDER BY id ASC""".format(argv[4])

    cursor.execute(prompt)

    for row in cursor.fetchall():
        if row[1] == argv[4]:
            print(row)

    cursor.close()
    db.close()
