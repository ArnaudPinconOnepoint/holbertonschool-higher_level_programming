#!/usr/bin/python3
"""
A script that deletes all State objects with a name
containing the letter 'a' from the database hbtn_0e_6_usa.

Usage: ./script_name.py <mysql username> <mysql password>
<database name>

This script connects to a MySQL database using SQLAlchemy and
removes State objects that contain the letter 'a' in their names.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states_with_a(username, password, database):
    """
    Connects to a MySQL database and deletes all State objects
    with a name containing the letter 'a'.

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

    # Query and delete State objects with names containing 'a'
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)

    # Commit the changes to the database
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

    # Delete State objects with names containing 'a'
    delete_states_with_a(username, password, database)
