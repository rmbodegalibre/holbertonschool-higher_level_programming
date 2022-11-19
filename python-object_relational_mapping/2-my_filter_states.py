#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
This script takes 4 arguments: mysql username, mysql password, database name
and state name searched (no argument validation needed)
This uses the module MySQLdb (import MySQLdb)
This script connects to a MySQL server running on localhost at port 3306
This uses format to create the SQL query with the user input
Results are sorted in ascending order by states.id
Results are displayed as they are in the example below
This code do not be executed when imported
"""
import MySQLdb
import sys


def mysql_db():
    conn = ""
    conn = MySQLdb.connect(port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}%'\
                ORDER BY id ASC".format(argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == '__main__':
    mysql_db()
