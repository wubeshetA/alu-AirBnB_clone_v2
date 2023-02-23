#!/usr/bin/python3
""" Database storage module """
from sqlalchemy import create_engine
# import declarative base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

Base = declarative_base()
class DBStorage:

    # private class attributes
    __engine = None
    __session = None

    def __init__(self):
        
        # get environment variables
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        port = os.getenv('HBNB_MYSQL_PORT')
        env = os.getenv('HBNB_ENV')
        storage_type = os.getenv('HBNB_STORAGE_TYPE')

        url = f'mysql+mysqldb://{user}:{pwd}@{host}:{port}/{db}'
        self.__engine = create_engine(url, pool_pre_ping=True)
        # drop all tables if the environment variable HBNB_ENV is equal to test
        if env == 'test':
            Base.metadata.drop_all(self.__engine)
    
    

