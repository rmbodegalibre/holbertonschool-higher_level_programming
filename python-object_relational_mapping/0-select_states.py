#!/usr/bin/python3
"""
This script lists all states of the database hbtn_0e_0_usa:
-This script takes 3 arguments: mysql username, mysql password and
 database name (no argument validation needed)
-use the module MySQLdb (import MySQLdb)
-This script connects to a MySQL server running on localhost at port 3306
-Results are sorted in ascending order by states.id
-Results are displayed as the example: (1, 'California')
-This code should not be executed when imported
"""
import MySQLdb
import sys


if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
