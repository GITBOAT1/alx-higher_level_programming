#!/usr/bin/python3
"""Start link class to table in database"""
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column
from sqlalchemy import (create_engine)


Base = declarative_base()


class State(Base):
    """state class"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return("<States(id='%s', name='%s')>" % (self.id, self.name))


if __name__ == "__main__":
    """ starting point"""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
