#!/usr/bin/python3
"""
prints the
reuslt in formated way
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=argv[1],
                               passwd=argv[2],
                               db=argv[3])

    cursor = database.cursor()
    prompt = """SELECT cities.name
                FROM cities
                WHERE cities.state_id = (
                    SELECT id
                    FROM states
                    WHERE name = %s
                    LIMIT 1
                )
                GROUP BY cities.name"""

    cursor.execute(prompt, (argv[4],))

    result = ", ".join(["{}".format(x[0]) for x in cursor.fetchall()])
    print(result)

    cursor.close()
    database.close()
