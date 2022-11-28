#!/usr/bin/python3
"""
This script takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
It takes 4 arguments: mysql username, mysql password and database name
and state name (SQL injection free!)
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
    cur.execute("SELECT cities.name\
                    FROM cities INNER JOIN states\
                    ON states.id = cities.state_id\
                    WHERE states.name = %s", (sys.argv[4],))
    # print(", ".join([result[0] for result in cursor.fetchall()]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    pass
    cur.close()
    conn.close()


if __name__ == '__main__':
    mysql_db()
