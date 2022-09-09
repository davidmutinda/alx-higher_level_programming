#!/usr/bin/python3
"""
This module that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost',
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT name FROM cities\
                WHERE cities.state_id = (\
                SELECT id FROM states\
                WHERE name ='{}')\
                ORDER BY cities.id".format(argv[4]))
    rows = cur.fetchall()
    for count, row in enumerate(rows):
        if count < len(rows) - 1:
            print(row[0], end=", ")
        else:
            print(row[0])
