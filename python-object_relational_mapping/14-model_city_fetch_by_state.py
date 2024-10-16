#!/usr/bin/python3
"""Fetch all City objects from the database hbtn_0e_14_usa."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./14-model_city_fetch_by_state.py "
              "<mysql username> <mysql password> <database name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create a database connection
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/'
        f'{database}', pool_pre_ping=True
    )

    # Create all tables in the engine (if not exist)
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query to get all cities with their states
    results = session.query(City).join(State).order_by(City.id).all()

    # Check if results are empty
    if not results:
        print("No cities found.")
    else:
        # Display results
        for city in results:
            print(f"{city.state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()
