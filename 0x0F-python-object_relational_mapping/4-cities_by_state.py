#!/usr/bin/python3
"""lists all states from db hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    sto = db.stosor()
    sto.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    lines = sto.fetchall()
    for l in lines:
        print(l)
    sto.close()
    db.close()