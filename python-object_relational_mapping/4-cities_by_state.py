#!/usr/bin/python3
"""Module"""
import MySQLdb
import sys


def list_cities(user, pwd, db, search):
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost",
                         user=user, passwd=pwd, db=db, port=3306)
    cursor = db.cursor()

    # Execute the query
    query = "SELECT * FROM cities"
    cursor.execute(query, (search,))

    # Fetch all the results
    cities = cursor.fetchall()

    # Display the results
    for city in cities:
        print(city)

    # Close the cursor and the database connection
    cursor.close()
    db.close()


if __name__ == "__main__":

    # Get the arguments
    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    # List states
    list_cities(user, pwd, db)
