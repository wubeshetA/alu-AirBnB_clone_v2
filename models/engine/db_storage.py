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
    
    def all(self, cls=None):
        """ query on the current database session """
        # create a dictionary
        obj_dict = {}
        if cls is None:
            for table in Base.metadata.tables:
                for obj in self.__session.query(table):
                    key = obj.__class__.__name__ + '.' + obj.id
                    obj_dict[key] = obj
        else:
            for obj in self.__session.query(cls):
                key = obj.__class__.__name__ + '.' + obj.id
                obj_dict[key] = obj
        return obj_dict
    
    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)
    
    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()
    
    def delete(self, obj=None):
        """ delete from the current database session obj if not None """
        if obj is not None:
            self.__session.delete(obj)
    
    def reload(self):
        """ create all tables in the database """
        Base.metadata.create_all(self.__engine)
        # create a configured "Session" class
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        # create a Session
        self.__session = Session()

        
