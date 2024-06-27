#!/usr/bin/python3
""" State Module for HBNB project """
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel
from models.city import City


class State(BaseModel):
    """
    State class represents a state in the application.

    Attributes:
        __tablename__ (str): The name of the database table for states.
        name (str): The name of the state.
        cities (list): The list of City instances associated with the state.
    """
    __tablename__ = 'states'
    name = Column(
        String(128),
        nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            'City',
            cascade='all, delete, delete-orphan',
            backref='state'
        )
    else:
        @property
        def cities(self):
            """Returns the list of City instances with state_id equals
            to the current State.id"""
            from models import storage
            all_cities = storage.all(City)
            return [city for city in all_cities.values() if city.state_id == self.id]
