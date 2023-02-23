#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
# import sqlalchemy modules
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(Base, BaseModel):
    """ State model class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    # create a relationship with cities
    cities = relationship('City', back_populates='state', cascade='all, delete')
