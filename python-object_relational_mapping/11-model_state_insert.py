#!/usr/bin/python3
"""
A script that adds the State object "Louisiana" to the database
hbtn_0e_6_usa.

Usage: ./script_name.py <mysql username> <mysql password>
<database name>

This script:
- Connects to a MySQL database using SQLAlchemy.
- Adds a new State object "Louisiana" to the states table.
- Prints the new state's id after creation.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def add_state(username, password, database):
    """
    Connects to a MySQL database and adds the State object
    "Louisiana".

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        database (str): The name of the MySQL database.

    Prints:
        The id of the new State object after creation.
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

    # Create a new State object
    new_state = State(name="Louisiana")

    # Add and commit the new state to the database
    session.add(new_state)
    session.commit()

    # Print the new state's id
    print(new_state.id)

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

    # Add the State object "Louisiana"
    add_state(username, password, database)
