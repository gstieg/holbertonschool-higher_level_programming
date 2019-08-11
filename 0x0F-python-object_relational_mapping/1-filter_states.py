#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv
if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    new = conn.cursor()
    new.execute("SELECT\
    * FROM states WHERE name LIKE 'N%'\
    ORDER BY states.id ASC")
    for row in new.fetchall():
        print(row)
    new.close()
    conn.close()
