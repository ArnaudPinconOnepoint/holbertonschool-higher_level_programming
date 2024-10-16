#!/usr/bin/python3
"""
A script that prints the first State object from the
database hbtn_0e_6_usa.

Usage: ./script_name.py <mysql username> <mysql password>
<database name>

This script:
- Connects to a MySQL database using SQLAlchemy.
- Retrieves and prints the first State object ordered by id.
- If the table is empty, prints 'Nothing'.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def print_first_state(username, password, database):
    """
    Connects to a MySQL database and prints the first State object.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        database (str): The name of the MySQL database.

    Prints:
        The first State object in the format: <id>: <name>.
        If no state is found, prints 'Nothing'.
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

    # Query the first State object ordered by id
    first_state = session.query(State).order_by(State.id).first()

    # Print the first state or 'Nothing' if table is empty
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()


if __name__ == "__main__":
    # Ensure correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./script_name.py <mysql username> "
              "<mysql password> <database name>")
        sys.exit(1)

    # Get MySQL credentials and database from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Print the first State object
    print_first_state(username, password, database)
