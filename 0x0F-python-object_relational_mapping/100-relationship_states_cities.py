#!/usr/bin/python3
"""
This script creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""
from sys import argv
from sqlalchemy import create_engine
from relationship_state import State
from relationship_city import City, Base
from sqlalchemy.orm import sessionmaker, relationship

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Carlifonia")
    new_state.cities.append(City(name="San Francisco"))
    session.add(new_state)
    session.commit()
    session.close()
