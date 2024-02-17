#!/usr/bin/python3
"""lists all states from db hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    sto = db.cursor()
    sto.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")
    lines = sto.fetchall()
    for l in lines:
        print(l)
    sto.close()
    db.close()
