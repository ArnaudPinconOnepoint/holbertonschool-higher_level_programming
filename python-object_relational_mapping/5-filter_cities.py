#!/usr/bin/python3
"""Module to list all cities"""
import MySQLdb
import sys


def list_cities(user, pwd, db, name):
    """List all cities from the specified database."""
    # Connect to the MySQL server
    db_connection = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=pwd,
        db=db,
        port=3306
    )

    cursor = db_connection.cursor()

    # Execute the query to select all cities ordered by cities.id
    query = "SELECT cities.id, cities.name, states.name FROM cities " \
            "JOIN states ON cities.state_id = states.id " \
            " WHERE states.name = %s ORDER BY cities.id ASC"

    cursor.execute(query, (name,))

    # Fetch all the results
    cities = cursor.fetchall()

    # Display the results
    for city in cities:
        print(city)

    # Close the cursor and the database connection
    cursor.close()
    db_connection.close()


if __name__ == "__main__":

    # Get the arguments
    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    name = sys.argv[4]

    # List cities
    list_cities(user, pwd, db, name)
