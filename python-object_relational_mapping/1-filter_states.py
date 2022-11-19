#!/usr/bin/python3
"""
This script lists all states with a name starting with N (upper N) of
the database hbtn_0e_0_usa:
This script takes 3 arguments: mysql username, mysql password and database
name (no argument validation needed)
This uses the module MySQLdb (import MySQLdb)
This connects to a MySQL server running on localhost at port 3306
Results be sorted in ascending order by states.id
Results be displayed as they are in the example below
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
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
                ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == '__main__':
    mysql_db()
