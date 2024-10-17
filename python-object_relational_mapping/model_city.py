#!/usr/bin/python3
"""Module"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

# Create the base class for our model
Base = declarative_base()

# Define the City class
class City(Base):
    """Class representing a city."""
    __tablename__ = 'cities'

    # Define the columns
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

