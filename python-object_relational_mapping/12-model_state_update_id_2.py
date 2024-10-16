#!/usr/bin/python3
"""
A script that changes the name of a State object in the
database hbtn_0e_6_usa.

Usage: ./script_name.py <mysql username> <mysql password>
<database name>

This script:
- Connects to a MySQL database using SQLAlchemy.
- Updates the State object with id = 2 to have the name
  "New Mexico".
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def change_state_name(username, password, database):
    """
    Connects to a MySQL database and changes the name of the
    State object with id = 2 to "New Mexico".

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        database (str): The name of the MySQL database.
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

    # Query the State object with id = 2
    state = session.query(State).filter(State.id == 2).first()

    # Change the state name if found
    if state:
        state.name = "New Mexico"
        session.commit()

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

    # Change the name of the State object
    change_state_name(username, password, database)
