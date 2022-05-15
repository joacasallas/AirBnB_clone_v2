#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import models
from models.city import City

class State(BaseModel, Base):
    __tablename__ = 'states'
    """ State class """
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state')
    