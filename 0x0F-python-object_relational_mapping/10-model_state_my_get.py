#!/usr/bin/python3
"""
queries the local database
for all state row entries
that conatin the letter "a"
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).order_by(State.id).filter(
            State.name == argv[4]).first()

    if result:
        print(result.id)
    else:
        print("Not found")

    session.close()
