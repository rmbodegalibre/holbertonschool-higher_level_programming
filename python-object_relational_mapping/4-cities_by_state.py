#!/usr/bin/python3
"""
This script lists all cities of the database hbtn_0e_0_usa
It takes 3 arguments: mysql username, mysql password and database name
It uses the module MySQLdb (import MySQLdb)
It connects to a MySQL server running on localhost at port 3306
Results are sorted in ascending order by cities.id
It uses only execute() once
This code is not executed when imported
"""
import MySQLdb
import sys


def mysql_db():
    conn = ""
    conn = MySQLdb.connect(port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                    FROM states RIGHT JOIN cities\
                    ON states.id = cities.state_id")
    # [print(state) for state in cursor.fetchall()]
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    pass
    cur.close()
    conn.close()


if __name__ == '__main__':
    mysql_db()
