#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
# import sqlalchemy modules
from sqlalchemy import Column, ForeignKey, String
from os import environ

storage_type = 'HBNB_TYPE_STORAGE'

if storage_type in environ.keys() and environ.get('HBNB_TYPE_STORAGE') == 'db':
    class City(BaseModel, Base):
        """ The city class, contains state ID and name """

        __tablename__ = 'cities'

        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

else:
    class City(BaseModel):
        """ The city class, contains state ID and name """

        state_id = ""
        name = ""
