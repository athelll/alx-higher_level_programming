#!/usr/bin/python3
"""
creates city and
states objects with
a relationship that affects
each other and commits it to
the DB
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine) 
    Session = sessionmaker(bind=engine)
    session = Session()

    new = State(name='California')
    new2 = City(name="San Francisco")
    new.cities.append(new2)

    session.add(new)
    session.add(new2)

    session.commit()
    session.close()
