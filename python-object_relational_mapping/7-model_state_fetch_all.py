#!/usr/bin/python3
"""
A script that lists all State objects from the database
hbtn_0e_6_usa.

Usage: ./script_name.py <mysql username> <mysql password>
<database name>

This script:
- Connects to a MySQL database using SQLAlchemy.
- Retrieves all State objects sorted by id in ascending order.
- Prints each State in the format: <id>: <name>.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states(username, password, database):
    """
    Connects to a MySQL database and lists all State objects.
    
    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        database (str): The MySQL database name.
    
    Prints:
        Each State object in the format: <id>: <name>.
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

    # Query all State objects, sorted by id
    states = session.query(State).order_by(State.id).all()

    # Print each state as <id>: <name>
    for state in states:
        print(f"{state.id}: {state.name}")

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

    # List all State objects
    list_states(username, password, database)
