#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create the base class for our model
Base = declarative_base()

# Define the State class
class State(Base):
    __tablename__ = 'states'

    # Define the columns
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

# Database connection setup
def main():
    # Define the connection string to connect to the MySQL server
    user = 'your_username'  # Replace with your MySQL username
    password = 'your_password'  # Replace with your MySQL password
    database = 'your_database'  # Replace with your MySQL database name
    host = 'localhost'
    port = 3306

    # Create the MySQL engine using SQLAlchemy
    engine = create_engine('mysql+mysqldb://' + user + ':' + password +
                           '@' + host + ':' + str(port) + '/' + database,
                           echo=True)


    # Create all tables in the database (if they don't exist)
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    main()
