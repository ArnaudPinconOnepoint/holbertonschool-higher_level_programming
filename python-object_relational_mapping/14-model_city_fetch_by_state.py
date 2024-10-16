#!/usr/bin/python3
"""
This script lists all City objects from the database hbtn_0e_14_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import Base, State

def main():
    """Main function to fetch and display cities."""
    # Retrieve arguments
    if len(sys.argv) != 4:
        return

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create an engine and session
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}', echo=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to get cities with their corresponding states
    cities = session.query(City).join(State).order_by(City.id).all()

    # Display results
    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()

if __name__ == '__main__':
    main()
