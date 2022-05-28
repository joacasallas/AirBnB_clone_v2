#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    '''State class'''
    if models.storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state')
    else:
        name=""

    def __init__(self, *args, **kwargs):
        '''initialization'''
        super().__init__(*args, **kwargs)

    if models.storage_t != "db":    
        @property
        def cities(self):
            '''getter'''
            list_city = []
            cities = models.storage.all(City)
            for value in cities.values():
                if value.state_id == self.id:
                    list_city.append(value)
            return list_city
