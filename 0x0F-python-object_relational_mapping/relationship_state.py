#!/usr/bin/python3
"""
Defines Class states
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()


class State(Base):
    """
     Creatse the schema for
     the table "states"
     Linked to the Local MySql server
    """

    __tablename__ = "states"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")
