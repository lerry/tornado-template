#!/usr/bin/env python
# coding:utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///test.db', echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
       return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)

#Base.metadata.create_all(engine) 
Session = sessionmaker(bind=engine)

session = Session()
user = User('lerry', 'lerry', '123')
session.add(user)
session.commit()
print dir(user)
print user.name