#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv
if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    new = conn.cursor()
    new.execute("SELECT cities.name\
    FROM cities JOIN states ON cities.state_id=states.id WHERE states.name\
    LIKE BINARY %s ORDER BY cities.id ASC", (argv[4],))
    rows = []
    for row in new.fetchall():
        rows.append(row[0])
    print(", ".join(rows))
    new.close()
    conn.close()
