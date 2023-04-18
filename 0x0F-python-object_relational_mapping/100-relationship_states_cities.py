#!/usr/bin/python3
"""
    A script that creates the State “California” with the City
    “San Francisco” from the database hbtn_0e_100_usa
"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    my_state = State(name="California")
    my_city = City(name="San Francisco")
    my_state.cities.append(my_city)

    session.add(my_state)
    session.add(my_city)
    session.commit()
    session.close()
