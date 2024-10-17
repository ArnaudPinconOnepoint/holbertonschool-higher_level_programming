#!/usr/bin/python3
"""Module to fetch cities by state."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import State, Base

def main():
    """Main function to fetch and print cities."""
    if len(sys.argv) != 4:
        print("Usage: ./14-model_city_fetch_by_state.py "
              "<mysql username> <mysql password> <database name>")
        return

    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    host = 'localhost'
    port = 3306

    # Create the MySQL engine using SQLAlchemy
    engine = create_engine(
        f'mysql+mysqldb://{user}:{password}@{host}:{port}/'
        f'{database}', echo=False)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to get all cities and their associated states
    cities = session.query(City).join(State).order_by(City.id).all()

    # Print the results in the specified format
    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()

if __name__ == '__main__':
    main()
