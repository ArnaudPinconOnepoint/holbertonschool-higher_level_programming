#!/usr/bin/python3
"""To list all states name start with N"""
import MySQLdb
import sys


def list_states(user, pwd, db):
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost",
                         user=user, passwd=pwd, db=db, port=3306)
    cursor = db.cursor()

    # Execute the query to select all states, ordered by states.id
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all the results
    states = cursor.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close the cursor and the database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        sys.exit(1)

    # Get the arguments
    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    # List states
    list_states(user, pwd, db)
