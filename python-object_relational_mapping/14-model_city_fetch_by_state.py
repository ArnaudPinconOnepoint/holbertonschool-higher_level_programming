#!/usr/bin/python3
"""
A script that fetches all City objects from the database hbtn_0e_14_usa,
sorted by cities.id.

Usage: ./14-model_city_fetch_by_state.py <mysql username>
<mysql password> <database name>

This script connects to a MySQL database using SQLAlchemy
and displays all City objects in the format: <state name>: (<city id>) <city name>.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def fetch_cities_by_state(username, password, database):
    """
    Fetches and prints all City objects from the database hbtn_0e_14_usa,
    sorted by cities.id.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        database (str): The name of the MySQL database.
    """
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all cities and their corresponding states
    cities = session.query(City).order_by(City.id).all()
    
    for city in cities:
        state = session.query(State).filter(State.id == city.state_id).first()
        if state:
            print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()


if __name__ == "__main__":
    # Ensure correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./14-model_city_fetch_by_state.py <mysql username> "
              "<mysql password> <database name>")
        sys.exit(1)

    # Get MySQL credentials and database from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Fetch and print City objects
    fetch_cities_by_state(username, password, database)
