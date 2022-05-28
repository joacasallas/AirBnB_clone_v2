#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage():
    """Manage DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """Create engine"""
        username = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                username, password, host, database), pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in session"""
        dict_cls = {}
        list_cls = [User, State, City, Amenity, Place, Review]
        if cls is None:
            for i in list_cls:
                i = eval(i)
                for object in self.__session.query(i).all():
                    key = object.__class__.__name__ + '.' + object.id
                    dict_cls[key] = object
        else:
            for object in self.__session.query(i).all():
                key = object.__class__.__name__ + '.' + object.id
                dict_cls[key] = object
        return dict_cls

    def new(self, obj):
        """ add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)
        self.save

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            expire_on_commit=False, bind=self.__engine)
        Session = scoped_session(session_factory)
        self.__session = Session()


    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
