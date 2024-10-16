#!/usr/bin/python3
"""City class definition."""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """City class representing the cities table."""
    __tablename__ = 'cities'

    id = Column(
        Integer, primary_key=True, autoincrement=True, nullable=False
    )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # Relationship to link City to State
    state = relationship("State", back_populates="cities")
