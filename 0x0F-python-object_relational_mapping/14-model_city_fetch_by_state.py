#!/usr/bin/python3
"""
communicates to local db
and queries for specfic columns
of rows in state tables that shares a
relationship the cities tables
-----------------------------
(via primary and foreign keys)
-----------------------------
"""

from sys import argv
from model_city import City
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State.name, City.id, City.name)\
                    .filter(City.state_id == State.id)\
                    .order_by(City.state_id).all()

    for x in result:
        print('{}: ({}) {}'.format(x[0], x[1], x[2]))

    session.close()
