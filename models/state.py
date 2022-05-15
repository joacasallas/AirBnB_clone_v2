#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Table, ForeignKey
import models



class State(BaseModel, Base):
    class attribute __tablename__ = 'states'
    """ State class """
    name = Column(String(128), nullable=False)
    
    
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)