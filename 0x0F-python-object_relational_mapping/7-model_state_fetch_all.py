#!/usr/bin/python3

from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]), echo=False)
    with Session(bind=engine) as session:
        result = session.query(State).order_by(State.id)
        for row in result:
            print("{}: {}".format(row.id, row.name))
