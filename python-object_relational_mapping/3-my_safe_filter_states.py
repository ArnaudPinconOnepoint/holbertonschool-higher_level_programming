#!/usr/bin/python3
"""Module with param"""
import MySQLdb
import sys


def list_states(user, pwd, db, search):
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost",
                         user=user, passwd=pwd, db=db, port=3306)
    cursor = db.cursor()

    # Execute the query
    query = "SELECT * FROM states WHERE BINARY name = %s"\
        "ORDER BY id ASC"
    cursor.execute(query, (search,))

    # Fetch all the results
    states = cursor.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close the cursor and the database connection
    cursor.close()
    db.close()


if __name__ == "__main__":

    # Get the arguments
    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    search = sys.argv[4]

    # List states
    list_states(user, pwd, db, search)
