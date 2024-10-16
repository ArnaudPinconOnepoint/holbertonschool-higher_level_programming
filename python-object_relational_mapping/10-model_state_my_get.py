#!/usr/bin/python3
"""
A script that prints the State object with the name passed as an
argument from the database hbtn_0e_6_usa.

Usage: ./script_name.py <mysql username> <mysql password>
<database name> <state name>

This script:
- Connects to a MySQL database using SQLAlchemy.
- Retrieves and prints the State object with the given name.
- If no state with that name exists, prints 'Not found'.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def print_state_by_name(username, password, database, state_name):
    """
    Connects to a MySQL database and prints the State object
    with the given name.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        database (str): The name of the MySQL database.
        state_name (str): The name of the state to search for.

    Prints:
        The id of the State object with the given name.
        If no state is found, prints 'Not found'.
    """
    engine = create_engine(
        'mysql+mysqldb://' + username + ':' + password +
        '@localhost:3306/' + database,
        pool_pre_ping=True
    )

    # Bind the engine to the metadata of Base class
    Base.metadata.bind = engine

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object by name using parameterized queries
    state = session.query(State).filter(State.name == state_name).first()

    # Print the state id or 'Not found' if no state exists
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()


if __name__ == "__main__":
    # Ensure correct number of arguments
    if len(sys.argv) != 5:
        print("Usage: ./script_name.py <mysql username> "
              "<mysql password> <database name> <state name>")
        sys.exit(1)

    # Get MySQL credentials and database from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Print the State object by name
    print_state_by_name(username, password, database, state_name)
