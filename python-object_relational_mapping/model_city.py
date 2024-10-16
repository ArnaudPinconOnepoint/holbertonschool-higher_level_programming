#!/usr/bin/python3
"""
Module defining the City class that maps to the cities table
in the hbtn_0e_14_usa database using SQLAlchemy.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """
    City class that defines the cities table structure.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    state = relationship('State', back_populates='cities')
