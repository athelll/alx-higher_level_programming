#!/usr/bin/python3
"""
Defines the class
City which is the schema
of the table cities
"""

from model_state import Base, State
from sqlalchemy import Integer, String, Column, ForeignKey


class City(Base):
    """City Schema class"""

    __tablename__ = "cities"
    id = Column(Integer, nullable=False, primary_key=True)  # autoincrements
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
