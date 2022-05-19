#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import models
from models.city import City


class State(BaseModel):
    """ State class """
    name = ""

    def __init__(self, *args, **kwargs):
        """inherit from base  and Basemodel init"""
        super().__init__(*args, **kwargs)


"""class State(BaseModel, Base):
    '''State class'''
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state')"""

"""def __init__(self, *args, **kwargs):
        '''initialization'''
        super().__init__(*args, **kwargs)

        @property
        def cities(self):
            '''getter'''
            list_city = []
            cities = models.storage.all(City)
            for value in cities.values():
                if value.state_id == self.id:
                    list_city.append(value)
            return list_city"""
