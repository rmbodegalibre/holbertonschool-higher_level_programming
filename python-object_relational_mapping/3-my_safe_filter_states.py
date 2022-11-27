#!/usr/bin/python3
"""
This script takes in arguments and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument. But this time, write one that
is safe of MySQL injections!
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
    cur.execute("SELECT * FROM states WHERE name =%s", (sys.argv[4],))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    pass
    cur.close()
    conn.close()


if __name__ == '__main__':
    mysql_db()