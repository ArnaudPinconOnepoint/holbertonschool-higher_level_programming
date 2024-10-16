#!/usr/bin/python3
"""Module to list all cities"""
import MySQLdb
import sys


def list_cities(user, pwd, db, state_name):
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
    query = """
        SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """

    # Pass a tuple containing the state name to avoid SQL injection
    cursor.execute(query, (state_name,))

    # Fetch all the results
    cities = cursor.fetchall()

    # Check if any results were returned
    if cities:
        # Join all the city names with a comma and a space, then print them
        print(", ".join([city[0] for city in cities]))
    else:
        # If no cities were found, print an empty string
        print("")

    # Close the cursor and the database connection
    cursor.close()
    db_connection.close()


if __name__ == "__main__":

    # Ensure the correct number of arguments are provided
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py <mysql_username> <mysql_password> <database_name> <state_name>")
        sys.exit(1)

    # Get the arguments
    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]

    # List cities
    list_cities(user, pwd, db, state_name)
