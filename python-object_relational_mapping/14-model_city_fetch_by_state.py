#!/usr/bin/python3
"""
Python file similar to model_state.py named model_city.py that contains the class definition of a City
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = (
        session.query(City, State)
        .filter(City.state_id == State.id)
        .order_by(City.id)
        .all()
    )

    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.commit

    session.close()
