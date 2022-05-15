import uuid
from datetime import date, datetime
from xmlrpc.client import DateTime
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
import models


class DBStorage ():
    __engine = None
    __session = None
    
    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb:')
        
    
    




