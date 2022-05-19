#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import models
from models.city import City
from os import getenv

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state')

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """getter for cities that return
            a list of city instance equale to
            curent state id
            """
            new_list = []
            for key, obj_city in models.storage.all(City).items():
                if obj_city.state_id == self.id:
                    new_list.append(obj_city)
            return new_list
